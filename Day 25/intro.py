"""with open("weather_data.csv",mode="r") as data:
    data_list=data.readlines()
    for val in data_list:
        val=val.strip()
print(data_list)
"""

"""import csv
with open("weather_data.csv") as data_file:
    data=csv.reader(data_file)
    temperature=[]
    for row in data:
        if(row[1]=='temp'):
            continue
        num=int(row[1])
        temperature.append(num)
temperature.pop(0)
print(temperature)
"""

import pandas

data=pandas.read_csv("weather_data.csv")
#print(data["temp"])
"""data_dict=data.to_dict()
data_list=data["temp"].to_list
print(data_list)
average=data["temp"].mean()
maximum=data["temp"].max()
print(f"Maximum is {maximum}")"""
maximum=data["temp"].max()
#GET the row
#print(data[data.temp==maximum])
"""monday=data[data.day=="Monday"]
monday_temp=int(monday.temp)
monday_temp_F=monday_temp*1.8+32

print(monday_temp_F)"""
#Create a data frame from scratch
data_dict={
    "Name":["Rahima","Mahira","Humaira"],
    "Scores":[55,93,88]
}
data=pandas.DataFrame(data_dict)
print(data)
data.to_csv("new_data.csv")

