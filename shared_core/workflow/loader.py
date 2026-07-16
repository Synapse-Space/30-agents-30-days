import csv

class CSVLoader:
    def load(self,path):
        with open(path, newline="") as file:
            render=csv.DictReader(file)

            return list(render)