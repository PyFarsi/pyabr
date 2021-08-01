from libabr import System, Control, Files, Colors, Script, App, Res
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import uic
import requests

control = Control()
files = Files()
colors = Colors()
app = App()
res = Res()
def getdata (name):
    return control.read_record (name,'/etc/gui')

def Upper (getcityname):
    getcitynamef = getcityname[0].upper()
    getcitynamel = getcityname[1:]
    return f"{getcitynamef}{getcitynamel}"

class MainApp(QWidget):

    def onCloseProcess (self):
        if not app.check('weather'):
            self.Widget.Close()
        else:
            QTimer.singleShot(1,self.onCloseProcess)

    def onCheckCity (self):
        if self.External==[]:
            if files.readall('/etc/location/city')=='':
                self.Widget.hide()
                app.switch('weather')
                self.Env.RunApp('input', [res.get('@string/city'), self.w_])
                app.switch('weather')
            else:
                self.External = [files.readall('/etc/location/city')]
        else:
            try:
                self.External = [files.readall('/etc/location/city')]
            except:
                self.Widget.hide()
                app.switch('weather')
                self.Env.RunApp('input', [res.get('@string/city'), self.w_])
                app.switch('weather')

    def __init__(self, ports):
        super(MainApp, self).__init__()

        self.Env = ports[1]
        self.Widget = ports[2]
        self.External = ports[4]

        self.onCloseProcess()
        self.onCheckCity()

        self.Widget.Resize(self, 600, 500)
        self.Widget.SetWindowTitle(res.get('@string/app_name'))
        self.Widget.SetWindowIcon(QIcon(res.get(res.etc('weather',"logo"))))
        self.vmbox = QVBoxLayout()
        self.btnInfo = QToolButton()
        self.btnInfo.setMinimumSize(128,128)
        self.btnInfo.setIconSize(QSize(128,128))
        self.btnInfo.setStyleSheet(f'background-color: {getdata("appw.body.bgcolor")};color: {getdata("appw.body.fgcolor")};border-radius: 64% 64%;margin-left: {str(int(self.width()/2.666666))}%;')
        self.btnInfo.setIcon(QIcon(res.get('@icon/breeze-cloud')))
        self.vmbox.addWidget(self.btnInfo)
        self.extral = QWidget()
        self.vmbox.addWidget(self.extral)
        self.hbox = QHBoxLayout()
        self.setLayout(self.vmbox)
        self.extral.setLayout(self.hbox)
        self.text1 = QTextBrowser()
        self.extral.setStyleSheet(f'background-color: {getdata("appw.body.bgcolor")};color: {getdata("appw.body.fgcolor")}')
        self.text1.setAlignment(Qt.AlignRight)
        self.text1.setStyleSheet(
            f'background-color: {getdata("appw.body.bgcolor")};color: {getdata("appw.body.fgcolor")}')
        self.text1.setFont(self.Env.font())

        self.text2 = QTextBrowser()
        self.text2.setStyleSheet(
            f'background-color: {getdata("appw.body.bgcolor")};color: {getdata("appw.body.fgcolor")}')
        self.text2.setAlignment(Qt.AlignLeft)
        self.text2.setFont(self.Env.font())

        ##################################################

        self.text1.append('City:')
        self.text1.append('Temperature:')
        self.text1.append('Temperature (k):')
        self.text1.append('Temperature (F):')
        self.text1.append('Air pressure:')
        self.text1.append('Humidity:')
        self.text1.append('Description:')

        try:
                Url = f"https://api.openweathermap.org/data/2.5/weather?q={self.External[0]}&appid=6f3b33e8218c2f0a443e3d8db121bb68"
                result = requests.get(Url)
                data = result.json()

                # گرفتن اطلاعات
                main = data["main"]
                # گرفتن دما
                pre_temp = main["temp"]
                temp = pre_temp - 275.15
                temp = round(temp)
                # گرفتن فشار
                pressure = main["pressure"]
                tempf = round(int(temp) * 9 / 5 + 32)
                # رطوبت هوا
                humidity = main["humidity"]

                # توضیحات
                weather = data["weather"]
                description = weather[0]["description"]

                type = weather[0]['main'].lower()

                if 'few' in type and 'wind' in type and 'clouds' in type:
                    self.btnInfo.setIcon(QIcon(res.get('@icon/breeze-weather-few-clouds-wind')))
                elif 'clear' in type and 'wind' in type:
                    self.btnInfo.setIcon(QIcon(res.get('@icon/breeze-weather-clear-wind')))
                elif 'snow' in type and 'scattered' in type:
                    self.btnInfo.setIcon(QIcon(res.get('@icon/breeze-weather-snow-scattered')))
                elif 'shower' in type and 'scattered' in type:
                    self.btnInfo.setIcon(QIcon(res.get('@icon/breeze-weather-snow-scattered')))
                elif 'cloud' in type and 'wind' in type:
                    self.btnInfo.setIcon(QIcon(res.get('@icon/breeze-weather-clouds-wind')))
                elif 'many' in type and 'clouds' in type and 'wind' in type:
                    self.btnInfo.setIcon(QIcon(res.get('@icon/breeze-weather-many-clouds-wind')))
                elif 'many' in type and 'clouds' in type:
                    self.btnInfo.setIcon(QIcon(res.get('@icon/breeze-weather-many-clouds')))
                elif 'freezing' in type and 'rain' in type:
                    self.btnInfo.setIcon(QIcon(res.get('@icon/breeze-weather-freezing-rain')))
                elif 'overcast' in type and 'wind' in type:
                    self.btnInfo.setIcon(QIcon(res.get('@icon/breeze-weather-overcast-wind')))
                elif 'clear' in type:
                    self.btnInfo.setIcon(QIcon(res.get('@icon/breeze-weather-clear')))
                elif 'fog' in type:
                    self.btnInfo.setIcon(QIcon(res.get('@icon/breeze-weather-fog')))
                elif 'hail' in type:
                    self.btnInfo.setIcon(QIcon(res.get('@icon/breeze-weather-hail')))
                elif 'mist' in type:
                    self.btnInfo.setIcon(QIcon(res.get('@icon/breeze-weather-mist')))
                elif 'snow' in type and 'rain' in type:
                    self.btnInfo.setIcon(QIcon(res.get('@icon/breeze-weather-snow-rain')))
                elif 'snow' in type:
                    self.btnInfo.setIcon(QIcon(res.get('@icon/breeze-weather-snow')))
                elif 'storm' in type:
                    self.btnInfo.setIcon(QIcon(res.get('@icon/breeze-weather-storm')))
                elif 'showers' in type:
                    self.btnInfo.setIcon(QIcon(res.get('@icon/breeze-weather-showers')))
                elif 'overcast' in type:
                    self.btnInfo.setIcon(QIcon(res.get('@icon/breeze-weather-overcast')))
                elif 'rain' in type:
                    self.btnInfo.setIcon(QIcon(res.get('@icon/breeze-weather-rain')))
                elif 'few' in type:
                    self.btnInfo.setIcon(QIcon(res.get('@icon/breeze-weather-few-clouds')))
                elif 'clouds' in type:
                    self.btnInfo.setIcon(QIcon(res.get('@icon/breeze-weather-clouds')))
                else:
                    self.btnInfo.setIcon(QIcon(res.get('@icon/breeze-weather-none-available')))


                self.text2.append(Upper(self.External[0]))
                self.text2.append(str(temp))
                self.text2.append(str(pre_temp))
                self.text2.append(str(tempf))
                self.text2.append(str(pressure))
                self.text2.append(str(humidity))
                self.text2.append(Upper(description))
        except:
            app.switch('weather')
            self.Widget.hide()
            self.Env.RunApp('input', [res.get('@string/city'), self.w_])
            app.switch('weather')

        ##################################################

        self.hbox.addWidget(self.text1)
        self.hbox.addWidget(self.text2)


        self.Widget.DisableFloat()

    def w_(self,cityname):
        files.write('/etc/location/city',cityname.lower())
        self.Env.RunApp('weather',[cityname.lower()])