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
from pyabr.chat import *

class ChannelConnector (MainApp):
    def connect_(self):

        if self.leChannel.property('text')=='':
            pass
        else:
            control.write_record ('host',self.leChannel.property('text'),'/etc/channel')

        c = Channel()
        c.Connect (self.leUsername.property('text'),self.lePassword.property('text'))

        self.close()
        app.start ('chat','')

    def __init__(self):
        super(ChannelConnector, self).__init__()

        self.load (res.get('@layout/ChannelConnector'))

        self.setProperty('title',res.get('@string/c_channel'))

        self.leChannel = self.findChild('leChannel')
        self.leChannel.setProperty('placeholderText',res.get('@string/e_channel'))
        self.leUsername = self.findChild('leUsername')
        self.leUsername.setProperty('placeholderText',res.get('@string/e_username'))
        self.lePassword = self.findChild('lePassword')
        self.lePassword.setProperty('placeholderText',res.get('@string/e_password'))
        self.btnConnect = self.findChild('btnConnect')
        self.btnConnect.setProperty('text',res.get('@string/connect'))
        self.btnConnect.clicked.connect (self.connect_)

class MainApp (MainApp):
    su = files.readall('/proc/info/su')


    def connector_(self):
        self.close()
        self.w = ChannelConnector()

    cselp = ''

    def sendMessage_(self):
        c = Channel()
        if not self.leSend.property('text')=='' or self.leSend.property('text')==' ' or self.leSend.property('text')=='  ':
            c.Send (self.cselp,self.leSend.property('text'))

        self.leSend.setProperty('text','')
        self.addChatModel (c.Get(self.cselp))

    timeloop = 100

    def loop(self):
        if not self.csel.property("text")=='' and not self.csel.property("text")=='..':
            self.recontact.setProperty('visible',False)
            self.rechat.setProperty('visible',True)
            self.title.setProperty('visible',True)
            self.addcontact.setProperty('visible',False)
            self.add.setProperty('visible',False)
            self.cselp = self.csel.property('text')
            self.back.setProperty('visible',True)
            self.leSend.setProperty('visible',True)
            self.place.setProperty('visible',True)
            self.btnSend.setProperty('visible',True)
            self.title.setProperty('title',self.xfullname.property('text'))
            self.btnSend.clicked.connect (self.sendMessage_)

            self.timeloop = 6000

        elif self.csel.property("text")=='..':
            self.recontact.setProperty('visible',True)
            self.rechat.setProperty('visible',False)
            self.title.setProperty('visible',False)
            self.addcontact.setProperty('visible',True)
            self.add.setProperty('visible',True)
            self.back.setProperty('visible',False)
            self.leSend.setProperty('visible',False)
            self.place.setProperty('visible',False)
            self.btnSend.setProperty('visible',False)

            self.timeloop = 100

        
        if self.act.property('text')=='delete':
            c = Channel()
            c.Delete (self.cid.property('text'))
            self.addChatModel (c.Get(self.cselp))

        elif self.act.property('text')=='delchat':
            c = Channel()
            c.DeleteChat (self.cselp)
            self.close()
            app.start ('chat','')
            
        elif self.act.property('text')=='clear':
            c = Channel()
            c.Clear (self.cselp)
            self.addChatModel (c.Get(self.cselp))

        c = Channel()
        try:
            self.addChatModel (c.Get(self.cselp))
        except:
            pass

        self.addContactModel (c.Contacts())

        self.csel.setProperty('text','')

        QTimer.singleShot(self.timeloop,self.loop)

    def addcontact_(self):
        self.x = Input(res.get('@string/e_contact'),self.addcontact__)

    def addcontact__(self,username):
        c = Channel()
        c.AddContact (username)

    def __init__(self):
        super(MainApp, self).__init__()
        c = Channel()
        self.addContactModel (c.Contacts())
        self.load (res.get('@layout/chat'))
        self.setProperty('title',res.get('@string/chat'))
        self.add = self.findChild('add')
        self.add.clicked.connect (self.connector_)
        self.csel = self.findChild('csel')
        self.addcontact = self.findChild('addcontact')
        self.addcontact.clicked.connect (self.addcontact_)
        self.rechat = self.findChild('rechat')
        self.recontact = self.findChild('recontact')
        self.title = self.findChild('title')

        self.xfullname = self.findChild('xfullname')
        self.back = self.findChild('back')
        self.leSend = self.findChild('leSend')
        self.leSend.setProperty('placeholderText',res.get('@string/e_send'))
        self.place = self.findChild('place')
        self.btnSend = self.findChild('btnSend')
        self.cid = self.findChild('cid')
        self.csender = self.findChild('csender')
        self.cgiver = self.findChild('cgiver')
        self.cdata = self.findChild('cdata')
        self.act = self.findChild('act')
        self.delete_c = self.findChild('delete_c')
        self.delete_m = self.findChild('delete_m')
        self.history_m= self.findChild('history_m')
        self.profimg2 = self.findChild('profimg2')
        self.profimg2.setProperty('source',res.qmlget(res.etc('chat','profimg2')))

        self.loop()

application = QtGui.QGuiApplication([])
application.setWindowIcon (QIcon(res.get(res.etc('chat','logo'))))

su = files.readall('/proc/info/su')
if files.isfile (f'/etc/chat/{su}/pass') and files.isfile (f'/etc/chat/{su}/user'):
    w = MainApp()
else:
    w = ChannelConnector()

application.exec()