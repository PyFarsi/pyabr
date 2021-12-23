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

        self.load(res.get("@layout/sysinfo"))


        self.host = self.findChild ('host')
        self.cs = self.findChild ('cs')
        self.bl = self.findChild ('bl')
        self.os = self.findChild ('os')
        self.kname = self.findChild ('kname')
        self.su = self.findChild ('su')
        self.de = self.findChild ('de')
        self.gui = self.findChild ('gui')
        self.arch = self.findChild ('arch')

        self.host1 = self.findChild ('host1')
        self.cs1 = self.findChild ('cs1')
        self.bl1 = self.findChild ('bl1')
        self.os1 = self.findChild ('os1')
        self.kname1 = self.findChild ('kname1')
        self.su1 = self.findChild ('su1')
        self.de1 = self.findChild ('de1')
        self.gui1 = self.findChild ('gui1')
        self.arch1 = self.findChild ('arch1')

        self.setProperty ('title',res.get('@string/sysinfo'))
        app.launchedlogo(self.property('title'), res.etc('sysinfo', 'logo'))
        self.logo = self.findChild ('logo')
        self.logo.setProperty('source',res.qmlget(res.etc('sysinfo','cloud')))



        # check direction
        if res.getdata ('locale')=='fa' or res.getdata('locale')=='ar':
            self.host1.setProperty ('text',res.get('@string/host')+":  ")
            self.cs1.setProperty ('text',res.get('@string/cs')+":  ")
            self.bl1.setProperty ('text',res.get('@string/bl')+":  ")
            self.os1.setProperty ('text',res.get('@string/os')+":  ")
            self.kname1.setProperty ('text',res.get('@string/kname')+":  ")
            self.su1.setProperty ('text',res.get('@string/su')+":  ")
            self.de1.setProperty ('text',res.get('@string/de')+":  ")
            self.gui1.setProperty ('text',res.get('@string/gui')+":  ")
            self.arch1.setProperty ('text',res.get('@string/arch')+":  ")

            self.host.setProperty ('text',files.readall('/proc/info/host'))
            self.cs.setProperty ('text',f"{files.readall('/proc/info/cs')} {files.readall('/proc/info/ver')} ({files.readall('/proc/info/cd')})")
            self.bl.setProperty ('text',files.readall('/proc/info/bl'))
            self.os.setProperty ('text',files.readall('/proc/info/os'))
            self.kname.setProperty ('text',files.readall('/proc/info/kname'))
            self.su.setProperty ('text',files.readall('/proc/info/su'))
            self.de.setProperty ('text',files.readall('/proc/info/de'))
            self.gui.setProperty ('text',files.readall('/proc/info/gui'))
            self.arch.setProperty ('text',files.readall('/proc/info/arch'))
        else:
            self.host.setProperty ('text',res.get('@string/host')+":  ")
            self.cs.setProperty ('text',res.get('@string/cs')+":  ")
            self.bl.setProperty ('text',res.get('@string/bl')+":  ")
            self.os.setProperty ('text',res.get('@string/os')+":  ")
            self.kname.setProperty ('text',res.get('@string/kname')+":  ")
            self.su.setProperty ('text',res.get('@string/su')+":  ")
            self.de.setProperty ('text',res.get('@string/de')+":  ")
            self.gui.setProperty ('text',res.get('@string/gui')+":  ")
            self.arch.setProperty ('text',res.get('@string/arch')+":  ")

            self.host1.setProperty ('text',files.readall('/proc/info/host'))
            self.cs1.setProperty ('text',f"{files.readall('/proc/info/cs')} {files.readall('/proc/info/ver')} ({files.readall('/proc/info/cd')})")
            self.bl1.setProperty ('text',files.readall('/proc/info/bl'))
            self.os1.setProperty ('text',files.readall('/proc/info/os'))
            self.kname1.setProperty ('text',files.readall('/proc/info/kname'))
            self.su1.setProperty ('text',files.readall('/proc/info/su'))
            self.de1.setProperty ('text',files.readall('/proc/info/de'))
            self.gui1.setProperty ('text',files.readall('/proc/info/gui'))
            self.arch1.setProperty ('text',files.readall('/proc/info/arch'))

appx = QtGui.QGuiApplication([])
appx.setWindowIcon (QIcon(res.get(res.etc('sysinfo','logo'))))

w = MainApp()
appx.exec()