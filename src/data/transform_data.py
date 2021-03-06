"""
Transforme los archivos xls a csv.
Transforme los archivos landing a raw. Hay
un archivo CSV por cada archivo XLS en la capa landing. Cada archivo CSV
tiene como columnas la fecha en formato YYYY-MM-DD y las horas H00, ...,
H23.

"""

import os
import pandas as pd

def transform_data():
    """
    Transforma los archivos xls a csv.

    """
    #raise NotImplementedError("Implementar esta función")
    #cwd=os.getcwd()

    path_landing = 'data_lake/landing/'
    path_raw = 'data_lake/raw/'
    list_files = os.listdir(path_landing)

    for file in list_files:
        
        try :
            df_energia = pd.read_excel(path_landing + file,engine='openpyxl')
      
        except : # pylint: disable=W0702
            df_energia = pd.read_excel(path_landing + file )
        
        if  df_energia.columns[0]!='Fecha':
            skip=df_energia.iloc[:,0][df_energia.iloc[:,0]=='Fecha'].index.tolist()[0]
            df_energia=df_energia.iloc[skip:,:]
            new_header = df_energia.iloc[0]
            df_energia = df_energia[1:] 
            df_energia.columns = new_header
        
        df_energia=df_energia.iloc[:,:25]
        df_energia=df_energia.dropna()
        df_energia = df_energia.melt(id_vars=['Fecha'], value_name='Precio', var_name='Hora')
        df_energia['Hora']=df_energia['Hora'].astype(int)
        df_energia['Fecha']=pd.to_datetime(df_energia['Fecha'], format='%Y-%m-%d')
        df_energia=df_energia.sort_values(['Fecha','Hora']).fillna(method='ffill')
        df_energia=df_energia.sort_values(['Fecha','Hora']).fillna(method='bfill')
        df_energia=df_energia.drop_duplicates()
        df_energia.to_csv(path_raw+file.split('.')[0]+'.csv',index=False)

if __name__ == "__main__":
    import doctest
    transform_data()
    doctest.testmod()
    