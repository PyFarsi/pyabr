from pyabr.core import *
from pyabr.quick import *
from pyabr.cloud import *
import sys

class MainApp(MainApp): 
    def enc_(self):
        m = Message()
        m.Write (self.text.property('text'))
        m.Save()

        files.copy (f"/etc/external-key/Message.bin",f"{self.userpath}/Message.raz")

        self.close()

    def __init__(self):
        super(MainApp, self).__init__()
        self.load (res.get('@layout/negar'))
        self.setProperty('title',res.getname('negar'))
        app.launchedlogo(self.property('title'), res.etc('negar', 'logo'))

        self.user = files.readall('/proc/info/su')

        self.userpath = ''

        if self.user=='root':
            self.userpath = '/root/Documents'
        else:
            self.userpath = f'/desk/{self.user}/Documents'

        self.text = self.findChild('text')
        self.btnEncrypt = self.findChild('btnEncrypt')
        self.btnEncrypt.clicked.connect(self.enc_)
        self.btnEncrypt.setProperty('placeholderText',res.get('@string/encrypt'))

        if sys.argv[1:]==[]:
            self.close()

        files.copy(f"{sys.argv[1]}",'/etc/external-key/Public Key.pem')


application = QtGui.QGuiApplication([])
w = MainApp()
application.setWindowIcon(QIcon(res.get(res.etc('raz','logo'))))
application.exec()