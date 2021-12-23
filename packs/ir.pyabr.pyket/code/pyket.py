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
            
class MainApp (MainApp):

    def loop (self):

        if not self.psel.property('text')=='':
            self.scroll.setProperty('visible',False)
            self.package_exec.setProperty('visible',True)
            self.back.setProperty('visible',True)
            self.title.setProperty('visible',True)
            self.pkgImage.setProperty('source',self.psellogo.property('text'))
            self.pkgTitle.setProperty('text',self.pselnamex.property('text'))
            self.title.setProperty('text',self.pselnamex.property('text'))

            self.show_info()

            if self.pselinstalled.property('text')=='Yes':
                self.btnInstall.setProperty('visible',False)
                self.btnUninstall.setProperty('visible',True)
                self.btnOpen.setProperty('visible',True)
                if self.pseltype.property('text')=='application':
                    self.btnOpen.setProperty('enabled',True)
                    self.entry = control.read_record ('entry',f'/app/packages/{self.psel.property("text")}.manifest')
                else:
                    self.btnOpen.setProperty('enabled',False)
                
                if self.psel.property('text') in files.readall('/etc/paye/permanetly_applications'):
                    self.btnUninstall.setProperty('enabled',False)
                else:
                    self.btnUninstall.setProperty('enabled',True)
            else:
                self.btnInstall.setProperty('visible',True)
                self.btnOpen.setProperty('visible',False)
                self.btnUninstall.setProperty('visible',False)
        else:
            self.scroll.setProperty('visible',True)
            self.package_exec.setProperty('visible',False)
            self.back.setProperty('visible',False)
            self.title.setProperty('visible',False)   


        if not self.act.property('text')=='':
            if self.act.property('text')=='open':
                if not self.entry=='':
                    app.start (self.entry,'')
                self.entry = ''
            elif self.act.property('text')=='uninstall':
                self.ar = Ask (f'{res.get("@string/uninstall")} {self.psel.property("text")}',res.get('@string/uninstall_message').replace('{0}',self.psel.property("text")),self.uninstall__)
            elif self.act.property('text')=='install':
                self.ar = Ask (f'Install {res.get("@string/install")}',res.get('@string/install_message').replace('{0}',self.psel.property("text")),self.install__)
            elif self.act.property('text')=='update':
                self.ar = Ask (f'Update {res.get("@string/update")}',res.get('@string/update_message').replace('{0}',self.psel.property("text")),self.install__)

        self.act.setProperty('text','')
        QTimer.singleShot(10,self.loop)

    def uninstall__(self,yes):
        if yes:
            System (f'sudo paye rm {self.psel.property("text")}')
            self.addPackageModel()
            self.psel.setProperty('text','')
        self.psel.setProperty('text','')

    def set_progressbar_value (self,value):
        self.pro.setProperty('value',value/100)
        if value == 100:
            System (f'sudo paye upak /app/cache/gets/{self.psel.property("text")}.pa')
            self.addPackageModel()
            self.psel.setProperty('text','')
            return

    def install__(self,yes):
        if yes:
            self.pro.setProperty('visible',True)
            mirror = control.read_record  ('mirror',f'/app/mirrors/{self.psel.property("text")}.manifest')
            the_url = f'{mirror}/{self.psel.property("text")}.pa'
            the_filesize = requests.get(the_url, stream=True).headers['Content-Length']
            the_filepath = f'/app/cache/gets/{self.psel.property("text")}.pa'
            the_fileobj = open(files.input(the_filepath), 'wb')
            self.downloadThread = downloadThread(the_url, the_filesize, the_fileobj, buffer=10240)
            self.downloadThread.download_proess_signal.connect(self.set_progressbar_value)
            self.downloadThread.start()

    def show_info(self):
        if res.getdata('locale')=='fa' or res.getdata('locale')=='ar':
            self.pkgName.setProperty('text',self.psel.property('text'))
            self.pkgVersion.setProperty('text',self.pselversion.property('text'))
            self.pkgBuild.setProperty('text','1400-07-08')
            self.pkgCopyright.setProperty('text',self.pselcopyright.property('text'))
            self.pkgLicense.setProperty('text',self.psellicense.property('text'))
            self.pkgUnpack.setProperty('text',self.pselunpack.property('text'))
            self.pkgMirror.setProperty('text',self.pselmirror.property('text'))

            self.pkgName1.setProperty('text',res.get('@string/package_name')+": ")
            self.pkgVersion1.setProperty('text',res.get('@string/package_version')+": ")
            self.pkgBuild1.setProperty('text',res.get('@string/bl')+": ")
            self.pkgCopyright1.setProperty('text',res.get('@string/copyright')+": ")
            self.pkgLicense1.setProperty('text',res.get('@string/license')+": ")
            self.pkgUnpack1.setProperty('text',res.get('@string/unpack')+": ")
            self.pkgMirror1.setProperty('text',res.get('@string/mirror')+": ")
        else:
            self.pkgName.setProperty('text',res.get('@string/package_name')+": ")
            self.pkgVersion.setProperty('text',res.get('@string/package_version')+": ")
            self.pkgBuild.setProperty('text',res.get('@string/bl')+": ")
            self.pkgCopyright.setProperty('text',res.get('@string/copyright')+": ")
            self.pkgLicense.setProperty('text',res.get('@string/license')+": ")
            self.pkgUnpack.setProperty('text',res.get('@string/unpack')+": ")
            self.pkgMirror.setProperty('text',res.get('@string/mirror')+": ")

            self.pkgName1.setProperty('text',self.psel.property('text'))
            self.pkgVersion1.setProperty('text',self.pselversion.property('text'))
            self.pkgBuild1.setProperty('text','1400-07-08')
            self.pkgCopyright1.setProperty('text',self.pselcopyright.property('text'))
            self.pkgLicense1.setProperty('text',self.psellicense.property('text'))
            self.pkgUnpack1.setProperty('text',self.pselunpack.property('text'))
            self.pkgMirror1.setProperty('text',self.pselmirror.property('text'))
            
        self.pkgDescription.setProperty('text',self.pseldescription.property('text'))

    def __init__(self):
        super(MainApp, self).__init__()
        System (f'sudo paye in {files.readall("/etc/paye/sources")}')
        self.addPackageModel()
        self.load (res.get('@layout/pyket'))
        self.psel = self.findChild('psel')
        self.pselnamex = self.findChild('pselnamex')
        self.pkgImage = self.findChild('pkgImage')
        self.pkgImage.setProperty('source',res.qmlget(res.etc('pyket','pkgImage')))
        self.pkgTitle = self.findChild('pkgTitle')
        self.pselcopyright = self.findChild('pselcopyright')
        self.psellicense = self.findChild('psellicense')
        self.pselunpack = self.findChild('pselunpack')
        self.pselversion = self.findChild('pselversion')
        self.pselbuild = self.findChild('pselbuild')
        self.pselmirror = self.findChild('pselmirror')
        self.pseldescription = self.findChild('pseldescription')
        self.pseltype = self.findChild('pseltype')
        self.pselinstalled = self.findChild('pselinstalled')
        self.psellogo = self.findChild('psellogo')
        self.package_exec = self.findChild('package_exec')
        self.scroll = self.findChild('scroll')
        self.back = self.findChild('back')
        self.title = self.findChild('title')
        self.btnOpen = self.findChild('btnOpen')
        self.btnOpen.setProperty('text',res.get('@string/open'))
        self.btnInstall = self.findChild('btnInstall')
        self.btnInstall.setProperty('text',res.get('@string/install'))
        self.btnUninstall = self.findChild('btnUninstall')
        self.btnUninstall.setProperty('text',res.get('@string/uninstall'))
        self.btnUpdate = self.findChild('btnUpdate')
        self.btnUpdate.setProperty('text',res.get('@string/update'))
        self.act = self.findChild('act')
        self.pro = self.findChild('pro')
        self.pkgName = self.findChild('pkgName')
        self.pkgVersion = self.findChild('pkgVersion')
        self.pkgBuild = self.findChild('pkgBuild')
        self.pkgCopyright = self.findChild('pkgCopyright')
        self.pkgLicense = self.findChild('pkgLicense')
        self.pkgUnpack = self.findChild('pkgUnpack')
        self.pkgMirror = self.findChild('pkgMirror')

        self.pkgName1 = self.findChild('pkgName1')
        self.pkgVersion1 = self.findChild('pkgVersion1')
        self.pkgBuild1 = self.findChild('pkgBuild1')
        self.pkgCopyright1 = self.findChild('pkgCopyright1')
        self.pkgLicense1 = self.findChild('pkgLicense1')
        self.pkgUnpack1 = self.findChild('pkgUnpack1')
        self.pkgMirror1 = self.findChild('pkgMirror1')

        self.pkgDescription = self.findChild('pkgDescription')

        self.setProperty('title',res.get('@string/pyket'))
        app.launchedlogo(self.property('title'), res.etc('pyket', 'logo'))
        self.loop()

application = QtGui.QGuiApplication([])
application.setWindowIcon (QIcon(res.get(res.etc('pyket','logo'))))

w = Sudo(MainApp)

application.exec()