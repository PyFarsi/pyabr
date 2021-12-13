'''
    Pyabr OS

    Python Cloud Operating System Platform (c) 2021 PyFarsi. Free Software GNU General Public License v3.0

    - Informations

    * Name:             Pyabr
    * Founder:          Mani Jamali
    * Developers:       PyFarsi Community
    * Package Manager:  Paye, PyPI
    * License:          GNU General Publice License v3.0

    - Official Website

    * Persian Page:     https://pyabr.ir
    * English Page:     https://en.pyabr.ir
'''

from pyabr.core import *
from pyabr.quick import *
import requests

class MainApp (MainApp):
    tempx = 0
    def tempK_(self):
        self.tempx = 2
        self.loop()
    def tempF_(self):
        self.tempx = 1
        self.loop()
    def tempC_(self):
        self.tempx = 0
        self.loop()

    def loop (self):
        Url = f"https://api.openweathermap.org/data/2.5/weather?q={files.readall('/etc/default/baadcity')}&appid=6f3b33e8218c2f0a443e3d8db121bb68"
        result = requests.get(Url)
        data = result.json()
        main = data["main"]
        pre_temp = main["temp"]
        temp = pre_temp - 275.15
        temp = round(temp)
        pressure = main["pressure"]
        tempf = round(int(temp) * 9 / 5 + 32)
        humidity = main["humidity"]
        weather = data["weather"]
        description = weather[0]["description"]
        type = weather[0]['main'].lower()
        tempf = int(int(temp)*9/5+32)

        self.txtTemp = self.findChild('txtTemp')
        self.background = self.findChild('background')

        if self.tempx==0:
            self.txtTemp.setProperty('text',res.num(str(temp))+' °C')
        elif self.tempx==1:
            self.txtTemp.setProperty('text',res.num(str(tempf))+' °F')
        elif self.tempx==2:
            self.txtTemp.setProperty('text',res.num(str(pre_temp))+' k')

        if 'few' in type and 'wind' in type and 'clouds' in type:
            self.background.setProperty('source',res.qmlget(res.etc('baad','BaaD_FewClouds')))
        elif 'clear' in type and 'wind' in type:
            self.background.setProperty('source',res.qmlget(res.etc('baad','BaaD_Clear')))
        elif 'snow' in type and 'scattered' in type:
            self.background.setProperty('source',res.qmlget(res.etc('baad','Baad_Snow')))
        elif 'shower' in type and 'scattered' in type:
            self.background.setProperty('source',res.qmlget(res.etc('baad','Baad_Rain')))
        elif 'cloud' in type and 'wind' in type:
            self.background.setProperty('source',res.qmlget(res.etc('baad','BaaD_Clouds')))
        elif 'many' in type and 'clouds' in type and 'wind' in type:
            self.background.setProperty('source',res.qmlget(res.etc('baad','BaaD_FewClouds')))
        elif 'many' in type and 'clouds' in type:
            self.background.setProperty('source',res.qmlget(res.etc('baad','BaaD_FewClouds')))
        elif 'freezing' in type and 'rain' in type:
            self.background.setProperty('source',res.qmlget(res.etc('baad','BaaD_Frozen')))
        elif 'overcast' in type and 'wind' in type:
            self.background.setProperty('source',res.qmlget(res.etc('baad','BaaD_FewClouds')))
        elif 'clear' in type:
            self.background.setProperty('source',res.qmlget(res.etc('baad','BaaD_Clear')))
        elif 'fog' in type:
            self.background.setProperty('source',res.qmlget(res.etc('baad','BaaD_Fog')))
        elif 'hail' in type:
            self.background.setProperty('source',res.qmlget(res.etc('baad','BaaD_Hails')))
        elif 'mist' in type:
            self.background.setProperty('source',res.qmlget(res.etc('baad','BaaD_BlackClouds')))
        elif 'snow' in type and 'rain' in type:
            self.background.setProperty('source',res.qmlget(res.etc('baad','BaaD_Rain')))
        elif 'snow' in type:
            self.background.setProperty('source',res.qmlget(res.etc('baad','Baad_Snow')))
        elif 'storm' in type:
            self.background.setProperty('source',res.qmlget(res.etc('baad','BaaD_‌BlackClouds')))
        elif 'showers' in type:
            self.background.setProperty('source',res.qmlget(res.etc('baad','BaaD_Rain')))
        elif 'overcast' in type:
            self.background.setProperty('source',res.qmlget(res.etc('baad','BaaD_Clouds')))
        elif 'rain' in type:
            self.background.setProperty('source',res.qmlget(res.etc('baad','BaaD_Rain')))
        elif 'few' in type:
            self.background.setProperty('source',res.qmlget(res.etc('baad','BaaD_FewClouds')))
        elif 'clouds' in type:
            self.background.setProperty('source',res.qmlget(res.etc('baad','BaaD_Clouds')))
        else:
            self.background.setProperty('source',res.qmlget(res.etc('baad','BaaD_Clear')))

        QTimer.singleShot(5000,self.loop)

    def __init__(self):
        super(MainApp, self).__init__()

        self.load (res.get('@layout/baad'))
        self.setProperty('title',res.get('@string/baad'))

        self.loop()

        self.tempF = self.findChild('tempF')
        self.tempF.clicked.connect (self.tempF_)
        self.tempC = self.findChild('tempC')
        self.tempC.clicked.connect (self.tempC_)
        self.tempK = self.findChild('tempK')
        self.tempK.clicked.connect (self.tempK_)

application = QtGui.QGuiApplication([])
application.setWindowIcon (QIcon(res.get(res.etc('baad','logo'))))

def cityWriter (city):
    files.write ('/etc/default/baadcity',city)
    app.start('baad','')

try:
    w = MainApp()
except:
    w = Input (res.get('@string/e_city'),cityWriter)

application.exec()