import luigi
from luigi import Task, LocalTarget

class ingestdata(Task):

    def output(self):
        return LocalTarget('data_lake/landing/archivo.txt')

    def run(self):
        from ingest_data import ingest_data
        with self.output().open("w") as outfile:
            ingest_data()

class transformdata(Task):

    def requires(self):
        return ingestdata()
    
    def output(self):
        return LocalTarget('data_lake/raw/archivo.txt')

    def run(self):
        from transform_data import transform_data
        with self.output().open("w") as outfile:
            transform_data()

class cleandata(Task):
    
    def requires(self):
        return transformdata()
    
    def output(self):
        return LocalTarget('data_lake/cleansed/archivo.txt')

    def run(self):
        from clean_data import clean_data
        with self.output().open("w") as outfile:
            clean_data()

class computedailyprices(Task):
    
    def requires(self):
        return cleandata()
    
    def output(self):
        return LocalTarget('data_lake/business/archivo.txt')

    def run(self):
        from compute_daily_prices import compute_daily_prices
        with self.output().open("w") as outfile:
            compute_daily_prices()

class computemonthlyprices(Task):
    
    def requires(self):
        return computedailyprices()
    
    def output(self):
        return LocalTarget('data_lake/business/archivo1.txt')

    def run(self):
        from compute_monthly_prices import compute_monthly_prices
        with self.output().open("w") as outfile:
            compute_monthly_prices()

if __name__ == "__main__":
    luigi.run(["computemonthlyprices", "--local-scheduler"])
    #raise NotImplementedError("Implementar esta función")

if __name__ == "__main__":
    import doctest

    doctest.testmod()


