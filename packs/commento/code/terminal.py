#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os

#from PyQt4.QtCore import QTimer
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from pyqterm import TerminalWidget
from pyqterm.procinfo import ProcessInfo
from libabr import Res, Control , Files, App

res = Res()
control = Control()
app = App()
files = Files()

def getdata (value): return control.read_record(value,'/etc/gui')

class MainApp(QTabWidget):
    def onCloseProcess (self):
        if not app.check(self.AppName):
            self.Widget.Close()
        else:
            QTimer.singleShot(1,self.onCloseProcess)

    def __init__(self,args, parent=None):
        super(MainApp, self).__init__(parent)

        self.Backend = args[0]
        self.Env = args[1]
        self.Widget = args[2]
        self.AppName = args[3]
        self.External = args[4]

        self.onCloseProcess()

        self.setStyleSheet(
            f'background-color: {getdata("appw.body.bgcolor")};color: {getdata("appw.body.fgcolor")};')

        self.proc_info = ProcessInfo()
        self.setTabPosition(QTabWidget.South)
        self.Widget.SetWindowTitle(res.get('@string/app_name'))
        self.Widget.Resize(self,800,600)
        self.Widget.SetWindowIcon (QIcon(res.get(res.etc('commento','logo'))))
        self._terms = []
        self.tabCloseRequested[int].connect(self._on_close_request)
        self.currentChanged[int].connect(self._on_current_changed)
        QTimer.singleShot(0, self.new_terminal)  # create lazy on idle
        self.startTimer(0)

    def _on_close_request(self, idx):
        term = self.widget(idx)
        term.stop()

    def _on_current_changed(self, idx):
        term = self.widget(idx)
        self._update_title(term)

    def new_terminal(self):
        files.write('/proc/info/su',self.Env.username)
        term = TerminalWidget(self)
        term.session_closed.connect(self._on_session_closed)
        self.addTab(term, res.get('@string/app_name'))
        self._terms.append(term)
        self.setCurrentWidget(term)
        term.setFocus()

    def timerEvent(self, event):
        self._update_title(self.currentWidget())

    def _update_title(self, term):
        if term is None:
            self.Widget.setWindowTitle(res.get('@string/app_name'))
            return
        idx = self.indexOf(term)
        pid = term.pid()
        self.proc_info.update()
        child_pids = [pid] + self.proc_info.all_children(pid)
        for pid in reversed(child_pids):
            cwd = self.proc_info.cwd(pid)
            if cwd:
                break
        try:
            user = self.Env.username
            hostname = files.readall('/proc/info/host')
            title = user+"@"+hostname
        except:
            title = res.get('@string/app_name')
        self.setTabText(idx, title)
        self.setWindowTitle(title)

    def _on_session_closed(self):
        term = self.sender()
        try:
            self._terms.remove(term)
        except:
            pass
        self.removeTab(self.indexOf(term))
        widget = self.currentWidget()
        if widget:
            widget.setFocus()
        if self.count() == 0:
            self.new_terminal()