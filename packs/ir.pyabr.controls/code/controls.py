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
import os.path
from os import SEEK_HOLE
from pyabr.core import *
from pyabr.quick import *
import hashlib,subprocess,sys,shutil

class MainApp (MainApp):

    def btnGtk_click_(self,name):
        f = open('/stor/etc/default/openbox.xml.bak', 'r')
        openboxrc = f.read()
        f.close()

        f = open('/stor/etc/default/openbox.xml', 'w')
        f.write(openboxrc.replace('<name>Win10</name>', f'<name>{name}</name>'))
        f.close()

        # copy theme to /usr/share/themes
        if os.path.isdir(f'/stor/usr/share/themes/{name}') and not os.path.isdir(f'/usr/share/themes/{name}'):
            subprocess.call(f'ln -sv /stor/usr/share/themes/{name} /usr/share/themes/{name}',shell=True)

        shutil.copyfile('/stor/etc/default/openbox.xml', '/root/.config/openbox/rc.xml')
        subprocess.call(['openbox', '--reconfigure'])

    def btnGtk_click(self):
        self.w = ApplicationTheme (self.btnGtk_click_)

    def btnIcon_click_(self, name):
        control.write_record('icon-theme',name,'/etc/gui')

    def btnIcon_click(self):
        self.w = IconTheme(self.btnIcon_click_)

    def btnCursor_click_(self, name):
        if os.path.isdir(f'/stor/usr/share/themes/{name}') and not os.path.isdir(f'/usr/share/icons/{name}'):
            shutil.copytree(f'/stor/usr/share/themes/{name}',f'/usr/share/icons/{name}')

        shutil.copyfile(f'/usr/share/icons/{name}/index.theme','/usr/share/icons/default/index.theme')

    def btnCursor_click(self):
        self.w = CursorTheme(self.btnCursor_click_)

    def btnShell_click_(self, name):
        pass

    def btnShell_click(self):
        self.w = ShellTheme(self.btnShell_click_)

    def themes_(self):
        self.txtGTK = self.findChild('txtGTK')
        self.txtGTK1 = self.findChild('txtGTK1')
        self.txtIcon = self.findChild('txtIcon')
        self.txtIcon1 = self.findChild('txtIcon1')
        self.txtCursor = self.findChild('txtCursor')
        self.txtCursor1 = self.findChild('txtCursor1')
        self.txtShell = self.findChild('txtShell')
        self.txtShell1 = self.findChild('txtShell1')

        self.btnGTK = self.findChild('btnGTK')
        self.btnIcon = self.findChild('btnIcon')
        self.btnCursor = self.findChild('btnCursor')
        self.btnShell = self.findChild('btnShell')

        self.btnGTK.clicked.connect (self.btnGtk_click)
        self.btnIcon.clicked.connect (self.btnIcon_click)
        self.btnCursor.clicked.connect (self.btnCursor_click)
        self.btnShell.clicked.connect (self.btnShell_click)

        if res.getdata('locale') == 'fa' or res.getdata('locale') == 'ar':
            self.txtGTK1.setProperty('text',res.get('@string/gtk'))
            self.txtIcon1.setProperty('text',res.get('@string/icon'))
            self.txtCursor1.setProperty('text',res.get('@string/cursor'))
            self.txtShell1.setProperty('text',res.get('@string/shell'))
        else:
            self.txtGTK.setProperty('text',res.get('@string/gtk'))
            self.txtIcon.setProperty('text',res.get('@string/icon'))
            self.txtCursor.setProperty('text',res.get('@string/cursor'))
            self.txtShell.setProperty('text',res.get('@string/shell'))


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
            self.host1.setProperty ('text',res.get('@string/host'))
            self.cs1.setProperty ('text',res.get('@string/cs'))
            self.bl1.setProperty ('text',res.get('@string/bl'))
            self.os1.setProperty ('text',res.get('@string/os'))
            self.kname1.setProperty ('text',res.get('@string/kname'))
            self.su1.setProperty ('text',res.get('@string/su'))
            self.de1.setProperty ('text',res.get('@string/de'))
            self.gui1.setProperty ('text',res.get('@string/gui'))
            self.arch1.setProperty ('text',res.get('@string/arch'))

            self.host.setProperty ('text',files.readall('/proc/info/host'))
            self.cs.setProperty ('text',f"{files.readall('/proc/info/cs')} {files.readall('/proc/info/ver')} ({files.readall('/proc/info/cd')})")
            self.bl.setProperty ('text',files.readall('/proc/info/bl'))
            self.os.setProperty ('text',files.readall('/proc/info/os'))
            self.kname.setProperty ('text',files.readall('/proc/info/kname'))
            self.su.setProperty ('text',files.readall('/proc/info/su'))
            self.de.setProperty ('text',files.readall('/proc/info/de'))
            self.gui.setProperty ('text',files.readall('/proc/info/gui'))
            self.arch.setProperty ('text',files.readall('/proc/info/arch'))
        else:
            self.host.setProperty ('text',res.get('@string/host'))
            self.cs.setProperty ('text',res.get('@string/cs'))
            self.bl.setProperty ('text',res.get('@string/bl'))
            self.os.setProperty ('text',res.get('@string/os'))
            self.kname.setProperty ('text',res.get('@string/kname'))
            self.su.setProperty ('text',res.get('@string/su'))
            self.de.setProperty ('text',res.get('@string/de'))
            self.gui.setProperty ('text',res.get('@string/gui'))
            self.arch.setProperty ('text',res.get('@string/arch'))

            self.host1.setProperty ('text',files.readall('/proc/info/host'))
            self.cs1.setProperty ('text',f"{files.readall('/proc/info/cs')} {files.readall('/proc/info/ver')} ({files.readall('/proc/info/cd')})")
            self.bl1.setProperty ('text',files.readall('/proc/info/bl'))
            self.os1.setProperty ('text',files.readall('/proc/info/os'))
            self.kname1.setProperty ('text',files.readall('/proc/info/kname'))
            self.su1.setProperty ('text',files.readall('/proc/info/su'))
            self.de1.setProperty ('text',files.readall('/proc/info/de'))
            self.gui1.setProperty ('text',files.readall('/proc/info/gui'))
            self.arch1.setProperty ('text',files.readall('/proc/info/arch'))

    wselp = ''

    def loop (self):
        if not self.fsel.property('text')=='':
            if self.fsel.property('text')=='sysinfo':
                self.controlview.setProperty('visible',False)
                self.sysinfo_exec.setProperty('visible',True)
                self.back.setProperty('visible',True)
                self.scroll.setProperty('enabled',False)
                self.scroll.setProperty('visible',False)
                self.title.setProperty('text',res.get('@string/sysinfo'))
                self.sysinfo_()

            elif self.fsel.property('text')=='apper':
                self.controlview.setProperty('visible',False)
                self.apper_exec.setProperty('visible',True)
                self.scroll.setProperty('enabled',False)
                self.scroll.setProperty('visible',False)
                self.back.setProperty('visible',True)
                self.title.setProperty('text',res.get('@string/appearance'))

            elif self.fsel.property('text')=='theme':
                self.controlview.setProperty('visible',False)
                self.theme_exec.setProperty('visible',True)
                self.scroll.setProperty('enabled',False)
                self.scroll.setProperty('visible',False)
                self.back.setProperty('visible',True)
                self.title.setProperty('text',res.get('@string/themes'))

                self.themes_()

            elif self.fsel.property('text')=='users':
                self.controlview.setProperty('visible',False)
                self.users_exec.setProperty('visible',True)
                self.adduser_exec.setProperty('visible',False)
                self.back.setProperty('visible',True)
                self.adduser.setProperty('visible',True)
                self.back_users.setProperty('visible',False)
                self.title.setProperty('text',res.get('@string/accounts'))
                self.scroll.setProperty('enabled',False)
                self.scroll.setProperty('visible',False)
                self.apply2.clicked.connect (self.apply_adduser_)

            elif self.fsel.property('text')=='showuser':
                self.showuser_exec.setProperty('visible',True)
                self.users_exec.setProperty('visible',False)
                self.back.setProperty('visible',False)
                self.back_users.setProperty('visible',True)
                self.adduser.setProperty('visible',False)
                userdb = f'/etc/users/{self.usel.property("text")}'
                fullname = control.read_record ('fullname',userdb)
                profile = control.read_record ('profile',userdb)

                if fullname=='':
                    self.title.setProperty('text',self.usel.property("text"))
                else:
                    self.title.setProperty('text',fullname)

                self.leUsername_show.setProperty('text',self.usel.property("text"))
                self.leFullName_show.setProperty('text',fullname)
                if self.usel.property('text')=='root':
                    self.cbSudoers_show.setProperty('visible',False)
                    self.removeuser.setProperty('visible',False)
                    self.savechanges.setProperty('visible',True)
                elif self.usel.property('text')=='guest':
                    self.cbSudoers_show.setProperty('visible',False)
                    self.removeuser.setProperty('visible',False)
                    self.savechanges.setProperty('visible', False)
                else:
                    self.savechanges.setProperty('visible', True)
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
                self.scroll.setProperty('enabled',False)
                self.scroll.setProperty('visible',False)

            elif self.fsel.property('text')=='display':
                self.controlview.setProperty('visible',False)
                self.display_exec.setProperty('visible',True)
                self.back.setProperty('visible',True)
                self.title.setProperty('text',res.get('@string/display'))
                self.change_reso.clicked.connect (self.change_reso_)
                self.scroll.setProperty('enabled',False)
                self.scroll.setProperty('visible',False)

            elif self.fsel.property('text')=='network':
                self.controlview.setProperty('visible',False)
                self.network_exec.setProperty('visible',True)
                self.back.setProperty('visible',True)
                self.title.setProperty('text',res.get('@string/wifi'))
                self.scroll.setProperty('enabled',False)
                self.scroll.setProperty('visible',False)

            elif self.fsel.property('text')=='languages':
                self.controlview.setProperty('visible',False)
                self.languages_exec.setProperty('visible',True)
                self.back.setProperty('visible',True)
                self.title.setProperty('text',res.get('@string/languages'))
                self.scroll.setProperty('enabled',False)
                self.scroll.setProperty('visible',False)
                self.apply3.clicked.connect (self.languages__)

            elif self.fsel.property('text')=='..':
                self.controlview.setProperty('visible',True)
                self.network_exec.setProperty('visible',False)
                self.languages_exec.setProperty('visible',False)
                self.sysinfo_exec.setProperty('visible',False)
                self.apper_exec.setProperty('visible',False)
                self.theme_exec.setProperty('visible',False)
                self.scroll.setProperty('enabled',True)
                self.scroll.setProperty('visible',True)
                self.display_exec.setProperty('visible',False)
                self.adduser.setProperty('visible',False)
                self.changepassword_exec.setProperty('visible',False)
                self.back_users.setProperty('visible',False)
                self.users_exec.setProperty('visible',False)
                self.showuser_exec.setProperty('visible',False)
                self.adduser_exec.setProperty('visible',False)
                self.back.setProperty('visible',False)
                self.title.setProperty('text',res.get('@string/controls'))

                if self.stWifi.property('checked'):
                    subprocess.call('nmcli radio wifi on',shell=True)
                    subprocess.call('nmcli radio wifi > /stor/etc/network/radio',shell=True)
                else:
                    subprocess.call('nmcli radio wifi off',shell=True)
                    subprocess.call('nmcli radio wifi > /stor/etc/network/radio',shell=True)

        try:
            self.dock_location = self.cbDock.property('currentValue')
        except:
            pass

        if not self.wsel.property('text')=='':
            self.wselp = self.wsel.property('text')
            self.x = Ask (res.get('@string/connect_to').replace('{0}',self.wselp),res.get('@string/connect_tom').replace('{0}',self.wselp),self.wifi_connect_)
        self.wsel.setProperty('text','')
        self.fsel.setProperty ('text','')
        QTimer.singleShot (100,self.loop)

    def wifi_connect_(self,yes):
        if yes:
            status = subprocess.check_output(f'nmcli device wifi connect "{self.wselp}"',shell=True).decode()
            files.write('/etc/network/status',status)

            QTimer.singleShot(500,self.check_connection_)

    def check_connection_(self):
        status = control.read_list('/etc/network/status')[1]

        if status.startswith ('D'):
            self.x = Text (res.get('@string/connected').replace('{0}',self.wselp),res.get('@string/connectedm').replace('{0}',self.wselp))
        else:
            QTimer.singleShot(100,self.enter_password_)

    def enter_password_(self):
        self.x = Password (res.get('@string/password_placeholder').replace('{0}',self.wselp),self._enter_password_)

    def _enter_password_ (self,password):
        status = subprocess.check_output(f'nmcli device wifi connect "{self.wselp}" password "{password}"', shell=True).decode()
        files.write('/etc/network/status', status)
        self.password = password

        QTimer.singleShot(500, self.check_password_)

    def check_password_(self):
        status = control.read_list('/etc/network/status')[1]

        if status.startswith('D'):
            self.x = Text (res.get('@string/connected').replace('{0}',self.wselp),res.get('@string/connectedm').replace('{0}',self.wselp))

            files.write('/etc/network/init.sa',f'nmcli device wifi connect "{self.wselp}" password "{self.password}"')
        else:
            self.x = Text (res.get('@string/n_connected').replace('{0}',self.wselp),res.get('@string/n_connected').replace('{0}',self.wselp))

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

        currentIndex2 = self.wmTheme.property('currentIndex')

        control.remove_record ('dock',f'/etc/users/{self.username}')
        
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

        elif currentIndex==5:
            control.write_record ('dock','windows-top',f'/etc/users/{self.username}')

        elif currentIndex==6:
            control.write_record ('dock','windows-left',f'/etc/users/{self.username}')

        elif currentIndex==7:
            control.write_record ('dock','windows-right',f'/etc/users/{self.username}')

        elif currentIndex==8:
            control.write_record ('dock','unity',f'/etc/users/{self.username}')

        elif currentIndex==9:
            control.write_record ('dock','unity-top',f'/etc/users/{self.username}')

        elif currentIndex==10:
            control.write_record ('dock','unity-left',f'/etc/users/{self.username}')

        elif currentIndex==11:
            control.write_record ('dock','unity-right',f'/etc/users/{self.username}')

        f = open('/stor/etc/default/openbox.xml.bak','r')
        openboxrc = f.read()
        f.close()

        if currentIndex2==1:
            f = open('/stor/etc/default/openbox.xml', 'w')
            f.write(openboxrc.replace('<name>Win10</name>','<name>Afterpiece</name>'))
            f.close()

            shutil.copyfile('/stor/etc/default/openbox.xml', '/root/.config/openbox/rc.xml')
            subprocess.call(['openbox', '--reconfigure'])
        elif currentIndex2==2:
            f = open('/stor/etc/default/openbox.xml', 'w')
            f.write(openboxrc.replace('<name>Win10</name>','<name>Win10</name>'))
            f.close()

            shutil.copyfile('/stor/etc/default/openbox.xml', '/root/.config/openbox/rc.xml')
            subprocess.call(['openbox', '--reconfigure'])

        elif currentIndex2==3:
            f = open('/stor/etc/default/openbox.xml', 'w')
            f.write(openboxrc.replace('<name>Win10</name>','<name>Arc_OSX</name>'))
            f.close()

            shutil.copyfile('/stor/etc/default/openbox.xml', '/root/.config/openbox/rc.xml')
            subprocess.call(['openbox', '--reconfigure'])

        elif currentIndex2==4:
            f = open('/stor/etc/default/openbox.xml', 'w')
            f.write(openboxrc.replace('<name>Win10</name>','<name>Arc-Dark-OSX</name>'))
            f.close()
            shutil.copyfile('/stor/etc/default/openbox.xml', '/root/.config/openbox/rc.xml')
            subprocess.call(['openbox', '--reconfigure'])

        app.signal('apps')
        app.signal('dock')

        self.fsel.setProperty('text','..')

    def clean_(self):
        self.apply2.setProperty('enabled',True)
        self.title.setProperty('text',res.get('@string/adduser'))
    
    def apply_adduser_(self):   
        if not files.isfile(f"/etc/users/{self.leUsername.property('text')}") and not self.leUsername.property('text')=='guest':
            self.apply2.setProperty('enabled',True)
            
            files.create (f"/etc/users/{self.leUsername.property('text')}")
            files.mkdir (f"/desk/{self.leUsername.property('text')}")
            if not files.isdir (f'/etc/key/{self.leUsername.property("text")}'):
                files.mkdir(f'/etc/key/{self.leUsername.property("text")}')

            if not files.isdir (f'/etc/chat/{self.leUsername.property("text")}'):
                files.mkdir(f'/etc/chat/{self.leUsername.property("text")}')

            if not files.isdir (f'/etc/drive/{self.leUsername.property("text")}'):
                files.mkdir(f'/etc/drive/{self.leUsername.property("text")}')

            control.write_record(f'/desk/{self.leUsername.property("text")}',f"drwxr-x---/{self.leUsername.property('text')}",'/etc/permtab')
            control.write_record ('code',hashlib.sha3_512(self.lePassword.property('text').encode()).hexdigest(),f"/etc/users/{self.leUsername.property('text')}")
            control.write_record ('fullname',self.leFullName.property('text'),f"/etc/users/{self.leUsername.property('text')}")
            control.write_record ('profile','@icon/users',f"/etc/users/{self.leUsername.property('text')}")
            if self.cbSudoers.property('checked'):
                files.write ('/etc/sudoers',f"{self.leUsername.property('text')}\n")

            k = Key(self.leUsername.property('text')) # create public key and private key for created user

            self.addUserModel()
            self.fsel.setProperty('text','users')
        else:
            self.apply2.setProperty('enabled',False)
            self.title.setProperty('text',res.get('@string/exists_message').replace('{0}',self.leUsername.property('text')))
            QTimer.singleShot(3000,self.clean_)

    def getdata (self,name):
        x = control.read_record(name,f'/etc/users/{self.username}')
        if x=='' or x==None:
            x = res.getdata(name)

        return x

    def adduser_(self):
        self.adduser_exec.setProperty('visible',True)
        self.title.setProperty('text',res.get('@string/adduser'))
        self.users_exec.setProperty('visible',False)
        self.back.setProperty('visible',False)
        self.back_users.setProperty('visible',True)
        self.adduser.setProperty('visible',False)

    profile_show = '@icon/users'

    def change_profile_img_(self):
        self.x = Select (self.change_profile_img__)

    def change_profile_img__(self,filename):
        self.imgProfile_show.setProperty('source',files.input_qml(filename))
        self.profile_show = filename

    def change_reso_(self):
        subprocess.call(['xrandr','-s',self.rsel.property('text')])
        files.write ('/proc/info/randr',self.rsel.property('text'))
        self.fsel.setProperty('text','..')

    def savechanges_(self):
        userdb = f"/etc/users/{self.usel.property('text')}"

        control.write_record('fullname',self.leFullName_show.property('text'),userdb)
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

    def languages__(self):
        lang = self.lsel.property('text').split('.')[0]
        control.remove_record('locale','/etc/gui')
        control.write_record ('locale',lang,'/etc/gui')
        self.fsel.setProperty('text','..')

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
                self.title.setProperty('text',res.get('@string/not_matched'))
                self.savechanges2.setProperty('enabled',False)
                QTimer.singleShot(3000,self.clean2_)
        else:
            self.title.setProperty('text',res.get('@string/wrong_password'))
            self.savechanges2.setProperty('enabled',False)
            QTimer.singleShot(3000,self.clean2_)

    def removeuser_(self):
        self.x = Ask(f'{res.get("@string/remove")} {self.usel.property("text")}',res.get('@string/remove_user_message').replace('{0}',self.usel.property('text')),self.removeuser__)

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
        self.addNetworkModel()
        self.addDisplayModel()
        self.addLanguageModel()
        self.load (res.get('@layout/controls'))
        self.setProperty('title',res.get('@string/controls'))
        app.launchedlogo(self.property('title'), res.etc('controls', 'logo'))
        self.fsel = self.findChild('fsel')
        self.lsel = self.findChild('lsel')
        self.controlview = self.findChild ('controlview')
        self.back = self.findChild('back')
        self.logo = self.findChild ('logo')
        self.logo.setProperty('source',res.qmlget('@icon/cloud'))
        self.sysinfo = self.findChild ('sysinfo')
        self.sysinfo_exec = self.findChild ('sysinfo_exec')
        self.sysinfo.setProperty('text',res.get('@string/sysinfo'))
        self.info = self.findChild('info')
        self.info.setProperty('source',res.qmlget('@icon/info'))
        self.usersimg = self.findChild ('usersimg')
        self.usersimg.setProperty('source',res.qmlget('@icon/users'))
        self.setProperty('text',res.get('@string/controls'))
        self.title = self.findChild('title')
        self.title.setProperty('text',res.get('@string/controls'))

        self.apper = self.findChild ('apper')
        self.apper_exec = self.findChild ('apper_exec')
        self.apper.setProperty('text',res.get('@string/appearance'))

        self.txtTheme = self.findChild ('txtTheme')
        self.theme_exec = self.findChild ('theme_exec')
        self.txtTheme.setProperty('text',res.get('@string/themes'))

        self.imgTheme = self.findChild('imgTheme')
        self.imgTheme.setProperty('source',res.qmlget('@icon/theme'))

        self.display = self.findChild ('display')
        self.displayimg = self.findChild ('displayimg')
        self.displayimg.setProperty('source',res.qmlget('@icon/display'))
        self.display.setProperty('text',res.get('@string/display'))
        self.display_exec = self.findChild ('display_exec')

        self.users = self.findChild ('users')
        self.users_exec = self.findChild ('users_exec')
        self.languages = self.findChild ('languages')
        self.languages.setProperty('text',res.get('@string/languages'))
        self.languages_exec = self.findChild ('languages_exec')
        self.users.setProperty('text',res.get('@string/accounts'))
        self.adduser_exec = self.findChild('adduser_exec')
        self.network_exec = self.findChild('network_exec')
        self.network = self.findChild('network')
        self.network.setProperty('text',res.get('@string/wifi'))
        self.btnChange_desktop = self.findChild('btnChange_desktop')
        self.btnChange_desktop.setProperty('text',res.get('@string/desktop'))
        self.btnChange_desktop.clicked.connect (self.set_desktop_bg)
        self.btnChange_lock = self.findChild('btnChange_lock')
        self.btnChange_lock.setProperty('text',res.get('@string/lock'))
        self.btnChange_lock.clicked.connect (self.set_lock_bg)
        self.btnChange_unlock = self.findChild('btnChange_unlock')
        self.btnChange_unlock.setProperty('text',res.get('@string/unlock'))
        self.btnChange_unlock.clicked.connect (self.set_unlock_bg)
        self.btnChange_enter = self.findChild('btnChange_enter')
        self.btnChange_enter.setProperty('text',res.get('@string/login'))
        self.btnChange_enter.clicked.connect (self.set_enter_bg)
        self.imgChange_desktop = self.findChild('imgChange_desktop')
        self.imgChange_desktop.setProperty('source',res.qmlget(res.etc('controls','imgChange_desktop')))
        self.imgChange_lock = self.findChild('imgChange_lock')
        self.imgChange_lock.setProperty('source',res.qmlget(res.etc('controls','imgChange_lock')))
        self.imgChange_unlock = self.findChild('imgChange_unlock')
        self.imgChange_unlock.setProperty('source',res.qmlget(res.etc('controls','imgChange_unlock')))
        self.imgChange_enter = self.findChild('imgChange_enter')
        self.imgChange_enter.setProperty('source',res.qmlget(res.etc('controls','imgChange_enter')))
        self.adduser = self.findChild('adduser')
        self.back_users = self.findChild('back_users')
        self.wmTheme = self.findChild('wmTheme')
        self.cbDock = self.findChild ('cbDock')
        self.apply = self.findChild('apply')
        self.cancel = self.findChild('cancel')
        self.cancel.setProperty('text',res.get('@string/cancel'))
        self.apply.setProperty('text',res.get('@string/apply'))
        self.apply.clicked.connect (self.apply_)
        self.txtDock = self.findChild ('txtDock')
        self.txtDock.setProperty('text',res.get('@string/dock_location'))
        self.txtWallpapers = self.findChild ('txtWallpapers')
        self.txtWallpapers.setProperty('text',res.get('@string/change_wallpaper'))
        # add user objects #
        self.leUsername = self.findChild('leUsername')
        self.leUsername.setProperty('placeholderText',res.get('@string/e_username'))
        self.lePassword = self.findChild('lePassword')
        self.lePassword.setProperty('placeholderText',res.get('@string/e_password'))
        self.w100 = self.findChild ('w100')
        self.w100.setProperty('source',res.qmlget('@icon/w100'))
        self.cbSudoers = self.findChild('cbSudoers')
        self.cbSudoers.setProperty('text',res.get('@string/sudoers'))
        self.stWifi = self.findChild('stWifi')
        self.leFullName = self.findChild('leFullName')
        self.leFullName.setProperty('placeholderText',res.get('@string/fullname'))
        self.apply2 = self.findChild('apply2')
        self.apply2.setProperty('text',res.get('@string/apply'))
        self.showuser_exec = self.findChild ('showuser_exec')
        self.usel = self.findChild ('usel')
        self.leUsername_show = self.findChild('leUsername_show')
        self.lang = self.findChild ('lang')
        self.lang.setProperty('source',res.qmlget('@icon/lang'))
        self.leUsername_show.setProperty('placeholderText',res.get('@string/e_username'))    
        self.rsel = self.findChild('rsel')
        self.cbSudoers_show = self.findChild('cbSudoers_show')
        self.cbSudoers_show.setProperty('text',res.get('@string/sudoers'))
        self.leFullName_show = self.findChild('leFullName_show')
        self.leFullName_show.setProperty('placeholderText',res.get('@string/fullname'))
        self.imgProfile_show = self.findChild('imgProfile_show')
        self.imgProfile_show.setProperty('source',res.qmlget('@icon/users'))
        self.btnProfile_show = self.findChild('btnProfile_show')
        self.savechanges = self.findChild('savechanges')
        self.savechanges.setProperty('text',res.get('@string/savechanges'))
        self.changepassword = self.findChild('changepassword')
        self.changepassword.setProperty('text',res.get('@string/change_password'))
        self.removeuser = self.findChild('removeuser')
        self.leoldPassword_change = self.findChild('leoldPassword_change')
        self.leoldPassword_change.setProperty('placeholderText',res.get('@string/oldpass'))
        self.leNewPassword_change = self.findChild('leNewPassword_change')
        self.leNewPassword_change.setProperty('placeholderText',res.get('@string/newpass'))
        self.leCofirmPassword_change = self.findChild('leConfirmPassword_change')
        self.leCofirmPassword_change.setProperty('placeholderText',res.get('@string/confirmpass'))
        self.savechanges2 = self.findChild('savechanges2')
        self.savechanges2.setProperty('text',res.get('@string/savechanges'))
        self.changepassword_exec = self.findChild('changepassword_exec')
        self.wsel = self.findChild('wsel')
        self.wallpaper = self.findChild('wallpaper')
        self.wallpaper.setProperty('source',res.qmlget('@icon/wallpaper'))
        self.cancel3 = self.findChild('cancel3')
        self.cancel3.setProperty('text',res.get('@string/cancel'))
        self.cancel2 = self.findChild('cancel2')
        self.cancel2.setProperty('text',res.get('@string/cancel'))
        self.cancel_reso =  self.findChild('cancel_reso')
        self.cancel_reso.setProperty('text',res.get('@string/cancel'))
        self.change_reso = self.findChild('change_reso')
        self.scroll = self.findChild('scroll')
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

        self.apply3 = self.findChild('apply3')
        self.apply3.setProperty('text',res.get('@string/apply'))
        self.cancel4 = self.findChild('cancel4')
        self.cancel4.setProperty('text',res.get('@string/cancel'))

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
        elif self.getdata('dock')=='windows' or self.getdata('dock')=='windows-bottom': 
            self.dock_location = 4
            self.cbDock.setProperty('currentIndex',4)
        elif self.getdata('dock')=='windows-top': 
            self.dock_location = 5
            self.cbDock.setProperty('currentIndex',5)
        elif self.getdata('dock')=='windows-left': 
            self.dock_location = 6
            self.cbDock.setProperty('currentIndex',6)
        elif self.getdata('dock')=='windows-right': 
            self.dock_location = 7
            self.cbDock.setProperty('currentIndex',7)
        elif self.getdata('dock')=='unity' or self.getdata('dock')=='unity-bottom':
            self.dock_location = 8
            self.cbDock.setProperty('currentIndex',8)
        elif self.getdata('dock')=='unity-top':
            self.dock_location = 9
            self.cbDock.setProperty('currentIndex',9)
        elif self.getdata('dock')=='unity-left':
            self.dock_location = 10
            self.cbDock.setProperty('currentIndex',10)
        elif self.getdata('dock')=='unity-right':
            self.dock_location = 11
            self.cbDock.setProperty('currentIndex',11)


        self.adduser.clicked.connect (self.adduser_)

        # Get Wifi on or off
        subprocess.call('nmcli radio wifi > /stor/etc/network/radio',shell=True)

        if 'enabled' in files.readall('/etc/network/radio'):
            self.stWifi.setProperty('checked',True)
        else:
            self.stWifi.setProperty('checked',False)

        # args #
        if not sys.argv[1:]==[]:
            try:
                self.fsel.setProperty('text',sys.argv[1])
            except:
                pass

        self.loop()

application = QtGui.QGuiApplication([])
application.setWindowIcon (QIcon(res.get(res.etc('controls','logo'))))
w = Sudo(MainApp)
application.exec()