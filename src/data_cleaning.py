# ## Cleaning objectives
# - Change date column to date time -- COMPLETE 
# - Change height and weight columns to float -- COMPLETE
# - Strip product text -- COMPLETE 
# - Removed whitespace from all str columns -- COMPLETE
# - Remove products 15 oz Ribeye tail A & 5.5 oz Tenderloin A. -- COMPLETE 
# - Change column names to match data model -- COMPLETE 

from src.config import CLEANING_CONFIGS, RENAMING_SPLICING_CONFIGS, CSV_NAMES, DROP_ROWS
from src.data_load import log_data
import pandas as pd

def clean_csv(csv_path):
    df = pd.read_csv(csv_path)
    df = clean_column_names(df, RENAMING_SPLICING_CONFIGS)
    df = strip_whitespace(df)
    df = row_drop(df, DROP_ROWS)
    # if statement to make sure we pick right table when assigning the cleaned csv name.
    if len(df.columns) == 4:
        df = change_dtypes(df, CLEANING_CONFIGS)
        log_data('metric csv successful\n')
        return make_csv(df, CSV_NAMES[0])
    else:
        log_data('spec csv successful\n')
        return make_csv(df, CSV_NAMES[1])
        
def change_dtypes(df, config: dict|list):
    for col, dtype in config.items():
        if col == 'date_time':
            df[col] = pd.to_datetime(df[col], format='%m/%d/%Y %I:%M:%S %p')
        else:
            df[col] = df[col].astype(dtype)  
    return df 

def strip_whitespace(df):
    for x in df.columns:
        if type(df[x].values[0]) == str:
            df[x] = df[x].str.strip()
    return df

def clean_column_names(df,config):
    df.columns = df.columns.str.lower().str.strip().str.replace(" ", "_")
    # this check is to make sure we grab the metric table and not the specs.
    if len(df.columns) > 6:
        df = df[config["m_splicing_config"]]
        df = df.rename(columns= config["m_renaming_config"])
    else:
        df = df.rename(columns=config["s_rename_config"])
    return df

def make_csv(df, file_name):
    new_file_path = f'data/cleaned/{file_name}'
    df.to_csv(new_file_path, index=False)
    return f'{new_file_path} created.\n'
    
    
def row_drop(df, config):
    drop_condition = df.loc[(df['product_name'] == config[0]) | (df['product_name'] == config[1]) | (df['product_name'] == config[2]) | (df['product_name'] == config[3])].index
    df = df.drop(drop_condition)
    return df
