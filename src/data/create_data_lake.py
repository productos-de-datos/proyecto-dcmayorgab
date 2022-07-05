

def create_data_lake():
    """Cree el data lake con sus capas.

    Esta función debe crear la carpeta `data_lake` en la raiz del proyecto. El data lake contiene
    las siguientes subcarpetas:

    ```
    .
    |
    \___ data_lake/
         |___ landing/
         |___ raw/
         |___ cleansed/
         \___ business/
              |___ reports/
              |    |___ figures/
              |___ features/
              |___ forecasts/

    ```


    """
    # raise NotImplementedError("Implementar esta función")

    import os

    os.mkdir("data_lake")

    directory = [
        "landing",
        "raw",
        "cleansed",
        "business",
    ]

    for folder in directory:
        os.mkdir(os.path.join("./data_lake/", folder))

    dir_business = [
        "business/reports",
        "business/reports/figures",
        "business/features",
        "business/forecasts",
    ]

    for folder in dir_business:
        os.mkdir(os.path.join("./data_lake/", folder))

if __name__ == "__main__":
    import doctest
    create_data_lake() 
    doctest.testmod()
