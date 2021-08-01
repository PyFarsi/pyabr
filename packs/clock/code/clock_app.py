#######################################################################################
#  In the name of God, the Compassionate, the Merciful
#  Pyabr (c) 2020 Mani Jamali. GNU General Public License v3.0
#
#  Official Website: 		https://pyabr.ir
#  Programmer & Creator:    Mani Jamali <manijamali2003@gmail.com>
#  Gap channel: 			@pyabr
#  Gap group:   			@pyabr_community
#  Git source:              github.com/PyFarsi/pyabr
#
#######################################################################################

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from libabr import *
from PyQt5 import uic
import requests,shutil,os,importlib
app = App()
res = Res()
files = Files()
control = Control()
commands = Commands()
def getdata (name):
    return control.read_record (name,'/etc/gui')

class MainApp(QMainWindow):
    def showTime_lock (self):

        try:
        # getting current time
            current_time = QTime.currentTime()

        # converting QTime object to string
            label_time = current_time.toString('hh:mm:ss')

        # showing it to the label
            self.lbl.setText(res.num(label_time))
        except:
            pass

        # Define method to handle the start button
    def Start(self):
        app.switch('clock')
            # Set the caption of the start button based on previous caption
        if self.start.text() == res.get('@string/stop'):
            self.start.setText(res.get('@string/resume'))
            self.startWatch = False
        else:
                # making startWatch to true
            self.startWatch = True
            self.start.setText(res.get('@string/stop'))

        # Define method to handle the reset button
    def Reset(self):
        self.startWatch = False
            # Reset all counter variables
        self.counter = 0
        self.minute = '00'
        self.second = '00'
        self.count = '00'
            # Set the initial values for the stop watch
        self.label.setText(res.num(str(self.counter)))

    def showCounter(self):
        # Check the value of startWatch  variable to start or stop the Stop Watch
        if self.startWatch:
            # Increment counter by 1
            self.counter += 1

            # Count and set the time counter value
            cnt = int((self.counter/10 - int(self.counter/10))*10)
            self.count = '0' + str(cnt)

            # Set the second value
            if int(self.counter/10) < 10 :
                self.second = '0' + str(int(self.counter / 10))
            else:
                self.second = str(int(self.counter / 10))
                # Set the minute value
                if self.counter / 10 == 60.0 :
                    self.second == '00'
                    self.counter = 0
                    min = int(self.minute) + 1
                    if min < 10 :
                        self.minute = '0' + str(min)
                    else:
                        self.minute = str(min)


        # Merge the mintue, second and count values
        text = f"{self.minute}:{self.second}:{self.count}"
        # Display the stop watch values in the label
        self.label.setText(res.num(text))

    def __init__(self,ports):
        super(MainApp, self).__init__()

        self.Backend = ports[0]
        self.Env = ports[1]
        self.Widget = ports[2]
        self.AppName = ports[3]
        self.External = ports[4]

        self.setStyleSheet(f'background-color: {getdata("appw.body.bgcolor")};color: {getdata("appw.body.fgcolor")}')
        self.setFont(self.Env.font())
        self.tabs = QTabWidget()
        self.tabs.setFont(self.Env.font())
        self.tabs.setStyleSheet(f'background-color: {getdata("appw.body.bgcolor")};color: {getdata("appw.body.fgcolor")}')
        self.tabs.setFont(self.Env.font())

        self.x1 = QMainWindow()
        self.x1.setFont(self.Env.font())
        self.x1.setStyleSheet(f'background-color: {getdata("appw.body.bgcolor")};color: {getdata("appw.body.fgcolor")}')
        self.x2 = QWidget()
        self.x2.setFont(self.Env.font())
        self.x2.setStyleSheet(f'background-color: {getdata("appw.body.bgcolor")};color: {getdata("appw.body.fgcolor")}')

        self.tabs.addTab(self.x1,res.get('@string/app_name'))
        self.tabs.addTab(self.x2,res.get('@string/stopwatch'))

        app.switch('clock')

        self.Widget.SetWindowTitle (res.get('@string/app_name'))
        self.Widget.SetWindowIcon (QIcon(res.get(res.etc('clock','logo'))))

        self.lbl = QLabel()
        self.lbl.setText('18:36:32')
        self.lbl.setFont(self.Env.font())
        self.lbl.setStyleSheet(f'background-color: {getdata("appw.body.bgcolor")};color: {getdata("appw.body.fgcolor")}')

        self.x1.setCentralWidget(self.lbl)
        self.setCentralWidget(self.tabs)

        ## Clock ##
        # creating a timer object
        timer = QTimer(self)

        # adding action to timer
        timer.timeout.connect(self.showTime_lock)

        # update the timer every second
        timer.start(1000)

        self.lbl.setFont(QFont(self.Env.font().family(),50))
        self.lbl.setAlignment(Qt.AlignCenter)

        self.counter = 0
        self.minute = '00'
        self.second = '00'
        self.count = '00'
        self.startWatch = False

        # Create label to display the watch
        self.label = QLabel()
        self.label.setStyleSheet(f'background-color: {getdata("appw.body.bgcolor")};color: {getdata("appw.body.fgcolor")}')

        self.cl = QVBoxLayout()
        self.clvw = QWidget()
        self.clv = QHBoxLayout()
        self.clvw.setLayout(self.clv)

        self.cl.addWidget(self.label)
        self.cl.addWidget(self.clvw)
        # Set geometry for the label

        # Create start button
        app.switch('clock')
        self.start = QPushButton(res.get('@string/start'))
        self.start.setStyleSheet(f'background-color: {getdata("appw.body.bgcolor")};color: {getdata("appw.body.fgcolor")}')
        app.switch('clock')
        # Set geometry to the start button
        # Call start() method when the start button is clicked
        self.start.pressed.connect(self.Start)
        self.start.setFont(self.Env.font())
        self.clv.addWidget(self.start)

        # Create reset button
        app.switch('clock')
        resetWatch = QPushButton(res.get('@string/reset'))
        resetWatch.setStyleSheet(f'background-color: {getdata("appw.body.bgcolor")};color: {getdata("appw.body.fgcolor")}')
        app.switch('clock')
        # Set geometry to the stop button
        # Call reset() method when the reset button is clicked
        resetWatch.pressed.connect(self.Reset)
        resetWatch.setFont(self.Env.font())
        self.clv.addWidget(resetWatch)

        # Create timer object
        stopw = QTimer(self.x2)
        # Add a method with the timer
        stopw.timeout.connect(self.showCounter)
        # Call start() method to modify the timer value
        stopw.start(100)

        self.label.setFont(QFont(self.Env.font().family(), 50))
        self.label.setAlignment(Qt.AlignCenter)

        self.x2.setLayout(self.cl)