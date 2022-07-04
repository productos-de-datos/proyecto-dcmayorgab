
import pandas as pd
import os


def transform_data():
    """Transforme los archivos xls a csv.

    Transforme los archivos data_lake/landing/*.xls a data_lake/raw/*.csv. Hay
    un archivo CSV por cada archivo XLS en la capa landing. Cada archivo CSV
    tiene como columnas la fecha en formato YYYY-MM-DD y las horas H00, ...,
    H23.

    """
    #raise NotImplementedError("Implementar esta función")

    cwd=os.getcwd()
    path_landing = os.path.join(cwd, 'data_lake/landing/') 
    path_raw = os.path.join(cwd, 'data_lake/raw/') 
    list_files = os.listdir(path_landing)


    for file in list_files:
        
        
        try :
            df_energia = pd.read_excel(path_landing + file,engine='openpyxl')
    
            
        except :
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
        df_energia.to_csv(os.path.join(path_raw,file.split('.')[0]+'.csv'),index=False)

if __name__ == "__main__":
    import doctest
    transform_data()

    doctest.testmod()
