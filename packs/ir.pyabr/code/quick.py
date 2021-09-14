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

import json
from typing import Container

from PyQt5 import QtQml, QtWidgets, QtCore, QtGui, QtQuick
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtQml import *
from PyQt5.QtQuick import *
from pyabr.core import *
import sys,os,shutil

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

    FileName = QtCore.Qt.UserRole+1000
    FileExt = QtCore.Qt.UserRole+1001
    FileSize = QtCore.Qt.UserRole+1002
    FileMimeType = QtCore.Qt.UserRole+1003
    FileLogo = QtCore.Qt.UserRole+1004
    FilePermission = QtCore.Qt.UserRole+1005
    FilePath = QtCore.Qt.UserRole+1006

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

    def FileModel (self,d):
        model = QtGui.QStandardItemModel()
        roles = {
            self.FileName:b'name',
            self.FileExt:b'ext',
            self.FileSize:b'size',
            self.FileMimeType:b'mimetype',
            self.FileLogo:b'logo',
            self.FilePermission:b'permission',
            self.FilePath:b'path'
        }
        model.setItemRoleNames(roles)

        directory = d

        listx = []
        listy = []
        lista = []

        for i in files.list(directory):
            if files.isdir(f'{directory}/{i}'):
                listx.append(i)

        listx.sort()

        for i in files.list(directory):
            if files.isfile(f'{directory}/{i}'):
                listy.append(i)

        listy.sort()

        for i in listx:
            lista.append(i)
        for i in listy:
            lista.append(i)

        for i in lista:
            it = QtGui.QStandardItem(i)
            it.setData(i, self.FileName)

            # generate ext #
            ext =os.path.splitext(i)[1] # https://www.tutorialspoint.com/How-to-extract-file-extension-using-Python
            it.setData(ext,self.FileExt)

            # generate permissions #
            perm = permissions.get_permissions(files.output(f'{directory}/{i}'))
            it.setData(perm,self.FilePermission)


            # generate icon #
            if ext=='':
                if files.isdir (f'{directory}/{i}'):
                    if files.isfile (f'{directory}/{i}/.logo'):
                        it.setData(res.qmlget(files.readall(f'{directory}/{i}/.logo')),self.FileLogo)
                    else:
                        it.setData(res.qmlget('@icon/breeze-folder'),self.FileLogo)
                else:
                    if i.startswith('ic') and 'dev' in directory:
                        it.setData(res.qmlget('@icon/breeze-drive'),self.FileLogo)
                    else:
                        it.setData(res.qmlget('@icon/breeze-txt'),self.FileLogo)
            else:
                if files.isfile(f'{directory}/{i}'):
                    if i.endswith('.desk'):
                        it.setData(res.qmlget(control.read_record (f'logo',f'{directory}/{i}')),self.FileLogo)
                    elif i.endswith ('.png') or i.endswith ('.jpg') or i.endswith ('.jpeg') or i.endswith ('.bmp') or i.endswith ('.tiff') or i.endswith ('.tif') or i.endswith ('.gif') or i.endswith ('.svg'):
                        it.setData(files.input_qml(f'{directory}/{i}'),self.FileLogo)
                    else:
                        it.setData(res.qmlget(control.read_record (f'{ext.replace(".","")}.icon','/etc/ext')),self.FileLogo)
                else:
                    if files.isfile (f'{directory}/{i}/.logo'):
                        it.setData(res.qmlget(files.readall(f'{directory}/{i}/.logo')),self.FileLogo)
                    else:
                        it.setData(res.qmlget('@icon/breeze-folder'),self.FileLogo)

            # generate size of file #
            size = files.size(f'{directory}/{i}')

            kB = 1024
            MB = kB*kB
            GB = MB*MB
            TB = GB*GB

            if size<kB:
                size_z = f'{str(size)} B'

            elif size>=kB and size<MB:
                size_z = f'{str(int(size/kB))} kB'

            elif size>=MB and size<GB:
                size_z = f'{str(int(size/MB))} MB'

            elif size>=GB and size<TB:
                size_z = f'{str(int(size/GB))} TB'

            else:
                size_z = f'{str(int(size/TB))} TB'
                
            it.setData(size_z,self.FileSize)

            # generate path #
            it.setData(f'{directory}/{i}',self.FilePath)

            # generate file mime type
            try:
                it.setData(control.read_record (f'{ext.replace(".","")}.text','/etc/ext'),self.FileMimeType)
            except:
                it.setData('Folder',self.FileMimeType)

            model.appendRow(it)

        return model

    def addItemModel (self,nameModel,listModel):
        self.newmodel = self.ItemModel(listModel)
        self.rootContext().setContextProperty(nameModel, self.newmodel)

    def addFileModel (self,directory):
        self.newmodelx = self.FileModel(directory)
        self.rootContext().setContextProperty('FileModel', self.newmodelx)

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
        self.btnOK.setProperty('text', res.get('@string/baran.ok'))
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
        self.btnOK.setProperty('text', res.get('@string/baran.ok'))
        self.btnOK.clicked.connect(self.ok_)
        self.btnCancel = self.findChild('btnCancel')
        self.btnCancel.setProperty('text', res.get('@string/baran.cancel'))
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
        self.btnOK.setProperty('text', res.get('@string/baran.ok'))
        self.btnOK.clicked.connect(self.ok_)
        self.btnCancel = self.findChild('btnCancel')
        self.btnCancel.setProperty('text', res.get('@string/baran.cancel'))
        self.btnCancel.clicked.connect(self.close)

class Password (MainApp):
    def ok_(self):
        self.close()
        self.function(self.leText.property('text'))

    def __init__(self,title,function):
        super(Password, self).__init__()
        files.write('/proc/info/id', 'password')
        self.load(res.get('@layout/password'))
        self.setProperty('title', title)
        self.function = function
        self.leText = self.findChild('leText')
        self.btnOK = self.findChild('btnOK')
        self.btnOK.setProperty('text', res.get('@string/baran.ok'))
        self.btnOK.clicked.connect(self.ok_)
        self.btnCancel = self.findChild('btnCancel')
        self.btnCancel.setProperty('text', res.get('@string/baran.cancel'))
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
        self.btnSelect.setProperty('title',res.get('@string/baran.sel'))

class Select (MainApp):

    file = ''

    def loop (self):
        if not self.fsel.property('text')=='':

            if files.isdir (self.fsel.property('text')) or self.fsel.property('text')=='..':
                commands.cd ([self.fsel.property('text')])
                self.addFileModel(files.readall('/proc/info/pwd'))
                self.btnSelect.setProperty('enabled',False)
            else:
                self.file = self.fsel.property('text')
                self.btnSelect.setProperty('enabled',True)

        self.fsel.setProperty('text','')
        QTimer.singleShot (10,self.loop)

    
    def select_(self):
        if not self.file == '':
            self.function (f"{self.file}")
            self.close()

    def __init__(self,function):
        super(MainApp, self).__init__()

        self.function = function

        self.addFileModel(files.readall('/proc/info/pwd'))
        self.load (res.get('@layout/select'))
        self.setProperty('title',res.get('@string/baran.file'))
        self.fsel = self.findChild ('fsel')

        self.btnCancel = self.findChild('btnCancel')
        self.btnCancel.setProperty('text', res.get('@string/baran.cancel'))
        self.btnSelect = self.findChild('btnSelect')
        self.btnCancel.clicked.connect (self.close)
        self.btnSelect.setProperty('text', res.get('@string/baran.sel'))
        self.btnSelect.clicked.connect (self.select_)

        self.loop()


class Open (MainApp):

    def loop (self):
        if not self.fsel.property('text')=='':

            if files.isdir (self.fsel.property('text')) or self.fsel.property('text')=='..':
                commands.cd ([self.fsel.property('text')])
                self.addFileModel(files.readall('/proc/info/pwd'))

                self.btnOpen.setProperty('enabled',True)
            else:
                self.btnOpen.setProperty('enabled',False)


        self.fsel.setProperty('text','')
        QTimer.singleShot (10,self.loop)

    def open_(self):
        if files.isdir (f"{files.readall('/proc/info/pwd')}/{self.fsel.property('text')}"):
            self.function (f"{files.readall('/proc/info/pwd')}/{self.fsel.property('text')}")
            self.close()

    def __init__(self,function):
        super(MainApp, self).__init__()

        self.function = function

        self.addFileModel(files.readall('/proc/info/pwd'))
        self.load (res.get('@layout/open'))
        self.setProperty('title',res.get('@string/baran.dir'))
        self.fsel = self.findChild ('fsel')

        self.btnCancel = self.findChild('btnCancel')
        self.btnCancel.setProperty('text', res.get('@string/baran.cancel'))
        self.btnOpen = self.findChild('btnOpen')
        self.btnCancel.clicked.connect (self.close)
        self.btnOpen.setProperty('text',res.get('@string/baran.open'))
        self.btnOpen.clicked.connect (self.open_)

        self.loop()


class Save (MainApp):

    def loop (self):
        if not self.fsel.property('text')=='':

            if files.isdir (self.fsel.property('text')) or self.fsel.property('text')=='..':
                commands.cd ([self.fsel.property('text')])
                self.addFileModel(files.readall('/proc/info/pwd'))
            
        if not self.leName.property('text')=='':
            self.btnSave.setProperty('enabled',True)


        self.fsel.setProperty('text','')
        QTimer.singleShot (10,self.loop)

    def save_(self):
        self.function (f"{files.readall('/proc/info/pwd')}/{self.leName.property('text')}")
        self.close()

    def __init__(self,function):
        super(MainApp, self).__init__()

        self.function = function

        self.addFileModel(files.readall('/proc/info/pwd'))
        self.load (res.get('@layout/save'))
        self.setProperty('title',res.get('@string/baran.save'))
        self.fsel = self.findChild ('fsel')

        self.btnCancel = self.findChild('btnCancel')
        self.btnCancel.setProperty('text',res.get('@string/baran.cancel'))
        self.btnSave = self.findChild('btnSave')
        self.btnCancel.clicked.connect (self.close)
        self.btnSave.clicked.connect (self.save_)
        self.btnSave.setProperty('text',res.get('@string/baran.save'))

        self.leName = self.findChild('leName')
        self.leName.setProperty('placeholderText',res.get('@string/baran.fn'))

        self.loop()

# Ask Dialog
class Install (MainApp):

    def install_(self):
        System (f'paye upak {self.package}')
        self.close()

    def ok_(self):
        self.pro.setProperty('visible',True)
        QTimer.singleShot(3000,self.install_)

    def no_(self):
        self.close()

    def __init__(self,package:str):
        super(Install, self).__init__()
        self.package = package
        files.write('/proc/info/id','install')
        self.load(res.get('@layout/install'))
        self.setProperty('title',res.get('@string/baran.packtitle').replace('{0}',package).replace('/','') )
        shutil.unpack_archive (files.input (package),files.input('/tmp/package-installer'),'zip')
        shutil.unpack_archive (files.input('/tmp/package-installer/control.zip'),files.input('/tmp/package-installer.control'),'zip')
        files.removedirs ('/tmp/package-installer')
        
        self.pro = self.findChild('pro')
        self.name = self.findChild('name')
        self.name.setProperty('text',control.read_record ('name','/tmp/package-installer.control/manifest'))
        self.description = self.findChild('descriptionx')
        self.description.setProperty('text',control.read_record ('description','/tmp/package-installer.control/manifest'))
        self.btnOK = self.findChild('btnOK')
        self.btnOK.setProperty('text', res.get('@string/baran.install'))
        self.btnOK.clicked.connect(self.ok_)
        self.btnCancel = self.findChild('btnCancel')
        self.btnCancel.setProperty('text', res.get('@string/baran.cancel'))
        self.btnCancel.clicked.connect(self.no_)