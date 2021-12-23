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
import sys

from pyabr.core import *
from pyabr.quick import *

control = Control()
files = Files()
colors = Colors()
app = App()
res = Res()

def getdata (name):
    return control.read_record (name,'/etc/gui')

application = QGuiApplication(sys.argv)
app.switch('pysys')
application.setWindowIcon (QIcon(res.get(res.etc('pysys','logo'))))

class MainApp (MainApp):

    def loop (self):
        if self.background_text.property('text')=='shutdown':
            self.close()
            app.signal('shutdown')
        elif self.background_text.property('text')=='lock':
            self.close()
            app.signal('lock')
        elif self.background_text.property('text')=='logout':
            self.close()
            app.signal('logout')
        elif self.background_text.property('text')=='reboot':
            self.close()
            app.signal('restart')
        elif self.background_text.property('text')=='suspend':
            self.close()
            app.signal('sleep')

        self.background_text.setProperty('text','')
        QTimer.singleShot(10,self.loop)

    def __init__(self):
        super(MainApp, self).__init__()

        self.load(res.get('@layout/pysys'))
        self.setProperty('title',res.get('@string/power_options'))
        self.background_text = self.findChild('background_text')
        app.launchedlogo(self.property('title'), res.etc('pysys', 'logo'))

        self.shutdown = self.findChild ('shutdown')
        self.shutdown.setProperty('source',res.qmlget(res.etc('pysys','shutdown')))

        self.lock = self.findChild ('lock')
        self.lock.setProperty('source',res.qmlget(res.etc('pysys','lock')))

        self.logout = self.findChild ('logout')
        self.logout.setProperty('source',res.qmlget(res.etc('pysys','logout')))

        self.reboot = self.findChild ('reboot')
        self.reboot.setProperty('source',res.qmlget(res.etc('pysys','reboot')))

        self.suspend = self.findChild ('suspend')
        self.suspend.setProperty('source',res.qmlget(res.etc('pysys','suspend')))

        self.loop()

w = MainApp()
application.exec()