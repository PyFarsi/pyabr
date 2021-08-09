'''
    Pyabr OS

    Python Cloud Operating System Platform (c) 2021 PyFarsi. Free Software GNU General Public License v3.0

    - Informations

    * Name:             Pyabr
    * Founder:          Mani Jamali
    * Developers:       PyFarsi Community
    * Package Manager:  Paye, Apt, Dpkg, PyPI
    * License:          GNU General Publice License v3.0

    * Source code:      https://github.com/PyFarsi/pyabr
    * PyPI:             https://pypi.org/project/pyabr

    - Download Pyabr OS

    * AMD64, Intel64:   https://dl.pyabr.ir/pyabr-x86_64.iso     
    * ARM64:            https://dl.pyabr.ir/pyabr-arm64.img
    * Platform:         https://dl.pyabr.ir/stor.sb
    * Wheel Package:    https://dl.pyabr.ir/pyabr.whl
    
    - Channels:

    * Official Website: https://pyabr.ir
    * Telegram Channel: https://t.me/pyfarsi
    * Gap Channel:      https://gap.im/pyabr
    * Sorosh Channel:   https://splus.ir/pyabr
    * Instagram:        https://instagram.com/pyabrir
    * Hoorsa:           https://hoorsa.com/pyabr
    * Aparat:           https://aparat.com/pyabr

'''
import requests
import sys
from libabr import *
files = Files()
colors = Colors()
# func
if sys.argv[1:]==[]:
    CityName = input('Enter your city name: ').lower()
else:
    CityName = sys.argv[1]

result = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={CityName}&appid=6f3b33e8218c2f0a443e3d8db121bb68")
data = result.json()
if data["cod"] == "404":
    colors.show('weather','fail',"Something wrong!")
else:
    # گرفتن اطلاعات
    main = data["main"]
    # گرفتن دما
    pre_temp = main["temp"]
    temp = pre_temp - 275.15
    temp = round(temp)
    # گرفتن فشار
    pressure = main["pressure"]
    # رطوبت هوا
    humidity = main["humidity"]
    # توضیحات
    weather = data["weather"]
    description = weather[0]["description"]
    print("Temperature (k):",int(pre_temp))
    print("Temperature (C):",temp)
    print("Temperature (F):",str(int(int(temp)*9/5+32))) # http://banbaey.blogfa.com/post/690
    print("Air pressure:",pressure)
    print("Humidity:",humidity)
    print("Description:",description)

    files.write('/etc/location/city', CityName)