import csv
import numpy as np
import pandas as pd
import plotly.express as px

def getDataSource(data_path):
    coffee_amt = []
    sleep_hours = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            coffee_amt.append(float(row["Coffee in ml"]))
            sleep_hours.append(float(row["sleep in hours"]))

    return {"x" : coffee_amt, "y": sleep_hours}

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print("Correlation between ml of coffee and hours of sleep :-  \n--->",correlation[0,1])

def setup():
    data_path  = "data2.csv"

    datasource = getDataSource(data_path)
    findCorrelation(datasource)

setup()