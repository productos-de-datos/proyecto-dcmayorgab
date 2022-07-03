"""
Módulo de ingestión de datos.
-------------------------------------------------------------------------------

"""
import os
import urllib.request

def ingest_data():
    """Ingeste los datos externos a la capa landing del data lake.

    Del repositorio jdvelasq/datalabs/precio_bolsa_nacional/xls/ descarge los
    archivos de precios de bolsa nacional en formato xls a la capa landing. La
    descarga debe realizarse usando únicamente funciones de Python.

    """
    # raise NotImplementedError("Implementar esta función")
    get_urls()
    get_files()

def get_urls():
    with open('urls.txt','w') as f:

        for year in range(1995,2022):
            url = 'https://github.com/jdvelasq/datalabs/blob/master/datasets/precio_bolsa_nacional/xls/'
            if year not in [2016,2017]:
                url = url + str(year)+'.xlsx?raw=true'
                f.write(url)
                f.write('\n')
            else:
                url = url + str(year)+'.xls?raw=true'    
                f.write(url)
                f.write('\n')




def get_files():
    landing='./data_lake/landing/'
    with open('./urls.txt','r') as f:
        for i in f.readlines():
            urllib.request.urlretrieve(i,landing+ i.split('/')[-1].split('?')[0])





if __name__ == "__main__":
    import doctest

    doctest.testmod()
