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

class MainApp (MainApp):

    def showTime (self):
        current_time = QTime.currentTime()
  
        # converting QTime object to string
        label_time = current_time.toString('hh:mm:ss')
        self.leClock.setProperty('text',res.num(label_time))

    def time_(self):
        self.leClock.setProperty('visible',True)
        self.leStopwatch.setProperty('visible',False)
        self.restart.setProperty('visible',False)
        self.start.setProperty('visible',False)
        self.pause.setProperty('visible',False)

    def stopwatch_(self):
        self.leClock.setProperty('visible',False)
        self.leStopwatch.setProperty('visible',True)
        self.restart.setProperty('visible',True)
        self.start.setProperty('visible',True)
        self.pause.setProperty('visible',True)

    def showTime2 (self):
        time = QDateTime.currentDateTime()


    def __init__(self):
        super(MainApp, self).__init__()

        self.load (res.get('@layout/clock'))
        self.setProperty('title',res.get('@string/clock'))

        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)

        timer2 = QTimer(self)
        timer2.timeout.connect(self.showCounter)
        timer2.start(100)

        self.counter = 0
        self.minute = '00'
        self.second = '00'
        self.count = '00'
        self.startWatch = False

        self.leClock = self.findChild ('leClock')
        self.time = self.findChild ('time')
        self.time.clicked.connect (self.time_)
        self.stopwatch = self.findChild ('stopwatch')
        self.stopwatch.clicked.connect (self.stopwatch_)
        self.leStopwatch = self.findChild ('leStopwatch')

        self.restart = self.findChild ('restart')
        self.restart.clicked.connect (self.Reset)
        self.pause = self.findChild ('pause')
        self.pause.clicked.connect (self.Pause)
        self.start = self.findChild ('start')
        self.start.clicked.connect (self.Start)

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
        self.leStopwatch.setProperty('text',res.num(text))

    def Reset(self):
        self.startWatch = False
            # Reset all counter variables
        self.counter = 0
        self.minute = '00'
        self.second = '00'
        self.count = '00'
            # Set the initial values for the stop watch
        self.leStopwatch.setProperty('text',res.num(str(self.counter)))

    def Start(self):
        self.startWatch = True

    def Pause (self):
        self.startWatch = False

application = QtGui.QGuiApplication([])
application.setWindowIcon (QIcon(res.get(res.etc('clock','logo'))))

w = MainApp()
application.exec()