import pandas
import matplotlib.pyplot as plt
from datetime import datetime

data = pandas.read_csv("improved_water.csv")

data.columns = ["Country", "Year"," Rural"," Urban"," Total"," Rural"," Urban"," Total"]

#print(data.Country.head())
data.Urban.hist()

plt.show()
