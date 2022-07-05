import os
import pandas as pd

def compute_monthly_prices():
    """Compute los precios promedios mensuales.

    Usando el archivo data_lake/cleansed/precios-horarios.csv, compute el prcio
    promedio mensual. Las
    columnas del archivo data_lake/business/precios-mensuales.csv son:

    * fecha: fecha en formato YYYY-MM-DD

    * precio: precio promedio mensual de la electricidad en la bolsa nacional



    """
    # raise NotImplementedError("Implementar esta función")
    cwd=os.getcwd()
    path=os.path.join(cwd, 'data_lake/cleansed/precios-horarios.csv') 
    df=pd.read_csv(path)
    df['Precio']=df['Precio'].astype('float')
    df['Fecha']=pd.to_datetime(df['Fecha'], format='%Y-%m-%d')
    df=df[['Fecha','Precio']].groupby(pd.Grouper(key='Fecha', freq='1M')).mean().reset_index()
    df['Fecha']=df['Fecha'].apply(lambda dt: dt.replace(day=1))
    df.to_csv(os.path.join(cwd, 'data_lake/business/precios-mensuales.csv') , index=False )

if __name__ == "__main__":
    import doctest
    compute_monthly_prices()
    doctest.testmod()
