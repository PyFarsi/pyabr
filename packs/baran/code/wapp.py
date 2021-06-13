from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtPrintSupport import *

import os
import sys

from libabr import *

res = Res()
control = Control()
files = Files()
app = App()
commands = Commands()

app.switch('browser')

f = QFont()
f.setFamily(control.read_record("font","/etc/gui"))
f.setPointSize(int(control.read_record("fontsize","/etc/gui")))

def getdata (name):
    return control.read_record (name,'/etc/gui')

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setFont(f)

        try:
            self.add_new_tab(QUrl(files.readall('/tmp/url.tmp')))
        except:
            self.add_new_tab(QUrl(control.read_record("engine","/etc/webconfig")))

        self.showFullScreen()

    def add_new_tab(self, qurl=None):

        if qurl is None:
            qurl = QUrl(control.read_record('engine','/etc/webconfig'))

        browser = QWebEngineView()
        browser.setUrl(qurl)

        self.setCentralWidget(browser)

app = QApplication(sys.argv)

window = MainWindow()

app.exec_()
