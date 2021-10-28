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
    def clean_(self):
        self.o1.setProperty('text','')

        try:
                    files.remove ('/tmp/calculator_result.txt')
                    files.remove ('/tmp/calculator_program.pyc')
                    files.remove ('/tmp/calculator_program.py')
        except:
                    pass
    def calc_(self):
        try:
            if int(self.sender().property('text'))>0:
                self.o21.setProperty('enabled',True)

                # Enable all ops
                self.o10.setProperty('enabled',True)
                self.o5.setProperty('enabled',True)
                self.o4.setProperty('enabled',True)
                self.o3.setProperty('enabled',True)
                self.o2.setProperty('enabled',True)
                self.o19.setProperty('enabled',True)
        except:
            try:
                if self.sender().property('text') == '+' or self.sender().property('text') == '-' or self.sender().property('text') == '*' or self.sender().property('text') == '/' * self.sender().property('text') == '%' or self.sender().property('text') == '+/-':
                    self.o10.setProperty('enabled',False)
                    self.o5.setProperty('enabled',False)
                    self.o4.setProperty('enabled',False)
                    self.o3.setProperty('enabled',False)
                    self.o2.setProperty('enabled',False)
            except:
                pass

        if '.' in self.o1.property('text'):
            self.o22.setProperty('enabled',False)


        if self.sender().property('text')=='=':
            files.write ('/tmp/calculator_program.py',f'''from pyabr.core import *
calc = {self.o1.property("text")}
try:
    files.write("/tmp/calculator_result.txt",str(calc))
except:
    pass''')
            commands.cc (['/tmp/calculator_program.py'])
            System ('/tmp/calculator_program')
            try:
                self.o1.setProperty('text',files.readall('/tmp/calculator_result.txt'))
                
            except:
                self.o1.setProperty('text','Invalid entered')
            self.o22.setProperty('enabled',True)
        elif self.sender().property('text')=='AC':
            self.o1.setProperty ('text','')
            self.o22.setProperty('enabled',True)
            self.o19.setProperty('enabled',False)
            self.o10.setProperty('enabled',False)
            self.o5.setProperty('enabled',False)
            self.o4.setProperty('enabled',False)
            self.o3.setProperty('enabled',False)
            self.o2.setProperty('enabled',False)
        elif  self.sender().property('text')=='+/-':
            self.o1.setProperty ('text',self.o1.property('text')+'-')
        elif not self.sender().property('text')=='C':
            self.o1.setProperty ('text',self.o1.property('text')+self.sender().property('text'))

    def __init__(self):
        super(MainApp, self).__init__()

        self.load (res.get('@layout/calculator'))
        self.setProperty ('title',res.get('@string/calculator'))

        self.o1 = self.findChild('o1')
        self.o2 = self.findChild('o2')
        self.o2.clicked.connect (self.calc_)
        self.o3 = self.findChild('o3')
        self.o3.clicked.connect (self.calc_)
        self.o4 = self.findChild('o4')
        self.o4.clicked.connect (self.calc_)
        self.o5 = self.findChild('o5')
        self.o5.clicked.connect (self.calc_)
        self.o7 = self.findChild('o7')
        self.o7.clicked.connect (self.calc_)
        self.o8 = self.findChild('o8')
        self.o8.clicked.connect (self.calc_)
        self.o9= self.findChild('o9')
        self.o9.clicked.connect (self.calc_)
        self.o10 = self.findChild('o10')
        self.o10.clicked.connect (self.calc_)
        self.o11 = self.findChild('o11')
        self.o11.clicked.connect (self.calc_)
        self.o12 = self.findChild('o12')
        self.o12.clicked.connect (self.calc_)
        self.o13 = self.findChild('o13')
        self.o13.clicked.connect (self.calc_)
        self.o14 = self.findChild('o14')
        self.o14.clicked.connect (self.calc_)
        self.o15 = self.findChild('o15')
        self.o15.clicked.connect (self.calc_)
        self.o16 = self.findChild('o16')
        self.o16.clicked.connect (self.calc_)
        self.o17 = self.findChild('o17')
        self.o17.clicked.connect (self.calc_)
        self.o18 = self.findChild('o18')
        self.o18.clicked.connect (self.calc_)
        self.o19 = self.findChild('o19')
        self.o19.clicked.connect (self.calc_)
        self.o20 = self.findChild('o20')
        self.o20.clicked.connect (self.calc_)
        self.o21 = self.findChild('o21')
        self.o21.clicked.connect (self.calc_)
        self.o22 = self.findChild('o22')
        self.o22.clicked.connect (self.calc_)
        self.o23 = self.findChild('o23')
        self.o23.clicked.connect (self.calc_)

application = QtGui.QGuiApplication([])
application.setWindowIcon (QIcon(res.get(res.etc('calculator','logo'))))

w = MainApp()
application.exec()