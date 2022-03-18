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

from pyabr.core import *
from pyabr.quick import *

class MainApp (MainApp):
    def clean(self):
        self.txtWrong.setProperty('text','')
        self.leProjectName.setProperty('text','')
        self.lePackageName.setProperty('text','')
        self.btnCreate.setProperty('enabled',True)

    def create_(self):
        # check fields
        if self.leProjectName.property('text')=='':
            self.btnCreate.setProperty('enabled',False)
            self.txtWrong.setProperty('text','Please enter your project name.')
            QTimer.singleShot(3000,self.clean)

        if self.lePackageName.property('text')=='':
            self.btnCreate.setProperty('enabled',False)
            self.txtWrong.setProperty('text','Please enter your package name.')
            QTimer.singleShot(3000,self.clean)

        # check project folder
        if not self.leProjectName.property('text')=='':
            if files.isdir (f"{self.projectdir}/{self.leProjectName.property('text')}") and files.isfile (f"{self.projectdir}/{self.leProjectName.property('text')}/.project"):
                self.btnCreate.setProperty('enabled',False)
                self.txtWrong.setProperty('text','This Project has already exists.')
                QTimer.singleShot(3000,self.clean)

        # check package name from main repo / selected repo

        if not self.lePackageName.property('text')=='':
            r = Repo(self.lePackageName.property('text'))
            if not r.CanCreate():
                self.btnCreate.setProperty('enabled',False)
                self.txtWrong.setProperty('text','This Package name has already used by another user.')
                QTimer.singleShot(3000,self.clean)

        #                   create project 
        # 0     pyqt qml    [done]
        # 1     pyqt        [done]
        # 2     web app
        # 3     python
        # 4     saye
        # 5     pashmak
        # 6     hascal
        # 7     c
        # 8    c++

        self.prodir = f"{self.projectdir}/{self.leProjectName.property('text')}"
        self.projectType = self.cbType.property('currentIndex')
        commands.cd ([self.projectdir])

        # create project
        
        if self.projectType==0:
            System(f"paye crt python-quick {self.leProjectName.property('text')}")
        elif self.projectType==1:
            System(f"paye crt python-qt {self.leProjectName.property('text')}")
        elif self.projectType==2:
            System(f"paye crt python-webapp {self.leProjectName.property('text')}")
        elif self.projectType==3:
            System(f"paye crt python-console {self.leProjectName.property('text')}")
        elif self.projectType==4:
            System(f"paye crt saye-console {self.leProjectName.property('text')}")
        elif self.projectType==5:
            System(f"paye crt pashmak-console {self.leProjectName.property('text')}")
        elif self.projectType==6:
            System(f"paye crt hascal-console {self.leProjectName.property('text')}")
        elif self.projectType==7:
            System(f"paye crt c-console {self.leProjectName.property('text')}")
        elif self.projectType==8:
            System(f"paye crt cpp-console {self.leProjectName.property('text')}")

        # change all names in project
        commands.mv ([f'{self.prodir}/ir.pyabr.hello',f"{self.prodir}/{self.lePackageName.property('text')}"])

        # write a new config file
        files.write (f'{self.prodir}/config',f'''project_name: {self.lePackageName.property('text')}
project_pack: {self.lePackageName.property('text')}.pa
project_dir: {self.lePackageName.property('text')}
project_entry: {self.leProjectName.property('text')}''')

        # write a new compile file

        if self.projectType<=3:
            files.write(f"{self.prodir}/{self.lePackageName.property('text')}/control/compile",f"{self.leProjectName.property('text')}.py:usr/app/{self.leProjectName.property('text')}.pyc")
        elif self.projectType==6:
            files.write(f"{self.prodir}/{self.lePackageName.property('text')}/control/compile",f"{self.leProjectName.property('text')}.has:usr/app/{self.leProjectName.property('text')}")
        elif self.projectType==7:
            files.write(f"{self.prodir}/{self.lePackageName.property('text')}/control/compile",f"{self.leProjectName.property('text')}.c:usr/app/{self.leProjectName.property('text')}")
        elif self.projectType==8:
            files.write(f"{self.prodir}/{self.lePackageName.property('text')}/control/compile",f"{self.leProjectName.property('text')}.cpp:usr/app/{self.leProjectName.property('text')}")

        # manifest
        su = files.readall('/proc/info/su')
        namex = control.read_record ('fullname',f'/etc/users/{su}')

        if namex==None:
            namex = files.readall(f'/etc/key/{su}/user')

        files.write (f"{self.prodir}/{self.lePackageName.property('text')}/control/manifest",f'''name: {self.lePackageName.property('text')}
name[en]: {self.leProjectName.property('text')}
copyright: (c) 2021 {namex}
license: Your license
unpack: /
version: 1.0.0
description: Description of project
compile: Yes
entry: {self.leProjectName.property('text')}
build: yyyy-mm-dd''')

        # write desktop file if project is a desktop    
        
        # rename application desktop file
        if files.isfile (f"{self.prodir}/{self.lePackageName.property('text')}/data/usr/share/applications/hello.desk"):
            files.write(f"{self.prodir}/{self.lePackageName.property('text')}/data/usr/share/applications/hello.desk",f'''name[en]: {self.leProjectName.property('text')}
logo: @icon/app
exec: {self.leProjectName.property('text')}
application: Yes
category: tools''')
            commands.mv ([f"{self.prodir}/{self.lePackageName.property('text')}/data/usr/share/applications/hello.desk",f"{self.prodir}/{self.lePackageName.property('text')}/data/usr/share/applications/{self.leProjectName.property('text')}.desk"])
        
        if files.isfile (f"{self.prodir}/{self.lePackageName.property('text')}/data/usr/share/layouts/hello.qml"):
            commands.mv ([f"{self.prodir}/{self.lePackageName.property('text')}/data/usr/share/layouts/hello.qml",f"{self.prodir}/{self.lePackageName.property('text')}/data/usr/share/layouts/{self.leProjectName.property('text')}.qml"])
        
        if files.isfile (f"{self.prodir}/{self.lePackageName.property('text')}/code/hello.py"):
            files.write(f"{self.prodir}/{self.lePackageName.property('text')}/code/hello.py",files.readall(f"{self.prodir}/{self.lePackageName.property('text')}/code/hello.py").replace('@layout/hello',f'@layout/{self.leProjectName.property("text")}'))
            commands.mv ([f"{self.prodir}/{self.lePackageName.property('text')}/code/hello.py",f"{self.prodir}/{self.lePackageName.property('text')}/code/{self.leProjectName.property('text')}.py"])
        
        if files.isfile (f"{self.prodir}/{self.lePackageName.property('text')}/code/hello.c"):
            commands.mv ([f"{self.prodir}/{self.lePackageName.property('text')}/code/hello.c",f"{self.prodir}/{self.lePackageName.property('text')}/code/{self.leProjectName.property('text')}.c"])
        
        if files.isfile (f"{self.prodir}/{self.lePackageName.property('text')}/code/hello.cpp"):
            commands.mv ([f"{self.prodir}/{self.lePackageName.property('text')}/code/hello.cpp",f"{self.prodir}/{self.lePackageName.property('text')}/code/{self.leProjectName.property('text')}.cpp"])
        
        if files.isfile (f"{self.prodir}/{self.lePackageName.property('text')}/code/hello.has"):
            commands.mv ([f"{self.prodir}/{self.lePackageName.property('text')}/code/hello.has",f"{self.prodir}/{self.lePackageName.property('text')}/code/{self.leProjectName.property('text')}.has"])
        
        if files.isfile (f"{self.prodir}/{self.lePackageName.property('text')}/data/usr/app/hello.sa"):
            commands.mv ([f"{self.prodir}/{self.lePackageName.property('text')}/data/usr/app/hello.sa",f"{self.prodir}/{self.lePackageName.property('text')}/data/usr/app/{self.leProjectName.property('text')}.sa"])
        
        if files.isfile (f"{self.prodir}/{self.lePackageName.property('text')}/data/usr/app/hello.pashm"):
            commands.mv ([f"{self.prodir}/{self.lePackageName.property('text')}/data/usr/app/hello.pashm",f"{self.prodir}/{self.lePackageName.property('text')}/data/usr/app/{self.leProjectName.property('text')}.pashm"])
        
        app.start('vscode',self.leProjectName.property('text'))

    def __init__(self):
        super(MainApp, self).__init__()
        self.addProjectModel()
        self.load (res.get('@layout/pishkhan'))
        
        # check synced user
        self.user = files.readall("/proc/info/su")
        self.setProperty('title',res.getname('pishkhan'))

        if not (files.isfile (f"/etc/key/{self.user}/user") or files.isfile (f"/etc/key/{self.user}/pass")):
            self.close()
            app.start('sync','pishkhan')

        if self.user == 'root':
            self.projectdir = f"/root/Projects"
        else:
            self.projectdir = f"/desk/{self.user}/Projects"

        # finds
        self.leProjectName = self.findChild('leProjectName')
        self.lePackageName = self.findChild('lePackageName')
        self.cbType =        self.findChild('cbType')
        self.btnCreate =     self.findChild('btnCreate')
        self.btnCreate.clicked.connect(self.create_)
        self.txtWrong =      self.findChild('txtWrong')
        
application = QtGui.QGuiApplication([])
application.setWindowIcon (QIcon(res.get(res.etc('pishkhan','logo'))))

w = MainApp()
application.exec()