import pandas as pd

#Creamos una funcion para mostrar los tipos de columnas, cantidad de filas nulas y % de nulos
def resumen(df):
    print(f'data shape: {df.shape}')
    resumen = pd.DataFrame(df.dtypes, columns=['data type'])
    resumen['#missing'] = df.isnull().sum()
    resumen['%missing'] = df.isnull().sum()*100/len(df)
    #resumen['#unique'] = df.nunique()
    return resumen