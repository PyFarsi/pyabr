from pyabr.core import *
from pyabr.quick import *
import sys

class Download (MainApp):
    def save_(self,filename):
        commands.mv (['/tmp/download.tmp',filename])

    def set_progressbar_value (self,value):
        self.pro.setProperty('value',value/100)
        if value == 100:
            self.close()
            self.x = Save (self.save_)
            return

    def download_(self):
        the_filesize = requests.get(self.leDownload.property('text'), stream=True).headers['Content-Length']
        the_fileobj = open(files.input('/tmp/download.tmp'), 'wb')
        self.downloadThread = DownloadThread(self.leDownload.property('text'), the_filesize, the_fileobj, buffer=10240)
        self.downloadThread.download_proess_signal.connect(self.set_progressbar_value)
        self.downloadThread.start()

    def __init__(self,link):
        super(MainApp, self).__init__()

        self.load(res.get('@layout/download'))
        self.pro = self.findChild('pro')
        self.setProperty('title',res.get('@string/download'))
        self.btnDownload = self.findChild('btnDownload')
        self.btnDownload.setProperty('text',res.get('@string/download'))
        self.leDownload = self.findChild('leDownload')
        self.leDownload.setProperty('text',link)
        self.leDownload.setProperty('placeholderText',res.get('@string/url'))

        self.btnDownload.clicked.connect (self.download_)

appx = QApplication([])
w = Download(sys.argv[1])
appx.exec()