import os
import pandas as pd

files = os.listdir('C:/Users/Breno/PycharmProjects/api-vitivinicultura/datasets/csv')

for file in files:
    csv_file = pd.read_csv(f'datasets/csv/{file}', sep=';')
    output_name = os.path.basename(file)
    csv_file.to_json(f'datasets/json/{output_name}.json', orient='records')
