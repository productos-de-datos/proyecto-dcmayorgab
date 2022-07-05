import os
import pandas as pd


def make_features():
    """Prepara datos para pronóstico.

    Cree el archivo data_lake/business/features/precios-diarios.csv. Este
    archivo contiene la información para pronosticar los precios diarios de la
    electricidad con base en los precios de los días pasados. Las columnas
    correspoden a las variables explicativas del modelo, y debe incluir,
    adicionalmente, la fecha del precio que se desea pronosticar y el precio
    que se desea pronosticar (variable dependiente).

    En la carpeta notebooks/ cree los notebooks de jupyter necesarios para
    analizar y determinar las variables explicativas del modelo.

    """
    #raise NotImplementedError("Implementar esta función")
    cwd = os.getcwd()
    path = os.path.join(cwd,"data_lake/business/precios-diarios.csv")
    df_precios = pd.read_csv(path)
    df_precios.to_csv(os.path.join(cwd, 'data_lake/business/features/precios_diarios.csv') , index=False )






if __name__ == "__main__":
    import doctest
    make_features()
    doctest.testmod()
