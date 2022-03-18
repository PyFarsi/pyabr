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
import resource

from pyabr.core import *
from pyabr.quick import *
import sys

class MainApp (MainApp):
    def loop(self):
        if not self.capx.property('text')=='':
            self.close()
            app.start('ayene','')
        QTimer.singleShot(1000,self.loop)
    def __init__(self):
        super(MainApp, self).__init__()

        if files.readall('/proc/info/su') == 'root':
            user = f'/stor/root'
        else:
            user = f'/stor/desk/{files.readall("/proc/info/su")}'

        os.environ['HOME'] = user

        self.load (res.get('@layout/ayene'))

        self.setProperty('title',res.getname('ayene'))
        app.launchedlogo(self.property('title'), res.etc('ayene', 'logo'))

        self.photoPreview = self.findChild('photoPreview')
        self.capx = self.findChild('capx')
        self.loop()

application = QtGui.QGuiApplication([])
application.setWindowIcon (QIcon(res.get(res.etc('ayene','logo'))))

if not os.path.isfile ('/run/initramfs/memory/data/pyabr/modules/09-camera.sb'):
    w = DataInstaller ('ayene','https://dl.pyabr.ir/09-camera.sb','09-camera.sb')
else:
    w = MainApp()
    
application.exec()