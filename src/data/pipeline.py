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
import sys

sys.path.append("src/data")

class IngestData(luigi.Task):

    def output(self):
        return luigi.LocalTarget('ingest.txt')

    def run(self):
        with self.output().open('w') as f:
            ingest_data.ingest_data()
        
        
class TransformData(luigi.Task):
    
    def requires(self):
        return IngestData()
    
    def output(self):
        return luigi.LocalTarget("TransformData.txt")

    def run(self):
        with self.output().open("w") as outfile:
            transform_data.transform_data()   

class cleanData(luigi.Task):
    def requires(self):
        return TransformData()

    def output(self):
        return luigi.LocalTarget("cleanData.txt")

    def run(self):
        with self.output().open("w") as outfile:
            clean_data.clean_data()

class dailyReports(luigi.Task):
    def requires(self):
        return cleanData()

    def output(self):
        return luigi.LocalTarget("dailyReports.txt")

    def run(self):
        with self.output().open("w") as outfile:
            compute_daily_prices.compute_daily_prices()
            
class monthlyReports(luigi.Task):
    def requires(self):
        return cleanData()

    def output(self):
        return luigi.LocalTarget("monthlyReports.txt")

    def run(self):
        with self.output().open("w") as outfile:
            compute_monthly_prices.compute_monthly_prices()

class reports_prices(luigi.Task):
    def requires(self):
        return [dailyReports(), monthlyReports()]
    
if __name__ == "__main__":
    import doctest

    luigi.run(["reports_prices"])
    doctest.testmod()



