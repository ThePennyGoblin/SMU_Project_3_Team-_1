import pandas as pd
from sqlalchemy import create_engine
from src.config.config import PRIMARY_KEYS, CSV_PATHS, TABLE_NAMES, MERGE_CONFIG
from dotenv import load_dotenv
import os

load_dotenv()

DB_USER = os.getenv('DB_USER')
DB_PASS = os.getenv('DB_PASS')
DB_HOST = os.getenv('DB_HOST')
DB_NAME = os.getenv('NEW_DB_NAME')
DB_PORT = os.getenv('DB_PORT')

db_url = f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(db_url, isolation_level='AUTOCOMMIT')

def dump_data():
    """
    Loads cleaned CSV data into a PostgreSQL database after adjusting it to match the desired data model.

    The function performs the following steps:
    1. Reads and processes CSV files by adding primary key columns.
    2. Transforms data by merging dataframes based on configuration.
    3. Loads the transformed data into the specified database tables.

    Returns:
        str: Confirmation message indicating that all tables were created successfully.
    """
    
    # zipping primary key with appropriate csv path to make primary key cols.
    table_config = list(zip(CSV_PATHS, PRIMARY_KEYS))
    
    dfs_to_transform = []
    dfs_to_load = []
    
    for csv_path, primary_key in table_config:
        df = pd.read_csv(csv_path)
        df = make_id_column(df, primary_key)
        dfs_to_transform.append(df)
        log_data(f'{primary_key} column created.\n')
    
    transform_config = list(zip(dfs_to_transform, PRIMARY_KEYS))
    
    for df, primary_key in transform_config: 
        if  primary_key == 'product_id':
            dfs_to_load.append(df)
        else:
            merge_df = dfs_to_transform[1]
            df = merge_dataframes(df, merge_df, MERGE_CONFIG['join_key'])
            final_df = df[MERGE_CONFIG['final_cols']]
            dfs_to_load.append(final_df)
    
    loading_config = list(zip(dfs_to_load, TABLE_NAMES))
    loading_config.reverse()
    
    for table, table_name in loading_config:
        print(load_table(table, table_name))
        log_data(f'{table_name} loaded.\n')
        
    return 'All tables created successfully.'

def make_id_column(dataframe, primary_key: str):
    """
    Adds a primary key column to a DataFrame.

    Args:
        dataframe (pandas.DataFrame): DataFrame to which the primary key column will be added.
        primary_key (str): Name of the primary key column.

    Returns:
        pandas.DataFrame: DataFrame with the primary key column added and reordered.
    """
    dataframe[primary_key] = dataframe.index + 1
    dataframe = rearrange_cols(dataframe, primary_key)
    return dataframe


def rearrange_cols(dataframe, primary_key: str):
    """
    Reorders the columns of a DataFrame to place the primary key column first.

    Args:
        dataframe (pandas.DataFrame): DataFrame whose columns will be reordered.
        primary_key (str): Name of the primary key column to be placed first.

    Returns:
        pandas.DataFrame: DataFrame with reordered columns.
    """
    new_order = [primary_key] + [col for col in dataframe.columns if col != primary_key]
    dataframe = dataframe[new_order]
    return dataframe

def load_table(dataframe, table: str) -> str:
    """
    Loads a DataFrame into a specified PostgreSQL table.

    Args:
        dataframe (pandas.DataFrame): DataFrame to be loaded into the database.
        table (str): Name of the database table where the data will be loaded.

    Returns:
        str: Confirmation message indicating the table was loaded successfully.
    """
    dataframe.to_sql(table, con=engine, index = False, if_exists ='append')
    return f'{table} loaded to database.'

def merge_dataframes(left_df, right_df, join_key: str):
    """
    Merges two DataFrames on a specified join key.

    Args:
        left_df (pandas.DataFrame): Left DataFrame to be merged.
        right_df (pandas.DataFrame): Right DataFrame to be merged.
        join_key (str): Column name to join on.

    Returns:
        pandas.DataFrame: Merged DataFrame.
    """
    left_df = left_df.merge(right_df, how='left', on = join_key)
    return left_df

def log_data(data):
    """
    Logs data to a file.

    Args:
        data (str): Data to be logged.

    Writes the provided data to 'outputs/log.txt'.
    """
    with open('outputs/log.txt', 'a') as file:
        file.write(data)