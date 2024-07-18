from src.app.db_operations import query_metrics, query_specs
from src.app.plot import normalize_outliers
from src.config.config import VITAL_STATS_CONFIG
import numpy as np
import pandas as pd


def make_overall_card_weight(engine):
    m_df = query_metrics(engine)
    # transform > 50 weights as those are obvious outliers. 
    m_df = normalize_outliers(m_df, 'measured_weight', 50)
    s_df = query_specs(engine)

    m_df = m_df.merge(s_df[['product_name', 'weight_min', 'weight_max']], on='product_name', how='left')
    # Group by product_name and calculate relevant metrics
    grouped = m_df.groupby('product_name').agg(
    Count=('measured_weight', 'size'),
    Min_Weight=('measured_weight', 'min'),
    Max_Weight=('measured_weight', 'max'),
    Average_Weight=('measured_weight', 'mean')
    ).reset_index()
    
    # Calculate additional metrics
    grouped['Pct_In_Spec'] = m_df.groupby('product_name').apply(
        lambda x: (x['measured_weight'].between(x['weight_min'], x['weight_max'])).mean() * 100
    ).values

    grouped['Count_Offspec'] = m_df.groupby('product_name').apply(
        lambda x: (~x['measured_weight'].between(x['weight_min'], x['weight_max'])).sum()
    ).values

    grouped['Compliant'] = grouped['Pct_In_Spec'] > 95

    # Format the Pct_In_Spec column
    grouped['Pct_In_Spec'] = grouped['Pct_In_Spec'].apply(lambda x: f"{x:.2f}%")

    # Rename columns for consistency
    grouped.rename(columns={
        'product_name': 'Product',
        'Min_Weight': 'Min Weight',
        'Max_Weight': 'Max Weight',
        'Average_Weight': 'Average Weight',
        'Pct_In_Spec': 'Pct In Spec',
        'Count_Offspec': 'Count Offspec'
    }, inplace=True)
    
    
    return grouped


def make_overall_card_height(engine):
    
    m_df = query_metrics(engine)
    s_df = query_specs(engine)

    m_df = m_df.merge(s_df[['product_name', 'height_min', 'height_max']], on='product_name', how='left')
    
    # Group by product_name and calculate relevant metrics for height
    grouped_height = m_df.groupby('product_name').agg(
        Count_Height=('measured_height', 'size'),
        Min_Height=('measured_height', 'min'),
        Max_Height=('measured_height', 'max'),
        Average_Height=('measured_height', 'mean')
    ).reset_index()

    # Calculate additional height metrics
    grouped_height['Pct_In_Spec_Height'] = m_df.groupby('product_name').apply(
        lambda x: (x['measured_height'].between(x['height_min'], x['height_max'])).mean() * 100
    ).values

    grouped_height['Count_Offspec_Height'] = m_df.groupby('product_name').apply(
        lambda x: (~x['measured_height'].between(x['height_min'], x['height_max'])).sum()
    ).values

    grouped_height['Compliant_Height'] = grouped_height['Pct_In_Spec_Height'] > 95

    # Format the Pct_In_Spec_Height column
    grouped_height['Pct_In_Spec_Height'] = grouped_height['Pct_In_Spec_Height'].apply(lambda x: f"{x:.2f}%")

    # Rename columns for consistency
    grouped_height.rename(columns={
        'product_name': 'Product',
        'Min_Height': 'Min Height',
        'Max_Height': 'Max Height',
        'Average_Height': 'Average Height',
        'Pct_In_Spec_Height': 'Pct In Spec Height',
        'Count_Offspec_Height': 'Count Offspec',
        'Compliant_Height': 'Compliant'
    }, inplace=True)

    # Display the final height table
    return grouped_height


def product_specific_card(engine, product_name, config_key):
    
    card_config = VITAL_STATS_CONFIG[config_key]
    
    m_df = query_metrics(engine, product_name)
    # transform > 50 weights as those are obvious outliers. 
    if config_key == 'weight':
        m_df = normalize_outliers(m_df, card_config[2], 50)
    
    s_df = query_specs(engine, product_name)
    
    
    min_spec = s_df[card_config[0]].values[0]
    max_spec = s_df[card_config[1]].values[0]
    avg_ = np.mean(m_df[card_config[2]])
    count_ = len(m_df[card_config[2]])
    min_ = np.min(m_df[card_config[2]])
    max_ = np.max(m_df[card_config[2]])
    in_spec = m_df[card_config[2]].apply(lambda x: min_spec <= x <= max_spec)
    percent_in_spec = (np.sum(in_spec)/np.sum(count_))*100
    out_spec_val = m_df.loc[~in_spec, card_config[2]].values
    count_oos = len(out_spec_val)
    compliance = percent_in_spec > 95.00

    # Create dataframe for subplot weight information
    subplot_ = pd.DataFrame({
    'Product': [product_name],
    'Count': [count_],
    'Min': [min_],
    'Max': [max_],
    'Average': [avg_],
    'Pct In Spec': f"{percent_in_spec:.2f}%",
    'Count Offspec': [count_oos],
    'Compliant': [compliance]
    })

    return subplot_.T

def action_card(engine):
    df_w = make_overall_card_weight(engine)
    df_h = make_overall_card_height(engine)
    
    df_w = df_w[['Product', 'Compliant']]
    df_w = df_w.loc[df_w['Compliant'] == False]


    df_h = df_h[['Product','Compliant']]
    df_h = df_h.loc[df_h['Compliant'] == False]
    
    weight_dict = df_w.to_dict(orient='records')
    height_dict = df_h.to_dict(orient='records')
    
    return (weight_dict + height_dict)
    
    