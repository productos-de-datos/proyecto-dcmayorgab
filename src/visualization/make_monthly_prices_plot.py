import os
import pandas as pd
import matplotlib.pyplot as plt

def make_monthly_prices_plot():
    """Crea un grafico de lines que representa los precios promedios diarios.

    Usando el archivo data_lake/business/precios-diarios.csv, crea un grafico de
    lines que representa los precios promedios diarios.

    El archivo se debe salvar en formato PNG en data_lake/business/reports/figures/daily_prices.png.

    """
    # raise NotImplementedError("Implementar esta función")
    cwd=os.getcwd()
    path=os.path.join(cwd, 'data_lake/business/precios-mensuales.csv')
    img_path=os.path.join(cwd, 'data_lake/business/reports/figures/monthly_prices.png')
    df=pd.read_csv(path )
    df.plot.line(x='Fecha', y='Precio')
    plt.locator_params(nbins=8)
    plt.savefig(img_path)

if __name__ == "__main__":
    import doctest
    make_monthly_prices_plot()
    doctest.testmod()
