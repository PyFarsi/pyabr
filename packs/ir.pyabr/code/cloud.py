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
import requests,wget

class Drive:
    host = control.read_record ('host','/etc/cloud')
    connect = f'{host}/{control.read_record ("connect","/etc/cloud")}'
    upload = f'{host}/{control.read_record ("upload","/etc/cloud")}'
    accept = f'{host}/{control.read_record ("accept","/etc/cloud")}'
    link = f'{host}/{control.read_record ("link","/etc/cloud")}'

    username = ''
    password = ''

    # Init
    def __init__(self):
        su = files.readall('/proc/info/su')
        try:
            self.username = files.readall(f'/etc/drive/{su}/user')
            self.password = files.readall(f'/etc/drive/{su}/pass')
        except:
            pass

    # Connect or Create user
    def Connect (self,username,password):
        self.x = requests.post(self.connect,data={'username':username,'password':password})

        su = files.readall('/proc/info/su')

        if self.x.text == '1':
            files.write (f'/etc/drive/{su}/user',username)
            files.write (f'/etc/drive/{su}/pass',password)
            self.username = username
            self.password = password
        else:
            colors.show ('cloud','fail',f'user already exists.')

    # Upload a file
    def Upload (self,filename):
        self.x = requests.post(self.upload, files={'file':open(files.input(filename),'rb')})

        if self.x.text=='1':
            self.x = requests.post(self.accept,data={'name':files.output(filename),'username':self.username,'password':self.password})

            if self.x.text=='1':
                pass
            else:
                colors.show ('cloud','fail',f'error while accepting file.')
        else:
            colors.show ('cloud','fail',f'error while uploading file.')

    # Get a direct and shared link
    def Link (self,filename):
        self.x = requests.post(self.link,data={'name':files.output(filename),'username':self.username,'password':self.password})

        return f'{self.host}/{self.x.text}'

    # Download a file from cloud
    def Download (self,filename):
        try:
            if files.isfile (filename): files.remove(filename)
            wget.download(self.Link(filename),files.input(filename))
        except:
            pass

# CNS = Cloud Name Server
class Domain ():
    def __init__(self,url):

        # check syntax
        if not url.startswith('abr://'):
            colors.show ('cloud','fail',f'{url}: wrong syntax of URL.')
            exit()

        # splitors 
        # abr://pyabr.ir/index.qml

        spl = url.split('://')[1].split('/')
        domain = spl[0]
        path = ''
        if spl[1:]==[]:
            path = '/index.qml'
        else: 
            for i in spl[1:]:
                path += f'/{i}'

        # check domain
        if not files.isfile (f'/etc/domain/{domain}'):
            colors.show ('cloud','fail',f'{domain}: domain not found.')
            exit()

        # requesting
        if files.isfile ('/usr/share/layouts/debug.qml'): files.remove ('/usr/share/layouts/debug.qml')
        wget.download(f"{files.readall(f'/etc/domain/{domain}')}/{path}",files.input("/usr/share/layouts/debug.qml"))

        app.start ('debug','')