"""
Cree el data lake con sus capas.
Esta función debe crear la carpeta `data_lake` en la raiz del proyecto.
"""
import os


def create_data_lake():
    """
    Crea el data lake con sus capas.
    """

    os.mkdir("./data_lake")
    carpetas = ["landing", "raw", "cleansed", "business"]
    carpetas_business = ["reports", "features", "forecasts"]
    _=[os.mkdir(os.path.join("data_lake/", c)) for c in carpetas]
    _=[os.mkdir(os.path.join("data_lake/business/", c))
     for c in carpetas_business]
    os.mkdir("./data_lake/business/reports/figures")
    return None
    #raise NotImplementedError("Implementar esta función")


if __name__ == "__main__":
    import doctest
    create_data_lake()
    doctest.testmod()
