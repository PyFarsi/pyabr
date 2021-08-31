from pyabr.core import *
from pyabr.quick import *

class MainApp(MainApp):
    def __init__(self, ports):
        super(MainApp, self).__init__()

        self.load (res.get('@layout/app'))

application = QtGui.QGuiApplication([])
w = MainApp()
application.exec()