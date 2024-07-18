CLEANING_CONFIGS = {
    'measured_weight': 'float',
    'date_time': 'date_time'
    }

RENAMING_SPLICING_CONFIGS = {
    "s_rename_config" : {
        "product":"product_name",
        "thick_min": "height_min",
        "thick_max": "height_max"
    },
    "m_renaming_config":{
        "product":"product_name",
        "date_time":"date_time",
        "external_measurement_weight_0":"measured_weight",
        "height;_avg":"measured_height"
    },
    "m_splicing_config":
        ["product",
         "date_time",
         "external_measurement_weight_0",
         "height;_avg"]
}

DROP_ROWS = ['TEST BLOCK A', 'TEST BLOCK B', '5.5 oz Tenderloin A', '15 oz  Ribeye Tail A', .05]

CSV_PATHS = ['data/cleaned/generic_butcher_cleaned.csv', 'data/cleaned/generic_butcher_spec_cleaned.csv']
CSV_NAMES = ['generic_butcher_cleaned.csv', 'generic_butcher_spec_cleaned.csv']

PRIMARY_KEYS = ['metric_id', 'product_id']

MERGE_CONFIG = {
    'join_key': 'product_name',
    'right_df': CSV_PATHS[1],
    'final_cols': ['metric_id', 'product_id', 'product_name', 'date_time', 'measured_weight', 'measured_height']
}

TABLE_NAMES = ['metrics', 'products']

HIST_CONFIG = {
    'weight': ['measured_weight', 'weight_min', 'weight_max', .25, 'Weight (oz)'],
    'height': ['measured_height', 'height_min', 'height_max', .1, 'Height (in)']
}

OUTLIERS_CONFIG = {
    'col': 'measured_weight',
    'outlier': 50
}

VITAL_STATS_CONFIG = {
    'weight': ['weight_min', 'weight_max', 'measured_weight'],
    'height': ['height_min', 'height_max', 'measured_height']
}


