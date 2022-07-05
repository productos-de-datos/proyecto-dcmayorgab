"""
Ingeste los datos externos a la capa landing del data lake.
Del repositorio jdvelasq/datalabs/precio_bolsa_nacional/xls/ descarge los
archivos de precios de bolsa nacional en formato xls a la capa landing. La
descarga debe realizarse usando únicamente funciones de Python.

"""
#import os
import urllib.request


def ingest_data():
    """
    Realiza la ingesta de datos

    """
    # raise NotImplementedError("Implementar esta función")
    get_urls()
    get_files()


def get_urls():
    """
    Crea una lista de urls

    """
    with open('urls.txt', 'w',encoding="utf-8") as file:

        for year in range(1995, 2022):
            url_part1 = 'https://github.com/jdvelasq/datalabs/blob/master'
            url_part2 = '/datasets/precio_bolsa_nacional/xls/'
            url=url_part1+url_part2
            if year not in [2016, 2017]:
                url = url + str(year)+'.xlsx?raw=true'
                file.write(url)
                file.write('\n')
            else:
                url = url + str(year)+'.xls?raw=true'
                file.write(url)
                file.write('\n')


def get_files():
    """
    Crea los archivos

    """
    # cwd=os.getcwd()
    landing = 'data_lake/landing/'
    # landing='./data_lake/landing/'
    with open('./urls.txt', 'r',encoding="utf-8") as file:
        for i in file.readlines():
            urllib.request.urlretrieve(
                i, landing+i.split('/')[-1].split('?')[0])


if __name__ == "__main__":
    import doctest
    ingest_data()
    doctest.testmod()
