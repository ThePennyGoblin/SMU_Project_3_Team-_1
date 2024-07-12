import os
cleaning_configs = {
    'measured_weight': 'float',
    'date_time': 'date_time'
    }

renaming_splicing_configs = {
    "s_rename_config" : {
        "product":"product_name"
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

drop_rows = ['TEST BLOCK A', 'TEST BLOCK B', '5.5 oz Tenderloin A', '15 oz  Ribeye Tail A']

csv_names = ('generic_butcher_cleaned.csv', 'generic_butcher_spec_cleaned.csv')