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
    #raise NotImplementedError("Implementar esta función")
    #cwd = os.getcwd()
    #path = os.path.join(cwd,"data_lake/business/precios-diarios.csv")
    #dfp = pd.read_csv("data_lake/business/precios-diarios.csv")
    #dfp.to_csv(os.path.join(cwd, 'data_lake/business/features/precios_diarios.csv') , index=False )
    #dfp.to_csv('data_lake/business/features/precios-diarios.csv' , index=False )

    import pandas as pd

    datos_precios_diarios = pd.read_csv(
        "data_lake/business/precios-diarios.csv", index_col=0
    )

    datos_precios_diarios.to_csv(
        "data_lake/business/features/precios_diarios.csv",
        encoding="utf-8",
        index=False,
    )



if __name__ == "__main__":
    import doctest
    make_features()
    doctest.testmod()
