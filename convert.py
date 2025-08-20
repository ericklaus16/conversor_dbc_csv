import os
import pyreaddbc
import pandas as pd

input_dir = 'dbc'
output_dir = 'csv'

os.makedirs(output_dir, exist_ok=True)

# Converte todos os arquivos .dbc na pasta de entrada 
for filename in os.listdir(input_dir):
    if filename.lower().endswith('.dbc'):
        dbc_path = os.path.join(input_dir, filename)
        csv_filename = os.path.splitext(filename)[0] + '.csv'
        csv_path = os.path.join(output_dir, csv_filename)

        # Lê o arquivo DBC 
        df = pyreaddbc.read_dbc(dbc_path)

        def decode_cell(x):
            if isinstance(x, bytes):
                try:
                    return x.decode('utf-8')
                except UnicodeDecodeError:
                    return x.decode('latin1')
            return x

        # Binário -> String
        df = df.applymap(decode_cell)

        # Salva como CSV
        df.to_csv(csv_path, index=False, sep=";")
        print(f'Convertido: {dbc_path} -> {csv_path}')