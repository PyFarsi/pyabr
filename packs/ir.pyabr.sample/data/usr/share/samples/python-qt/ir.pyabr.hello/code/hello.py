from pyabr.core import *
from pyabr.quick import *

class MainApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainApp, self).__init__()

        self.show()

application = QtWidgets.QApplication([])
w = MainApp()
application.exec()