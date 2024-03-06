import pandas

def datatype_per_column(df):
    for column in df.columns:
        unique_data_types = df[column].apply(type).unique()
        print(f"Columna '{column}': {unique_data_types}")
