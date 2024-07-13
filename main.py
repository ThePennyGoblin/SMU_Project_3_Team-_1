from src.data_cleaning import clean_csv
from src.db_model import establish_db
from src.data_load import dump_data

raw_metric_path = 'data/raw/Generic_Butcher_Company_2024_06.csv'
raw_spec_path = 'data/raw/Generic_Butcher_Company_2024_06_SPEC_SHEET.csv'


# apply cleaning transformations on raw csvs.
print(clean_csv(raw_metric_path))
print(clean_csv(raw_spec_path))

# create db if it doesn't exist and make the tables per the ERD model.
print(establish_db() + '\n')

print(dump_data())

