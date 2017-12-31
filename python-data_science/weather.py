import pandas
import matplotlib.pyplot as plt
from datetime import datetime

data = pandas.read_csv("weather_year.csv")

data.columns = ["date", "max_temp", "mean_temp", "min_temp", "max_dew",
                "mean_dew", "min_dew", "max_humidity", "mean_humidity",
                "min_humidity", "max_pressure", "mean_pressure",
                "min_pressure", "max_visibilty", "mean_visibility",
                "min_visibility", "max_wind", "mean_wind", "min_wind",
                "precipitation", "cloud_cover", "events", "wind_dir"]


first_date = data.date.values[0]
#print(datetime.strptime(first_date, "%Y-%m-%d"))
data.date = data.date.apply(lambda d: datetime.strptime(d, "%Y-%m-%d"))
#print(data.date.head())

# makes the date data go into the data index
data.index = data.date
print(data.ix[datetime(2012, 8, 19)])

# drops all date data
data = data.drop(["date"], axis=1)
data.columns

Index([max_temp, mean_temp, min_temp, max_dew, mean_dew, min_dew, max_humidity, mean_humidity, min_humidity, max_pressure, mean_pressure, min_pressure, max_visibilty, mean_visibility, min_visibility, max_wind, mean_wind, min_wind, precipitation, cloud_cover, events, wind_dir], dtype=object)


plt.show()
