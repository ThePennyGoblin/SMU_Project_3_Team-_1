import pandas as pd

def query_metrics(engine, product_name=None):
    """
    Queries the 'metrics' table in the database and returns the result as a DataFrame.

    Args:
        engine (sqlalchemy.engine.Engine): SQLAlchemy engine object for database connection.
        product_name (str, optional): Name of the product to filter the query by. Defaults to None.

    Returns:
        pandas.DataFrame: DataFrame containing the query result. If `product_name` is provided, the result is filtered by the specified product name.
    """
    
    if product_name:
        query = """
        SELECT *
        FROM metrics
        WHERE product_name = %(product_name)s;
        """
        df = pd.read_sql(query, engine, params={'product_name': product_name})
    else:
        query = """
        SELECT *
        FROM metrics;
        """
        df = pd.read_sql(query, engine)
        
    return df

def query_specs(engine, product_name=None):
    """
    Queries the 'products' table in the database and returns the result as a DataFrame.

    Args:
        engine (sqlalchemy.engine.Engine): SQLAlchemy engine object for database connection.
        product_name (str, optional): Name of the product to filter the query by. Defaults to None.

    Returns:
        pandas.DataFrame: DataFrame containing the query result. If `product_name` is provided, the result is filtered by the specified product name.
    """
    
    if product_name:
        query = """
        SELECT *
        FROM products
        WHERE product_name = %(product_name)s;
        """
        df = pd.read_sql(query, engine, params={'product_name': product_name})
    else:
        query = """
        SELECT *
        FROM products;
        """
        df = pd.read_sql(query, engine)
        
    return df

def query_product_list(engine):
    """
    Queries the 'products' table in the database to retrieve the list of product names.

    Args:
        engine (sqlalchemy.engine.Engine): SQLAlchemy engine object for database connection.

    Returns:
        pandas.DataFrame: DataFrame containing the list of product names.
    """
    
    query = """
    SELECT product_name
    FROM products;
    """
    df = pd.read_sql(query, engine)
    return df