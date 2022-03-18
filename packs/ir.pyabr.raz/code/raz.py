from pyabr.core import *
from pyabr.quick import *
from pyabr.cloud import *

class MainApp(MainApp):
    def sendMail_(self):
        m = Mail()
        m.Subject(self.leSubject.property('text'))
        m.Write(self.text.property('text'))
        m.Send(self.leUsername.property('text'))
        self.addMailModel()
        self.back.setProperty('visible',False)
        self.add.setProperty('visible',True)
        self.leUsername.setProperty('visible',False)
        self.leSubject.setProperty('visible',False)
        self.text.setProperty('visible',False)
        self.btnSend.setProperty('visible',False)
        self.scroll.setProperty('visible',True)

        try:
            self.addMailModel()
        except:
            pass

    def showMail_(self):
        self.back.setProperty('visible',True)
        self.add.setProperty('visible',False)
        self.scroll.setProperty('visible',False)
        self.showMail.setProperty('visible',True)
        self.textShow.setProperty('visible',True)

    def __init__(self):
        super(MainApp, self).__init__()
        try:
            self.addMailModel()
        except:
            pass

        self.load (res.get('@layout/raz'))
        
        self.setProperty('title',res.getname('raz'))
        app.launchedlogo(self.property('title'), res.etc('raz', 'logo'))

        self.user = files.readall('/proc/info/su')

        self.sel = self.findChild('sel')
        self.leSubject = self.findChild('leSubject')
        self.leSubject.setProperty('placeholderText',res.get('@string/subject'))
        self.leUsername = self.findChild('leUsername')
        self.leUsername.setProperty('placeholderText',res.get('@string/e_username'))
        self.scroll = self.findChild('scroll')
        self.btnSend = self.findChild('btnSend')
        self.btnSend.setProperty('placeholderText',res.get('@string/send'))
        self.btnSend.clicked.connect (self.sendMail_)
        self.text = self.findChild('text')

        self.back = self.findChild('back')
        self.add = self.findChild('add')
        self.showMail = self.findChild('showMail')
        self.textShow = self.findChild('textShow')
        self.loop()

    def loop (self):
        if not self.sel.property('text')=='':
            if files.isfile(f"/etc/key/{self.user}/Message.bin"): files.remove (f"/etc/key/{self.user}/Message.bin")
            wget.download (f"https://cloud.pyabr.ir/{self.sel.property('text')}",files.input(f"/etc/key/{self.user}/Message.bin"))
            m = Message()
            msg = m.Read()
            print (msg)
            self.textShow.setProperty('text',msg)

            self.showMail_()
        self.sel.setProperty('text','')
        QTimer.singleShot(1000,self.loop)

application = QtGui.QGuiApplication([])
w = MainApp()
application.setWindowIcon(QIcon(res.get(res.etc('raz','logo'))))
application.exec()