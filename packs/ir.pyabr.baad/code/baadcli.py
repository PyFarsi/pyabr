import requests
import sys
from pyabr.core import *

# func
if sys.argv[1:]==[]:
    CityName = input('Enter your city name: ').lower()
else:
    CityName = sys.argv[1]

result = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={CityName}&appid=6f3b33e8218c2f0a443e3d8db121bb68")
data = result.json()
if data["cod"] == "404":
    colors.show('baadcli','fail',"Something wrong!")
else:
    # گرفتن اطلاعات
    main = data["main"]
    # گرفتن دما
    pre_temp = main["temp"]
    temp = pre_temp - 275.15
    temp = round(temp)
    tempf = int(int(temp)*9/5+32)
    pressure = main["pressure"]
    humidity = main["humidity"]
    weather = data["weather"]
    description = weather[0]["description"]
    print(f"     Temperature: {str(int(pre_temp))} k | {str(temp)} °C | {str(tempf)} °F")
    print("     Air pressure:",pressure)
    print("         Humidity:",humidity)
    print("      Description:",description)

    files.write('/etc/default/baadcity', CityName)