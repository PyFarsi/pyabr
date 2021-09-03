from pyabr.core import *
from pyabr.quick import *

class MainApp(QtWidgets.QMainWindow):
    def __init__(self, ports):
        super(MainApp, self).__init__()

        self.show()

application = QtCore.QApplication([])
w = MainApp()
application.exec()