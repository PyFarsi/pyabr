import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import queue     #If this template is not loaded, pyinstaller may not be able to run the requests template after packaging
import requests, baran
################################################

from libabr import Files, Control, Res, App

files = Files()
res = Res()
control = Control()
app = App()

class LineEdit (baran.BLineEdit):
    def __init__(self,ports):
        super(LineEdit, self).__init__()
        self.Env = ports[1]
################################################
class MainApp(QWidget):
    def __init__(self,ports, *args, **kwargs):
        super(MainApp, self).__init__(*args, **kwargs)

        self.Backend = ports[0]
        self.Env = ports[1]
        self.Widget = ports[2]
        self.AppName = ports[3]
        self.External = ports[4]

        ## Download history ##
        if files.isdir('.download-history'):
            files.removedirs('.download-history')

        files.create('.download-history')

        self.Widget.Resize (self,500,200)
        self.Widget.SetWindowTitle (res.get('@string/app_name'))
        self.Widget.SetWindowIcon (QIcon(res.get('@icon/breeze-dmgr')))


        layout = QVBoxLayout(self)

        self.leUrl = LineEdit(ports)
        self.leUrl.setFont(self.Env.font())
        self.leUrl.setStyleSheet('border: none;')
        self.leUrl.setPlaceholderText(res.get('@string/link'))
        layout.addWidget(self.leUrl)


        # Increase progress bar
        self.progressBar = QProgressBar(self, minimumWidth=400)
        self.progressBar.setValue(0)
        layout.addWidget(self.progressBar)

        # Add Download Button
        self.pushButton = QPushButton(self, minimumWidth=100)
        self.pushButton.setText(res.get('@string/download'))
        layout.addWidget(self.pushButton)

        # Binding Button Event
        self.pushButton.clicked.connect(self.on_pushButton_clicked)

    # Download button event
    def on_pushButton_clicked(self):
        the_url = self.leUrl.text()
        the_filesize = requests.get(the_url, stream=True).headers['Content-Length']
        the_filepath = '/tmp/download-manager.tmp'

        the_fileobj = open(files.input(the_filepath), 'wb')
        #### Create a download thread
        self.downloadThread = downloadThread(the_url, the_filesize, the_fileobj, buffer=10240)
        self.downloadThread.download_proess_signal.connect(self.set_progressbar_value)
        self.downloadThread.start()

    # Setting progress bar
    def set_progressbar_value(self, value):
        self.progressBar.setValue(value)
        if value == 100:
            app.switch('dmgr')
            self.Env.RunApp('select', [res.get('@string/saveafile'), 'save', self.saveas_])
            app.switch('dmgr')
            return

    def saveas_(self,filename):
        if not files.isdir(filename):
            files.cut('/tmp/download-manager.tmp',filename)
            files.append('.download-history',self.leUrl.text()+":"+files.output(filename))

##################################################################
#Download thread
##################################################################
class downloadThread(QThread):
    download_proess_signal = pyqtSignal(int)                        #Create signal

    def __init__(self, url, filesize, fileobj, buffer):
        super(downloadThread, self).__init__()
        self.url = url
        self.filesize = filesize
        self.fileobj = fileobj
        self.buffer = buffer

    def run(self):
        try:
            rsp = requests.get(self.url, stream=True)                #Streaming download mode
            offset = 0
            for chunk in rsp.iter_content(chunk_size=self.buffer):
                if not chunk: break
                self.fileobj.seek(offset)                            #Setting Pointer Position
                self.fileobj.write(chunk)                            #write file
                offset = offset + len(chunk)
                proess = offset / int(self.filesize) * 100
                self.download_proess_signal.emit(int(proess))        #Sending signal
            #######################################################################
            self.fileobj.close()    #Close file
            self.exit(0)            #Close thread


        except Exception as e:
            print(e)

