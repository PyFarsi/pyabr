import os
import requests,json,hashlib,datetime
from requests.api import get
from pyabr.core import *

class Channel:
    host = control.read_record('host','/etc/channel')
    send = control.read_record('send','/etc/channel')
    get = control.read_record('get','/etc/channel')
    connect = control.read_record('connect','/etc/channel')
    addcontact = control.read_record('addcontact','/etc/channel')
    contact = control.read_record('contact','/etc/channel')
    clear = control.read_record('clear','/etc/channel')
    delete = control.read_record('del','/etc/channel')
    delchat = control.read_record('delchat','/etc/channel')

    username = ''
    password = ''

    def __init__(self):
        super(Channel,self).__init__()
        su = files.readall ('/proc/info/su')

        try:
            self.username = files.readall (f'/etc/chat/{su}/user')
            self.password = files.readall (f'/etc/chat/{su}/pass')
        except:
            pass

    def Connect (self,username,password):
        # fullname
        su = files.readall ('/proc/info/su')
        fullname = control.read_record ('fullname',f'/etc/users/{su}')
        if fullname == None: fullname = username

        # save username & password
        files.write (f'/etc/chat/{su}/user',username)
        files.write (f'/etc/chat/{su}/pass',password)

        self.username = username
        self.password = password

        # connect
        x = requests.post (f'{self.host}/{self.connect}',data={"username":username,"password":password,"fullname":fullname})
        return x.text

    def Send (self,giver,data):
        x = requests.post(f'{self.host}/{self.send}',data={"sender":self.username,"giver":giver,"password":self.password,"data":data})
        return x.text

    def AddContact (self,username):
        x = requests.post(f'{self.host}/{self.addcontact}',data={"me":self.username,"username":username,"password":self.password})
        return x.text

    def Get (self,giver):
        x = requests.post(f'{self.host}/{self.get}',data={"sender":self.username,"giver":giver,"password":self.password})
        try:
            return json.loads(x.text)
        except:
            return []

    def Contacts (self):
        x = requests.post(f'{self.host}/{self.contact}',data={"username":self.username,"password":self.password})
        try:
            return json.loads(x.text)
        except:
            return []

    def Clear (self,giver):
        x = requests.post(f'{self.host}/{self.clear}',data={"sender":self.username,"password":self.password,"giver":giver})
        return x.text

    def DeleteChat (self,giver):
        x = requests.post(f'{self.host}/{self.delchat}',data={"sender":self.username,"password":self.password,"giver":giver})
        return x.text

    def Delete (self,id):
        x = requests.post(f'{self.host}/{self.delete}',data={"username":self.username,"password":self.password,"id":str(id)})
        return x.text