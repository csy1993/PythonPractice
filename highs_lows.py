'''
* @Author: csy 
* @Date: 2019-06-11 22:37:54 
* @Last Modified by:   csy 
* @Last Modified time: 2019-06-11 22:37:54 
'''
import csv
from matplotlib import pyplot as plt
from datetime import datetime

# filename='sitka_weather_07-2014.csv'
# filename='sitka_weather_2014.csv'
filename='death_valley_2014.csv'
with open(filename) as f:
    reader=csv.reader(f)
    header_row=next(reader)
    dates,highs,lows=[],[],[]
    for row in reader:
        try:
            current_date=datetime.strptime(row[0],"%Y-%m-%d")
            high=int(row[1])
            low=int(row[3])
        except ValueError:
            print(current_date,'missing data')
        else:
            highs.append(high)
            dates.append(current_date)
            lows.append(low)
    print("High temperature is:\n"+str(highs))
    for index,column_header in enumerate(header_row):
        print(index,column_header)
fig=plt.figure(dpi=128,figsize=(10,6))
plt.plot(dates,highs,c='red',alpha=0.5)#alpha为透明度,0为透明
plt.plot(dates,lows,c='blue',alpha=0.5)
plt.fill_between(dates,highs,lows,facecolor='blue',alpha=0.1)
# plt.title("Daily high temperatures,July 2014",fontsize=24)
plt.title("Daily high and low temperatures - 2014",fontsize=24)
plt.xlabel('',fontsize=16)
fig.autofmt_xdate()#避免横坐标重叠
plt.ylabel("Temperature(F)",fontsize=16)
plt.tick_params(axis="both",which='major',labelsize=16)
plt.show()