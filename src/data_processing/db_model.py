from src.config.private_info import DB_NAME, test_def_db, test_new_db
from src.data_processing.data_load import log_data
from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError


def establish_db():
    print(create_db(DB_NAME, test_def_db))
    if type(DB_NAME) == bool:
        return 'DB already exists'
    else:
        return create_tables(DB_NAME)


def create_db(db_name: str, db_url: str) -> str:
    
    engine = create_engine(db_url, isolation_level='AUTOCOMMIT')
    
    with engine.connect() as connection:
        # Check to see if db already exists otherwise create it. 
        result = [x for x in connection.execute(text(f"select datname from pg_database where datname = '{db_name}';"))]
        if len(result):
            log_data(f'{db_name} already exists.\n')
            return True
        else:
            connection.execute(text(f"CREATE DATABASE {db_name}"))
            log_data(f"Database {db_name} created.\n")
            
    return f'{db_name} created.'

def create_tables(db_name: str):
    # new_db_url = f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:5432/{db_name}"
    engine = create_engine(test_new_db)
    
    with open('data/sql/schema.sql', 'r', encoding='utf-8-sig') as file:
        table_create_query = file.read()
    
    with engine.begin() as connection:
        try:
            for query in table_create_query.split(';'):
                if query.strip():
                    connection.execute(text(query))
                    log_data('query executed\n')
                else:
                    log_data(f'This query {repr(query)}, is whitepsace.\n')
            log_data('Executed table creation query from sql file.\n')
        except SQLAlchemyError as e:
            log_data(f'Unable to execute query: {str(e)}')

    return 'Table query execution complete.'