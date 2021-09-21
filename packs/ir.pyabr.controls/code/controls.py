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

    def sysinfo_ (self):
        self.host = self.findChild ('host')
        self.cs = self.findChild ('cs')
        self.bl = self.findChild ('bl')
        self.os = self.findChild ('os')
        self.kname = self.findChild ('kname')
        self.su = self.findChild ('su')
        self.de = self.findChild ('de')
        self.gui = self.findChild ('gui')
        self.arch = self.findChild ('arch')

        self.host1 = self.findChild ('host1')
        self.cs1 = self.findChild ('cs1')
        self.bl1 = self.findChild ('bl1')
        self.os1 = self.findChild ('os1')
        self.kname1 = self.findChild ('kname1')
        self.su1 = self.findChild ('su1')
        self.de1 = self.findChild ('de1')
        self.gui1 = self.findChild ('gui1')
        self.arch1 = self.findChild ('arch1')

        # check direction
        if res.getdata ('locale')=='fa' or res.getdata('locale')=='ar':
            self.host1.setProperty ('text',res.get('@string/sysinfo.host')+":  ")
            self.cs1.setProperty ('text',res.get('@string/sysinfo.cs')+":  ")
            self.bl1.setProperty ('text',res.get('@string/sysinfo.bl')+":  ")
            self.os1.setProperty ('text',res.get('@string/sysinfo.os')+":  ")
            self.kname1.setProperty ('text',res.get('@string/sysinfo.kname')+":  ")
            self.su1.setProperty ('text',res.get('@string/sysinfo.su')+":  ")
            self.de1.setProperty ('text',res.get('@string/sysinfo.de')+":  ")
            self.gui1.setProperty ('text',res.get('@string/sysinfo.gui')+":  ")
            self.arch1.setProperty ('text',res.get('@string/sysinfo.arch')+":  ")

            self.host.setProperty ('text',files.readall('/proc/info/host'))
            self.cs.setProperty ('text',files.readall('/proc/info/cs'))
            self.bl.setProperty ('text',files.readall('/proc/info/bl'))
            self.os.setProperty ('text',files.readall('/proc/info/os'))
            self.kname.setProperty ('text',files.readall('/proc/info/kname'))
            self.su.setProperty ('text',files.readall('/proc/info/su'))
            self.de.setProperty ('text',files.readall('/proc/info/de'))
            self.gui.setProperty ('text',files.readall('/proc/info/gui'))
            self.arch.setProperty ('text',files.readall('/proc/info/arch'))
        else:
            self.host.setProperty ('text',res.get('@string/sysinfo.host')+":  ")
            self.cs.setProperty ('text',res.get('@string/sysinfo.cs')+":  ")
            self.bl.setProperty ('text',res.get('@string/sysinfo.bl')+":  ")
            self.os.setProperty ('text',res.get('@string/sysinfo.os')+":  ")
            self.kname.setProperty ('text',res.get('@string/sysinfo.kname')+":  ")
            self.su.setProperty ('text',res.get('@string/sysinfo.su')+":  ")
            self.de.setProperty ('text',res.get('@string/sysinfo.de')+":  ")
            self.gui.setProperty ('text',res.get('@string/sysinfo.gui')+":  ")
            self.arch.setProperty ('text',res.get('@string/sysinfo.arch')+":  ")

            self.host1.setProperty ('text',files.readall('/proc/info/host'))
            self.cs1.setProperty ('text',files.readall('/proc/info/cs'))
            self.bl1.setProperty ('text',files.readall('/proc/info/bl'))
            self.os1.setProperty ('text',files.readall('/proc/info/os'))
            self.kname1.setProperty ('text',files.readall('/proc/info/kname'))
            self.su1.setProperty ('text',files.readall('/proc/info/su'))
            self.de1.setProperty ('text',files.readall('/proc/info/de'))
            self.gui1.setProperty ('text',files.readall('/proc/info/gui'))
            self.arch1.setProperty ('text',files.readall('/proc/info/arch'))

    def loop (self):
        if not self.fsel.property('text')=='':
            if self.fsel.property('text')=='sysinfo':
                self.controlview.setProperty('visible',False)
                self.sysinfo_exec.setProperty('visible',True)
                self.back.setProperty('visible',True)
                self.title.setProperty('text',res.get('@string/sysinfo.app_name'))
                self.sysinfo_()

            elif self.fsel.property('text')=='apper':
                self.controlview.setProperty('visible',False)
                self.apper_exec.setProperty('visible',True)
                self.back.setProperty('visible',True)
                self.title.setProperty('text',res.get('@string/controls.apper'))

            elif self.fsel.property('text')=='users':
                self.controlview.setProperty('visible',False)
                self.users_exec.setProperty('visible',True)
                self.back.setProperty('visible',True)
                self.title.setProperty('text',res.get('@string/users.app_name'))

            elif self.fsel.property('text')=='..':
                self.controlview.setProperty('visible',True)
                self.sysinfo_exec.setProperty('visible',False)
                self.apper_exec.setProperty('visible',False)
                self.users_exec.setProperty('visible',False)
                self.back.setProperty('visible',False)
                self.title.setProperty('text',res.get('@string/controls.app_name'))

        try:
            self.dock_location = self.cbDock.property('currentValue')
        except:
            pass

        self.fsel.setProperty ('text','')
        QTimer.singleShot (100,self.loop)

    desktop_bg = '/usr/share/backgrounds/breeze-next.png'
    lock_bg = '/usr/share/backgrounds/breeze-splash.jpg'
    unlock_bg = '/usr/share/backgrounds/breeze-splash.jpg'
    enter_bg = '/usr/share/backgrounds/breeze-splash.jpg'
    dock_location = 0
    username = files.readall('/proc/info/su')

    def set_desktop_bg_(self,filename):
        self.imgChange_desktop.setProperty('source',files.input_qml(filename))
        self.desktop_bg = filename

    def set_lock_bg_(self,filename):
        self.imgChange_lock.setProperty('source',files.input_qml(filename))
        self.lock_bg = filename

    def set_unlock_bg_(self,filename):
        self.imgChange_unlock.setProperty('source',files.input_qml(filename))
        self.unlock_bg = filename

    def set_enter_bg_(self,filename):
        self.imgChange_enter.setProperty('source',files.input_qml(filename))
        self.enter_bg = filename

    def set_desktop_bg (self):
        self.x = Select (self.set_desktop_bg_)

    def set_lock_bg (self):
        self.x = Select (self.set_lock_bg_)

    def set_unlock_bg (self):
        self.x = Select (self.set_unlock_bg_)

    def set_enter_bg (self):
        self.x = Select (self.set_enter_bg_)

    def apply_(self):
        
        control.write_record ('desktop.background',self.desktop_bg,f'/etc/users/{self.username}')
        control.write_record ('enter.background',self.enter_bg,f'/etc/users/{self.username}')
        control.write_record ('lock.background',self.lock_bg,f'/etc/users/{self.username}')
        control.write_record ('unlock.background',self.unlock_bg,f'/etc/users/{self.username}')
        app.signal ('background')
        QTimer.singleShot(1000,self.apply2_)


    def apply2_(self):
        currentIndex = self.cbDock.property('currentIndex')
        
        if currentIndex==0:
            control.write_record ('dock','bottom',f'/etc/users/{self.username}')

        elif currentIndex==1:
            control.write_record ('dock','top',f'/etc/users/{self.username}')

        elif currentIndex==2:
            control.write_record ('dock','left',f'/etc/users/{self.username}')

        elif currentIndex==3:
            control.write_record ('dock','right',f'/etc/users/{self.username}')

        elif currentIndex==4:
            control.write_record ('dock','windows',f'/etc/users/{self.username}')

        app.signal ('dock')

        self.fsel.setProperty('text','..')
        

    def getdata (self,name):
        x = control.read_record(name,f'/etc/users/{self.username}')
        if x=='' or x==None:
            x = res.getdata(name)

        return x

    def __init__(self):
        super(MainApp, self).__init__()
        self.addUserModel()
        self.load (res.get('@layout/controls'))
        self.setProperty('title',res.get('@string/controls.app_name'))
        self.fsel = self.findChild('fsel')
        self.controlview = self.findChild ('controlview')
        self.back = self.findChild('back')

        self.sysinfo = self.findChild ('sysinfo')
        self.sysinfo_exec = self.findChild ('sysinfo_exec')
        self.sysinfo.setProperty('text',res.get('@string/sysinfo.app_name'))
        self.title = self.findChild('title')
        self.title.setProperty('text',res.get('@string/controls.app_name'))

        self.apper = self.findChild ('apper')
        self.apper_exec = self.findChild ('apper_exec')
        self.apper.setProperty('text',res.get('@string/controls.apper'))

        self.users = self.findChild ('users')
        self.users_exec = self.findChild ('users_exec')
        self.users.setProperty('text',res.get('@string/users.app_name'))

        self.btnChange_desktop = self.findChild('btnChange_desktop')
        self.btnChange_desktop.setProperty('text',res.get('@string/wallpaper.desktop'))
        self.btnChange_desktop.clicked.connect (self.set_desktop_bg)
        self.btnChange_lock = self.findChild('btnChange_lock')
        self.btnChange_lock.setProperty('text',res.get('@string/wallpaper.lock'))
        self.btnChange_lock.clicked.connect (self.set_lock_bg)
        self.btnChange_unlock = self.findChild('btnChange_unlock')
        self.btnChange_unlock.setProperty('text',res.get('@string/wallpaper.unlock'))
        self.btnChange_unlock.clicked.connect (self.set_unlock_bg)
        self.btnChange_enter = self.findChild('btnChange_enter')
        self.btnChange_enter.setProperty('text',res.get('@string/wallpaper.enter'))
        self.btnChange_enter.clicked.connect (self.set_enter_bg)

        self.imgChange_desktop = self.findChild('imgChange_desktop')
        self.imgChange_lock = self.findChild('imgChange_lock')
        self.imgChange_unlock = self.findChild('imgChange_unlock')
        self.imgChange_enter = self.findChild('imgChange_enter')

        self.cbDock = self.findChild ('cbDock')
        self.apply = self.findChild('apply')
        self.cancel = self.findChild('cancel')
        self.cancel.setProperty('text',res.get('@string/controls.cancel'))
        self.apply.setProperty('text',res.get('@string/controls.apply'))
        self.apply.clicked.connect (self.apply_)

        self.txtDock = self.findChild ('txtDock')
        self.txtDock.setProperty('text',res.get('@string/controls.dock_location'))
        self.txtWallpapers = self.findChild ('txtWallpapers')
        self.txtWallpapers.setProperty('text',res.get('@string/controls.change_wallpaper'))

        # Get backgrounds #
        self.desktop_bg = self.getdata("desktop.background")
        self.lock_bg = self.getdata("lock.background")
        self.unlock_bg = self.getdata("unlock.background")
        self.enter_bg = self.getdata("enter.background")

        if self.desktop_bg.startswith('@background/'):
            self.imgChange_desktop.setProperty('source',res.qmlget(self.desktop_bg))
        else:
            self.imgChange_desktop.setProperty('source',files.input_qml(self.desktop_bg))

        if self.lock_bg.startswith('@background/'):
            self.imgChange_lock.setProperty('source',res.qmlget(self.lock_bg))
        else:
            self.imgChange_lock.setProperty('source',files.input_qml(self.lock_bg))

        if self.unlock_bg.startswith('@background/'):
            self.imgChange_unlock.setProperty('source',res.qmlget(self.unlock_bg))
        else:
            self.imgChange_unlock.setProperty('source',files.input_qml(self.unlock_bg))

        if self.enter_bg.startswith('@background/'):
            self.imgChange_enter.setProperty('source',res.qmlget(self.enter_bg))
        else:
            self.imgChange_enter.setProperty('source',files.input_qml(self.enter_bg))

        if self.getdata('dock')=='bottom': 
            self.dock_location = 0
            self.cbDock.setProperty('currentIndex',0)
        elif self.getdata('dock')=='top': 
            self.dock_location = 1
            self.cbDock.setProperty('currentIndex',1)
        elif self.getdata('dock')=='left': 
            self.dock_location = 2
            self.cbDock.setProperty('currentIndex',2)
        elif self.getdata('dock')=='right': 
            self.dock_location = 3
            self.cbDock.setProperty('currentIndex',3)
        elif self.getdata('dock')=='windows': 
            self.dock_location = 4
            self.cbDock.setProperty('currentIndex',4)

        self.loop()

application = QtGui.QGuiApplication([])
w = MainApp()
application.exec()