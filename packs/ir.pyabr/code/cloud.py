from pyabr.core import *
import requests, wget

class Account:
    username = ''
    password = ''

    # Create an Online Account
    # uadd -i mani
    # Enter password: mani

    host = control.read_record('host','/etc/cloud')
    createbackend = control.read_record('create','/etc/cloud')
    uploadbackend = control.read_record('upload','/etc/cloud')
    publickeybackend = control.read_record('publickey','/etc/cloud')
    connectbackend = control.read_record('connect','/etc/cloud')
    acceptbackend = control.read_record('accept','/etc/cloud')
    linkbackend = control.read_record('link','/etc/cloud')
    unlinkbackend = control.read_record('unlink','/etc/cloud')

    def Create(self,username,password):
        
        self.user = files.readall('/proc/info/su')
        self.x = requests.post(f'{self.host}/{self.createbackend}', data={'username': username, 'password': password})
        self.username = username
        self.password = password

        if self.x.text=='S':
            self.x = requests.post(f'{self.host}/{self.uploadbackend}',
                                   files={'file': open(f'/stor/etc/key/{self.user}/Public Key.pem', 'rb')})
            if self.x.text == 'S':
                self.x = requests.post(f'{self.host}/{self.publickeybackend}',
                                       data={'username': username, 'password': password})
                
                files.write(f'/etc/key/{self.user}/user',username)
                files.write(f'/etc/key/{self.user}/pass',password)

        return self.x.text

    # Connect to an Online Account
    # uadd -i mani
    # Enter password: mani
    def Connect (self,username,password):
        self.user = files.readall('/proc/info/su')
        self.x = requests.post(f'{self.host}/{self.connectbackend}',data={"username":username,"password":password})

        if self.x.text=='S':
            files.write(f'/etc/key/{self.user}/user', username)
            files.write(f'/etc/key/{self.user}/pass', password)


        return self.x.text

class Drive:
    username = ''
    password = ''

    host = control.read_record('host','/etc/cloud')
    createbackend = control.read_record('create','/etc/cloud')
    uploadbackend = control.read_record('upload','/etc/cloud')
    publickeybackend = control.read_record('publickey','/etc/cloud')
    connectbackend = control.read_record('connect','/etc/cloud')
    acceptbackend = control.read_record('accept','/etc/cloud')
    linkbackend = control.read_record('link','/etc/cloud')
    unlinkbackend = control.read_record('unlink','/etc/cloud')

    # Connect to drive
    # sync
    def __init__(self):
        self.user = files.readall('/proc/info/su')

        if files.isfile(f'/etc/key/{self.user}/user') and files.isfile(f'/etc/key/{self.user}/pass'):
            username = files.readall(f'/etc/key/{self.user}/user')
            password = files.readall(f'/etc/key/{self.user}/pass')

            account = Account()
            connect = account.Connect(username,password)

            if connect=='S':
                self.username = username
                self.password = password

    # Upload to drive
    # up /readme.txt
    def Upload (self,filename):
        self.x = requests.post(f'{self.host}/{self.uploadbackend}', files={'file':open(files.input(filename),'rb')})

        if self.x.text=='S':
            self.x = requests.post(f'{self.host}/{self.acceptbackend}',data={'name':files.output(filename),'username':self.username,'password':self.password})

        return self.x.text

    # Generate link from drive
    # ln /readme.txt
    def Link (self,filename):
        self.x = requests.post(f'{self.host}/{self.linkbackend}',data={'name':files.output(filename),'username':self.username,'password':self.password})

        return f'{self.host}/{self.x.text}'

    # Download file from drive
    # down /readme.txt
    def Download(self, filename):
        try:
            if files.isfile(filename):
                files.remove(filename)
            wget.download(self.Link(filename), files.input(filename))
        except:
            pass

    # Unlink (Remove) file from drive
    # uln /readme.txt
    def Unlink (self,filename):
        self.x = requests.post(f'{self.host}/{self.unlinkbackend}',
                               data={'name': files.output(filename), 'username': self.username,
                                     'password': self.password})

        return self.x.text

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

class Repo:
    repo = control.read_record('repo','/etc/cloud')
    push = control.read_record('push','/etc/cloud')
    host = control.read_record('host','/etc/cloud')
    createbackend = control.read_record('create','/etc/cloud')
    uploadbackend = control.read_record('upload','/etc/cloud')
    publickeybackend = control.read_record('publickey','/etc/cloud')
    connectbackend = control.read_record('connect','/etc/cloud')
    acceptbackend = control.read_record('accept','/etc/cloud')
    linkbackend = control.read_record('link','/etc/cloud')
    unlinkbackend = control.read_record('unlink','/etc/cloud')
    username = ''
    password = ''
    package = ''

    def __init__(self,package):
        self.package = package
        self.user = files.readall('/proc/info/su')

        if files.isfile(f'/etc/key/{self.user}/user') and files.isfile(f'/etc/key/{self.user}/pass'):
            username = files.readall(f'/etc/key/{self.user}/user')
            password = files.readall(f'/etc/key/{self.user}/pass')

            account = Account()
            connect = account.Connect(username,password)

            if connect=='S':
                self.username = username
                self.password = password

    # Can create package width this name
    def CanCreate (self):
        try:
            second = self.package.split('.')[1]
            self.x = requests.post(f'{self.host}/{self.repo}',data={'name':self.package})

            if self.x.text=='S':
                return True
            else:
                return False
        except:
            return False

    def Push (self):
        self.x = requests.post(f'{self.host}/{self.uploadbackend}', files={'file':open(files.input(self.package+".pa"),'rb')})

        if self.x.text=='S':
            self.x = requests.post(f'{self.host}/{self.push}',data={'name':self.package,'username':self.username,'password':self.password})
                
        return self.x.text

class Mail:
    username = ''
    password = ''
    host     = control.read_record('host','/etc/cloud')
    send     = control.read_record('send','/etc/cloud')
    getkey   = control.read_record('getkey','/etc/cloud')
    give     = control.read_record('give','/etc/cloud')
    inbox    = control.read_record('inbox','/etc/cloud')
    uploadbackend = control.read_record('upload','/etc/cloud')
    data     = ''
    subject  = ''

    def __init__(self):
        self.user = files.readall('/proc/info/su')

        if files.isfile(f'/etc/key/{self.user}/user') and files.isfile(f'/etc/key/{self.user}/pass'):
            username = files.readall(f'/etc/key/{self.user}/user')
            password = files.readall(f'/etc/key/{self.user}/pass')

            account = Account()
            connect = account.Connect(username,password)

            if connect=='S':
                self.username = username
                self.password = password
                
    def GetKey (self,username):
        self.x = requests.post(f'{self.host}/{self.getkey}',data={'username':username})

        if self.x.text.startswith('E'):
            return self.x.text
        else:
            return f"{self.host}/{self.x.text}"

    def Write (self,text):
        self.data += text

    def Subject (self,subject):
        self.subject = subject

    def Send (self,giver):
        # get public key of giver
        self.x = self.GetKey(giver)

        if not self.x.startswith('E'):
            # Download giver public key
            wget.download(self.x,files.input("/etc/external-key/Public Key.pem"))

            # Write Mail
            m = Message()
            m.Write(self.data)
            m.Save()

            self.x = requests.post(f'{self.host}/{self.uploadbackend}', files={'file':open(files.input('/etc/external-key/Message.bin'),'rb')})

            if self.x.text=='S':
                self.x = requests.post(f'{self.host}/{self.send}',data={'sender':self.username,'giver':giver,'subject':self.subject,'password':self.password})
            print (self.x.text)
        return self.x

    def Inbox (self):
        self.x = requests.post(f'{self.host}/{self.inbox}',data={'username':self.username,'password':self.password})
        return self.x.text

class Notifications:
    username = ''
    password = ''
    host     = control.read_record('host','/etc/cloud')
    notif      = control.read_record('notif','/etc/cloud')

    def __init__(self):
        self.user = files.readall('/proc/info/su')

        if files.isfile(f'/etc/key/{self.user}/user') and files.isfile(f'/etc/key/{self.user}/pass'):
            username = files.readall(f'/etc/key/{self.user}/user')
            password = files.readall(f'/etc/key/{self.user}/pass')

            account = Account()
            connect = account.Connect(username,password)

            if connect=='S':
                self.username = username
                self.password = password

    def Show (self):
        self.x = requests.post(f'{self.host}/{self.notif}',data={'username':self.username,'password':self.password})

        return self.x.text