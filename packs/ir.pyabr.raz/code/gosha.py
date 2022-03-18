from pyabr.core import *
from pyabr.quick import *
from pyabr.cloud import *
import sys

class MainApp(MainApp): 
    def __init__(self):
        super(MainApp, self).__init__()
        self.load (res.get('@layout/gosha'))
        self.setProperty('title',res.getname('gosha'))
        app.launchedlogo(self.property('title'), res.etc('gosha', 'logo'))

        self.user = files.readall('/proc/info/su')

        self.userpath = ''

        if self.user=='root':
            self.userpath = '/root/Documents'
        else:
            self.userpath = f'/desk/{self.user}/Documents'

        self.text = self.findChild('text')

        if sys.argv[1:]==[]:
            self.close()

        files.copy(f"{sys.argv[1]}",f'/etc/key/{self.user}/Message.bin')

        m = Message()
        self.text.setProperty('text',m.Read())


application = QtGui.QGuiApplication([])
w = MainApp()
application.setWindowIcon(QIcon(res.get(res.etc('raz','logo'))))
application.exec()