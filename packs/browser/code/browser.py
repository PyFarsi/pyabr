#######################################################################################
#  In the name of God, the Compassionate, the Merciful
#  Pyabr (c) 2020 Mani Jamali. GNU General Public License v3.0
#
#  Official Website: 		http://pyabr.rf.gd
#  Programmer & Creator:    Mani Jamali <manijamali2003@gmail.com>
#  Gap channel: 			@pyabr
#  Gap group:   			@pyabr_community
#  Git source:              github.com/manijamali2003/pyabr
#
#######################################################################################

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import QWebEngineView

import os
import sys

from libabr import Res, Control, Files, App

res = Res()
control = Control()
files = Files()
app = App()

class AboutDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super(AboutDialog, self).__init__(*args, **kwargs)

        QBtn = QDialogButtonBox.Ok  # No cancel
        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        layout = QVBoxLayout()

        logo = QLabel()
        img = res.get('@icon/ma-icon-128')
        logo.setPixmap(QPixmap(img))
        layout.addWidget(logo)

        layout.addWidget(QLabel("Version 23.35.211.233232"))
        layout.addWidget(QLabel("Copyright 2015 Mozarella Inc."))

        for i in range(0, layout.count()):
            layout.itemAt(i).setAlignment(Qt.AlignHCenter)

        layout.addWidget(self.buttonBox)

        self.setLayout(layout)

class MainApp(QMainWindow):
    def __init__(self,ports, *args, **kwargs):
        super(MainApp, self).__init__(*args, **kwargs)
        self.Backend = ports[0]
        self.Env = ports[1]
        self.Widget = ports[2]
        self.AppName = ports[3]
        self.External = ports[4]

        self.Widget.SetWindowTitle (res.get('@string/app_name'))
        self.Widget.SetWindowIcon(QIcon(res.get(res.etc(self.AppName,"logo"))))
        self.Widget.Resize(self,self.Env.width(),self.Env.height())

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

        back_btn = QAction(QIcon(res.get('@icon/arrow-180')), res.get('@string/ba'), self)
        back_btn.setFont(self.Env.font())
        back_btn.setStatusTip(res.get('@string/ba'))
        back_btn.triggered.connect(lambda: self.tabs.currentWidget().back())
        navtb.addAction(back_btn)

        next_btn = QAction(QIcon(res.get('@icon/arrow-000')), res.get('@string/fw'), self)
        next_btn.setFont(self.Env.font())
        next_btn.setStatusTip(res.get('@string/fw'))
        next_btn.triggered.connect(lambda: self.tabs.currentWidget().forward())
        navtb.addAction(next_btn)

        reload_btn = QAction(QIcon(res.get('@icon/arrow-circle-315')), res.get('@string/rl'), self)
        reload_btn.setFont(self.Env.font())
        reload_btn.setStatusTip(res.get('@string/rl'))
        reload_btn.triggered.connect(lambda: self.tabs.currentWidget().reload())
        navtb.addAction(reload_btn)

        home_btn = QAction(QIcon(res.get('@icon/home')), res.get('@string/hm'), self)
        home_btn.setFont(self.Env.font())
        home_btn.setStatusTip(res.get('@string/hm'))
        home_btn.triggered.connect(self.navigate_home)
        navtb.addAction(home_btn)

        navtb.addSeparator()

        self.httpsicon = QLabel()  # Yes, really!
        self.httpsicon.setPixmap(QPixmap(res.get('@icon/lock-nossl')))
        navtb.addWidget(self.httpsicon)

        self.urlbar = QLineEdit()
        self.urlbar.returnPressed.connect(self.navigate_to_url)
        navtb.addWidget(self.urlbar)

        stop_btn = QAction(QIcon(res.get('@icon/cross-circle')), res.get('@string/st'), self)
        stop_btn.setFont(self.Env.font())
        stop_btn.setStatusTip(res.get('@string/st'))
        stop_btn.triggered.connect(lambda: self.tabs.currentWidget().stop())
        navtb.addAction(stop_btn)

        # Uncomment to disable native menubar on Mac
        # self.menuBar().setNativeMenuBar(False)

        file_menu = self.menuBar().addMenu(res.get('@string/file'))
        file_menu.setFont(self.Env.font())

        img = res.get('@icon/ui-tab--plus')
        new_tab_action = QAction(QIcon(img), res.get('@string/ntab'), self)
        new_tab_action.setFont(self.Env.font())
        new_tab_action.setStatusTip(res.get('@string/ntab'))
        new_tab_action.triggered.connect(lambda _: self.add_new_tab())
        file_menu.addAction(new_tab_action)

        img = res.get('@icon/disk--arrow')
        open_file_action = QAction(QIcon(img), res.get('@string/of'), self)
        open_file_action.setStatusTip(res.get('@string/of'))
        open_file_action.setFont(self.Env.font())
        open_file_action.triggered.connect(self.open_file)
        file_menu.addAction(open_file_action)

        help_menu = self.menuBar().addMenu(res.get('@string/hl'))
        help_menu.setFont(self.Env.font())

        img = res.get('@icon/question')
        about_action = QAction(QIcon(img), res.get('@string/ab'), self)
        about_action.setFont(self.Env.font())
        about_action.setStatusTip(res.get('@string/ab'))  # Hungry!
        about_action.triggered.connect(self.about)
        help_menu.addAction(about_action)

        img = res.get('@icon/lifebuoy')
        navigate_mozarella_action = QAction(QIcon(img),res.get('@string/pg'), self)
        navigate_mozarella_action.setStatusTip(res.get('@string/pc'))
        navigate_mozarella_action.setFont(self.Env.font())
        navigate_mozarella_action.triggered.connect(self.navigate_mozarella)
        help_menu.addAction(navigate_mozarella_action)

        self.add_new_tab(QUrl(control.read_record('default','/etc/webconfig')), 'Homepage')

        self.show()

        img = res.get('@icon/ma-icon-64')
        self.setWindowIcon(QIcon(img))

    def add_new_tab(self, qurl=None, label="Blank"):

        if qurl is None:
            qurl = QUrl('')

        self.browser = QWebEngineView()
        self.browser.setUrl(qurl)
        i = self.tabs.addTab(self.browser, label)

        self.tabs.setCurrentIndex(i)

        # More difficult! We only want to update the url when it's from the
        # correct tab
        self.browser.urlChanged.connect(lambda qurl, browser=self.browser:
                                        self.update_urlbar(qurl, self.browser))

        self.browser.loadFinished.connect(lambda _, i=i, browser=self.browser:self.tabs.setTabText(i, self.browser.page().title()))

        self.Loop()

    def Loop(self):
        self.browser.update()
        QTimer.singleShot(50,self.Loop)

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
        self.Widget.setWindowTitle(f"%s - {res.get('@string/app_name')}" % title)

    def navigate_mozarella(self):
        self.tabs.currentWidget().setUrl(QUrl("https://gap.im/pyabr"))

    def about(self):
        dlg = AboutDialog()
        dlg.exec_()

    def open_file(self):
        app.switch('browser')
        self.Env.RunApp('select',[res.get('@string/owp'),'open',self.open_file_])
        app.switch('browser')

    def open_file_(self,filename):
        html = files.readall(filename)

        self.tabs.currentWidget().setHtml(html)
        self.urlbar.setText(filename)

    def navigate_home(self):
        self.tabs.currentWidget().setUrl(QUrl(control.read_record('default','/etc/webconfig')))

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
            img = res.get('@icon/lock-ssl')
            self.httpsicon.setPixmap(QPixmap(img))
        else:
            # Insecure padlock icon
            img = res.get('@icon/lock-nossl')
            self.httpsicon.setPixmap(QPixmap(img))

        self.urlbar.setText(q.toString())
        self.urlbar.setCursorPosition(0)
