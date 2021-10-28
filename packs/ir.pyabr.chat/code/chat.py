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

        if not files.isfile ('/tmp/chat-success.tmp'):
            self.w = Text (res.get("@string/exists").replace('{0}',self.leUsername.property("text")),f'{self.leUsername.property("text")} {res.get("@string/exists_message")}')
        else:
            self.close()
            app.start('chat','')

    def __init__(self):
        super(ChannelConnector, self).__init__()

        self.load (res.get('@layout/ChannelConnector'))

        self.setProperty('title','Connect to channel')

        self.leChannel = self.findChild('leChannel')
        self.leUsername = self.findChild('leUsername')
        self.lePassword = self.findChild('lePassword')
        self.btnConnect = self.findChild('btnConnect')
        self.btnConnect.clicked.connect (self.connect_)

class MainApp (MainApp):
    su = files.readall('/proc/info/su')


    def connector_(self):
        self.close()
        self.w = ChannelConnector()

    cselp = ''

    def sendMessage_(self):
        #if not (self.leSend.property('text')==''):
        c = Channel()
        m = Message()
        m.Write (files.readall (f'/etc/chat/{su}/user')+": "+self.leSend.property('text'))
        m.Save()
        c.Send (self.cselp)

        self.leSend.setProperty('text','')

    def openfile__(self,filename):
        c = Channel()
        c.File (filename,self.cselp)

    def openfile_(self):
        self.x = Select (self.openfile__)

    def loop(self):
        if not self.csel.property("text")=='' and not self.csel.property("text")=='..':
            self.recontact.setProperty('visible',False)
            self.rechat.setProperty('visible',True)
            self.title.setProperty('visible',True)
            self.addcontact.setProperty('visible',False)
            self.add.setProperty('visible',False)
            self.profimg.setProperty('visible',True)
            self.profimg2.setProperty('visible',True)
            self.cselp = self.csel.property('text')
            self.back.setProperty('visible',True)
            self.leSend.setProperty('visible',True)
            self.place.setProperty('visible',True)
            self.btnSend.setProperty('visible',True)
            self.profimg2.setProperty('source',self.xprofile.property('text'))
            self.title.setProperty('title',self.xfullname.property('text'))
            self.btnSend.clicked.connect (self.sendMessage_)
            self.btnFile.clicked.connect (self.openfile_)
            c = Channel()
            c.Key(self.cselp)

        elif self.csel.property("text")=='..':
            self.recontact.setProperty('visible',True)
            self.rechat.setProperty('visible',False)
            self.title.setProperty('visible',False)
            self.addcontact.setProperty('visible',True)
            self.add.setProperty('visible',True)
            self.profimg.setProperty('visible',False)
            self.back.setProperty('visible',False)
            self.profimg2.setProperty('visible',False)
            self.leSend.setProperty('visible',False)
            self.place.setProperty('visible',False)
            self.btnSend.setProperty('visible',False)

        if not self.cselp=='':
            try:
                c = Channel()
                self.addChatModel(c.Give(self.cselp))
            except:
                pass

        self.csel.setProperty('text','')

        QTimer.singleShot(2000,self.loop)

    def addcontact_(self):
        self.x = Input('Enter your contact username',self.addcontact__)

    def addcontact__(self,username):
        try:
            c = Channel()
            c.AddContact (username)
            self.addContactModel (c.Contacts())
        except:
            pass

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
        self.profimg = self.findChild('profimg')
        self.profimg2 = self.findChild('profimg2')

        self.xfullname = self.findChild('xfullname')
        self.xprofile = self.findChild('xprofile')
        self.back = self.findChild('back')
        self.leSend = self.findChild('leSend')
        self.place = self.findChild('place')
        self.btnSend = self.findChild('btnSend')
        self.cid = self.findChild('cid')
        self.csender = self.findChild('csender')
        self.cgiver = self.findChild('cgiver')
        self.cdata = self.findChild('cdata')

        self.btnFile = self.findChild('btnFile')
        self.btnStickers = self.findChild('btnStickers')
        self.loop()

application = QtGui.QGuiApplication([])
application.setWindowIcon (QIcon(res.get(res.etc('chat','logo'))))

su = files.readall('/proc/info/su')
if files.isfile (f'/etc/chat/{su}/pass') and files.isfile (f'/etc/chat/{su}/user'):
    w = MainApp()
else:
    w = ChannelConnector()
application.exec()