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

import sys, subprocess,os,shutil,requests

from libabr import Files, Control, Permissions, Colors, Process, Modules, Package, Commands, Res, System,App

modules = Modules()
files = Files()
control = Control()
colors = Colors()
process = Process()
permissions = Permissions()
pack = Package()
commands = Commands()
res = Res()
app = App()

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
def getdata (name):
    return control.read_record (name,'/etc/gui')

class UserListView (QListView):
    def format(self, it, text):
        self.logo = control.read_record('loginw.userlogo',f'/etc/users/{it.whatsThis()}')
        if self.logo==None:
            it.setIcon(QIcon(res.get('@icon/account')))
        else:
            it.setIcon(QIcon(res.get(self.logo)))
            
        self.fullname = control.read_record('fullname',f'/etc/users/{it.whatsThis()}')
        
        if not self.fullname==None:
            it.setText(self.fullname)
        else:
            it.setText(it.whatsThis())
        
        it.setFont(self.Env.font())

    def __init__(self,ports):
        super().__init__()
        self.ports = ports

        self.Backend = ports[0]
        self.Env = ports[1]
        self.Widget = ports[2]
        self.AppName = ports[3]
        self.External = ports[4]

        self.entry = QStandardItemModel()
        self.setModel(self.entry)
        self.setIconSize(QSize(80, 80))
        self.clicked[QModelIndex].connect(self.on_clicked)
        # When you receive the signal, you call QtGui.QStandardItemModel.itemFromIndex()

        self.setStyleSheet("""
                       QScrollBar
                       {
                       background : white;
                       }
                       QScrollBar::handle
                       {
                       background : #123456;
                       border-radius: 6% 6%;
                       }
                       QScrollBar::handle::pressed
                       {
                       background : #ABCDEF;
                       border-radius: 6% 6%;
                       }""".replace('white', getdata("menu.scroll.bgcolor")).replace('#123456',
                                                                                     getdata(
                                                                                         "menu.scroll.color")).replace(
            '6',
            getdata(
                "menu.scroll.round-size")).replace(
            '#ABCDEF', getdata("menu.scroll.color-hover")))
        # on the given model index to get a pointer to the item

        self.listdir = files.list('/etc/users')
        self.listdir.sort()

        for text in self.listdir:
            it = QStandardItem(text)
            it.setWhatsThis(text)
            self.format(it, text)
            self.entry.appendRow(it)


        self.itemOld = QStandardItem("text")

    def on_clicked(self, index):
        self.item = self.entry.itemFromIndex(index)

        x = hasattr(self.item, 'whatsThis')  # W3CSHCOOL.COM LEARN IT

        if x == True:
            if files.isfile(f'/etc/users/{self.item.whatsThis()}'):
                w = ShowUserInformation([self.Backend,self.Env,self.Widget,self.AppName,[self.item.whatsThis(),self]])
                w.setGeometry(0,0,self.Env.width(),self.Env.height())
                self.Widget.layout().addWidget (w)

##################################################################
#Download thread
##################################################################

class ShowUserInformation (QMainWindow):
    def run_app_ (self):
        self.Backend.RunApp(self.selected,[None])
    def __init__(self,ports):
        super(ShowUserInformation, self).__init__()

        self.Backend = ports[0]
        self.Env = ports[1]
        self.Widget = ports[2]
        self.AppName = ports[3]
        self.External = ports[4]

        self.XShowpackages = self.External[1]
        self.XShowpackages.hide()

        self.path = f'/etc/users/{self.External[0]}'

        self.fullname = control.read_record('fullname',self.path)
        self.gender = control.read_record('gender', self.path)
        self.company = control.read_record('company', self.path)
        self.blood_type = control.read_record('blood_type', self.path)
        self.phone = control.read_record('phone', self.path)
        self.email = control.read_record('email', self.path)
        self.birthday = control.read_record('birthday',self.path)

        self.resize(self.Env.width(),self.Env.height())


        self.btnBack = QPushButton()
        self.btnBack.setFont(self.Env.font())
        self.btnBack.clicked.connect(self.xhide)
        app.switch('users')
        self.btnBack.setText(res.get('@string/back'))
        app.switch('users')
        self.btnBack.setGeometry(0, 0, self.Env.width(), 50)
        self.btnBack.setStyleSheet('background-color: #123456;color:white;')
        self.layout().addWidget(self.btnBack)



        self.btnImage = QToolButton()
        self.btnImage.setIconSize(QSize(128,128))

        self.logo = control.read_record('loginw.userlogo',self.path)
        if self.logo==None:
            self.btnImage.setIcon(QIcon(res.get('@icon/account')))
        else:
            self.btnImage.setIcon(QIcon(res.get(self.logo)))
            
        if self.fullname==None:
            self.namex = self.External[0]
        else:
            self.namex = self.fullname

        self.Env.SetWindowTitle(self.namex)

        self.btnImage.setStyleSheet('background-color:white;border-radius: 64% 64%;')
        self.btnImage.setGeometry(30, 70, 128, 128)
        self.layout().addWidget (self.btnImage)

        self.lblName = QLabel()


        if res.lang(self.namex)=='fa':
            self.lblName.setAlignment(Qt.AlignRight)
            self.lblName.setFont(QFont(self.Env.font().family(),16))
        else:
            f = QFont()
            f.setPointSize(16)
            self.lblName.setFont(f)

        self.lblName.setText(self.namex)
        self.lblName.setGeometry(60 + 128, 128 - 25, self.width(), 50)
        self.layout().addWidget(self.lblName)

        self.btnRemove = QPushButton()
        self.btnRemove.setFont(self.Env.font())
        self.btnRemove.setStyleSheet('''
        QPushButton {
        background-color: red;color:white;border-radius: 25% 25%;
        }
        QPushButton::hover {
        background-color: orange;color:white;border-radius: 25% 25%;
        }''')
        app.switch('users')
        self.btnRemove.setText(res.get('@string/remove'))
        app.switch('users')
        self.btnRemove.setGeometry(self.width()-260, 128-25, 100, 50)
        self.btnRemove.clicked.connect (self.removeAct_)
        self.layout().addWidget(self.btnRemove)

        self.btnEdit = QPushButton()
        self.btnEdit.setFont(self.Env.font())

        self.btnEdit.setStyleSheet('''
        QPushButton {
        background-color: green;color:white;border-radius: 25% 25%;
        }
        QPushButton::hover {
        background-color: lime;color:white;border-radius: 25% 25%;
        }''')
        self.btnEdit.setGeometry(self.width()-150, 128 - 25, 100, 50)
        self.btnEdit.setText(res.get('@string/edit'))
        self.btnEdit.clicked.connect (self.edituser_act)
        self.layout().addWidget(self.btnEdit)


        self.w = QWidget()
        self.w.setGeometry(30,200,self.width()-60,275)
        self.hbox = QHBoxLayout()
        self.w.setLayout(self.hbox)
        self.text1 = QTextBrowser()
        self.text1.setAlignment(Qt.AlignRight)
        self.text1.setFont(self.Env.font())

        self.text1.append(f'\nUsername:')

        if not self.fullname==None:
            self.text1.append(f'Fullname:')

        if not self.company == None:
            self.text1.append(f'Company:')

        if not self.gender == None:
            self.text1.append(f'Gender:')

        if not self.birthday == None:
            self.text1.append(f'Birthday:')

        if not self.blood_type == None:
            self.text1.append(f'Blood type:')

        if not self.phone == None:
            self.text1.append(f'Phone number:')

        if not self.email == None:
            self.text1.append(f'Email address:')
        self.hbox.addWidget(self.text1)

        self.text2 = QTextBrowser()
        self.text2.setFont(self.Env.font())
        self.text2.append("\n"+self.External[0])

        if not self.fullname == None:
            self.text2.append(self.fullname)

        if not self.company == None:
            self.text2.append(self.company)

        if not self.gender == None:
            self.text2.append(self.gender)

        if not self.birthday == None:
            self.text2.append(self.birthday)

        if not self.blood_type == None:
            self.text2.append(self.blood_type)

        if not self.phone == None:
            self.text2.append(self.phone)

        if not self.email == None:
            self.text2.append(self.email)

        self.text2.setAlignment(Qt.AlignLeft)
        self.hbox.addWidget(self.text2)
        self.layout().addWidget(self.w)

    def xhide (self):
        self.hide()
        self.XShowpackages.show()
        app.switch('users')
        self.Env.SetWindowTitle(res.get("@string/app_name"))
        app.switch('users')

    def removeAct_(self):
        if self.External[0]=='root':
            app.switch('users')
            self.Backend.RunApp('text', [res.get('@string/root'), res.get('@string/rootm')])
            app.switch('users')
        else:
            app.switch('users')
            self.Backend.RunApp ('bool',[res.get('@string/remove_user'),res.get('@string/removem'),self.remove_])
            app.switch('users')

    def remove_(self,yes):
        if yes:
            self.Env.Close()

            files.remove(f'/etc/users/{self.External[0]}')
            if files.isdir(f'/desk/{self.External[0]}'):
                files.removedirs(f'/desk/{self.External[0]}')

            self.Backend.RunApp('users',[None])

            app.switch('users')
            self.Backend.RunApp('text',[res.get('@string/removed'),res.get('@string/removedm')])
            app.switch('users')
            
    def edituser_act(self):
        app.switch('users')
        self.Backend.RunApp ('uedit',[self.External[0]])
        app.switch('users')

class MainApp (QMainWindow):

    def onCloseProcess (self):
        if not app.check('users'):
            self.Widget.Close()
        else:
            QTimer.singleShot(1,self.onCloseProcess)

    def refresh (self):
        self.x = UserListView([self.Env, self.Widget, self, self.AppName, self.External])
        self.setCentralWidget(self.x)

    def __init__(self,ports):
        super(MainApp, self).__init__()

        self.Backend = ports[0]
        self.Env = ports[1]
        self.Widget = ports[2]
        self.AppName = ports[3]
        self.External = ports[4]

        self.onCloseProcess()

        app.switch('users')

        self.Widget.SetWindowIcon(QIcon(res.get(res.etc('users',"logo"))))
        app.switch('users')
        self.Widget.SetWindowTitle (res.get('@string/app_name'))
        app.switch('users')
        self.Widget.Resize(self,720,640)

        self.menubar = QMenuBar()
        self.setMenuBar(self.menubar)
        self.addx = self.menubar.addAction(res.get('@string/add'))
        self.menubar.setFont(self.Env.font())

        if getdata('submenu.direction')=='ltr':
            self.menubar.setLayoutDirection(Qt.LeftToRight)
        else:
            self.menubar.setLayoutDirection(Qt.RightToLeft)

        self.x = UserListView([self.Env,self.Widget,self,self.AppName,self.External])
        self.setCentralWidget(self.x)