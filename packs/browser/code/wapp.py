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

app.switch('wapp')

f = QFont()
f.setFamily(control.read_record("font","/etc/gui"))
f.setPointSize(int(control.read_record("fontsize","/etc/gui")))

def getdata (name):
    return control.read_record (name,'/etc/gui')

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setFont(f)


        self.titlebar = QWidget()
        self.titlebar.setStyleSheet(f'background-color: {getdata("appw.title.bgcolor")};color: {getdata("appw.title.fgcolor")};')


        self.layouts = QHBoxLayout()
        self.titlebar.setLayout(self.layouts)

        # icon widget #
        if files.isfile('/tmp/wapp-logo.tmp'):
            self.icon = QIcon(res.get(files.readall('/tmp/wapp-logo.tmp')))
        else:
            self.icon = QIcon(res.get('@icon/breeze-wapp'))

        self.iconwidget = QLabel()
        self.iconwidget.setPixmap(
            self.icon.pixmap(int(getdata("appw.title.size")) - 18, int(getdata("appw.title.size")) - 18))
        self.iconwidget.resize(int(getdata("appw.title.size")), int(getdata("appw.title.size")))
        self.layouts.addWidget(self.iconwidget)

        self.iconwidget.setGeometry(0, 0, int(getdata("appw.title.size")), int(getdata("appw.title.size")))

        # text title #
        self.titletext = QLabel()
        self.titletext.setStyleSheet(
            f'background-color:  {getdata("appw.title.bgcolor")};color: {getdata("appw.title.fgcolor")};')
        self.titletext.setMaximumWidth(self.titlebar.width())
        self.titletext.setGeometry(int(getdata("appw.title.size")), 0, self.titlebar.width(),
                                   int(getdata("appw.title.size")))

        self.titletext.setFont(f)

        if files.isfile('/tmp/wapp-title.tmp'):
            self.titletext.setText(files.readall('/tmp/wapp-title.tmp'))
        else:
            self.titletext.setText(res.get('@string/app_name'))


        self.layouts.addWidget(self.titletext)

        round = '0'

        if getdata("appw.title.btn-round") == 'Yes':
            round = str(int((int(getdata("appw.title.size"))) - 16) / 2)

        # float button #

        self.btnEscape = QToolButton()
        self.btnEscape.setIcon(QIcon(res.get(getdata("appw.title.close"))))
        self.btnEscape.setMinimumSize(int(getdata("appw.title.size")) - 15, int(getdata("appw.title.size")) - 15)
        self.btnEscape.setGeometry(self.titlebar.width() - int(getdata("appw.title.size")), 0,
                                   int(getdata("appw.title.size")), int(getdata("appw.title.size")))
        self.btnEscape.clicked.connect(self.close)
        self.btnEscape.setStyleSheet(
            'QToolButton {border-radius: {0}% {0}%;} QToolButton::hover {border-radius: {0}% {0}%;background-color: {1}}'.replace(
                "{1}", getdata("appw.title.close-hover")).replace("{0}", round))
        self.layouts.addWidget(self.btnEscape)
        self.titlebar.setGeometry(0, 0, int(getdata('width')), int(getdata("appw.title.size")))


        try:
            self.add_new_tab(QUrl(files.readall('/tmp/url.tmp')))
        except:
            self.add_new_tab(QUrl(control.read_record("website","/etc/distro")))
        self.showFullScreen()
        self.resize(int(getdata("width")), int(getdata("height")))

    def add_new_tab(self, qurl=None):

        if qurl is None:
            qurl = QUrl(control.read_record('website','/etc/distro'))

        browser = QWebEngineView()
        browser.setUrl(qurl)

        browser.setGeometry(0, int(getdata("appw.title.size")),int(files.readall('/tmp/width.tmp')),int(files.readall('/tmp/height.tmp')) - int(getdata("appw.title.size")))

        self.layout().addWidget(browser)
        self.layout().addWidget(self.titlebar)

app = QApplication(sys.argv)

window = MainWindow()

app.exec_()
