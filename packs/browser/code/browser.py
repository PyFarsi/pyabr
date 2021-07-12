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

        self.titlebar = QWidget()
        self.titlebar.setStyleSheet(
            f'background-color: {getdata("appw.title.bgcolor")};color: {getdata("appw.title.fgcolor")};')

        self.layouts = QHBoxLayout()
        self.titlebar.setLayout(self.layouts)

        # icon widget #
        self.icon = QIcon(res.get('@icon/breeze-browser'))


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

        self.tabs = QTabWidget()
        self.tabs.setDocumentMode(True)
        self.tabs.tabBarDoubleClicked.connect(self.tab_open_doubleclick)
        self.tabs.currentChanged.connect(self.current_tab_changed)

        self.tabs.setTabsClosable(True)
        self.tabs.tabCloseRequested.connect(self.close_current_tab)
        self.tabs.setGeometry(0, int(getdata("appw.title.size")), int(files.readall('/tmp/width.tmp')),
                            int(files.readall("/tmp/height.tmp")) - int(getdata("appw.title.size")))

        self.layout().addWidget(self.tabs)
        self.layout().addWidget(self.titlebar)

        self.status = QStatusBar()
        self.setStatusBar(self.status)

        navtb = QToolBar(res.get('@string/nav'))
        navtb.setIconSize(QSize(16, 16))
        self.addToolBar(Qt.BottomToolBarArea,navtb)
        #addToolBar

        back_btn = QAction(QIcon(res.get('@icon/breeze-back')), res.get('@string/ba'), self)
        back_btn.triggered.connect(lambda: self.tabs.currentWidget().back())
        navtb.addAction(back_btn)

        next_btn = QAction(QIcon(res.get('@icon/breeze-next')), res.get('@string/fw'), self)
        next_btn.triggered.connect(lambda: self.tabs.currentWidget().forward())
        navtb.addAction(next_btn)

        reload_btn = QAction(QIcon(res.get('@icon/breeze-reload')), res.get('@string/rl'), self)
        reload_btn.triggered.connect(lambda: self.tabs.currentWidget().reload())
        navtb.addAction(reload_btn)

        home_btn = QAction(QIcon(res.get('@icon/breeze-home')), res.get('@string/hm'), self)
        home_btn.triggered.connect(self.navigate_home)
        navtb.addAction(home_btn)

        new_tab_action = QAction(QIcon(res.get('@icon/breeze-newtab')),res.get('@string/ntab'), self)
        new_tab_action.triggered.connect(lambda _: self.add_new_tab())
        new_tab_action.setFont(f)
        navtb.addAction(new_tab_action)

        navtb.addSeparator()

        self.httpsicon = QLabel()  # Yes, really!
        self.httpsicon.setPixmap(QPixmap(res.get('@icon/breeze-browser')))
        navtb.addWidget(self.httpsicon)

        self.urlbar = QLineEdit()
        self.urlbar.returnPressed.connect(self.navigate_to_url)
        navtb.addWidget(self.urlbar)

        stop_btn = QAction(QIcon(res.get('@icon/breeze-stop')), res.get('@string/st'), self)
        stop_btn.triggered.connect(lambda: self.tabs.currentWidget().stop())
        navtb.addAction(stop_btn)


        # Uncomment to disable native menubar on Mac
        # self.menuBar().setNativeMenuBar(False)

        self.menuBar().hide()

        self.add_new_tab(QUrl(control.read_record("engine","/etc/webconfig")), res.get('@string/hm'))
        self.showFullScreen()
        self.resize(int(getdata("width")),int(getdata("height")))

    def add_new_tab(self, qurl=None, label="Blank"):

        if qurl is None:
            qurl = QUrl('')

        browser = QWebEngineView()
        browser.setUrl(qurl)

        i = self.tabs.addTab(browser, label)

        self.tabs.setCurrentIndex(i)

        # More difficult! We only want to update the url when it's from the
        # correct tab
        browser.urlChanged.connect(lambda qurl, browser=browser:
                                   self.update_urlbar(qurl, browser))

        browser.loadFinished.connect(lambda _, i=i, browser=browser:
                                     self.tabs.setTabText(i, browser.page().title()))

    def tab_open_doubleclick(self, i):
        if i == -1:  # No tab under the click
            self.add_new_tab()

    def current_tab_changed(self, i):
        qurl = self.tabs.currentWidget().url()
        self.update_urlbar(qurl, self.tabs.currentWidget())
        self.update_title(self.tabs.currentWidget())

    def close_current_tab(self, i):
        if self.tabs.count() < 2:
            return

        self.tabs.removeTab(i)

    def update_title(self, browser):
        if browser != self.tabs.currentWidget():
            # If this signal is not from the current tab, ignore
            return

        title = self.tabs.currentWidget().page().title()
        self.setWindowTitle("%s - Mozarella Ashbadger" % title)

    def navigate_home(self):
        self.tabs.currentWidget().setUrl(QUrl(control.read_record('engine','/etc/webconfig')))



    def navigate_to_url(self):  # Does not receive the Url
        if self.urlbar.text().startswith('http'):
            q = QUrl(self.urlbar.text())
            if q.scheme() == "":
                q.setScheme("http")

            if q.toString().endswith('.apk') or q.toString().endswith('.exe') or q.toString().endswith(
                    '.pa') or q.toString().endswith('.zip') or q.toString().endswith('.rar') or q.toString().endswith(
                    '.deb') or q.toString().endswith('.msi') or q.toString().endswith('.xz') or q.toString().endswith(
                    '.gz') or q.toString().endswith('.bz2') or q.toString().endswith('.rpm') or q.toString().endswith(
                    '.run'):
                files.write('/tmp/download.tmp', q.toString())
                commands.start(['dmgr'])
                self.close()
            else:
                self.tabs.currentWidget().setUrl(q)
        else:
            if getdata('layout.keyless') == 'Yes':
                self.urlbar.setText(res.key(self.urlbar.text()))
            splitor = self.urlbar.text().split(',')
            strv = ''
            for i in splitor:
                if strv=='':
                    strv+=i
                else:
                    strv+="+"+i

            self.tabs.currentWidget().setUrl(QUrl(f'https://gerdoo.me/search/?query={strv}&t=nd'))

    def update_urlbar(self, q, browser=None):

        if browser != self.tabs.currentWidget():
            # If this signal is not from the current tab, ignore
            return

        if q.scheme() == 'https':
            # Secure padlock icon
            self.httpsicon.setPixmap(QPixmap(res.get('@icon/breeze-ssl')))

        elif q.toString().startswith ('abr://'):
            commands.cl([q.toString()])
            self.close()

        elif q.toString().endswith ('.apk') or q.toString().endswith ('.exe') or q.toString().endswith ('.pa') or q.toString().endswith ('.zip') or q.toString().endswith ('.rar') or q.toString().endswith ('.deb') or q.toString().endswith ('.msi') or q.toString().endswith ('.xz') or q.toString().endswith ('.gz') or q.toString().endswith ('.bz2') or q.toString().endswith ('.rpm') or q.toString().endswith ('.run'):
            files.write('/tmp/download.tmp',q.toString())
            commands.start(['dmgr'])
            self.close()

        else:
            # Insecure padlock icon
            self.httpsicon.setPixmap(QPixmap(res.get('@icon/breeze-browser')))

        self.urlbar.setText(q.toString())
        self.urlbar.setCursorPosition(0)


app = QApplication(sys.argv)

window = MainWindow()

app.exec_()
