import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
import requests,json,wget,hashlib,datetime
from requests.api import get
from pyabr.core import *

class Message:
    text = ''
    def __init__(self):
        pass

    def Write (self,text):
        self.text+=f"{text}\n"

    def Save (self):
        message = self.text.encode()

        su = files.readall('/proc/info/su')

        with open(files.input(f'/etc/external-key/Public Key.pem'), "rb") as key_file:
            public_key = serialization.load_pem_public_key(
                key_file.read(),
                backend=default_backend()
            )

        encrypted = public_key.encrypt(
            message,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )

        files.write (f'/etc/chat/{su}/Message.txt',self.text)

        f = open(files.input(f'/etc/chat/{su}/Message.bin'), 'wb')
        f.write(encrypted)
        f.close()

    def Read (self):
        su = files.readall('/proc/info/su')
        with open(files.input(f'/etc/key/{su}/Private Key.pem'), "rb") as key_file:
            private_key = serialization.load_pem_private_key(
                key_file.read(),
                password=None,
                backend=default_backend()
            )

        f = open(files.input(f'/etc/chat/{su}/Message.bin'), 'rb')
        encrypted = f.read()
        f.close()

        original_message = private_key.decrypt(
            encrypted,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )

        return original_message.decode('utf-8')

class Channel:
    host = control.read_record ("host","/etc/channel")
    upload = f'{host}/{control.read_record ("upload","/etc/channel")}'
    connect = f'{host}/{control.read_record ("connect","/etc/channel")}'
    give = f'{host}/{control.read_record ("give","/etc/channel")}'
    send = f'{host}/{control.read_record ("send","/etc/channel")}'
    public = f'{host}/{control.read_record ("public","/etc/channel")}'
    uploadprofile = f'{host}/{control.read_record ("uploadprofile","/etc/channel")}'
    update = f'{host}/{control.read_record ("update","/etc/channel")}'
    addcontact = f'{host}/{control.read_record ("addcontact","/etc/channel")}'
    contact = f'{host}/{control.read_record ("contact","/etc/channel")}'
    uploadfile =  f'{host}/{control.read_record ("uploadfile","/etc/channel")}'

    def __init__(self):
        pass

    fullname = ""
    profile = ""

    def GetUserData (self):
        if not res.getuserdata ('fullname')==None:
            self.fullname = res.getuserdata ('fullname')
        if not res.getuserdata ('profile')==None:
            self.profile = res.getuserdata ('profile')

    def Connect (self,username,password):
        su = files.readall('/proc/info/su')
        self.GetUserData()

        if not self.profile=='':
            try:
                if self.profile.startswith('@icon/'):
                    self.plink = requests.post(self.uploadprofile, files={'profile':open(res.get(self.profile),'rb')})
                else:
                    self.plink = requests.post(self.uploadprofile, files={'profile':open(files.input(self.profile),'rb')})
                self.plink = self.plink.text

            except:
                self.plink = ''

        x = requests.post(self.upload,files = {'message': open(f'/stor/etc/key/{su}/Public Key.pem', 'rb')})
        if x.text=='1':
            print(self.fullname)
            x = requests.post(self.connect,data={'username':username,'password':password,"fullname":self.fullname,"profile":self.plink})
            if x.text=='1':
                files.create ('/tmp/chat-success.tmp')
                files.write (f'/etc/chat/{su}/user',username)
                files.write (f'/etc/chat/{su}/pass',password)
            else:
                colors.show ('chat','fail',f'{username}: something went wrong.')
        else:
            colors.show ('chat','fail',f'error while uploading public key.')

    def Key (self,username):
        x = requests.post(f'{self.public}',data={'username':username})
        wget.download(f'{self.host}/{x.text}',files.input(f'/etc/external-key/Public Key.pem'))

    def AddContact (self,username):
        su = files.readall('/proc/info/su')
        requests.post(f'{self.addcontact}',data={'username':username,'me':files.readall(f'/etc/chat/{su}/user'),'password':files.readall(f'/etc/chat/{su}/pass')})

    def Send (self,giver):
        su = files.readall('/proc/info/su')
        x = requests.post(self.upload,files = {'message': open(files.input(f'/etc/chat/{su}/Message.bin'), 'rb')})
        if not x.text=='0':
            x = requests.post(self.send,data={'sender':files.readall(f'/etc/chat/{su}/user'),'giver':giver,'password':files.readall(f'/etc/chat/{su}/pass')})
            if not x.text=='0':
                files.copy (f'/etc/chat/{su}/Message.txt',f'/etc/chat/{su}/{x.text.replace("chats/","")}')
            else:
                colors.show ('chat','fail',f'error while error.')
        else:
            colors.show ('chat','fail',f'error while uploading.')

    def Give (self,giver):
        su = files.readall('/proc/info/su')
        x = requests.post(self.give,data={'sender':files.readall(f'/etc/chat/{su}/user'),'giver':giver,'password':files.readall(f'/etc/chat/{su}/pass')})
        x = json.loads(x.text)

        m = Message()

        for i in x:
            if not i['sender']==files.readall(f'/etc/chat/{su}/user'):
                try:
                    os.remove(files.input(f'/etc/chat/{su}/Message.bin'))
                except:
                    pass
                wget.download(f'{self.host}/{i["data"]}',files.input(f'/etc/chat/{su}/Message.bin'))
                i['data']=m.Read()
            else:
                i['data']=files.readall(f'/etc/chat/{su}/{i["data"].replace("chats/","")}')

        return x

    def Contacts (self):
        su = files.readall('/proc/info/su')

        x = requests.post(self.contact,data={'username':files.readall(f'/etc/chat/{su}/user'),'password':files.readall(f'/etc/chat/{su}/pass')})

        try:
            return json.loads(x.text)
        except:
            return []

    def File (self,filename,giver):
        self.x = requests.post(self.uploadfile, files={'file':open(files.input(filename),'rb')})

        if not self.x.text == '0':
            m = Message()
            m.Write(filename)
            m.Save()

            self.Send(giver)
        else:
            colors.show ('chat','fail',f'error while uploading.')