"""
Cree el archivo data_lake/business/features/precios-diarios.csv. Este
archivo contiene la información para pronosticar los precios diarios de la
electricidad con base en los precios de los días pasados. Las columnas
correspoden a las variables explicativas del modelo, y debe incluir,
adicionalmente, la fecha del precio que se desea pronosticar y el precio
que se desea pronosticar (variable dependiente).
En la carpeta notebooks/ cree los notebooks de jupyter necesarios para
analizar y determinar las variables explicativas del modelo.
"""

#import os
import pandas as pd


def make_features():
    """Prepara datos para pronóstico.

    Debido a que es una serie de tiempo no es necesario crear mas caracteristicas

    """
    try :
        dfp = pd.read_csv("data_lake/business/precios-diarios.csv")

        dfp.to_csv('data_lake/business/features/precios-diarios.csv',index=False)

        return dfp

    except : # pylint: disable=W0702
        return None

if __name__ == "__main__":
    import doctest
    make_features()
    doctest.testmod()
