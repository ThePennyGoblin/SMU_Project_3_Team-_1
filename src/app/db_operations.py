import pandas as pd

def query_metrics(engine, product_name=None):
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
    query = """
    SELECT product_name
    FROM products
    """
    df = pd.read_sql(query, engine)
    return df