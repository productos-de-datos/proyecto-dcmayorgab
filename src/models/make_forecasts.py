"""Construya los pronosticos con el modelo entrenado final.

Cree el archivo data_lake/business/forecasts/precios-diarios.csv. Este
archivo contiene tres columnas:

* La fecha.
* El precio promedio real de la electricidad.
* El pronóstico del precio promedio real.

"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.neural_network import MLPRegressor
import matplotlib.pyplot as plt
import pickle


def make_forecasts():
    """
    Construye los pronosticos con el modelo entrenado final.

    """
    # raise NotImplementedError("Implementar esta función")
    #cwd = os.getcwd()
    try:
        path = "data_lake/business/features/precios-diarios.csv"
        path_model = "models/precios-diarios.pkl"
        path_forecasts = "data_lake/business/forecasts/precios-diarios.csv"
        df = pd.read_csv(path)
        data = list(df['Precio'])
        data_d1 = [data[t] - data[t - 1] for t in range(1, len(data))]

        data_d1d12 = [data_d1[t] - data_d1[t - 7]
                      for t in range(7, len(data_d1))]
        scaler = MinMaxScaler()
        data_d1d12_scaled = scaler.fit_transform(
            np.array(data_d1d12).reshape(-1, 1))
        data_d1d12_scaled = [u[0] for u in data_d1d12_scaled]
        P = 7

        X = []
        for t in range(P - 1, len(data_d1d12_scaled) - 1):
            X.append([data_d1d12_scaled[t - n] for n in range(P)])

        d = data_d1d12_scaled[P:]
        mlp = pickle.load(open('src/models/precios-diarios.pkl', 'rb'))

        y_d1d12_scaled_m2 = mlp.predict(X)

        # Agrega el periodo que se quito
        y_d1d12_scaled_m2 = data_d1d12_scaled[0:P] + y_d1d12_scaled_m2.tolist()

        y_d1d12_m2 = scaler.inverse_transform(
            [[u] for u in y_d1d12_scaled_m2])  # Escalado
        y_d1d12_m2 = [u[0] for u in y_d1d12_m2.tolist()]

        y_d1_m2 = [y_d1d12_m2[t] + data_d1[t]
                   for t in range(len(y_d1d12_m2))]  # Agregar componente ciclica
        y_d1_m2 = data_d1[0:P] + y_d1_m2

        y_m2 = [y_d1_m2[t] + data[t]
                for t in range(len(y_d1_m2))]  # Agregar tendencia

        y_m2 = [data[0]] + y_m2

        df.rename(columns={'Precio': 'Precio_Real'}, inplace=True)

        df['Precio_Pronostico'] = y_m2

        df.to_csv(path_forecasts, index=False)

    except:  # pylint: disable=W0702
        return None


if __name__ == "__main__":
    import doctest
    make_forecasts()
    doctest.testmod()
