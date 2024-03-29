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

import json,time,requests,html2text
import subprocess
from pyabr.core import *

from PyQt5 import QtQml, QtWidgets, QtCore, QtGui, QtQuick
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtQml import *
from PyQt5.QtQuick import *

from pyabr.cloud import *

import sys,os,shutil,hashlib
import feedparser

# Main Entry
class MainApp (QtQml.QQmlApplicationEngine):

    # Default
    ObjectNameRole = QtCore.Qt.ItemDataRole.UserRole+1000
    TextRole = QtCore.Qt.ItemDataRole.UserRole + 1001
    IconRole = QtCore.Qt.ItemDataRole.UserRole + 1002
    FontRole = QtCore.Qt.ItemDataRole.UserRole + 1003
    FontSizeRole = QtCore.Qt.ItemDataRole.UserRole + 1004
    ColorRole = QtCore.Qt.ItemDataRole.UserRole + 1005
    EnabledRole = QtCore.Qt.ItemDataRole.UserRole + 1006
    VisibleRole = QtCore.Qt.ItemDataRole.UserRole + 1007

    # File
    FileName = QtCore.Qt.ItemDataRole.UserRole+1000
    FileExt = QtCore.Qt.ItemDataRole.UserRole+1001
    FileSize = QtCore.Qt.ItemDataRole.UserRole+1002
    FileMimeType = QtCore.Qt.ItemDataRole.UserRole+1003
    FileLogo = QtCore.Qt.ItemDataRole.UserRole+1004
    FilePermission = QtCore.Qt.ItemDataRole.UserRole+1005
    FilePath = QtCore.Qt.ItemDataRole.UserRole+1006

    # User
    Username = QtCore.Qt.ItemDataRole.UserRole+1001
    Profile = QtCore.Qt.ItemDataRole.UserRole+1002
    FullName = QtCore.Qt.ItemDataRole.UserRole+1003

    # Package

    PKG_NAME = QtCore.Qt.ItemDataRole.UserRole+1000
    PKG_NAMEX = QtCore.Qt.ItemDataRole.UserRole+1001
    PKG_COPYRIGHT =QtCore.Qt.ItemDataRole.UserRole+1002
    PKG_LICENSE = QtCore.Qt.ItemDataRole.UserRole+1003
    PKG_UNPACK = QtCore.Qt.ItemDataRole.UserRole+1004
    PKG_VERSION =QtCore.Qt.ItemDataRole.UserRole+1005
    PKG_BUILD = QtCore.Qt.ItemDataRole.UserRole+1006
    PKG_MIRROR = QtCore.Qt.ItemDataRole.UserRole+1007
    PKG_DESCRIPTION = QtCore.Qt.ItemDataRole.UserRole+1008
    PKG_TYPE = QtCore.Qt.ItemDataRole.UserRole+1009
    PKG_INSTALLED = QtCore.Qt.ItemDataRole.UserRole+1010
    PKG_LOGO = QtCore.Qt.ItemDataRole.UserRole+1011

    # Display
    DISPLAY = QtCore.Qt.ItemDataRole.UserRole+1000

    # Wifi
    BSSID = QtCore.Qt.ItemDataRole.UserRole+1002
    SSID = QtCore.Qt.ItemDataRole.UserRole+1000
    MODE = QtCore.Qt.ItemDataRole.UserRole+1003
    CHAN = QtCore.Qt.ItemDataRole.UserRole+1004
    RATE = QtCore.Qt.ItemDataRole.UserRole+1005
    SIGNAL = QtCore.Qt.ItemDataRole.UserRole+1006
    SECURITY = QtCore.Qt.ItemDataRole.UserRole+1007
    NETLOGO = QtCore.Qt.ItemDataRole.UserRole+1008

    NameRole = QtCore.Qt.ItemDataRole.UserRole+1001
    LabelRole = QtCore.Qt.ItemDataRole.UserRole+1002
    LogoRole = QtCore.Qt.ItemDataRole.UserRole+1003

    # User
    CName = QtCore.Qt.ItemDataRole.UserRole+1001
    CFullName = QtCore.Qt.ItemDataRole.UserRole+1003
    CProfile = QtCore.Qt.ItemDataRole.UserRole+1000

    # Mail
    MailID = QtCore.Qt.ItemDataRole.UserRole+1001
    MailSender = QtCore.Qt.ItemDataRole.UserRole+1002
    MailGiver = QtCore.Qt.ItemDataRole.UserRole+1003
    MailSubject = QtCore.Qt.ItemDataRole.UserRole+1004
    MailData = QtCore.Qt.ItemDataRole.UserRole+1005

    # Drives 
    DEV = QtCore.Qt.ItemDataRole.UserRole+1000 # /dev/sda1
    DEV_TITLE = QtCore.Qt.ItemDataRole.UserRole+1001 # Partition 1 (SDA1:)
    DEV_LOGO = QtCore.Qt.ItemDataRole.UserRole+1002

    # PROCESS MANAGER
    PICON = QtCore.Qt.ItemDataRole.UserRole+1000
    PNAME = QtCore.Qt.ItemDataRole.UserRole + 1001
    PUSER = QtCore.Qt.ItemDataRole.UserRole + 1002

    # Icon theme
    ITNAME = QtCore.Qt.ItemDataRole.UserRole+1000
    ITNAMEX = QtCore.Qt.ItemDataRole.UserRole+1001
    ITLOGO = QtCore.Qt.ItemDataRole.UserRole + 1002

    # Feeds

    FeedTitle = QtCore.Qt.ItemDataRole.UserRole+1000
    FeedImage = QtCore.Qt.ItemDataRole.UserRole+1001
    FeedLink = QtCore.Qt.ItemDataRole.UserRole+1002
    FeedSummary = QtCore.Qt.ItemDataRole.UserRole+1003
    
    # Jooya Web Search History
    
    JHLink = QtCore.Qt.ItemDataRole.UserRole+1000
    JHIcon = QtCore.Qt.ItemDataRole.UserRole+1001
    JHTitle = QtCore.Qt.ItemDataRole.UserRole+1002

    # Jooya Web Engines
    JEName = QtCore.Qt.ItemDataRole.UserRole+1000
    JEUrl = QtCore.Qt.ItemDataRole.UserRole+1001
    JEQUrl = QtCore.Qt.ItemDataRole.UserRole+1002
    JEKey = QtCore.Qt.ItemDataRole.UserRole+1003
    JEID = QtCore.Qt.ItemDataRole.UserRole+1004

    # Jooya Web Search History

    JBLink = QtCore.Qt.ItemDataRole.UserRole + 1000
    JBIcon = QtCore.Qt.ItemDataRole.UserRole + 1001
    JBTitle = QtCore.Qt.ItemDataRole.UserRole + 1002

    # Project Model
    ProjectName = QtCore.Qt.ItemDataRole.UserRole + 1000
    ProjectType = QtCore.Qt.ItemDataRole.UserRole + 1001
    ProjectPackage = QtCore.Qt.ItemDataRole.UserRole + 1002

    NOTitle = QtCore.Qt.ItemDataRole.UserRole + 1000
    NOLogo = QtCore.Qt.ItemDataRole.UserRole + 1001
    NOCommand = QtCore.Qt.ItemDataRole.UserRole + 1002
    NOText = QtCore.Qt.ItemDataRole.UserRole + 1003

    def shortText (self,value):
        if len(value)>=60:
            strv = ''

            j = 0

            for i in value:
                strv+=i
                j +=1
                if j>=60:
                    break

            return f"{strv}..."
        else:
            return value

    def longText (self,value):
        if len(value)>=70:
            strv = ''

            j = 0

            for i in value:
                strv+=i
                j +=1
                if j>=70:
                    break

            return f"{strv}..."
        else:
            return value

    def MailModel (self):
        model = QtGui.QStandardItemModel()
        roles = {
            self.MailID:b'id',
            self.MailSender:b'sender',
            self.MailGiver:b'giver',
            self.MailSubject:b'subject',
            self.MailData:b'data'
        }
        model.setItemRoleNames(roles)

        try:
            m = Mail()
            mails = json.loads(m.Inbox())

            for i in mails:
                it = QtGui.QStandardItem(i['id'])
                it.setData(i['id'],self.MailID)
                it.setData(i['sender'],self.MailSender)
                it.setData(i['giver'],self.MailGiver)
                it.setData(i['subject'],self.MailSubject)
                it.setData(i['data'],self.MailData)

                model.appendRow(it)
        except:
            pass
        
        return model

    def FeedModel (self):
        model = QtGui.QStandardItemModel()
        roles = {self.FeedTitle: b"title", self.FeedImage: b'image',self.FeedLink:b'link',self.FeedSummary:b'summary'}
        model.setItemRoleNames(roles)

        html2text.ignore_links = True
        html2text.ignore_images = True

        h = html2text.HTML2Text()

        for feedsite in control.read_list('/etc/feeds.list'):
            feeds = feedparser.parse (feedsite)

            for i in feeds.entries:

                # support zoomit feeds
                if 'zoomit.ir' in i['id']:
                    it = QtGui.QStandardItem(i['id'])
                    it.setData(self.shortText(i['title']),self.FeedTitle)
                    it.setData(i['summary'].split("\"")[3],self.FeedImage)
                    it.setData(self.longText(h.handle(i['summary'].split("\"")[4]).replace('/>','').replace('\n','')),self.FeedSummary)
                    it.setData(i['link'],self.FeedLink)

                elif 'khabaronline.ir' in i['id'] or 'mehrnews.com' in i['id']:
                    it = QtGui.QStandardItem(i['id'])
                    it.setData(self.shortText(i['title']), self.FeedTitle)
                    it.setData(i['links'][1]['href'], self.FeedImage)
                    it.setData(self.longText(i['summary']), self.FeedSummary)
                    it.setData(i['link'], self.FeedLink)
                    
                else:
                    try:
                        it = QtGui.QStandardItem(i['id'])
                        it.setData(self.shortText(i['title']), self.FeedTitle)
                        it.setData(i['summary'].split("\"")[3], self.FeedImage)
                        it.setData(self.longText(h.handle(i['summary'].split("\"")[4]).replace('/>', '').replace('\n', '')),
                                   self.FeedSummary)
                        it.setData(i['link'], self.FeedLink)
                    except:
                        pass

                model.appendRow(it)

        model.sort(1,Qt.DescendingOrder)

        return model

    def CopyDiskModel (self):
        model = QtGui.QStandardItemModel()
        roles = {self.DEV: b"dev", self.DEV_TITLE: b'title'}
        model.setItemRoleNames(roles)
        z = os.listdir('/dev')
        z.sort()

        for name in z:
            if name.startswith('sd'):
                it = QtGui.QStandardItem(name)
                it.setData(f'/dev/{name}',self.DEV)
                try:
                    it.setData(f'{res.get("@string/part")} {name[3]} ({name[0]}{name[1]}{name[2]}:)',self.DEV_TITLE)
                except:
                    it.setData(f'{res.get("@string/disk")} ({name}:)',self.DEV_TITLE)
                model.appendRow(it)
        return model
    
    
    def JooyaHistoryModel (self):
        model = QtGui.QStandardItemModel()
        roles = {self.JHLink:b'link',self.JHIcon:b'icon',self.JHTitle:b'title'}
        model.setItemRoleNames(roles)

        if files.readall('/proc/info/su') == 'root':
            self.username = f'/root'
        else:
            self.username = f'/desk/{files.readall("/proc/info/su")}'
        
        links = control.read_list(f'{self.username}/.jooya_history')
        icons = control.read_list(f'{self.username}/.jooya_history_icons')
        titles = control.read_list(f'{self.username}/.jooya_history_titles')


        i = 0
        for link in links:
                if (link.startswith('http://') or link.startswith('https://')):
                    it = QtGui.QStandardItem(link)
                    it.setData(link,self.JHLink)
                    it.setData(icons[i],self.JHIcon)
                    it.setData(titles[i],self.JHTitle)
                    i+=1
                    model.appendRow(it)
        return model

    def JooyaBookmarkModel(self):
        model = QtGui.QStandardItemModel()
        roles = {self.JBLink: b'link', self.JBIcon: b'icon', self.JBTitle: b'title'}
        model.setItemRoleNames(roles)

        if files.readall('/proc/info/su') == 'root':
            self.username = f'/root'
        else:
            self.username = f'/desk/{files.readall("/proc/info/su")}'

        links = control.read_list(f'{self.username}/.jooya_bookmarks')
        icons = control.read_list(f'{self.username}/.jooya_bookmarks_icons')
        titles = control.read_list(f'{self.username}/.jooya_bookmarks_titles')

        i = 0
        for link in links:
            if (link.startswith('http://') or link.startswith('https://') or link.startswith('stor:///')):
                it = QtGui.QStandardItem(link)
                it.setData(link, self.JBLink)
                it.setData(icons[i], self.JBIcon)
                try:
                    it.setData(titles[i], self.JBTitle)
                except:
                    it.setData(link,self.JBTitle)
                i += 1
                model.appendRow(it)
        return model

    def JooyaSearchEngineModel (self):
        model = QtGui.QStandardItemModel()
        roles = {self.JEName:b'name',self.JEUrl:b'url',self.JEQUrl:b'qurl',self.JEKey:b'key',self.JEID:b'id'}
        model.setItemRoleNames(roles)

        listwe = files.list('/etc/jooya/engines')

        for we in listwe:
            it = QtGui.QStandardItem(we)
            it.setData(we,self.JEID)
            it.setData(control.read_record('name',f'/etc/jooya/engines/{we}'),self.JEName)
            it.setData(control.read_record('url',f'/etc/jooya/engines/{we}'),self.JEUrl)
            it.setData(control.read_record('qurl',f'/etc/jooya/engines/{we}'),self.JEQUrl)
            it.setData(control.read_record('key',f'/etc/jooya/engines/{we}'),self.JEKey)
            model.appendRow(it)

        return model

    def ProcessModel (self):
        model = QtGui.QStandardItemModel()
        roles = {self.PNAME: b"name", self.PICON: b'icon',self.PUSER:b'user'}
        model.setItemRoleNames(roles)

        lista = subprocess.check_output(['wmctrl', '-l']).decode('utf-8').split('\n')
        list2 = []
        for i in lista:
            try:
                list2.append(i.split('  0 pyabr ')[1])
            except:
                pass

        list2 = list(dict.fromkeys(list2))

        for name in list2:
            it = QtGui.QStandardItem(name)
            it.setData(name, self.PNAME)

            if name=='Pyabr OS':
                it.setData('root',self.PUSER)
            else:
                it.setData(files.readall('/proc/info/su'),self.PUSER)

            correctname = name.replace(' ', '').replace('\n', '').replace('(', '').replace(')', '').replace('0',
                                                                                                            '').replace(
                '1', '').replace('2', '').replace('3', '').replace('4', '').replace('5', '').replace('6', '').replace(
                '7', '').replace('8', '').replace('9', '')
            if not control.read_record(correctname, '/etc/launched/logo.list') == None:
                it.setData(res.qmlget(control.read_record(correctname, '/etc/launched/logo.list')), self.PICON)
            else:
                it.setData(res.qmlget('@icon/breeze-app'), self.PICON)
            model.appendRow(it)
        return model

    def DrivesModel (self):
        model = QtGui.QStandardItemModel()
        roles = {self.DEV: b"dev", self.DEV_TITLE: b'title',self.DEV_LOGO:b'logo'}
        model.setItemRoleNames(roles)
        z = os.listdir('/dev')
        z.sort()

        for name in z:
            if name.startswith('sd'):
                it = QtGui.QStandardItem(name)
                it.setData(f'/dev/{name}',self.DEV)
                try:
                    it.setData(f'{res.get("@string/drive")} {name[3]} ({name[0]}{name[1]}{name[2]}:)',self.DEV_TITLE)
                except:
                    it.setData(f'{res.get("@string/disk")} ({name}:)',self.DEV_TITLE)
                it.setData(res.qmlget('@icon/harddisk'),self.DEV_LOGO)
                model.appendRow(it)
            elif name.startswith('sr'):
                it = QtGui.QStandardItem(name)
                it.setData(f'/dev/{name}',self.DEV)
                try:
                    it.setData(f'{res.get("@string/sr")} {name[3]} ({name[0]}{name[1]}{name[2]}:)',self.DEV_TITLE)
                except:
                    it.setData(f'{res.get("@string/srp")} ({name}:)',self.DEV_TITLE)
                it.setData(res.qmlget('@icon/cdrom'),self.DEV_LOGO)
                model.appendRow(it)
        return model

    def LanguageModel (self):
        model = QtGui.QStandardItemModel()
        roles = {self.NameRole: b"name", self.LabelRole: b'label'}
        model.setItemRoleNames(roles)
        for name in files.list('/usr/share/locales'):
            it = QtGui.QStandardItem(name)
            it.setData(name,self.NameRole)
            it.setData(control.read_record('name',f'/usr/share/locales/{name}'), self.LabelRole)
            model.appendRow(it)
        return model

    def ApplicationModel(self,ext):
        model = QtGui.QStandardItemModel()
        roles = {self.NameRole: b"name", self.LabelRole: b'label', self.LogoRole: b'logo'}
        model.setItemRoleNames(roles)
        for name in files.list('/usr/share/applications'):
            extx = os.path.splitext(ext)[1].replace('.','')
            if control.read_record (f'{extx}.external.{name.replace(".desk","")}','/etc/ext')=='Yes':
                it = QtGui.QStandardItem(name)
                it.setData(name, self.NameRole)
                namex = control.read_record(f'name[{res.getdata("locale")}]', f'/usr/share/applications/{name}')
                if namex == '' or namex == None:
                    namex = control.read_record(f'name[en]', f'/usr/share/applications/{name}')
                it.setData(namex, self.LabelRole)
                it.setData(res.qmlget(control.read_record('logo', f'/usr/share/applications/{name}')), self.LogoRole)
                model.appendRow(it)
        return model

    def IconThemeModel(self):
        model = QtGui.QStandardItemModel()
        roles = {self.ITNAME:b'name',self.ITNAMEX:b'namex',self.ITLOGO:b'logo'}
        model.setItemRoleNames(roles)
        for name in files.list('/usr/share/themes/icon'):
                it = QtGui.QStandardItem(name)
                it.setData(name, self.ITNAME)
                namex = control.read_record(f'name[{res.getdata("locale")}]', f'/usr/share/themes/icon/{name}')
                if namex == '' or namex == None:
                    namex = control.read_record(f'name[en]', f'/usr/share/themes/icon/{name}')
                it.setData(namex, self.ITNAMEX)
                it.setData(res.qmlget(control.read_record('logo', f'/usr/share/themes/icon/{name}')), self.ITLOGO)
                model.appendRow(it)
        return model


    def CursorThemeModel(self):
        model = QtGui.QStandardItemModel()
        roles = {self.ITNAME:b'name',self.ITNAMEX:b'namex',self.ITLOGO:b'logo'}
        model.setItemRoleNames(roles)
        for name in files.list('/usr/share/themes/cursor'):
                it = QtGui.QStandardItem(name)
                it.setData(name, self.ITNAME)
                namex = control.read_record(f'name[{res.getdata("locale")}]', f'/usr/share/themes/cursor/{name}')
                if namex == '' or namex == None:
                    namex = control.read_record(f'name[en]', f'/usr/share/themes/cursor/{name}')
                it.setData(namex, self.ITNAMEX)
                it.setData(res.qmlget(control.read_record('logo', f'/usr/share/themes/cursor/{name}')), self.ITLOGO)
                model.appendRow(it)
        return model

    def ShellThemeModel(self):
        model = QtGui.QStandardItemModel()
        roles = {self.ITNAME:b'name',self.ITNAMEX:b'namex',self.ITLOGO:b'logo'}
        model.setItemRoleNames(roles)
        for name in files.list('/usr/share/themes/shell'):
                it = QtGui.QStandardItem(name)
                it.setData(name, self.ITNAME)
                namex = control.read_record(f'name[{res.getdata("locale")}]', f'/usr/share/themes/shell/{name}')
                if namex == '' or namex == None:
                    namex = control.read_record(f'name[en]', f'/usr/share/themes/shell/{name}')
                it.setData(namex, self.ITNAMEX)
                it.setData(res.qmlget(control.read_record('logo', f'/usr/share/themes/shell/{name}')), self.ITLOGO)
                model.appendRow(it)
        return model

    def ApplicationThemeModel(self):
        model = QtGui.QStandardItemModel()
        roles = {self.ITNAME:b'name',self.ITNAMEX:b'namex',self.ITLOGO:b'logo'}
        model.setItemRoleNames(roles)
        for name in files.list('/usr/share/themes/gtk'):
                it = QtGui.QStandardItem(name)
                it.setData(name, self.ITNAME)
                namex = control.read_record(f'name[{res.getdata("locale")}]', f'/usr/share/themes/gtk/{name}')
                if namex == '' or namex == None:
                    namex = control.read_record(f'name[en]', f'/usr/share/themes/gtk/{name}')
                it.setData(namex, self.ITNAMEX)
                it.setData(res.qmlget(control.read_record('logo', f'/usr/share/themes/gtk/{name}')), self.ITLOGO)
                model.appendRow(it)
        return model


    def WindowThemeModel(self):
        model = QtGui.QStandardItemModel()
        roles = {self.ITNAME:b'name',self.ITNAMEX:b'namex',self.ITLOGO:b'logo'}
        model.setItemRoleNames(roles)
        for name in files.list('/usr/share/themes/qml'):
                it = QtGui.QStandardItem(name)
                it.setData(name, self.ITNAME)
                namex = control.read_record(f'name[{res.getdata("locale")}]', f'/usr/share/themes/qml/{name}')
                if namex == '' or namex == None:
                    namex = control.read_record(f'name[en]', f'/usr/share/themes/qml/{name}')
                it.setData(namex, self.ITNAMEX)
                it.setData(res.qmlget(control.read_record('logo', f'/usr/share/themes/qml/{name}')), self.ITLOGO)
                model.appendRow(it)
        return model


    def GlobalThemeModel(self):
        model = QtGui.QStandardItemModel()
        roles = {self.ITNAME:b'name',self.ITNAMEX:b'namex',self.ITLOGO:b'logo'}
        model.setItemRoleNames(roles)
        for name in files.list('/usr/share/themes/global'):
                it = QtGui.QStandardItem(name)
                it.setData(name, self.ITNAME)
                namex = control.read_record(f'name[{res.getdata("locale")}]', f'/usr/share/themes/global/{name}')
                if namex == '' or namex == None:
                    namex = control.read_record(f'name[en]', f'/usr/share/themes/global/{name}')
                it.setData(namex, self.ITNAMEX)
                it.setData(res.qmlget(control.read_record('logo', f'/usr/share/themes/global/{name}')), self.ITLOGO)
                model.appendRow(it)
        return model

    def ContactModel (self,list):
        model = QtGui.QStandardItemModel()
        roles = {
            self.CName:b'username',
            self.CFullName:b'fullname',
        }
        model.setItemRoleNames(roles)

        for i in list:
            it = QtGui.QStandardItem(i['username'])
            it.setData(i['username'],self.CName)
            
            if i['fullname']=='' or i['fullname']==None:
                it.setData(i['username'],self.CName)
            else:
                it.setData(i['fullname'],self.CFullName)
            model.appendRow(it)
        return model

    def NetworkModel (self):
        model = QtGui.QStandardItemModel()
        roles = {
            self.BSSID:b"bssid",
            self.SSID:b"ssid",
            self.SIGNAL:b"signal",
            self.MODE:b'mode',
            self.CHAN:b'chan',
            self.RATE:b'rate',
            self.SECURITY:b'security',
            self.NETLOGO:b'netlogo'
        }
        model.setItemRoleNames(roles)

        # list of wifi informations

        subprocess.call('nmcli -t -f BSSID dev wifi list > /stor/etc/network/bssid.list',shell=True)
        subprocess.call('nmcli -t -f SSID dev wifi list > /stor/etc/network/ssid.list',shell=True)
        subprocess.call('nmcli -t -f SIGNAL dev wifi list > /stor/etc/network/signal.list',shell=True)
        subprocess.call('nmcli -t -f MODE dev wifi list > /stor/etc/network/mode.list',shell=True)
        subprocess.call('nmcli -t -f CHAN dev wifi list > /stor/etc/network/chan.list',shell=True)
        subprocess.call('nmcli -t -f RATE dev wifi list > /stor/etc/network/rate.list',shell=True)
        subprocess.call('nmcli -t -f SECURITY dev wifi list > /stor/etc/network/security.list',shell=True)

        # get lists
        bssid = control.read_list('/etc/network/bssid.list')
        ssid = control.read_list('/etc/network/ssid.list')
        signal = control.read_list('/etc/network/signal.list')
        mode = control.read_list('/etc/network/mode.list')
        rate = control.read_list('/etc/network/rate.list')
        security = control.read_list('/etc/network/security.list')

        if '' in bssid:
            bssid.remove('')

        if '' in ssid:
            ssid.remove('')

        if '' in signal:
            signal.remove('')

        if '' in mode:
            mode.remove('')

        if '' in rate:
            rate.remove('')

        if '' in security:
            security.remove('')

        j = 0
        for i in ssid:
            it = QtGui.QStandardItem(i)
            it.setData(i,self.SSID)
            it.setData(bssid[j],self.BSSID)
            it.setData(signal[j],self.SIGNAL)
            try:
                if int(signal[j])<=20:
                    it.setData(res.qmlget('@icon/w020'),self.NETLOGO)
                elif int(signal[j])<=40:
                    it.setData(res.qmlget('@icon/w040'),self.NETLOGO)
                elif int(signal[j])<=80:
                    it.setData(res.qmlget('@icon/w080'),self.NETLOGO)
                elif int(signal[j])<=10:
                    it.setData(res.qmlget('@icon/w100'),self.NETLOGO)
            except:
                it.setData(res.qmlget('@icon/w020'),self.NETLOGO)
            it.setData(mode[j],self.MODE)
            it.setData(rate[j],self.RATE)
            it.setData(security[j],self.SECURITY)
            model.appendRow(it)
            j+=1
        return model

    def DisplayModel (self):
        model = QtGui.QStandardItemModel()
        roles = {
            self.DISPLAY:b"display",
        }
        model.setItemRoleNames(roles)

        os.system("xrandr | awk '{print $1}' > /stor/tmp/display.list")
        displaylist = control.read_list('/tmp/display.list')
        displaylist.pop(0)
        displaylist.pop(1)
        try:
            if '' in displaylist:
                displaylist.remove ('')
            if 'Virtual-1':
                displaylist.remove ('Virtual-1')
        except:
            pass
        displaylist.sort()

        for i in displaylist:
            it = QtGui.QStandardItem(i)
            it.setData(i,self.DISPLAY)
            model.appendRow(it)
        return model

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

    def UserModel (self):
        model = QtGui.QStandardItemModel()
        roles = {
            self.Username:b'username',
            self.Profile:b'profile',
            self.FullName:b'fullname',
        }
        model.setItemRoleNames(roles)

        listusers = files.list('/etc/users')

        for i in listusers:
            it = QtGui.QStandardItem(i)
            it.setData(i,self.Username)
            if control.read_record('fullname',f'/etc/users/{i}')=='':
                it.setData(i,self.FullName)
            else:
                it.setData(control.read_record('fullname',f'/etc/users/{i}'),self.FullName)

            try:
                if control.read_record('profile',f'/etc/users/{i}').startswith('@icon/'):
                    it.setData(res.qmlget(control.read_record('profile',f'/etc/users/{i}')),self.Profile)
                else:
                    it.setData(files.input_qml(control.read_record('profile',f'/etc/users/{i}')),self.Profile)
            except:
                it.setData(files.input_qml('@icon/users'), self.Profile)
            model.appendRow(it)

        return model

    def ProjectModel (self):
        model = QtGui.QStandardItemModel()
        roles = {
            self.ProjectName:b'name',
            self.ProjectType:b'type',
            self.ProjectPackage:b'package',
        }
        model.setItemRoleNames(roles)

        self.user = files.readall('/proc/info/su')
        if self.user=='root':
            self.projectdir = f'/root/Projects'
        else:
            self.projectdir = f'/desk/{self.user}/Projects'

        self.listprojects = files.list(self.projectdir)
        self.listprojects.sort()

        for i in self.listprojects:
            if files.isfile (f'{self.projectdir}/{i}/config'):
                it = QtGui.QStandardItem(i)
                it.setData(i,self.ProjectName)
                it.setData(control.read_record('project_type',f'{self.projectdir}/{i}/config'),self.ProjectType)
                it.setData(control.read_record('project_name',f'{self.projectdir}/{i}/config'),self.ProjectPackage)
                    
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

        hidden_files = files.readall('/etc/default/hidden_files')

        for i in files.list(directory):
            if files.isdir(f'{directory}/{i}'):
                if (i.startswith('.') or (i.startswith ('__') and i.endswith ('__'))) and hidden_files=='Yes':
                    pass
                else:
                    listx.append(i)

        listx.sort()

        for i in files.list(directory):
            if files.isfile(f'{directory}/{i}'):
                if (i.startswith('.') or (i.startswith ('__') and i.endswith ('__'))) and hidden_files=='Yes':
                    pass
                else:
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
                        it.setData(res.qmlget('@icon/folder'),self.FileLogo)
                else:
                    if i.lower()=='install':
                        it.setData(res.qmlget('@icon/file-install'),self.FileLogo)
                    elif i.lower() == 'makefile':
                        it.setData(res.qmlget('@icon/file-makefile'), self.FileLogo)
                    elif i.lower() == 'authers':
                        it.setData(res.qmlget('@icon/file-authers'), self.FileLogo)
                    elif i.lower() == 'copying':
                        it.setData(res.qmlget('@icon/file-copying'), self.FileLogo)
                    elif i.lower() == 'readme':
                        it.setData(res.qmlget('@icon/file-readme'), self.FileLogo)
                    elif i.lower() == 'credits':
                        it.setData(res.qmlget('@icon/file-credits'), self.FileLogo)
                    else:
                        it.setData(res.qmlget('@icon/file'),self.FileLogo)
            else:
                if files.isfile(f'{directory}/{i}'):
                    if i.endswith('.desk'):
                        it.setData(res.qmlget(control.read_record (f'logo',f'{directory}/{i}')),self.FileLogo)
                    elif i.endswith ('.png') or i.endswith ('.jpg') or i.endswith ('.jpeg') or i.endswith ('.bmp') or i.endswith ('.tiff') or i.endswith ('.tif') or i.endswith ('.gif') or i.endswith ('.svg'):
                        it.setData(files.input_qml(f'{directory}/{i}'),self.FileLogo)
                    else:
                        if res.get(f'@icon/file-{ext.replace(".","")}')=='':
                            it.setData(res.qmlget('@icon/file'),self.FileLogo)
                        else:
                            it.setData(res.qmlget(f'@icon/file-{ext.replace(".","")}'),self.FileLogo)
                else:
                    if files.isfile (f'{directory}/{i}/.logo'):
                        it.setData(res.qmlget(files.readall(f'{directory}/{i}/.logo')),self.FileLogo)
                    else:
                        it.setData(res.qmlget('@icon/folder'),self.FileLogo)

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

    def PackageModel(self):
        model = QtGui.QStandardItemModel()
        roles = {
            self.PKG_NAME:b'name',
            self.PKG_NAMEX:b'namex',
            self.PKG_BUILD:b'build',
            self.PKG_COPYRIGHT:b'copyright',
            self.PKG_LICENSE:b'license',
            self.PKG_DESCRIPTION:b'description',
            self.PKG_MIRROR:b'mirror',
            self.PKG_UNPACK:b'unpack',
            self.PKG_TYPE:b'type',
            self.PKG_INSTALLED:b'installed',
            self.PKG_VERSION:b'version',
            self.PKG_LOGO:b'logo'
        }
        model.setItemRoleNames(roles)

        packages = files.list('/app/mirrors')
        packages.sort()

        packagesx = []

        for j in packages:
            if j.endswith('.manifest'):
                packagesx.append(j)
        packagesx.sort()

        for i in packagesx:
            it = QtGui.QStandardItem(i)
            if files.isfile (f'/app/packages/{i}'):
                it.setData(True,self.PKG_INSTALLED)
            else:
                it.setData(False,self.PKG_INSTALLED)
                
            it.setData(control.read_record('build',f'/app/mirrors/{i}'),self.PKG_BUILD)
            it.setData(control.read_record('name',f'/app/mirrors/{i}'),self.PKG_NAME)
            it.setData(control.read_record('license',f'/app/mirrors/{i}'),self.PKG_LICENSE)
            it.setData(control.read_record('copyright',f'/app/mirrors/{i}'),self.PKG_COPYRIGHT)
            it.setData(control.read_record('unpack',f'/app/mirrors/{i}'),self.PKG_UNPACK)
            it.setData(control.read_record('mirror',f'/app/mirrors/{i}'),self.PKG_MIRROR)
            it.setData(control.read_record('description',f'/app/mirrors/{i}'),self.PKG_DESCRIPTION)
            it.setData(control.read_record('version',f'/app/mirrors/{i}'),self.PKG_VERSION)
            
            if files.isfile (f'/usr/share/applications/{control.read_record("entry",f"/app/mirrors/{i}")}.desk'):
                it.setData('application',self.PKG_TYPE)
            else:
                it.setData('package',self.PKG_TYPE)

            locale = res.getdata ('locale')
            
            if control.read_record (f'name[{locale}]',f'/app/mirrors/{i}')=='' or control.read_record (f'name[{locale}]',f'/app/mirrors/{i}')==None:
                it.setData( control.read_record ('name[en]',f'/app/mirrors/{i}'),self.PKG_NAMEX)
            else:
                it.setData( control.read_record (f'name[{locale}]',f'/app/mirrors/{i}'),self.PKG_NAMEX)

            #i = i.replace('.manifest','')


            if control.read_record('logo.inside',f'/app/mirrors/{i}')==None or res.get(control.read_record('logo.inside',f'/app/mirrors/{i}'))=='':
                if not control.read_record (f'logo',f'/app/mirrors/{i}')==None:
                    it.setData(control.read_record (f'logo',f'/app/mirrors/{i}'),self.PKG_LOGO)
                else:
                    it.setData(res.qmlget('@icon/archive'),self.PKG_LOGO)
            else:
                it.setData(res.qmlget(control.read_record('logo.inside',f'/app/mirrors/{i}')),self.PKG_LOGO)

            model.appendRow(it)
        return model


    def addItemModel (self,nameModel,listModel):
        self.newmodel = self.ItemModel(listModel)
        self.rootContext().setContextProperty(nameModel, self.newmodel)

    def addMailModel (self):
        self.mdlxa = self.MailModel()
        self.rootContext().setContextProperty('MailModel', self.mdlxa)

    def addFileModel (self,directory):
        self.newmodelx = self.FileModel(directory)
        self.rootContext().setContextProperty('FileModel', self.newmodelx)

    def addUserModel (self):
        self.newmodelx1 = self.UserModel()
        self.rootContext().setContextProperty('UserModel', self.newmodelx1)

    def addPackageModel (self):
        self.pkgmodel = self.PackageModel()
        self.rootContext().setContextProperty('PackageModel', self.pkgmodel)

    def addDisplayModel (self):
        self.displaymodel = self.DisplayModel()
        self.rootContext().setContextProperty('DisplayModel', self.displaymodel)

    def addNetworkModel (self):
        self.networkmdl = self.NetworkModel()
        self.rootContext().setContextProperty('NetworkModel', self.networkmdl)

    def addApplicationModel (self,ext):
        self.appmdl = self.ApplicationModel(ext)
        self.rootContext().setContextProperty('ApplicationModel', self.appmdl)

    def addLanguageModel (self):
        self.langmdl = self.LanguageModel()
        self.rootContext().setContextProperty('LanguageModel', self.langmdl)
        
    def addJooyaHistoryModel (self):
        self.jh = self.JooyaHistoryModel()
        self.rootContext().setContextProperty('JooyaHistoryModel', self.jh)

    def addJooyaBookmarkModel (self):
        self.jb = self.JooyaBookmarkModel()
        self.rootContext().setContextProperty('JooyaBookmarkModel', self.jb)

    def addJooyaSearchEngineModel (self):
        self.je = self.JooyaSearchEngineModel()
        self.rootContext().setContextProperty('JooyaSearchEngineModel', self.je)

    def addContactModel (self,listx):
        self.cntmdl = self.ContactModel(listx)
        self.rootContext().setContextProperty('ContactModel', self.cntmdl)

    def addCopyDiskModel (self):
        self.xdcopydiskmdl = self.CopyDiskModel()
        self.rootContext().setContextProperty('CopyDiskModel', self.xdcopydiskmdl)

    def addFeedModel (self):
        self.xdmx = self.FeedModel()
        self.rootContext().setContextProperty('FeedModel', self.xdmx)

    def addDrivesModel (self):
        self.xddrivesmodel = self.DrivesModel()
        self.rootContext().setContextProperty('DrivesModel', self.xddrivesmodel)

    def addProcessModel (self):
        self.xprocessmdl = self.ProcessModel()
        self.rootContext().setContextProperty('ProcessModel', self.xprocessmdl)

    def addProjectModel (self):
        self.apmdl = self.ProjectModel()
        self.rootContext().setContextProperty('ProjectModel', self.apmdl)

    def addIconThemeModel (self):
        self.xitmdl = self.IconThemeModel()
        self.rootContext().setContextProperty('IconThemeModel', self.xitmdl)

    def addCursorThemeModel (self):
        self.xctmdl = self.CursorThemeModel()
        self.rootContext().setContextProperty('CursorThemeModel', self.xctmdl)

    def addApplicationThemeModel (self):
        self.xatmdl = self.ApplicationThemeModel()
        self.rootContext().setContextProperty('ApplicationThemeModel', self.xatmdl)

    def addWindowThemeModel (self):
        self.xwtmdl = self.WindowThemeModel()
        self.rootContext().setContextProperty('WindowThemeModel', self.xwtmdl)

    def addShellThemeModel (self):
        self.xstmdl = self.ShellThemeModel()
        self.rootContext().setContextProperty('ShellThemeModel', self.xstmdl)

    def addGlobalThemeModel (self):
        self.xgtmdl = self.GlobalThemeModel()
        self.rootContext().setContextProperty('GlobalThemeModel', self.xgtmdl)

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

# Notification Dialog
class Notif (MainApp):

    def view_(self):
        self.close()
        app.start(self.app_,self.open_)

    def __init__(self,title:str,text:str,app_:str,open_:str):
        super(Notif, self).__init__()

        files.write('/proc/info/id','notif')

        self.app_ = app_
        self.open_ = open_

        self.load(res.get('@layout/notif'))
        self.setProperty('title', title)
        app.launchedlogo(title,res.etc(app_,'logo'))
        
        self.imgNotif = self.findChild('imgNotif')
        self.imgNotif.setProperty('source',res.qmlget(res.etc(app_,'logo')))
        self.txtText = self.findChild('txtText')
        self.txtText.setProperty('text', text)
        self.btnView = self.findChild('btnView')
        self.btnView.setProperty('text', res.get('@string/view'))
        self.btnView.clicked.connect(self.view_)

        QTimer.singleShot(8000,self.close)

# Sharelink Dialog
class Sharelink (MainApp):
    def __init__(self,title:str,text:str):
        super(Sharelink, self).__init__()
        files.write('/proc/info/id','sharelink')
        self.load(res.get('@layout/sharelink'))
        self.setProperty('title', title)
        self.leText = self.findChild('txtText')
        self.leText.setProperty('text', text)
        self.btnCopy = self.findChild('btnCopy')
        self.btnCopy.setProperty('text', res.get('@string/copy'))

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
        self.btnOK.setProperty('text', res.get('@string/ok'))
        self.btnOK.clicked.connect(self.ok_)
        self.btnCancel = self.findChild('btnCancel')
        self.btnCancel.setProperty('text', res.get('@string/cancel'))
        self.btnCancel.clicked.connect(self.close)

class Perm:
    def __init__(self):
        super(Perm, self).__init__()

        self.w = Text (res.get('@string/perm'),res.get('@string/perm_message'))

class Sudo:
    def done_(self,password):
        if hashlib.sha3_512(password.encode()).hexdigest()==control.read_record ('code',f'/etc/users/{self.su}'):
            self.x = self.app()
        else:
            self.x = Perm()

    def __init__(self, app):
        super(Sudo, self).__init__()

        su = files.readall('/proc/info/su')
        self.su = su
        self.app = app

        if su=='root':
            self.x = self.app()
        elif su=='guest':
            self.x = Perm()
        elif not su in files.readall('/etc/sudoers'):
            self.x = Perm()
        else:
            self.w = Password(res.get('@string/password_placeholder').replace('{0}',su),self.done_)

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
        self.setProperty('title',res.get('@string/fonts'))
        self.function = function
        self.bt = self.findChild("bt")
        self.btnSelect = self.findChild("btnSelect")
        self.btnCancel = self.findChild("btnCancel")
        self.btnCancel.clicked.connect(self.close)
        self.btnSelect.clicked.connect(self.ok_)
        self.btnSelect.setProperty('title',res.get('@string/select'))

class Select (MainApp):

    file = ''
    isdetail = False

    def loop (self):
        self.title.setProperty('text', files.readall('/proc/info/pwd'))
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

    def MakeDetail (self):
        if self.isdetail:
            self.ListView.setProperty('visible',True)
            self.Details.setProperty('visible',False)
            self.isdetail = False
        else:
            self.ListView.setProperty('visible',False)
            self.Details.setProperty('visible',True)
            self.isdetail = True

    def __init__(self,function):
        super(MainApp, self).__init__()

        self.function = function

        self.addFileModel(files.readall('/proc/info/pwd'))
        self.load (res.get('@layout/select'))
        self.setProperty('title',res.get('@string/select_file'))
        self.fsel = self.findChild ('fsel')

        self.btnCancel = self.findChild('btnCancel')
        self.title = self.findChild('title')
        self.btnCancel.setProperty('text', res.get('@string/cancel'))
        self.btnSelect = self.findChild('btnSelect')
        self.ListView = self.findChild('ListView')
        self.Details = self.findChild('Details')
        self.btnCancel.clicked.connect (self.close)
        self.btnSelect.setProperty('text', res.get('@string/select'))
        self.btnSelect.clicked.connect (self.select_)

        self.btnDetail = self.findChild('btnDetail')
        self.btnDetail.clicked.connect (self.MakeDetail)

        self.loop()


class Open (MainApp):

    isdetail = False

    def loop (self):
        if not self.fsel.property('text')=='':
            self.title.setProperty('text', files.readall('/proc/info/pwd'))
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

    def MakeDetail (self):
        if self.isdetail:
            self.ListView.setProperty('visible',True)
            self.Details.setProperty('visible',False)
            self.isdetail = False
        else:
            self.ListView.setProperty('visible',False)
            self.Details.setProperty('visible',True)
            self.isdetail = True

    def __init__(self,function):
        super(MainApp, self).__init__()

        self.function = function

        self.addFileModel(files.readall('/proc/info/pwd'))
        self.load (res.get('@layout/open'))
        self.setProperty('title',res.get('@string/select_folder'))
        self.fsel = self.findChild ('fsel')

        self.btnCancel = self.findChild('btnCancel')
        self.title = self.findChild('title')
        self.ListView = self.findChild('ListView')
        self.Details = self.findChild('Details')
        self.btnCancel.setProperty('text', res.get('@string/cancel'))
        self.btnOpen = self.findChild('btnOpen')
        self.btnDetail = self.findChild('btnDetail')
        self.btnDetail.clicked.connect (self.MakeDetail)
        self.btnCancel.clicked.connect (self.close)
        self.btnOpen.setProperty('text',res.get('@string/open'))
        self.btnOpen.clicked.connect (self.open_)

        self.loop()


class Save (MainApp):
    isdetail = False
    def loop (self):
        self.title.setProperty('text', files.readall('/proc/info/pwd'))
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

    def MakeDetail (self):
        if self.isdetail:
            self.ListView.setProperty('visible',True)
            self.Details.setProperty('visible',False)
            self.isdetail = False
        else:
            self.ListView.setProperty('visible',False)
            self.Details.setProperty('visible',True)
            self.isdetail = True

    def __init__(self,function):
        super(MainApp, self).__init__()

        self.function = function

        self.addFileModel(files.readall('/proc/info/pwd'))
        self.load (res.get('@layout/save'))
        self.setProperty('title',res.get('@string/save'))
        self.fsel = self.findChild ('fsel')

        self.btnCancel = self.findChild('btnCancel')
        self.title = self.findChild('title')
        self.btnCancel.setProperty('text',res.get('@string/cancel'))
        self.btnSave = self.findChild('btnSave')
        self.btnCancel.clicked.connect (self.close)
        self.btnSave.clicked.connect (self.save_)
        self.ListView = self.findChild('ListView')
        self.btnDetail = self.findChild('btnDetail')
        self.btnDetail.clicked.connect (self.MakeDetail)
        self.Details = self.findChild('Details')
        self.btnSave.setProperty('text',res.get('@string/save'))

        self.leName = self.findChild('leName')
        self.leName.setProperty('placeholderText',res.get('@string/fullname'))

        self.loop()

class IconTheme (MainApp):

    def loop (self):
        if not self.tsel.property('text')=='':
            self.btnChange.setProperty('enabled',True)

        QTimer.singleShot (10,self.loop)

    def change_(self):
        self.function (self.tsel.property('text'))
        self.close()

    def __init__(self,function):
        super(MainApp, self).__init__()

        self.function = function

        self.addIconThemeModel()
        self.load (res.get('@layout/icon_theme'))
        self.setProperty('title',res.get('@string/icon'))
        self.tsel = self.findChild ('tsel')
        self.btnCancel = self.findChild('btnCancel')
        self.title = self.findChild('title')
        self.ListView = self.findChild('ListView')
        self.btnCancel.setProperty('text', res.get('@string/cancel'))
        self.btnChange = self.findChild('btnChange')
        self.btnCancel.clicked.connect (self.close)
        self.btnChange.setProperty('text',res.get('@string/change'))
        self.btnChange.clicked.connect (self.change_)

        self.loop()

class ApplicationTheme (MainApp):

    def loop (self):
        if not self.tsel.property('text')=='':
            self.btnChange.setProperty('enabled',True)

        QTimer.singleShot (10,self.loop)

    def change_(self):
        self.function (self.tsel.property('text'))
        self.close()

    def __init__(self,function):
        super(MainApp, self).__init__()

        self.function = function

        self.addApplicationThemeModel()
        self.load (res.get('@layout/application_theme'))
        self.setProperty('title',res.get('@string/gtk'))
        self.tsel = self.findChild ('tsel')
        self.btnCancel = self.findChild('btnCancel')
        self.title = self.findChild('title')
        self.ListView = self.findChild('ListView')
        self.btnCancel.setProperty('text', res.get('@string/cancel'))
        self.btnChange = self.findChild('btnChange')
        self.btnCancel.clicked.connect (self.close)
        self.btnChange.setProperty('text',res.get('@string/change'))
        self.btnChange.clicked.connect (self.change_)

        self.loop()

class WindowTheme (MainApp):

    def loop (self):
        if not self.tsel.property('text')=='':
            self.btnChange.setProperty('enabled',True)

        QTimer.singleShot (10,self.loop)

    def change_(self):
        self.function (self.tsel.property('text'))
        self.close()

    def __init__(self,function):
        super(MainApp, self).__init__()

        self.function = function

        self.addWindowThemeModel()
        self.load (res.get('@layout/window_theme'))
        self.setProperty('title',res.get('@string/window'))
        self.tsel = self.findChild ('tsel')
        self.btnCancel = self.findChild('btnCancel')
        self.title = self.findChild('title')
        self.ListView = self.findChild('ListView')
        self.btnCancel.setProperty('text', res.get('@string/cancel'))
        self.btnChange = self.findChild('btnChange')
        self.btnCancel.clicked.connect (self.close)
        self.btnChange.setProperty('text',res.get('@string/change'))
        self.btnChange.clicked.connect (self.change_)

        self.loop()

class CursorTheme (MainApp):

    def loop (self):
        if not self.tsel.property('text')=='':
            self.btnChange.setProperty('enabled',True)

        QTimer.singleShot (10,self.loop)

    def change_(self):
        self.function (self.tsel.property('text'))
        self.close()

    def __init__(self,function):
        super(MainApp, self).__init__()

        self.function = function

        self.addCursorThemeModel()
        self.load (res.get('@layout/cursor_theme'))
        self.setProperty('title',res.get('@string/cursor'))
        self.tsel = self.findChild ('tsel')
        self.btnCancel = self.findChild('btnCancel')
        self.title = self.findChild('title')
        self.ListView = self.findChild('ListView')
        self.btnCancel.setProperty('text', res.get('@string/cancel'))
        self.btnChange = self.findChild('btnChange')
        self.btnCancel.clicked.connect (self.close)
        self.btnChange.setProperty('text',res.get('@string/change'))
        self.btnChange.clicked.connect (self.change_)

        self.loop()

class ShellTheme (MainApp):

    def loop (self):
        if not self.tsel.property('text')=='':
            self.btnChange.setProperty('enabled',True)

        QTimer.singleShot (10,self.loop)

    def change_(self):
        self.function (self.tsel.property('text'))
        self.close()

    def __init__(self,function):
        super(MainApp, self).__init__()

        self.function = function

        self.addShellThemeModel()
        self.load (res.get('@layout/shell_theme'))
        self.setProperty('title',res.get('@string/shell'))
        self.tsel = self.findChild ('tsel')
        self.btnCancel = self.findChild('btnCancel')
        self.title = self.findChild('title')
        self.ListView = self.findChild('ListView')
        self.btnCancel.setProperty('text', res.get('@string/cancel'))
        self.btnChange = self.findChild('btnChange')
        self.btnCancel.clicked.connect (self.close)
        self.btnChange.setProperty('text',res.get('@string/change'))
        self.btnChange.clicked.connect (self.change_)

        self.loop()

class GlobalTheme (MainApp):

    def loop (self):
        if not self.tsel.property('text')=='':
            self.btnChange.setProperty('enabled',True)

        QTimer.singleShot (10,self.loop)

    def change_(self):
        self.function (self.tsel.property('text'))
        self.close()

    def __init__(self,function):
        super(MainApp, self).__init__()

        self.function = function

        self.addGlobalThemeModel()
        self.load (res.get('@layout/global_theme'))
        self.setProperty('title',res.get('@string/global'))
        self.tsel = self.findChild ('tsel')
        self.btnCancel = self.findChild('btnCancel')
        self.title = self.findChild('title')
        self.ListView = self.findChild('ListView')
        self.btnCancel.setProperty('text', res.get('@string/cancel'))
        self.btnChange = self.findChild('btnChange')
        self.btnCancel.clicked.connect (self.close)
        self.btnChange.setProperty('text',res.get('@string/change'))
        self.btnChange.clicked.connect (self.change_)

        self.loop()

# Ask Dialog
class Install (MainApp):

    def install_(self):
        System ('sudo paye cl')
        System (f'sudo paye upak {self.package}')
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
        self.setProperty('title',res.get('@string/install_package').replace('{0}',package).replace('/','') )
        shutil.unpack_archive (files.input (package),files.input('/tmp/package-installer'),'zip')
        shutil.unpack_archive (files.input('/tmp/package-installer/control.zip'),files.input('/tmp/package-installer.control'),'zip')
        files.removedirs ('/tmp/package-installer')
        
        self.pro = self.findChild('pro')
        self.logo = self.findChild('logo')
        self.logo.setProperty('source',res.qmlget('@icon/archive'))
        self.name = self.findChild('name')
        self.name.setProperty('text',control.read_record ('name','/tmp/package-installer.control/manifest'))
        self.description = self.findChild('descriptionx')
        self.description.setProperty('text',control.read_record ('description','/tmp/package-installer.control/manifest'))
        self.btnOK = self.findChild('btnOK')
        self.btnOK.setProperty('text', res.get('@string/install'))
        self.btnOK.clicked.connect(self.ok_)
        self.btnCancel = self.findChild('btnCancel')
        self.btnCancel.setProperty('text', res.get('@string/cancel'))
        self.btnCancel.clicked.connect(self.no_)

class Download (MainApp):
    def save_(self,filename):
        commands.mv (['/tmp/download.tmp',filename])

    def set_progressbar_value (self,value):
        self.pro.setProperty('value',value/100)
        if value == 100:
            self.close()
            self.x = Save (self.save_)
            return

    def download_(self):
        the_filesize = requests.get(self.leDownload.property('text'), stream=True).headers['Content-Length']
        the_fileobj = open(files.input('/tmp/download.tmp'), 'wb')
        self.downloadThread = DownloadThread(self.leDownload.property('text'), the_filesize, the_fileobj, buffer=10240)
        self.downloadThread.download_proess_signal.connect(self.set_progressbar_value)
        self.downloadThread.start()
    def __init__(self):
        super(MainApp, self).__init__()

        self.load(res.get('@layout/download'))
        self.pro = self.findChild('pro')
        self.setProperty('title',res.get('@string/download'))
        self.btnDownload = self.findChild('btnDownload')
        self.btnDownload.setProperty('text',res.get('@string/download'))
        self.leDownload = self.findChild('leDownload')
        self.leDownload.setProperty('placeholderText',res.get('@string/url'))

        self.btnDownload.clicked.connect (self.download_)

class DownloadThread(QThread):
    download_proess_signal = pyqtSignal(int)                        #Create signal

    def __init__(self, url, filesize, fileobj, buffer):
        super(DownloadThread, self).__init__()
        self.url = url
        self.filesize = filesize
        self.fileobj = fileobj
        self.buffer = buffer

    def run(self):
        try:
            rsp = requests.get(self.url, stream=True)                #Streaming download mode
            offset = 0
            for chunk in rsp.iter_content(chunk_size=self.buffer):
                if not chunk: break
                self.fileobj.seek(offset)                            #Setting Pointer Position
                self.fileobj.write(chunk)                            #write file
                offset = offset + len(chunk)
                proess = offset / int(self.filesize) * 100
                self.download_proess_signal.emit(int(proess))        #Sending signal
            #######################################################################
            self.fileobj.close()    #Close file
            self.exit(0)            #Close thread


        except Exception as e:
            print(e)

class OpenWith(MainApp):
    def atonce_(self):
        app.start (self.asel.property('text').replace('.desk',''),f'"{self.filename}"')
        self.close()

    def always_ (self):
        ext = os.path.splitext(self.filename)[1].replace('.','')
        control.write_record (f'{ext}.always',self.asel.property('text').replace('.desk',''),'/etc/ext')
        self.atonce_()

    def __init__(self,filename):
        super(OpenWith, self).__init__()
        self.addApplicationModel(filename)
        self.load(res.get('@layout/openwith'))
        self.setProperty('title',res.get('@string/openwith'))

        self.filename = filename

        self.asel = self.findChild('asel')

        self.atonce = self.findChild('atOnce')
        self.atonce.clicked.connect (self.atonce_)
        self.atonce.setProperty('text',res.get('@string/atonce'))
        self.always = self.findChild('always')
        self.always.clicked.connect (self.always_)
        self.always.setProperty('text',res.get('@string/always'))


class FileInfo (MainApp):
    def access_show (self,perm,type):
        if type=='owner':
            if perm[1]=='r' and perm[2]=='w' and perm[3]=='x':
                return res.get('@string/rwx')
            elif perm[1]=='r' and perm[2]=='w' and perm[3]=='-':
                return res.get('@string/rw-')
            elif perm[1]=='r' and perm[2]=='-' and perm[3]=='-':
                return res.get('@string/r--')
            elif perm[1]=='-' and perm[2]=='-' and perm[3]=='-':
                return res.get('@string/---')
            elif perm[1]=='-' and perm[2]=='w' and perm[3]=='x':
                return res.get('@string/-wx')
            elif perm[1]=='-' and perm[2]=='-' and perm[3]=='x':
                return res.get('@string/--x')
            elif perm[1]=='-' and perm[2]=='w' and perm[3]=='-':
                return res.get('@string/-w-')
            else:
                return res.get('@string/---')

        elif type=='users':
            if perm[4]=='r' and perm[5]=='w' and perm[6]=='x':
                return res.get('@string/rwx')
            elif perm[4]=='r' and perm[5]=='w' and perm[6]=='-':
                return res.get('@string/rw-')
            elif perm[4]=='r' and perm[5]=='-' and perm[6]=='-':
                return res.get('@string/r--')
            elif perm[4]=='-' and perm[5]=='-' and perm[6]=='-':
                return res.get('@string/---')
            elif perm[4]=='-' and perm[5]=='w' and perm[6]=='x':
                return res.get('@string/-wx')
            elif perm[4]=='-' and perm[5]=='-' and perm[6]=='x':
                return res.get('@string/--x')
            elif perm[4]=='-' and perm[5]=='w' and perm[6]=='-':
                return res.get('@string/-w-')
            else:
                return res.get('@string/---')

        elif type=='guest':
            if perm[7]=='r' and perm[8]=='w' and perm[9]=='x':
                return res.get('@string/rwx')
            elif perm[7]=='r' and perm[8]=='w' and perm[9]=='-':
                return res.get('@string/rw-')
            elif perm[7]=='r' and perm[8]=='-' and perm[9]=='-':
                return res.get('@string/r--')
            elif perm[7]=='-' and perm[8]=='-' and perm[9]=='-':
                return res.get('@string/---')
            elif perm[7]=='-' and perm[8]=='w' and perm[9]=='x':
                return res.get('@string/-wx')
            elif perm[7]=='-' and perm[8]=='-' and perm[9]=='x':
                return res.get('@string/--x')
            elif perm[7]=='-' and perm[8]=='w' and perm[9]=='-':
                return res.get('@string/-w-')
            else:
                return res.get('@string/---')
        else:
            return res.get('@string/---')

    def __init__(self,filename):
        super(FileInfo, self).__init__()

        self.load(res.get('@layout/fileinfo'))

        self.setProperty('title',res.get('@string/info'))

        self.name = self.findChild('name')
        self.type = self.findChild('type')
        self.location = self.findChild('location')
        self.size = self.findChild('size')
        self.created = self.findChild('created')
        self.modified = self.findChild('modified')
        self.ownership = self.findChild('ownership')
        self.perma = self.findChild('perma')
        self.permb = self.findChild('permb')
        self.permc = self.findChild('permc')

        self.name1 = self.findChild('name1')
        self.type1 = self.findChild('type1')
        self.location1 = self.findChild('location1')
        self.size1 = self.findChild('size1')
        self.created1 = self.findChild('created1')
        self.modified1 = self.findChild('modified1')
        self.ownership1 = self.findChild('ownership1')
        self.perma1 = self.findChild('perma1')
        self.permb1 = self.findChild('permb1')
        self.permc1 = self.findChild('permc1')

        self._name = files.filename (filename)

        if '.' in filename and files.isfile (filename):
            ext =os.path.splitext(filename)[1]
            try:
                self._type = control.read_record (f'{ext.replace(".","")}.text','/etc/ext')
            except:
                self._type = res.get('@string/unknown')
        else:
            if files.isdir (filename):
                self._type = res.get('@string/folder')
            else:
                self._type = res.get('@string/unknown')

        #if not '/' in files.output(files.parentdir(filename)).replace('/.//',''):
        #    self._location = '/'
        #else:
        self._location = files.output(files.parentdir(filename)).replace('/.//','')

        size = files.size(filename)

        kB = 1024
        MB = kB*kB
        GB = MB*MB
        TB = GB*GB

        if size<kB:
            self._size = f'{str(size)} B'

        elif size>=kB and size<MB:
            self._size = f'{str(int(size/kB))} kB'

        elif size>=MB and size<GB:
            self._size = f'{str(int(size/MB))} MB'

        elif size>=GB and size<TB:
            self._size = f'{str(int(size/GB))} TB'

        else:
            self._size = f'{str(int(size/TB))} TB'

        perm = permissions.get_permissions(files.output(filename))

        self._created = time.ctime (os.path.getctime(files.input(filename)))
        self._modified = time.ctime (os.path.getctime(files.input(filename)))
        self._ownership = perm.split('/')[1]
        self._perma = self.access_show(perm,'owner')
        self._permb = self.access_show(perm,'users')
        self._permc = self.access_show(perm,'guest')

        if not (res.getuserdata ('locale')=='fa' or res.getuserdata ('locale')=='ar'):
            self.name1.setProperty('text',self._name)
            self.type1.setProperty('text',self._type)
            self.location1.setProperty('text',self._location)
            self.size1.setProperty('text',self._size)
            self.created1.setProperty('text',self._created)
            self.modified1.setProperty('text',self._modified)
            self.ownership1.setProperty('text',self._ownership)
            self.perma1.setProperty('text',self._perma)
            self.permb1.setProperty('text',self._permb)
            self.permc1.setProperty('text',self._permc)

            self.name.setProperty('text',res.get('@string/filename')+": ")
            self.type.setProperty('text',res.get('@string/type')+": ")
            self.location.setProperty('text',res.get('@string/location')+": ")
            self.size.setProperty('text',res.get('@string/size')+": ")
            self.created.setProperty('text',res.get('@string/created')+": ")
            self.modified.setProperty('text',res.get('@string/modified')+": ")
            self.ownership.setProperty('text',res.get('@string/ownership')+": ")
            self.perma.setProperty('text',res.get('@string/access_owner')+": ")
            self.permb.setProperty('text',res.get('@string/access_users')+": ")
            self.permc.setProperty('text',res.get('@string/access_guest')+": ")
        else:
            self.name.setProperty('text',self._name)
            self.type.setProperty('text',self._type)
            self.location.setProperty('text',self._location)
            self.size.setProperty('text',self._size)
            self.created.setProperty('text',self._created)
            self.modified.setProperty('text',self._modified)
            self.ownership.setProperty('text',self._ownership)
            self.perma.setProperty('text',self._perma)
            self.permb.setProperty('text',self._permb)
            self.permc.setProperty('text',self._permc)

            self.name1.setProperty('text',res.get('@string/filename')+": ")
            self.type1.setProperty('text',res.get('@string/type')+": ")
            self.location1.setProperty('text',res.get('@string/location')+": ")
            self.size1.setProperty('text',res.get('@string/size')+": ")
            self.created1.setProperty('text',res.get('@string/created')+": ")
            self.modified1.setProperty('text',res.get('@string/modified')+": ")
            self.ownership1.setProperty('text',res.get('@string/ownership')+": ")
            self.perma1.setProperty('text',res.get('@string/access_owner')+": ")
            self.permb1.setProperty('text',res.get('@string/access_users')+": ")
            self.permc1.setProperty('text',res.get('@string/access_guest')+": ")

class DataInstaller (MainApp):
    namex = ''
    link = ''
    dest = ''
    def restart_(self,yes):
        if yes:
            subprocess.call(['reboot'])

    def set_progressbar_value (self,value):
        self.pro.setProperty('value',value/100)
        if value == 100:
            self.close()
            self.b = Ask (res.get('@string/restart'),res.get('@string/need_restart').replace('{0}',self.namex),self.restart_)
            return

    def install_(self):
        the_url = self.link
        the_filesize = requests.get(the_url, stream=True).headers['Content-Length']
        the_filepath = f'/run/initramfs/memory/data/pyabr/modules/{self.dest}'
        the_fileobj = open(the_filepath, 'wb')
        self.downloadThread = DownloadThread(the_url, the_filesize, the_fileobj, buffer=10240)
        self.downloadThread.download_proess_signal.connect(self.set_progressbar_value)
        self.downloadThread.start()        

    def __init__(self,appname,link,dest):
        super(MainApp, self).__init__()

        self.load (res.get('@layout/datainstaller'))
        self.setProperty('title',res.get('@string/datainstaller'))

        self.namex = res.etc (appname,f'name[en]')
        self.logo = res.qmlget(res.etc (appname,'logo'))
        self.link = link
        self.dest = dest

        self.btnInstall = self.findChild ('btnInstall')
        self.pro = self.findChild ('pro')
        self.logox = self.findChild('logo')
        self.logox.setProperty('source',self.logo)
        self.name = self.findChild('name')
        self.name.setProperty('text',f"{self.namex} Data Installer")
        self.btnInstall.clicked.connect (self.install_)
        self.btnInstall.setProperty('text',res.get('@string/install'))
        self.btnCancel = self.findChild('btnCancel')
        self.btnCancel.setProperty('text',res.get('@string/cancel'))
        self.btnCancel.clicked.connect (self.close)

