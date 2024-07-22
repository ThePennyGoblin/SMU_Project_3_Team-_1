from src.config.config import CLEANING_CONFIGS, RENAMING_SPLICING_CONFIGS, CSV_NAMES, DROP_ROWS
from src.data_processing.data_load import log_data
import pandas as pd

def clean_csv(csv_path: str):
    """
    Reads a CSV file, cleans it based on predefined configurations, and saves the cleaned data to a new CSV file.

    Args:
        csv_path (str): Path to the raw CSV file.

    Returns:
        str: Confirmation message indicating the path to the newly created cleaned CSV file.

    The cleaning process includes:
    - Renaming and splicing columns based on the column count.
    - Stripping whitespace from string values.
    - Dropping specified rows.
    - Changing data types for specific columns.
    - Logging the success of the cleaning process.
    """
    df = pd.read_csv(csv_path)
    df = clean_column_names(df, RENAMING_SPLICING_CONFIGS)
    df = strip_whitespace(df)
    # if statement to make sure we pick right table when assigning the cleaned csv name.
    if len(df.columns) == 4:
        df = row_drop(df, DROP_ROWS)
        df = change_dtypes(df, CLEANING_CONFIGS)
        log_data('metric csv successful\n')
        return make_csv(df, CSV_NAMES[0])
    else:
        log_data('spec csv successful\n')
        return make_csv(df, CSV_NAMES[1])
        
def change_dtypes(df, config: dict):
    """
    Changes the data types of specified columns in a DataFrame.

    Args:
        df (pandas.DataFrame): DataFrame whose columns' data types need to be changed.
        config (dict): where keys are column names and values are target data types.

    Returns:
        pandas.DataFrame: DataFrame with updated column data types.
    """
    for col, dtype in config.items():
        if col == 'date_time':
            df[col] = pd.to_datetime(df[col], format='%m/%d/%Y %I:%M:%S %p')
        else:
            df[col] = df[col].astype(dtype)  
    return df 

def strip_whitespace(df):
    """
    Strips leading and trailing whitespace from all string values in a DataFrame.

    Args:
        df (pandas.DataFrame): DataFrame whose string columns need whitespace removal.

    Returns:
        pandas.DataFrame: DataFrame with whitespace removed from string values.
    """
    for x in df.columns:
        if type(df[x].values[0]) == str:
            df[x] = df[x].str.strip()
    return df

def clean_column_names(df, config: dict):
    """
    Cleans column names by converting to lowercase, stripping whitespace, and replacing spaces with underscores.
    Also renames and splices columns based on predefined configurations.

    Args:
        df (pandas.DataFrame): DataFrame whose columns need to be cleaned and renamed.
        config (dict): Dictionary containing renaming and splicing configurations.

    Returns:
        pandas.DataFrame: DataFrame with cleaned and renamed columns.
    """
    df.columns = df.columns.str.lower().str.strip().str.replace(" ", "_")
    # this check is to make sure we grab the metric table and not the specs.
    if len(df.columns) > 6:
        df = df[config["m_splicing_config"]]
        df = df.rename(columns= config["m_renaming_config"])
    else:
        df = df.rename(columns=config["s_rename_config"])
    return df

def make_csv(df, file_name: str):
    """
    Saves a DataFrame to a CSV file in the 'data/cleaned/' directory.

    Args:
        df (pandas.DataFrame): DataFrame to be saved.
        file_name (str): Name of the output CSV file.

    Returns:
        str: Confirmation message indicating the path to the newly created CSV file.
    """
    new_file_path = f'data/cleaned/{file_name}'
    df.to_csv(new_file_path, index=False)
    return f'{new_file_path} created.\n'
    
    
def row_drop(df, config: list):
    """
    Drops rows from a DataFrame based on specified conditions.

    Args:
        df (pandas.DataFrame): DataFrame from which rows need to be dropped.
        config (list): List of conditions for dropping rows. The first four elements are product names,
                       and the fifth element is a height threshold.

    Returns:
        pandas.DataFrame: DataFrame with specified rows dropped.
    """
    drop_condition = df.loc[(df['product_name'] == config[0]) | 
                            (df['product_name'] == config[1]) | 
                            (df['product_name'] == config[2]) | 
                            (df['product_name'] == config[3]) |
                            (df['measured_height'] < config[4]) 
                            ].index
    
    df = df.drop(drop_condition)
    return df