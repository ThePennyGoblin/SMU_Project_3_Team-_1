from data_cleaning import clean_csv

spec_path = 'resources/Generic_Butcher_Company_2024_06_SPEC_SHEET.csv'
metric_path = 'resources/Generic_Butcher_Company_2024_06.csv'

print(clean_csv(metric_path))
print(clean_csv(spec_path))

