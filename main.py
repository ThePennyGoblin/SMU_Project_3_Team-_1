from src.data_cleaning import clean_csv

spec_path = 'data/raw/Generic_Butcher_Company_2024_06_SPEC_SHEET.csv'
metric_path = 'data/raw/Generic_Butcher_Company_2024_06.csv'

print(clean_csv(metric_path))
print(clean_csv(spec_path))

