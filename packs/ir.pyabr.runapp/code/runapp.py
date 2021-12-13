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
from pyabr.cloud import *

def getdata (name):
    return control.read_record (name,'/etc/gui')

application = QGuiApplication(sys.argv)
application.setWindowIcon(QIcon(res.get(res.etc('runapp','logo'))))

class MainApp (MainApp):
    def clean(self):
        self.leRun.setProperty('placeholderText','')
        self.leRun.setProperty('enabled',True)

    def run_ (self):
        app.switch('runapp')
        cmdln = self.leRun.property('text').split(' ')
        command = cmdln[0]
        args = ''
        for i in cmdln[1:]:
            args+=" "+i

        if app.exists(command):
            app.start(command, args)
        elif self.leRun.property('text').startswith ('abr://'):
            self.d = Domain (self.leRun.property('text'))
        elif self.leRun.property('text').startswith ('https://') or self.leRun.property('text').startswith ('http://'):
            app.start ('chromium',self.leRun.property('text'))
        elif not command=='':
            self.leRun.setProperty('placeholderText',res.get('@string/application_not_found').replace('{0}',command))
            self.leRun.setProperty('enabled',False)

            QTimer.singleShot(3000,self.clean)

        self.leRun.setProperty('text','')

    def __init__(self):
        super(MainApp, self).__init__()

        self.load(res.get('@layout/runapp'))
        if not self.rootObjects():
            sys.exit(-1)

        self.setProperty('title',res.get('@string/runner'))

        self.leRun = self.findChild('leRun')
        self.btnRun = self.findChild('btnRun')
        self.btnRun.setProperty('text',res.get('@string/run'))
        self.btnRun.clicked.connect (self.run_)

w = MainApp()
application.exec()