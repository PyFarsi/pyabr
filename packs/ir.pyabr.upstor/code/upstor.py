
from pyabr.core import *
from pyabr.quick import *
import subprocess
class MainApp (MainApp):

    def set_progressbar_value (self,value):
        self.pro.setProperty('value',value/100)
        if value == 100:
            self.close()
            subprocess.call('mount /tmp/stor.sb /mnt',shell=True)
            subprocess.call('cp -r /mnt/stor/app /stor',shell=True)
            subprocess.call('cp -r /mnt/stor/proc /stor',shell=True)
            subprocess.call('cp -r /mnt/stor/usr /stor',shell=True)
            subprocess.call('cp -r /mnt/stor/vmabr.pyc /stor',shell=True)
            subprocess.call('cp -r /mnt/stor/etc/domain /stor/etc',shell=True)
            subprocess.call('cp -r /mnt/stor/etc/distro /stor/etc',shell=True)
            subprocess.call('cp -r /mnt/stor/etc/ext /stor/etc',shell=True)
            subprocess.call('cp -r /mnt/stor/etc/fhs /stor/etc',shell=True)
            subprocess.call('umount /mnt',shell=True)
            subprocess.call('rm /tmp/stor.sb',shell=True)
            subprocess.call('rm /stor/tmp/stor.txt',shell=True)
            return

    def install_(self):
        the_url = 'https://dl.pyabr.ir/stor.sb'
        the_filesize = requests.get(the_url, stream=True).headers['Content-Length']
        the_filepath = f'/tmp/stor.sb'
        the_fileobj = open(the_filepath, 'wb')
        self.downloadThread = DownloadThread(the_url, the_filesize, the_fileobj, buffer=10240)
        self.downloadThread.download_proess_signal.connect(self.set_progressbar_value)
        self.downloadThread.start()

    def __init__(self):
        super(MainApp, self).__init__()

        self.load (res.get('@layout/upstor'))
        self.setProperty('title',res.get('@string/upstor'))

        if files.isfile ('/tmp/stor.txt'): files.remove ('/tmp/stor.txt')
        commands.wget (['https://dl.pyabr.ir/stor.txt','/tmp/stor.txt'])

        if files.readall('/tmp/stor.txt')==files.readall('/proc/info/ver'):
            self.close()
            self.s = Text (res.get('@string/upstoru'),res.get('@string/upstorum'))
        else:
            self.btnUpgrade = self.findChild ('btnUpgrade')
            self.pro = self.findChild ('pro')
            self.logo = self.findChild('logo')
            self.name = self.findChild('name')
            self.name.setProperty('text',f'{res.get("@string/upstort")} {res.num(files.readall("/tmp/stor.txt"))}')
            self.logo.setProperty('source',res.qmlget(res.etc('upstor','cloud')))
            self.btnUpgrade.clicked.connect (self.install_)
            self.btnUpgrade.setProperty('text',res.get('@string/upstor'))

            self.btnCancel = self.findChild ('btnCancel')
            self.btnCancel.setProperty('text',res.get('@string/cancel'))
            self.btnCancel.clicked.connect (self.close)

application = QtGui.QGuiApplication([])
w = MainApp()
application.exec()