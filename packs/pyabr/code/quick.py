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

# Support QML easy
# Support Baran Desktop Enviroment
import json

from PyQt5 import QtQml, QtWidgets, QtCore, QtGui
from pyabr.core import *
import sys

# Main Entry
class MainApp (QtQml.QQmlApplicationEngine):

    ObjectNameRole = QtCore.Qt.UserRole+1000
    TextRole = QtCore.Qt.UserRole + 1001
    IconRole = QtCore.Qt.UserRole + 1002
    FontRole = QtCore.Qt.UserRole + 1003
    FontSizeRole = QtCore.Qt.UserRole + 1004
    ColorRole = QtCore.Qt.UserRole + 1005
    EnabledRole = QtCore.Qt.UserRole + 1006
    VisibleRole = QtCore.Qt.UserRole + 1007

    def ItemModel (self,listRow):
        model = QtGui.QStandardItemModel()
        roles = {
            self.ObjectNameRole:b"objectName",
            self.TextRole:b"text",
            self.IconRole:b"icon",
            self.FontRole:b"fontFamily",
            self.FontSizeRole:b"fontSize",
            self.ColorRole:b"color",
            self.EnabledRole:b"enabled",
            self.VisibleRole:b"visible",
        }
        model.setItemRoleNames(roles)

        for i in listRow:
            it = QtGui.QStandardItem(i['objectName'])
            if 'objectName' in i:
                it.setData(i['objectName'], self.ObjectNameRole)
            if 'text' in i:
                it.setData(i['text'], self.TextRole)
            if 'fontFamily' in i:
                it.setData(i['fontFamily'], self.FontRole)
            if 'fontSize' in i:
                it.setData(i['fontSize'], self.FontSizeRole)
            if 'color' in i:
                it.setData(i['color'], self.ColorRole)
            if 'enabled' in i:
                it.setData(i['enabled'], self.EnabledRole)
            if 'visible' in i:
                it.setData(i['visible'], self.VisibleRole)
            model.appendRow(it)
        return model

    def addItemModel (self,nameModel,listModel):
        self.newmodel = self.ItemModel(listModel)
        self.rootContext().setContextProperty(nameModel, self.newmodel)

    def setProperty(self,name,value):
        self.rootObjects()[0].setProperty(name,value)

    def property(self,name):
        return self.rootObjects()[0].property(name)

    def findChild (self,name):
        return self.rootObjects()[0].findChild(QtCore.QObject,name)

    def close (self):
        self.rootObjects()[0].close()

    def __init__(self):
        super(MainApp, self).__init__()

# Text Dialog
class Text (MainApp):
    def __init__(self,title:str,text:str):
        super(Text, self).__init__()
        files.write('/proc/info/id','text')
        self.load(res.get('@layout/text'))
        self.setProperty('title', title)
        self.txtText = self.findChild('txtText')
        self.txtText.setProperty('text', text)
        self.btnOK = self.findChild('btnOK')
        self.btnOK.setProperty('text', res.get('@string/ok'))
        self.btnOK.clicked.connect(self.close)

# Ask Dialog
class Ask (MainApp):

    def ok_(self):
        self.close()
        self.function(True)

    def no_(self):
        self.close()
        self.function(False)

    def __init__(self,title:str,text:str,function):
        super(Ask, self).__init__()
        files.write('/proc/info/id','ask')
        self.load(res.get('@layout/ask'))
        self.setProperty('title', title)
        self.function = function
        self.txtText = self.findChild('txtText')
        self.txtText.setProperty('text', text)
        self.btnOK = self.findChild('btnOK')
        self.btnOK.setProperty('text', res.get('@string/ok'))
        self.btnOK.clicked.connect(self.ok_)
        self.btnCancel = self.findChild('btnCancel')
        self.btnCancel.setProperty('text', res.get('@string/cancel'))
        self.btnCancel.clicked.connect(self.no_)

# Input Dialog
class Input (MainApp):
    def ok_(self):
        self.close()
        self.function(self.leText.property('text'))

    def __init__(self,title,function):
        super(Input, self).__init__()
        files.write('/proc/info/id', 'input')
        self.load(res.get('@layout/input'))
        self.setProperty('title', title)
        self.function = function
        self.leText = self.findChild('leText')
        self.btnOK = self.findChild('btnOK')
        self.btnOK.setProperty('text', res.get('@string/ok'))
        self.btnOK.clicked.connect(self.ok_)
        self.btnCancel = self.findChild('btnCancel')
        self.btnCancel.setProperty('text', res.get('@string/cancel'))
        self.btnCancel.clicked.connect(self.close)

# Font Dilog
class Font (MainApp):

    def ok_(self):
        self.close()
        self.function(self.bt.property('text'))

    def __init__(self,function):
        super(Font, self).__init__()
        files.write('/proc/info/id', 'font')
        fontlist = files.list('/usr/share/fonts')
        fonts = []
        for i in fontlist:
            fonts.append(json.loads(files.readall(f"/usr/share/fonts/{i}")))
        self.addItemModel("fontList",fonts)
        self.load(res.get('@layout/font'))
        self.function = function
        self.bt = self.findChild("bt")
        self.btnSelect = self.findChild("btnSelect")
        self.btnCancel = self.findChild("btnCancel")
        self.btnCancel.clicked.connect(self.close)
        self.btnSelect.clicked.connect(self.ok_)
        self.setProperty('title',res.get('@string/sel'))