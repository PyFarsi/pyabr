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

        self.tabs = QTabWidget()
        self.tabs.setDocumentMode(True)
        self.tabs.tabBarDoubleClicked.connect(self.tab_open_doubleclick)
        self.tabs.currentChanged.connect(self.current_tab_changed)
        self.tabs.setTabsClosable(True)
        self.tabs.tabCloseRequested.connect(self.close_current_tab)

        self.setCentralWidget(self.tabs)

        self.status = QStatusBar()
        self.setStatusBar(self.status)

        navtb = QToolBar(res.get('@string/nav'))
        navtb.setIconSize(QSize(16, 16))
        self.addToolBar(navtb)

        back_btn = QAction(QIcon(res.get('@icon/breeze-back')), res.get('@string/ba'), self)
        back_btn.triggered.connect(lambda: self.tabs.currentWidget().back())
        navtb.addAction(back_btn)

        next_btn = QAction(QIcon(res.get('@icon/breeze-next')), res.get('@string/fw'), self)
        next_btn.triggered.connect(lambda: self.tabs.currentWidget().forward())
        navtb.addAction(next_btn)

        reload_btn = QAction(QIcon(res.get('@icon/breeze-reload')), res.get('@string/fw'), self)
        reload_btn.triggered.connect(lambda: self.tabs.currentWidget().reload())
        navtb.addAction(reload_btn)

        home_btn = QAction(QIcon(res.get('@icon/breeze-home')), res.get('@string/hm'), self)
        home_btn.triggered.connect(self.navigate_home)
        navtb.addAction(home_btn)

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

        if getdata('submenu.direction') == 'ltr':
            self.menuBar().setLayoutDirection(Qt.LeftToRight)
        else:
            self.menuBar().setLayoutDirection(Qt.RightToLeft)

        self.file = QMenu()
        self.file.setTitle(res.get('@string/file'))
        self.menuBar().addMenu(self.file)

        new_tab_action = QAction(QIcon(res.get('@icon/breeze-newtab')),res.get('@string/ntab'), self)
        new_tab_action.triggered.connect(lambda _: self.add_new_tab())
        new_tab_action.setFont(f)
        self.file.addAction(new_tab_action)

        exitx = QAction(QIcon(res.get('@icon/breeze-close')),res.get('@string/close'), self)
        exitx.triggered.connect(self.close)
        exitx.setFont(f)
        self.file.addAction(exitx)

        self.add_new_tab(QUrl(control.read_record("engine","/etc/webconfig")), res.get('@string/hm'))
        self.showFullScreen()

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
        q = QUrl(self.urlbar.text())
        if q.scheme() == "":
            q.setScheme("http")

        self.tabs.currentWidget().setUrl(q)

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
