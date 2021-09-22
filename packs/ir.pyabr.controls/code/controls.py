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
import hashlib

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
                self.adduser_exec.setProperty('visible',False)
                self.back.setProperty('visible',True)
                self.adduser.setProperty('visible',True)
                self.back_users.setProperty('visible',False)
                self.title.setProperty('text',res.get('@string/users.app_name'))
                self.apply2.clicked.connect (self.apply_adduser_)

            elif self.fsel.property('text')=='showuser':
                self.showuser_exec.setProperty('visible',True)
                self.users_exec.setProperty('visible',False)
                self.back.setProperty('visible',False)
                self.back_users.setProperty('visible',True)
                self.adduser.setProperty('visible',False)
                userdb = f'/etc/users/{self.usel.property("text")}'
                fullname = control.read_record ('fullname',userdb)
                email = control.read_record ('email',userdb)
                phone = control.read_record ('phone',userdb)
                gender = control.read_record ('gender',userdb)
                blood_type = control.read_record ('blood_type',userdb)
                birthday = control.read_record ('birthday',userdb)
                profile = control.read_record ('profile',userdb)

                if fullname=='':
                    self.title.setProperty('text',self.usel.property("text"))
                    
                else:
                    self.title.setProperty('text',fullname)

                self.leUsername_show.setProperty('text',self.usel.property("text"))
                self.leFullName_show.setProperty('text',fullname)
                self.leEmail_show.setProperty('text',email)
                self.lePhone_show.setProperty('text',phone)
                self.cbGender_show.setProperty('currentValue',gender)
                self.cbBloodtype_show.setProperty('currentValue',blood_type)
                self.leBirthday_show.setProperty('text',birthday)

                if self.usel.property('text')=='root':
                    self.cbSudoers_show.setProperty('visible',False)
                    self.removeuser.setProperty('visible',False)
                else:
                    if self.usel.property('text') in files.readall('/etc/sudoers'):
                        self.cbSudoers_show.setProperty('checked',True)
                    else:
                        self.cbSudoers_show.setProperty('checked',False)


                if profile.startswith('@icon/'):
                    self.imgProfile_show.setProperty('source',res.qmlget(profile))
                else:
                    self.imgProfile_show.setProperty('source',files.input_qml(profile))
                self.btnProfile_show.clicked.connect (self.change_profile_img_)
                self.savechanges.clicked.connect (self.savechanges_)
                self.changepassword.clicked.connect (self.changepassword_show)
                self.removeuser.clicked.connect (self.removeuser_)

            elif self.fsel.property('text')=='..':
                self.controlview.setProperty('visible',True)
                self.sysinfo_exec.setProperty('visible',False)
                self.apper_exec.setProperty('visible',False)
                self.adduser.setProperty('visible',False)
                self.back_users.setProperty('visible',False)
                self.users_exec.setProperty('visible',False)
                self.showuser_exec.setProperty('visible',False)
                self.adduser_exec.setProperty('visible',False)
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

    def clean_(self):
        self.apply2.setProperty('enabled',True)
        self.title.setProperty('text',res.get('@string/users.add'))
    
    def apply_adduser_(self):   
        if not files.isfile(f"/etc/users/{self.leUsername.property('text')}") and not self.leUsername.property('text')=='guest':
            self.apply2.setProperty('enabled',True)
            
            files.create (f"/etc/users/{self.leUsername.property('text')}")
            files.mkdir (f"/desk/{self.leUsername.property('text')}")
            control.write_record ('code',hashlib.sha3_512(self.lePassword.property('text').encode()).hexdigest(),f"/etc/users/{self.leUsername.property('text')}")
            control.write_record ('fullname',self.leFullName.property('text'),f"/etc/users/{self.leUsername.property('text')}")
            control.write_record ('profile','@icon/breeze-users',f"/etc/users/{self.leUsername.property('text')}")
            control.write_record ('email',self.leEmail.property('text'),f"/etc/users/{self.leUsername.property('text')}")
            control.write_record ('phone',self.lePhone.property('text'),f"/etc/users/{self.leUsername.property('text')}")
            control.write_record ('birthday',self.leBirthday.property('text'),f"/etc/users/{self.leUsername.property('text')}")
            control.write_record ('blood_type',self.cbBloodtype.property('currentValue'),f"/etc/users/{self.leUsername.property('text')}")
            control.write_record ('gender',self.cbGender.property('currentValue'),f"/etc/users/{self.leUsername.property('text')}")

            if self.cbSudoers.property('checked'):
                files.write ('/etc/sudoers',f"{self.leUsername.property('text')}\n")

            self.addUserModel()
            self.fsel.setProperty('text','users')
        else:
            self.apply2.setProperty('enabled',False)
            #self.leUsername.setProperty('text','')
            self.title.setProperty('text','This user is already exists')
            QTimer.singleShot(3000,self.clean_)

    def getdata (self,name):
        x = control.read_record(name,f'/etc/users/{self.username}')
        if x=='' or x==None:
            x = res.getdata(name)

        return x

    def adduser_(self):
        self.adduser_exec.setProperty('visible',True)
        self.title.setProperty('text',res.get('@string/users.add'))
        self.users_exec.setProperty('visible',False)
        self.back.setProperty('visible',False)
        self.back_users.setProperty('visible',True)
        self.adduser.setProperty('visible',False)

    profile_show = '@icon/breeze-users'

    def change_profile_img_(self):
        self.x = Select (self.change_profile_img__)

    def change_profile_img__(self,filename):
        self.imgProfile_show.setProperty('source',files.input_qml(filename))
        self.profile_show = filename

    def savechanges_(self):
        userdb = f"/etc/users/{self.usel.property('text')}"

        control.write_record('fullname',self.leFullName_show.property('text'),userdb)
        control.write_record('email',self.leEmail_show.property('text'),userdb)
        control.write_record('phone',self.lePhone_show.property('text'),userdb)
        control.write_record('birthday',self.leBirthday_show.property('text'),userdb)
        control.write_record('gender',self.cbSudoers_show.property('currentValue'),userdb)
        control.write_record('blood_type',self.cbBloodtype_show.property('currentValue'),userdb)
        control.write_record('profile',self.profile_show,userdb)   

        app.signal('username')

        if self.cbSudoers_show.property('checked'):
            files.write ('/etc/sudoers',self.usel.property('text')+"\n")
        else:
            x = files.readall('/etc/sudoers').replace(self.usel.property('text'),'')
            files.write('/etc/sudoers',x)

        self.addUserModel()
        self.fsel.setProperty('text','users')

    def changepassword_show(self):
        self.changepassword_exec.setProperty('visible',True)
        self.title.setProperty('text',f'Change {self.usel.property("text")} password')
        self.showuser_exec.setProperty('visible',False)
        self.back.setProperty('visible',False)
        self.back_users.setProperty('visible',True)
        self.adduser.setProperty('visible',False)


        self.savechanges2.clicked.connect (self.savechanges2_)

    def clean2_(self):
        self.title.setProperty('text',f'Change {self.usel.property("text")} password')
        self.savechanges2.setProperty('enabled',True)

    def savechanges2_(self):
        userdb = f"/etc/users/{self.usel.property('text')}"

        if control.read_record('code',userdb)==hashlib.sha3_512(self.leoldPassword_change.property('text').encode()).hexdigest():
            if self.leNewPassword_change.property('text')==self.leCofirmPassword_change.property('text'):
                control.remove_record('code',userdb)
                control.write_record ('code',hashlib.sha3_512(self.leNewPassword_change.property('text').encode()).hexdigest(),userdb)
                self.addUserModel()
                self.fsel.setProperty('text','showuser')
            else:
                self.title.setProperty('text','Passwords mot matched')
                self.savechanges2.setProperty('enabled',False)
                QTimer.singleShot(3000,self.clean2_)
        else:
            self.title.setProperty('text','Wrong password! try again')
            self.savechanges2.setProperty('enabled',False)
            QTimer.singleShot(3000,self.clean2_)

    def removeuser_(self):
        self.x = Ask(f'Remove {self.usel.property("text")}',f'Do you want to remove {self.usel.property("text")}? this means lost all data in selected user.',self.removeuser__)

    def removeuser__(self,yes):
        if yes:
            try:
                files.remove (f'/etc/users/{self.usel.property("text")}')
                files.removedirs (f'/desk/{self.usel.property("text")}')
                self.addUserModel()
                self.fsel.setProperty('text','users')
            except:
                pass
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
        self.adduser_exec = self.findChild('adduser_exec')

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

        self.adduser = self.findChild('adduser')
        self.back_users = self.findChild('back_users')

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

        # add user objects #
        self.leUsername = self.findChild('leUsername')
        self.lePassword = self.findChild('lePassword')
        self.leEmail = self.findChild('leEmail')
        self.lePhone = self.findChild('lePhone')
        self.leBirthday = self.findChild('leBirthday')
        self.cbBloodtype = self.findChild('cbBloodtype')
        self.cbGender = self.findChild('cbGender')
        self.cbSudoers = self.findChild('cbSudoers')
        self.leFullName = self.findChild('leFullName')
        self.apply2 = self.findChild('apply2')
        self.showuser_exec = self.findChild ('showuser_exec')
        self.usel = self.findChild ('usel')

        self.leUsername_show = self.findChild('leUsername_show')
        self.lePassword_show = self.findChild('lePassword_show')
        self.leEmail_show = self.findChild('leEmail_show')
        self.lePhone_show = self.findChild('lePhone_show')
        self.leBirthday_show = self.findChild('leBirthday_show')
        self.cbBloodtype_show = self.findChild('cbBloodtype_show')
        self.cbGender_show = self.findChild('cbGender_show')
        self.cbSudoers_show = self.findChild('cbSudoers_show')
        self.leFullName_show = self.findChild('leFullName_show')
        self.imgProfile_show = self.findChild('imgProfile_show')
        self.btnProfile_show = self.findChild('btnProfile_show')
        self.savechanges = self.findChild('savechanges')
        self.changepassword = self.findChild('changepassword')
        self.removeuser = self.findChild('removeuser')


        self.leoldPassword_change = self.findChild('leoldPassword_change')
        self.leNewPassword_change = self.findChild('leNewPassword_change')
        self.leCofirmPassword_change = self.findChild('leConfirmPassword_change')
        self.savechanges2 = self.findChild('savechanges2')
        self.changepassword_exec = self.findChild('changepassword_exec')
        self.cancel3 = self.findChild('cancel3')

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

        self.adduser.clicked.connect (self.adduser_)

        self.loop()

application = QtGui.QGuiApplication([])
w = MainApp()
application.exec()