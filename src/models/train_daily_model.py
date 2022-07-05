import os
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.neural_network import MLPRegressor
import pickle



def train_daily_model():
    """Entrena el modelo de pronóstico de precios diarios.

    Con las features entrene el modelo de proóstico de precios diarios y
    salvelo en models/precios-diarios.pkl


    """
    # raise NotImplementedError("Implementar esta función")
   
    cwd = os.getcwd()
    path = os.path.join(cwd,"data_lake/business/features/precios_diarios.csv")
    path_model = os.path.join(cwd,"models/precios-diarios.pkl")
    df = pd.read_csv(path)
    data=list(df['Precio'])

    data_d1 = [data[t] - data[t - 1] for t in range(1, len(data))]
    data_d1d12 = [data_d1[t] - data_d1[t - 7] for t in range(7, len(data_d1))]
    scaler = MinMaxScaler()
    data_d1d12_scaled = scaler.fit_transform(np.array(data_d1d12).reshape(-1, 1))
    data_d1d12_scaled = [u[0] for u in data_d1d12_scaled]
    P = 7
    X = []
    for t in range(P - 1, len(data_d1d12_scaled) - 1):
        X.append([data_d1d12_scaled[t - n] for n in range(P)])
    d = data_d1d12_scaled[P:]
    H = 5  # Se escoge arbitrariamente

    np.random.seed(123456)

    mlp = MLPRegressor(
        hidden_layer_sizes=(H,),
        activation="tanh",
        learning_rate="adaptive",
        momentum=0.0,
        learning_rate_init=0.002,
        max_iter=100000,
    )
    mlp.fit(X[0:8675], data_d1d12_scaled[0:8675]) 
    pickle.dump(mlp, open("src/models/precios-diarios.pkl", 'wb'))

if __name__ == "__main__":
    import doctest
    train_daily_model()
    doctest.testmod()
