"""
Compute los precios promedios diarios.
Usando el archivo data_lake/cleansed/precios-horarios.csv, compute el prcio
promedio diario (sobre las 24 horas del dia) para cada uno de los dias. Las
columnas del archivo data_lake/business/precios-diarios.csv son:

* fecha: fecha en formato YYYY-MM-DD
* precio: precio promedio diario de la electricidad en la bolsa nacional

"""

import pandas as pd

def compute_daily_prices():
    """
    Computa los precios promedios diarios.
    """
    #raise NotImplementedError("Implementar esta función")

    path='data_lake/cleansed/precios-horarios.csv'
    dfe=pd.read_csv(path)
    dfe['Precio']=dfe['Precio'].astype('float')
    dfe['Fecha']=pd.to_datetime(dfe['Fecha'], format='%Y-%m-%d')
    dfe=dfe[['Fecha','Precio']].groupby(by='Fecha',as_index=False).mean()
    dfe.to_csv( 'data_lake/business/precios-diarios.csv'  , index=False)

if __name__ == "__main__":
    import doctest
    compute_daily_prices()
    doctest.testmod()
