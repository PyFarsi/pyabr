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

'''

E0   - Empty fields
E1   - Connection failed
E2   - User Exists
E3   - Cannot move file
E4   - User not found
E5   - Wrong password
E6   - File not found
E7   - Access denid

'''

from pyabr.core import *
from pyabr.quick import *
from pyabr.cloud import *

class MainApp (MainApp):

    def connect_(self):
        self.user = files.readall('/proc/info/su')
        if (self.user=='guest' or self.user=='root') and not files.isfile(f'/etc/key/{self.user}/Public Key.pem'):
            k = Key(self.user) # create public key and private key for created user
        a = Account()
        self.x = a.Connect (self.leUsername.property('text'),self.lePassword.property('text'))
        if self.x=='E0':
            self.w = Text(res.get('@string/sync_E0'),res.get('@string/sync_E0M'))
        elif self.x=='E1':
            self.w = Text(res.get('@string/sync_E1'),res.get('@string/sync_E1M'))
            self.leUsername.setProperty('text','')
            self.lePassword.setProperty('text','')
        elif self.x=='E4':
            self.x = a.Create (self.leUsername.property('text'),self.lePassword.property('text'))
            self.leUsername.setProperty('text','')
            self.lePassword.setProperty('text','')
            self.w = Text (res.get('@string/sync_S'),res.get('@string/sync_SM'))
            self.close()

            # check dashboard for developers
            if not sys.argv[1:]==[]:
                if sys.argv[1]=='pishkhan':
                    app.start('pishkhan','')

        elif self.x=='E5':
            self.w = Text(res.get('@string/sync_E5'),res.get('@string/sync_E5M'))
        elif self.x=='S':
            self.w = Text (res.get('@string/sync_S'),res.get('@string/sync_SM'))
            self.close()

            if not sys.argv[1:]==[]:
                if sys.argv[1]=='pishkhan':
                    app.start('pishkhan','')

    def __init__(self):
        super(MainApp, self).__init__()

        self.load (res.get('@layout/sync'))
        self.setProperty('title',res.get('@string/sync'))
        app.launchedlogo (self.property('title'),'@icon/users')

        self.leUsername = self.findChild('leUsername')
        self.leUsername.setProperty('placeholderText',res.get('@string/e_username'))
        self.lePassword = self.findChild('lePassword')
        self.lePassword.setProperty('placeholderText',res.get('@string/e_password'))
        self.btnCreate  = self.findChild('btnCreate')
        self.btnCreate.setProperty('placeholderText',res.get('@string/sync'))
        self.btnCreate.clicked.connect (self.connect_)

application = QtGui.QGuiApplication([])
application.setWindowIcon (QIcon(res.get(res.etc('sync','logo'))))

w = MainApp()
application.exec()
