import pandas as pd
import matplotlib.pyplot as plt

f=pd.read_csv("weather.csv")
print(f.head())

f["date"] = pd.to_datetime(f["time"], dayfirst=True)
#dayfirst used because the time in CSV was not in mm-dd-yyyy this line
#tells pd that date is first
f.drop(columns=["time"], inplace=True)

#now we rename the columns for much better interpretation
f.rename(columns={
    "rain_sum (mm)": "Rainfall",
    "wind_speed_10m_max (km/h)": "WindSpeed",
    "temperature_2m_max (°C)": "Temp_Max",
    "temperature_2m_min (°C)": "Temp_Min"
}, inplace=True)
print(f.columns,"/n")

#average temperature daily
f["AVG Temperature"] = (f["Temp_Max"] + f["Temp_Min"]) / 2
print(f["AVG Temperature"],"/n")

#average monthly temperature
f["Month"] = f["date"].dt.month
month_avg = f.groupby("Month")["AVG Temperature"].mean()
print("Monthly Average Temperature:")
print(month_avg)

#Hottest and coldest date
h= f.loc[f["Temp_Max"].idxmax()]
c= f.loc[f["Temp_Min"].idxmin()]
print("Hottest Day:", h["date"].date(), h["Temp_Max"], "°C")
print("Coldest Day:", c["date"].date(), c["Temp_Min"], "°C")

#for total rainfall and rainy days
total_rainfall= f["Rainfall"].sum()
rainy_days= f[f["Rainfall"] > 0].shape[0]
print("Total Rainfall:", total_rainfall, "mm")
print("Rainy Days:", rainy_days)

#Summer vs Winter comparison
#summer months (April, May, June).
#winter we take December, january and feb
#comparision od mean avg temperature in these seasons
summer=f[f["Month"].isin([4, 5, 6])]
winter=f[f["Month"].isin([12, 1, 2])]
print("Summer Avg Temp:", summer["AVG Temperature"].mean())
print("Winter Avg Temp:", winter["AVG Temperature"].mean())


################################################################
#final summary number report
print("\n" + "="*40)
print("        WEATHER SUMMARY REPORT")
print("="*40)

# Date range
print("Date Range:")
print("From:", f["date"].min().date())
print("To  :", f["date"].max().date())

# Temperature summary
print("\nTemperature Summary:")
print("Average Temperature:", round(f["AVG Temperature"].mean(), 2), "°C")
print("Maximum Temperature:", round(f["AVG Temperature"].max(), 2), "°C")
print("Minimum Temperature:", round(f["AVG Temperature"].min(), 2), "°C")

hottest_day = f.loc[f["AVG Temperature"].idxmax()]
coldest_day = f.loc[f["AVG Temperature"].idxmin()]

print("Hottest Day :", hottest_day["date"].date(), 
      "(", round(hottest_day["AVG Temperature"], 2), "°C )")

print("Coldest Day :", coldest_day["date"].date(), 
      "(", round(coldest_day["AVG Temperature"], 2), "°C )")

# Rainfall summary
print("\nRainfall Summary:")
print("Total Rainfall:", round(f["Rainfall"].sum(), 2), "mm")
print("Rainy Days   :", (f["Rainfall"] > 0).sum())

# Wind speed summary
print("\nWind Speed Summary:")
print("Average Wind Speed:", round(f["WindSpeed"].mean(), 2))
print("Maximum Wind Speed:", round(f["WindSpeed"].max(), 2))

# Seasonal comparison
summer_avg = f[f["Month"].isin([4,5,6])]["AVG Temperature"].mean()
winter_avg = f[f["Month"].isin([12,1,2])]["AVG Temperature"].mean()

print("\nSeasonal Comparison:")
print("Summer Average Temperature:", round(summer_avg, 2), "°C")
print("Winter Average Temperature:", round(winter_avg, 2), "°C")

print("\n" + "="*40)
print("        END OF REPORT")
print("="*40)
################################################################


#now let's analyse data in the best way possible by visualization using graphs

#temperature trend
plt.figure()
plt.plot(f["date"], f["AVG Temperature"])
plt.xlabel("Date")
plt.ylabel("Average Temperature (°C)")
plt.title("Temperature Trend Over Time")
plt.show()

#rainfall trend
plt.figure()
plt.plot(f["date"],f["Rainfall"])
plt.xlabel("Date")
plt.ylabel("Rainfall (mm)")
plt.title("Rainfall Trend Over Time")
plt.show()

#monthly raifall trend
monthly_rainfall = f.groupby("Month")["Rainfall"].sum()
plt.figure()
plt.bar(monthly_rainfall.index, monthly_rainfall.values)
plt.xlabel("Month")
plt.ylabel("Total Rainfall (mm)")
plt.title("Monthly Rainfall Pattern")
plt.show()


#summer vs winter plots
summer = f[f["Month"].isin([4, 5, 6])]
winter = f[f["Month"].isin([12, 1, 2])]

plt.figure()
plt.plot(summer["date"], summer["AVG Temperature"], label="Summer Temperature")
plt.plot(winter["date"], winter["AVG Temperature"], label="Winter Temperature")
plt.xlabel("Date")
plt.ylabel("Average Temperature (°C)")
plt.title("Inverse Temperature Trends: Summer vs Winter")
plt.legend()
plt.show()

#wind speed trend
plt.figure()
plt.plot(f["date"],f["WindSpeed"])
plt.xlabel("Date")
plt.ylabel("Wind Speed")
plt.title("Wind Speed Trend Over Time")
plt.show()

#wind speed trend month wise
monthly_wind = f.groupby("Month")["WindSpeed"].mean()

plt.figure()
plt.bar(monthly_wind.index, monthly_wind.values)
plt.xlabel("Month")
plt.ylabel("Average Wind Speed")
plt.title("Monthly Average Wind Speed")
plt.show()










