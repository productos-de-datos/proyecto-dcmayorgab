"""Realice la limpieza y transformación de los archivos CSV.

    Usando los archivos data_lake/raw/*.csv, cree el archivo data_lake/cleansed/precios-horarios.csv.
    Las columnas de este archivo son:

    * fecha: fecha en formato YYYY-MM-DD
    * hora: hora en formato HH
    * precio: precio de la electricidad en la bolsa nacional

    Este archivo contiene toda la información del 1997 a 2021.


    """


import pandas as pd
import os

def clean_data():

    """
    Formatea los archivos y los concatena

    """
    #raise NotImplementedError("Implementar esta función")

    #cwd=os.getcwd()
    path_raw =  'data_lake/raw/'
    path_cleaned= 'data_lake/cleansed/'
    list_files = [ 'data_lake/raw/'+i  for i in os.listdir(path_raw)]

    lst_df = []
       
    for path in list_files:

        dfp = pd.read_csv(path)
        lst_df.append(dfp)
            
        dfp = pd.concat(lst_df)
        dfp.to_csv(path_cleaned+'precios-horarios.csv',index=False)

    

# Tests
def test_file():
    import os
    assert os.path.isfile('data_lake/cleansed/precios-horarios.csv') is True




if __name__ == "__main__":
    import doctest
    clean_data()
    doctest.testmod()
