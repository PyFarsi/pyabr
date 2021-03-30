from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from libabr import *
from PyQt5 import uic
import requests,shutil,os
app = App()
res = Res()
files = Files()
control = Control()
commands = Commands()

class MainApp(QMainWindow):

    def onCloseProcess (self):
        if not app.check('uiv'):
            self.Widget.Close()
        else:
            QTimer.singleShot(1,self.onCloseProcess)

    def LoadUI (self):
        uic.loadUi(self.link,self)

        self.BackendPage(self.url)

        self.Widget.SetWindowTitle(self.windowTitle())
        self.Widget.SetWindowIcon(self.windowIcon())
        self.Widget.Resize(self, self.width(), self.height())

    def PageNotFound (self):
        self.Widget.Close()
        app.switch('uiv')
        self.Env.RunApp('text', ['Page not found', 'Cannot find this page; page not found.'])
        app.switch('uiv')

    def DomainNotExists (self):
        self.Widget.Close()
        app.switch('uiv')
        self.Env.RunApp('text', ['Domain not exists', 'Cannot find this domain; domain not exists.'])
        app.switch('uiv')

    def ConnectionFailed (self):
        self.Widget.Close()
        app.switch('uiv')
        self.Env.RunApp('text', ['Connection failed', 'Cannot load this page; connection failed.'])
        app.switch('uiv')

    def BackendPage (self,url):
        py = url.replace ('.xml','.py')

        if files.isfile (py):
            commands.cc ([py,'/abr.pyc'])

            try:
                x = __import__('abr')
                self.backend = x.MainApp (self)
            except:
                pass

            files.remove('/abr.pyc')
            files.remove(py)
        else:
            pass

    def __init__(self,args):
        super(MainApp, self).__init__()

        # ports
        self.Backend = args[0]
        self.Env = args[1]
        self.Widget = args[2]
        self.AppName = args[3]
        self.External = args[4]

        self.onCloseProcess()

        self.Widget.SetWindowIcon(QIcon(res.get(res.etc('uiv','logo'))))

        # External ui #
        if self.External==None:
            self.Widget.Close()
        else:
            if self.External==[]:
                self.Widget.Close()
            else:
                if self.External[0]==None:
                    self.Widget.Close()
                elif self.External[0].startswith ('abr://'):

                    url = (self.External[0].replace('abr://','').split('/'))
                    splitx = url[0].split ('.')
                    splitx.reverse()

                    urlx = '/srv'
                    for i in splitx:
                        urlx+='/'+i

                    if url[1:]==[]:
                        url = urlx + "/" + control.read_record("default",'/etc/abr')
                    else:
                        if url[1].__contains__('.'):
                            url = urlx + "/" + url[1]
                        else:
                            url = urlx + "/" + control.read_record("default",'/etc/abr')

                    if files.isfile(url):
                        uic.loadUi(files.input(url), self)
                        self.BackendPage(url)
                    else:
                        if not files.isdir(files.parentdir(url)): files.makedirs(files.parentdir(url))

                        try:
                            x = requests.post(control.read_record('server','/etc/abr'), data={'domain':files.input(url)})
                            y = requests.post(control.read_record('server', '/etc/abr'),data={'domain': files.input(url.replace('.xml','.py'))})

                            if x.text == '404' and self.External[0].endswith('.xml'):
                                QTimer.singleShot(100, self.PageNotFound)
                            elif x.text == '404':
                                QTimer.singleShot(100, self.DomainNotExists)
                            else:
                                files.write(url, x.text)
                                files.write(url.replace('.xml','.py'),y.text)
                                self.link = files.input(url)
                                self.url = url
                                QTimer.singleShot(100, self.LoadUI)
                        except:
                            QTimer.singleShot(100, self.ConnectionFailed)

                    self.Widget.SetWindowTitle(self.windowTitle())
                    self.Widget.SetWindowIcon(self.windowIcon())
                    self.Widget.Resize(self, self.width(), self.height())

                else:
                    uic.loadUi(files.input(self.External[0]),self)

                    self.Widget.SetWindowTitle (self.windowTitle())
                    self.Widget.SetWindowIcon (self.windowIcon())
                    self.Widget.Resize (self,self.width(),self.height())