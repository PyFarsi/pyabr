from PyQt5.QtCore import  *
from PyQt5.QtGui import  *
from PyQt5.QtWidgets import  *

URL = "https://example.com"

class MainApp (QMainWindow):

    def WebPage (self):
        self.Widget.Close()
        self.Env.RunApp('wapp', [URL])

    def __init__(self,ports):
        super(MainApp, self).__init__()

        self.Backend = ports[0]
        self.Env = ports[1]
        self.Widget = ports[2]
        self.AppName = ports[3]
        self.External = ports[4]

        QTimer.singleShot(1,self.WebPage)