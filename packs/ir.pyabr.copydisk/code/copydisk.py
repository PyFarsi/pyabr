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

from os import terminal_size
from pyabr.core import *
from pyabr.quick import *
import subprocess, multiprocessing

def _format_():
    subprocess.call(['mkfs.vfat','-I',f'{files.readall("/tmp/copydisk.tmp")}'])
    subprocess.call(['mount',f'{files.readall("/tmp/copydisk.tmp")}','/mnt'])
    subprocess.call(['cp','-r','/run/initramfs/memory/data/pyabr','/mnt'])
    subprocess.call('cd /mnt/pyabr/boot && sh bootinst.sh',shell=True)
    subprocess.call(['umount','/mnt'])

class MainApp (MainApp):
    def _format(self,yes):
        if yes:
            files.write ('/tmp/copydisk.tmp',self.dsel.property('text'))
            p2 = multiprocessing.Process(target=_format_)
            p2.start()
            
    def format_ (self):
        self.x = Ask (f"{res.get('@string/format')} {self.dsel.property('text')}",res.get('@string/formatm'),self._format)
        
    def __init__(self):
        super(MainApp, self).__init__()
        self.addCopyDiskModel()

        self.load (res.get('@layout/copydisk'))
        self.setProperty('title',res.get('@string/copydisk'))
        self.dsel = self.findChild ('dsel')
        self.btnCopy = self.findChild ('btnCopy')
        self.btnCopy.setProperty('text',res.get('@string/fcopy'))
        self.btnCopy.clicked.connect (self.format_)

        self.btnCancel = self.findChild ('btnCancel')
        self.harddiskz = self.findChild ('harddisk')
        self.harddiskz.setProperty('source',res.qmlget(res.etc('copydisk','logo')))
        self.btnCancel.setProperty('text',res.get('@string/cancel'))
        self.btnCancel.clicked.connect (self.close)


application = QtGui.QGuiApplication([])
application.setWindowIcon (QIcon(res.get(res.etc('copydisk','logo'))))

w = MainApp()
application.exec()