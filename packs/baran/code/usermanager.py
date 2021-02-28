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

import sys, subprocess,os,shutil

from libabr import Files, Control, Permissions, Colors, Process, Modules, Package, Commands, Res, System, App

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

class MainApp (QMainWindow):
    def __init__(self,ports):
        super(MainApp, self).__init__()

        self.Backend = ports[0]
        self.Env = ports[1]
        self.Widget = ports[2]
        self.AppName = ports[3]
        self.External = ports[4]

        self.Widget.SetWindowIcon(QIcon(res.get(res.etc('usermanager',"logo"))))
        app.switch('usermanager')
        self.Widget.SetWindowTitle (res.get('@string/app_name'))
        app.switch('usermanager')
        self.Widget.Resize(self,720,640)
        self.x = PackageListView([self.Env,self.Widget,self,self.AppName,self.External])
        self.setCentralWidget(self.x)

class PackageListView (QListView):
    def format(self, it, text):

        first_name = control.read_record('first_name',f'/etc/users/{it.text()}')
        last_name = control.read_record('last_name',f'/etc/users/{it.text()}')
        logo = control.read_record('loginw.userlogo',f'/etc/users/{it.text()}')

        namex = ''

        try:
            if not (first_name == None and last_name == None):
                namex = first_name + " " + last_name
            elif not first_name == None:
                namex = last_name
            elif not last_name == None:
                namex = first_name
            else:
                namex = it.text()
        except:
            namex = ''

        it.setText(namex)

        self.setIconSize(QSize(128,128))

        if logo==None:
            it.setIcon(QIcon(res.get('@icon/account')))
        else:
            it.setIcon(QIcon(res.get(logo)))


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
        # on the given model index to get a pointer to the item

        self.listdir = files.list('/etc/users')
        self.listdir.sort()

        for text in self.listdir:
            it = QStandardItem(text)
            it.setWhatsThis(text)
            it.setFont(self.Env.font())
            self.format(it, text)
            self.entry.appendRow(it)

        self.itemOld = QStandardItem("text")

    def on_clicked(self, index):
        self.item = self.entry.itemFromIndex(index)

        x = hasattr(self.item, 'whatsThis')  # W3CSHCOOL.COM LEARN IT

        if x == True:
            w = ShowUserInformation([self.Backend,self.Env,self.Widget,self.AppName,[self.item.whatsThis(),self]])
            w.setGeometry(0,0,self.Env.width(),self.Env.height())
            self.Widget.layout().addWidget (w)

class ShowUserInformation (QMainWindow):
    def __init__(self,ports):
        super(ShowUserInformation, self).__init__()

        self.Backend = ports[0]
        self.Env = ports[1]
        self.Widget = ports[2]
        self.AppName = ports[3]
        self.External = ports[4]

        app.switch('usermanager')

        self.XShowpackages = self.External[1]
        self.XShowpackages.hide()

        self.path = f'/etc/users/{self.External[0]}'

        self.btnBack = QPushButton()
        self.btnBack.setFont(self.Env.font())
        self.btnBack.clicked.connect(self.xhide)
        self.btnBack.setText('Back')
        self.btnBack.setGeometry(0, 0, self.Env.width(), 50)
        self.btnBack.setStyleSheet('background-color: #123456;color:white;')
        self.layout().addWidget(self.btnBack)

        first_name = control.read_record('first_name', self.path)
        last_name = control.read_record('last_name', self.path)
        logo = control.read_record('loginw.userlogo', self.path)

        if not (first_name == None and last_name == None):
            namex = first_name + " " + last_name
        elif not first_name == None:
            namex = last_name
        elif not last_name == None:
            namex = first_name
        else:
            namex = 'Not set'

        self.Env.SetWindowTitle(self.External[0])

        self.fullname = namex
        self.email = control.read_record('email',self.path)
        self.phone = control.read_record('phone', self.path)
        self.blood_type = control.read_record('blood_type', self.path)
        self.company = control.read_record('company', self.path)
        self.gender = control.read_record('gender', self.path)
        self.website = control.read_record('website', self.path)
        self.birthday = control.read_record('birthday', self.path)

        self.btnImage = QToolButton()
        self.btnImage.setIconSize(QSize(128, 128))

        if files.isfile (f'/etc/users/{self.External[0]}'):
            self.logo = control.read_record('loginw.userlogo',f'/etc/users/{self.External[0]}')
            if not self.logo==None:
                self.btnImage.setIcon(QIcon(res.get(self.logo)))
            else:
                self.btnImage.setIcon(QIcon(res.get('@icon/account')))
            self.Env.SetWindowTitle(self.External[0] + " account")
        else:
            self.btnImage.setIcon(QIcon(res.get('@icon/account')))

        self.btnImage.setStyleSheet('border-radius: 64% 64%;')
        self.btnImage.setGeometry(30, 70, 128, 128)
        self.layout().addWidget (self.btnImage)

        self.lblName = QLabel()
        self.lblName.setText(namex)
        self.lblName.setFont(self.Env.font())
        self.lblName.setGeometry(40 + 128, 128 - 25, self.width(), 50)

        f = QFont()
        f.setPointSize(20)
        self.lblName.setFont(f)
        self.layout().addWidget(self.lblName)

        self.btnRemove = QPushButton()
        if self.External[0]=='root':
            self.btnRemove.setVisible(False)

        self.btnRemove.setFont(self.Env.font())
        self.btnRemove.setStyleSheet('''
                QPushButton {
                background-color: red;color:white;border-radius: 25% 25%;
                }
                QPushButton::hover {
                background-color: orange;color:white;border-radius: 25% 25%;
                }''')
        self.btnRemove.clicked.connect(self.xuni)
        app.switch('usermanager')
        self.btnRemove.setText(res.get('@string/_rm'))
        app.switch('usermanager')
        self.btnRemove.setGeometry(self.width() - 260, 128 - 25, 150, 50)
        self.layout().addWidget(self.btnRemove)

        self.btnEdit = QPushButton()
        self.btnEdit.setFont(self.Env.font())
        self.btnEdit.setStyleSheet('''
                        QPushButton {
                        background-color: lime;color:green;border-radius: 25% 25%;
                        }
                        QPushButton::hover {
                        background-color: green;color:lime;border-radius: 25% 25%;
                        }''')
        self.btnEdit.clicked.connect(self.xedit)
        app.switch('usermanager')
        self.btnEdit.setText(res.get('@string/ed'))
        app.switch('usermanager')
        self.btnEdit.setGeometry(self.width() - 260+160, 128 - 25, 150, 50)
        self.layout().addWidget(self.btnEdit)

        self.w = QWidget()
        self.w.setGeometry(60,200,self.width()-60,400)
        self.hbox = QHBoxLayout()
        self.w.setLayout(self.hbox)
        f.setPointSize(12)
        self.text1 = QTextBrowser()
        self.text1.setFont(self.Env.font())
        self.text1.setAlignment(Qt.AlignRight)
        self.text1.append(f'\nUsername:\n')
        self.text1.append(f'Full name:\n')
        self.text1.append(f'Company name:\n')
        self.text1.append(f'Email address:\n')
        self.text1.append(f'Phone number:\n')
        self.text1.append(f'Gender:\n')
        self.text1.append(f'Birthday:\n')
        self.text1.append(f'Bloodtype:\n')
        self.text1.setFont(f)
        self.hbox.addWidget(self.text1)

        nots = 'Not set'

        self.text2 = QTextBrowser()
        self.text2.setFont(self.Env.font())
        self.text2.append(f'\n{self.External[0]}\n')
        if not self.fullname=='Not set':
            self.text2.append(self.fullname + "\n")
        else:
            self.text2.append(f'<font color="gray">{nots}</font><br/><br/>')

        if not self.company == None:
            self.text2.append(self.company + "\n")
        else:
            self.text2.append(f'<font color="gray">{nots}</font><br/><br/>')

        if not self.email == None:
            self.text2.append(self.email + "\n")
        else:
            self.text2.append(f'<font color="gray">{nots}</font><br/><br/>')

        if not self.phone == None:
            self.text2.append(self.phone + "\n")
        else:
            self.text2.append(f'<font color="gray">{nots}</font><br/><br/>')

        if not self.gender == None:
            self.text2.append(self.gender + "\n")
        else:
            self.text2.append(f'<font color="gray">{nots}</font><br/><br/>')

        if not self.birthday == None:
            self.text2.append(self.birthday + "\n")
        else:
            self.text2.append(f'<font color="gray">{nots}</font><br/><br/>')

        if not self.blood_type == None:
            self.text2.append(self.blood_type + "\n")
        else:
            self.text2.append(f'<font color="gray">{nots}</font><br/><br/>')

        self.text2.setAlignment(Qt.AlignLeft)
        self.text2.setFont(f)
        self.hbox.addWidget(self.text2)
        self.layout().addWidget(self.w)

    def xhide (self):
        self.hide()
        self.XShowpackages.show()
        app.switch('usermanager')
        self.Env.SetWindowTitle(res.get('@string/app_name'))
        app.switch('usermanager')

    # un install pack #
    def xuni (self):
        app.switch('usermanager')
        self.Backend.RunApp('bool', [res.get('@stirng/rm'), res.get("@string/rmm"), self.xuni_])
        app.switch('usermanager')

    def xuni_(self,yes):
        if yes:
            if files.isdir (f'/desk/{self.External[0]}'):
                files.removedirs(f'/desk/{self.External[0]}')
            if files.isfile(f'/etc/users/{self.External[0]}'):
                files.remove(f'/etc/users/{self.External[0]}')
            self.Env.Close()
            self.Backend.RunApp ('usermanager',[None])

    def xedit (self):
        app.switch('usermanager')
        self.Backend.RunApp('edituser',['edit',self.External[0]])
        app.switch('usermanager')
