import csv

def readUsersCsvFile(file: str):
    with open(file, 'r') as file:
        fileData = csv.DictReader(file)
        return list(fileData)