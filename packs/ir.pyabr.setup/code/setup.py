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
from pyabr.key import *
import hashlib,subprocess

class MainApp (MainApp):

    pagenum = 0

    def back_(self):
        if self.pagenum==4:
            self.page0.setProperty('visible',False)
            self.page1.setProperty('visible',False)
            self.page2.setProperty('visible',False)
            self.page3.setProperty('visible',True)
            self.page4.setProperty('visible',False)
            self.pagenum=3
            self.back.setProperty('visible',True)
        elif self.pagenum==3:
            self.page0.setProperty('visible',False)
            self.page1.setProperty('visible',False)
            self.page2.setProperty('visible',True)
            self.page3.setProperty('visible',False)
            self.page4.setProperty('visible',False)
            self.pagenum=2
            self.back.setProperty('visible',True)
        elif self.pagenum==2:
            self.page0.setProperty('visible',False)
            self.page1.setProperty('visible',True)
            self.page2.setProperty('visible',False)
            self.page3.setProperty('visible',False)
            self.page4.setProperty('visible',False)
            self.pagenum=1
            self.back.setProperty('visible',True)
        elif self.pagenum==1:
            self.page0.setProperty('visible',True)
            self.page1.setProperty('visible',False)
            self.page2.setProperty('visible',False)
            self.page3.setProperty('visible',False)
            self.page4.setProperty('visible',False)
            self.pagenum=0
            self.back.setProperty('visible',False)

    def next_(self):
        if self.pagenum==0:
            self.page0.setProperty('visible',False)
            self.page1.setProperty('visible',True)
            self.page2.setProperty('visible',False)
            self.page3.setProperty('visible',False)
            self.page4.setProperty('visible',False)
            self.pagenum=1
            self.back.setProperty('visible',True)
        elif self.pagenum==1:
            self.page0.setProperty('visible',False)
            self.page1.setProperty('visible',False)
            self.page2.setProperty('visible',True)
            self.page3.setProperty('visible',False)
            self.page4.setProperty('visible',False)
            self.back.setProperty('visible',True)
            self.pagenum=2
        elif self.pagenum==2:
            self.page0.setProperty('visible',False)
            self.page1.setProperty('visible',False)
            self.page2.setProperty('visible',False)
            self.page3.setProperty('visible',True)
            self.page4.setProperty('visible',False)
            self.back.setProperty('visible',True)
            self.pagenum=3
        elif self.pagenum==3:
            self.page0.setProperty('visible',False)
            self.page1.setProperty('visible',False)
            self.page2.setProperty('visible',False)
            self.page3.setProperty('visible',False)
            self.page4.setProperty('visible',True)
            self.pagenum=4
            self.back.setProperty('visible',False)
        elif self.pagenum==4:
            # Hostname #
            if not self.leHostname.property('text')=='':
                files.write ("/etc/hostname",self.leHostname.property('text'))

            # Root #
            control.write_record ('code',hashlib.sha3_512(self.leRootCode.property('text').encode()).hexdigest(),'/etc/users/root')

            # Main User #
            if not self.leUsername.property('text')=='':
                files.create (f'/etc/users/{self.leUsername.property("text")}')
                files.mkdir (f'/desk/{self.leUsername.property("text")}')

                if not files.isdir (f'/etc/key/{self.leUsername.property("text")}'):
                    files.mkdir (f'/etc/key/{self.leUsername.property("text")}')

                if not files.isdir (f'/etc/chat/{self.leUsername.property("text")}'):
                    files.mkdir (f'/etc/chat/{self.leUsername.property("text")}')

                if not files.isdir (f'/etc/cloud/{self.leUsername.property("text")}'):
                    files.mkdir (f'/etc/cloud/{self.leUsername.property("text")}')
                
                control.write_record ('code',hashlib.sha3_512(self.lePassword.property('text').encode()).hexdigest(),f'/etc/users/{self.leUsername.property("text")}')
                control.write_record (f'/desk/{self.leUsername.property("text")}',f'drwxr-----/{self.leUsername.property("text")}','/etc/permtab')
                
                if not self.leFullName.property('text')=='':
                    control.write_record ('fullname',self.leFullName.property('text'),f'/etc/users/{self.leUsername.property("text")}')
                    
                files.write ('/etc/sudoers',self.leUsername.property("text"))
                control.write_record('profile','@icon/breeze-users',f'/etc/users/{self.leUsername.property("text")}')

                k = Key(self.leUsername.property('text')) # create public key and private key for created user

            # Guest user #
            if self.chGuest.property('checked'):
                files.write ('/etc/guest','enable')

            print ( self.cmLang.property('index'))

            self.close()
            System ('paye rm setup')
            app.signal('logout')

    def __init__(self):
        super(MainApp, self).__init__()

        self.load (res.get('@layout/setup'))
        self.setProperty('title',res.get('@string/setup'))

        self.next = self.findChild ('next')
        self.next.clicked.connect (self.next_)
        self.back = self.findChild ('back')
        self.back.clicked.connect (self.back_)
        self.page = self.findChild ('page')
        self.page0 = self.findChild ('page0')
        self.page1 = self.findChild ('page1')
        self.page2 = self.findChild ('page2')
        self.page3 = self.findChild ('page3')
        self.page4 = self.findChild ('page4')
        self.leHostname = self.findChild ('leHostname')
        self.leHostname.setProperty('placeholderText',res.get('@string/enter_hostname'))
        self.leRootCode = self.findChild ('leRootCode')
        self.leRootCode.setProperty('placeholderText',res.get('@string/choose_root_password'))
        self.leUsername = self.findChild ('leUsername')
        self.leUsername.setProperty('placeholderText',res.get('@string/pick_username'))
        self.lePassword = self.findChild ('lePassword')
        self.lePassword.setProperty('placeholderText',res.get('@string/choose_password'))
        self.chGuest = self.findChild ('chGuest')
        self.cmLang = self.findChild ('cmLang')
        self.leFullName = self.findChild ('leFullName')
        self.leFullName.setProperty('placeholderText',res.get('@string/fullname'))
        self.lePhone = self.findChild ('lePhone')
        self.lePhone.setProperty('placeholderText',res.get('@string/phone'))
        self.leEmail = self.findChild ('leEmail')
        self.leEmail.setProperty('placeholderText',res.get('@string/email'))
        self.setup_message = self.findChild('setup_message')
        self.setup_message.setProperty('text',res.get('@string/setup_message'))
        self.back.setProperty('visible',False)

        self.setProperty('title',res.get('@string/baad'))


application = QtGui.QGuiApplication([])
application.setWindowIcon (QIcon(res.get(res.etc('setup','logo'))))

w = MainApp()
application.exec()