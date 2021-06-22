#######################################################################################
#  In the name of God, the Compassionate, the Merciful
#  Pyabr (c) 2020 Mani Jamali. GNU General Public License v3.0
#
#  Official Website: 		http://pyabr.rf.gd
#  Programmer & Creator:    Mani Jamali <manijamali2003@gmail.com>
#  Gap channel: 			@pyabr
#  Gap group:   			@pyabr_community
#  Git source:              github.com/PyFarsi/pyabr
#
#######################################################################################

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

app.switch('html')

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
        self.icon = QIcon(res.get('@icon/breeze-htmlv'))

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
            self.add_new_tab(files.readall(files.readall('/tmp/filename.tmp')))
        except:
            self.add_new_tab("<p>Please open some HTML file to read it by HTML Viewer application</p>")

        self.show()
        self.resize(int(getdata("width")), int(getdata("height")))

    def add_new_tab(self, qurl=None):

        if qurl is None:
            qurl = "<p>Please open some HTML file to read it by HTML Viewer application</p>"

        browser = QWebEngineView()
        browser.setHtml(qurl)
        browser.setGeometry(0, int(getdata("appw.title.size")),int(files.readall('/tmp/width.tmp')),int(files.readall('/tmp/height.tmp')) - int(getdata("appw.title.size")))

        self.layout().addWidget(browser)
        self.layout().addWidget(self.titlebar)

app = QApplication(sys.argv)

window = MainWindow()

app.exec_()
