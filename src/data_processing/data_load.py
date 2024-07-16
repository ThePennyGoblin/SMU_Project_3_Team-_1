import pandas as pd
from sqlalchemy import create_engine
from src.config.config import PRIMARY_KEYS, CSV_PATHS, TABLE_NAMES, MERGE_CONFIG
from src.config.private_info import test_new_db

engine = create_engine(test_new_db, isolation_level='AUTOCOMMIT')

def dump_data():
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
    dataframe[primary_key] = dataframe.index + 1
    dataframe = rearrange_cols(dataframe, primary_key)
    return dataframe

def rearrange_cols(dataframe, primary_key: str):
    new_order = [primary_key] + [col for col in dataframe.columns if col != primary_key]
    dataframe = dataframe[new_order]
    return dataframe

def load_table(dataframe, table: str) -> str:
    dataframe.to_sql(table, con=engine, index = False, if_exists ='append')
    return f'{table} loaded to database.'

def merge_dataframes(left_df, right_df, join_key: str):
    left_df = left_df.merge(right_df, how='left', on = join_key)
    return left_df

def log_data(data):
    with open('outputs/log.txt', 'a') as file:
        file.write(data)