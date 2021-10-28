from pyabr.core import *
from pyabr.quick import *
from threading import Thread
from pyqtconsole.console import PythonConsole

class MainApp(PythonConsole):
    def __init__(self):
        super(MainApp, self).__init__()
        self.show()
        self.eval_in_thread()
        
application = QtGui.QGuiApplication([])
w = MainApp()
application.exec()