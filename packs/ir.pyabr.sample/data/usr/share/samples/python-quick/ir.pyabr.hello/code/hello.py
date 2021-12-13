from pyabr.core import *
from pyabr.quick import *

class MainApp(MainApp):
    def __init__(self):
        super(MainApp, self).__init__()

        self.load (res.get('@layout/hello'))

application = QtGui.QGuiApplication([])
w = MainApp()
application.exec()