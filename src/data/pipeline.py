"""
Construya un pipeline de Luigi que:

* Importe los datos xls
* Transforme los datos xls a csv
* Cree la tabla unica de precios horarios.
* Calcule los precios promedios diarios
* Calcule los precios promedios mensuales

En luigi llame las funciones que ya creo.
"""

import ingest_data
import transform_data
import clean_data
import compute_daily_prices
import compute_monthly_prices
import luigi

# sys.path.append("src/data")

class Ingest_Data(luigi.Task):
    """Tarea de ingesta"""
    def output(self):
        return luigi.LocalTarget('ingest.txt')

    def run(self):
        with self.output().open('w'):
            ingest_data.ingest_data()


class TransformData(luigi.Task):
    """Tarea de transformar"""
    def requires(self):
        return Ingest_Data()

    def output(self):
        return luigi.LocalTarget("TransformData.txt")

    def run(self):
        with self.output().open("w") as outfile:
            transform_data.transform_data()


class cleanData(luigi.Task):
    """Tarea de limpiar"""
    def requires(self):
        return TransformData()

    def output(self):
        return luigi.LocalTarget("cleanData.txt")

    def run(self):
        with self.output().open("w") as outfile:
            clean_data.clean_data()


class dailyReports(luigi.Task):
    """Tarea de calculo diario"""
    def requires(self):
        return cleanData()

    def output(self):
        return luigi.LocalTarget("data_lake/business/precios-dias.csv")

    def run(self):
        with self.output().open("w") as outfile:
            compute_daily_prices.compute_daily_prices()


class monthlyReports(luigi.Task):
    """Tarea de calculo mensual"""
    def requires(self):
        return cleanData()

    def output(self):
        return luigi.LocalTarget("data_lake/business/precios-mes.csv")

    def run(self):
        with self.output().open("w") as outfile:
            compute_monthly_prices.compute_monthly_prices()


class reports_prices(luigi.Task):
    """Tarea de reportes"""
    def requires(self):
        return [dailyReports(), monthlyReports()]


if __name__ == "__main__":
    import doctest
    luigi.run(["reports_prices", "--local-scheduler"])
    doctest.testmod()
