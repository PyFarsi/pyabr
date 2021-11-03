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

class MainApp (MainApp):

    def __init__(self):
        super(MainApp, self).__init__()

        self.load (res.get('@layout/debug'))
application = QtGui.QGuiApplication([])
application.setWindowIcon (QIcon(res.get(res.etc('debug','logo'))))

w = MainApp()
application.exec()