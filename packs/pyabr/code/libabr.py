'''
    Pyabr OS

    Python Cloud Operating System Platform (c) 2021 PyFarsi. Free Software GNU General Public License v3.0

    - Informations

    * Name:             Pyabr
    * Founder:          Mani Jamali
    * Developers:       PyFarsi Community
    * Package Manager:  Paye, Apt, Dpkg, PyPI
    * License:          GNU General Publice License v3.0

    * Source code:      https://github.com/PyFarsi/pyabr
    * PyPI:             https://pypi.org/project/pyabr

    - Download Pyabr OS

    * AMD64, Intel64:   https://dl.pyabr.ir/pyabr-x86_64.iso     
    * ARM64:            https://dl.pyabr.ir/pyabr-arm64.img
    * Platform:         https://dl.pyabr.ir/stor.sb
    * Wheel Package:    https://dl.pyabr.ir/pyabr.whl
    
    - Channels:

    * Official Website: https://pyabr.ir
    * Telegram Channel: https://t.me/pyfarsi
    * Gap Channel:      https://gap.im/pyabr
    * Sorosh Channel:   https://splus.ir/pyabr
    * Instagram:        https://instagram.com/pyabrir
    * Hoorsa:           https://hoorsa.com/pyabr
    * Aparat:           https://aparat.com/pyabr

'''

import importlib, shutil, os, sys, hashlib, subprocess,time,datetime,getpass,py_compile,wget,requests,random
from termcolor import colored
def read_record (name,filename):
    file = open (filename,"r")
    strv = (file.read()).split("\n")
    file.close()

    for i in strv:
        if i.startswith(name):
            i = i.split(": ")
            if i[0]==(name):
                return i[1]

def read_list (filename):
    file = open (filename,"r")
    strv = (file.read()).split("\n")
    file.close()
    return strv

def write_record(name, value, filename):
    file = open (filename,'r')
    all = file.read()
    file.close()
    record = read_record(name, filename)
    os.remove(filename)
    if not (record == None):
        all = all.replace(f"\n{name}: {record}", "")
    file = open(filename,'w')
    file.write(f"{all}\n{name}: {value}")
    file.close()

# script #
class Script:
    def __init__(self,filename):
        permissions = Permissions()
        colors = Colors()
        files = Files()
        control = Control()

        # check perms #
        if not permissions.check(f'{files.output(filename)}.sa', "x", files.readall("/proc/info/su")):
            colors.show(filename, "perm", "")
            sys.exit(0)

        k = 0

        for cmd in  control.read_list(f'{filename}.sa'):
            k += 1
            ## Create cmdln with variables ##

            cmdln = cmd.split(" ")

            strcmdln = ""

            for i in cmdln:
                if str(i).startswith("$"):
                    select = files.readall("/proc/info/sel")
                    var = control.read_record(str(i).replace("$", ""), select)
                    if var == None:
                        strcmdln  += f" {i}"
                    else:
                        strcmdln  += f" {var}"
                else:
                    strcmdln  += f" {i}"

            cmdln = strcmdln.split(" ")
            cmdln.remove('')

            cmd = ""
            for j in cmdln:
                cmd  += f" {j}"

            if (cmdln == [] or cmdln[0].startswith("#")):
                continue
            elif hasattr(Commands, cmdln[0]):
                cmd = Commands()
                getattr(cmd, cmdln[0])(cmdln[1:])
            else:
                System(cmd)
# commands #
class Commands:
    def __init__(self):
        pass

    # start #
    
    def start (self,args):
        files = Files()
        colors = Colors()
        if args==[]:
            colors.show ('start','fail','no inputs.')
            sys.exit(0)
        if files.isfile (f'/usr/share/applications/{args[0]}.desk'):
            files.write('/tmp/start.tmp',args[0])
        else:
            colors.show('start', 'fail', f'{args[0]}: application not found.')

    def cl (self,args):
        files = Files()
        colors = Colors()

        if args==[]:
            colors.show ('cl','fail','no inputs.')
            sys.exit(0)

        files.write('/tmp/cloud.tmp',args[0])

    # kill process #
    def kill (self,args):
        colors = Colors()
        app = App()
        for i in args:
            if app.check(i):
                app.end(i)
            else:
                colors.show ('kill','fail',f'{i}: id process not found.')

    # un set a variable
    def unset(self,args):
        files = Files()
        colors = Colors()
        control = Control()
        permissions = Permissions()

        for name in args:
            if not (files.readall("/proc/info/sel")).startswith("/proc/"):
                if permissions.check(files.output(files.readall("/proc/info/sel")), "w", files.readall("/proc/info/su")):
                    control.remove_record(name, files.readall("/proc/info/sel"))
                else:
                    colors.show("unset", "perm", "")
            else:
                control.remove_record(name, files.readall("/proc/info/sel"))

    # pause
    def pause (self,args):

        self.sleep(['1000000'])

    # add controller data base
    def add (self,args):
        files = Files()
        for i in args:
            x = (files.readall(i)).split('\n')
            for j in x:
                if j.__contains__(': '):
                    s = j.split(': ')
                    self.set([f'{s[0]}:',s[1]])
    # zip #
    def zip (self, args):
        files = Files()
        colors = Colors()
        permissions = Permissions()
        if args==[]:
            colors.show ('zip','fail','no inputs.')
            sys.exit(0)

        src = args[0]

        if args[1:]==[]:
            dest = src
        else:
            dest = args[1]

        if not files.isdir (src):
            colors.show('zip', 'fail', f'{src}: source directory not found.')
            sys.exit(0)

        if files.isdir (f"{dest}.zip"):
            colors.show('zip', 'fail', f'{dest}.zip: dest is not a archive file.')
            sys.exit(0)

        if files.isfile (f"{dest}.zip"):
            colors.show('zip', 'warning', f'{dest}.zip: dest archives exists.')

        if permissions.check(files.output(src), "r", files.readall("/proc/info/su")) and permissions.check(files.output(f'{dest}.zip'), "w", files.readall("/proc/info/su")):
            shutil.make_archive(files.input(dest),'zip',files.input(src))
        else:
            colors.show('zip', 'perm', '')
            sys.exit(0)

    # zip #
    def tar (self, args):
        files = Files()
        colors = Colors()
        permissions = Permissions()

        if args==[]:
            colors.show ('tar','fail','no inputs.')
            sys.exit(0)

        src = args[0]

        if args[1:]==[]:
            dest = src
        else:
            dest = args[1]

        if not files.isdir (src):
            colors.show('tar', 'fail', f'{src}: source directory not found.')
            sys.exit(0)

        if files.isdir (f"{dest}.tar"):
            colors.show('tar', 'fail', f'{dest}.tar: dest is not a archive file.')
            sys.exit(0)

        if files.isfile (f"{dest}.tar"):
            colors.show('tar', 'warning', f'{dest}.tar: dest archives exists.')

        if permissions.check(files.output(src), "r", files.readall("/proc/info/su")) and permissions.check(files.output(f'{dest}.tar'), "w", files.readall("/proc/info/su")):
            shutil.make_archive(files.input(dest),'tar',files.input(src))
        else:
            colors.show('tar', 'perm', '')
            sys.exit(0)

    # pwd #
    def pwd (self,args):
        files = Files()

        print (files.readall('/proc/info/pwd'))

    def send (self,args):
        sms = Message()
        if args==[] or args[1:]==[]:
            args =  [input ('Enter giver id: '),input ('Type your message: ')]
        sms.send(args[0],args[1])

    def receive (self,args):
        sms = Message()
        sms.receive()

    # zip #
    def xzip (self, args):
        files = Files()
        colors = Colors()
        permissions = Permissions()

        if args==[]:
            colors.show ('xzip','fail','no inputs.')
            sys.exit(0)

        src = args[0]

        if args[1:]==[]:
            dest = src
        else:
            dest = args[1]

        if not files.isdir (src):
            colors.show('xzip', 'fail', f'{src}: source directory not found.')
            sys.exit(0)

        if files.isdir (f"{dest}.tar.xz"):
            colors.show('xzip', 'fail', f'{dest}.tar.xz: dest is not a archive file.')
            sys.exit(0)

        if files.isfile (f"{dest}.tar.xz"):
            colors.show('xzip', 'warning', f'{dest}.tar.xz: dest archives exists.')

        if permissions.check(files.output(src), "r", files.readall("/proc/info/su")) and permissions.check(files.output(f'{dest}.tar.xz'), "w", files.readall("/proc/info/su")):
            shutil.make_archive(files.input(dest),'xztar',files.input(src))
        else:
            colors.show('xzip', 'perm', '')
            sys.exit(0)

    # zip #
    def gzip (self, args):
        files = Files()
        colors = Colors()
        permissions = Permissions()
        if args==[]:
            colors.show ('gzip','fail','no inputs.')
            sys.exit(0)

        src = args[0]

        if args[1:]==[]:
            dest = src
        else:
            dest = args[1]

        if not files.isdir (src):
            colors.show('gzip', 'fail', f'{src}: source directory not found.')
            sys.exit(0)

        if files.isdir (f"{dest}.tar.gz"):
            colors.show('gzip', 'fail', f'{dest}.tar.gz: dest is not a archive file.')
            sys.exit(0)

        if files.isfile (f"{dest}.tar.gz"):
            colors.show('gzip', 'warning', f'{dest}.tar.gz: dest archive exists.')

        if permissions.check(files.output(src), "r", files.readall("/proc/info/su")) and permissions.check(files.output(f'{dest}.tar.gz'), "w", files.readall("/proc/info/su")):
            shutil.make_archive(files.input(dest),'gztar',files.input(src))
        else:
            colors.show('gzip', 'perm', '')
            sys.exit(0)

    # zip #
    def bzip (self, args):
        files = Files()
        colors = Colors()
        permissions = Permissions()

        if args==[]:
            colors.show ('bzip','fail','no inputs.')
            sys.exit(0)

        src = args[0]

        if args[1:]==[]:
            dest = src
        else:
            dest = args[1]

        if not files.isdir (src):
            colors.show('bzip', 'fail', f'{src}: source directory not found.')
            sys.exit(0)

        if files.isdir (f"{dest}.tar.bz2"):
            colors.show('bzip', 'fail', f'{dest}.tar.bz2: dest is not a archive file.')
            sys.exit(0)

        if files.isfile (f"{dest}.tar.bz2"):
            colors.show('bzip', 'warning', f'{dest}.tar.bz2: dest archive exists.')

        if permissions.check(files.output(src), "r", files.readall("/proc/info/su")) and permissions.check(files.output(f'{dest}.tar.bz2'), "w", files.readall("/proc/info/su")):
            shutil.make_archive(files.input(dest),'bztar',files.input(src))
        else:
            colors.show('bzip', 'perm', '')
            sys.exit(0)

    def unzip (self,args):
        files = Files()
        colors = Colors()
        permissions = Permissions()

        if args == []:
            colors.show('unzip', 'fail', 'no inputs.')
            sys.exit(0)

        src = args[0]

        if args[1:]==[]:
            dest = src
        else:
            dest = args[1]

        if not files.isfile (src):
            colors.show('unzip', 'fail', f'{src}: source archive not found.')
            sys.exit(0)

        if files.isfile (dest):
            colors.show('unzip', 'fail', f'{dest}: dest is a file.')
            sys.exit(0)

        if permissions.check(files.output(src), "r", files.readall("/proc/info/su")) and permissions.check(files.output(dest), "w", files.readall("/proc/info/su")):
            shutil.unpack_archive(files.input(src),files.input(dest),'zip')
        else:
            colors.show('unzip', 'perm', '')
            sys.exit(0)

    def xunzip (self, args):
        files = Files()
        colors = Colors()
        permissions = Permissions()
        if args == []:
            colors.show('xunzip', 'fail', 'no inputs.')
            sys.exit(0)

        src = args[0]

        if args[1:] == []:
            dest = src
        else:
            dest = args[1]

        if not files.isfile(src):
            colors.show('xunzip', 'fail', f'{src}: source archive not found.')
            sys.exit(0)

        if files.isfile(dest):
            colors.show('xunzip', 'fail', f'{dest}: dest is a file.')
            sys.exit(0)

        if permissions.check(files.output(src), "r", files.readall("/proc/info/su")) and permissions.check(
                files.output(dest), "w", files.readall("/proc/info/su")):
            shutil.unpack_archive(files.input(src), files.input(dest), 'xztar')
        else:
            colors.show('xunzip', 'perm', '')
            sys.exit(0)

    def gunzip(self, args):
        files = Files()
        colors = Colors()
        permissions = Permissions()

        if args == []:
            colors.show('gunzip', 'fail', 'no inputs.')
            sys.exit(0)

        src = args[0]

        if args[1:] == []:
            dest = src
        else:
            dest = args[1]

        if not files.isfile(src):
            colors.show('gunzip', 'fail', f'{src}: source archive not found.')
            sys.exit(0)

        if files.isfile(dest):
            colors.show('gunzip', 'fail', f'{dest}: dest is a file.')
            sys.exit(0)

        if permissions.check(files.output(src), "r", files.readall("/proc/info/su")) and permissions.check(
                files.output(dest), "w", files.readall("/proc/info/su")):
            shutil.unpack_archive(files.input(src), files.input(dest), 'gztar')
        else:
            colors.show('gunzip', 'perm', '')
            sys.exit(0)

    def bunzip(self, args):
        files = Files()
        colors = Colors()
        permissions = Permissions()
        if args == []:
            colors.show('bunzip', 'fail', 'no inputs.')
            sys.exit(0)

        src = args[0]

        if args[1:] == []:
            dest = src
        else:
            dest = args[1]

        if not files.isfile(src):
            colors.show('bunzip', 'fail', f'{src}: source archive not found.')
            sys.exit(0)

        if files.isfile(dest):
            colors.show('bunzip', 'fail', f'{dest}: dest is a file.')
            sys.exit(0)

        if permissions.check(files.output(src), "r", files.readall("/proc/info/su")) and permissions.check(
                files.output(dest), "w", files.readall("/proc/info/su")):
            shutil.unpack_archive(files.input(src), files.input(dest), 'bztar')
        else:
            colors.show('bunzip', 'perm', '')
            sys.exit(0)

    def untar(self, args):
        files = Files()
        colors = Colors()
        permissions = Permissions()

        if args == []:
            colors.show('untar', 'fail', 'no inputs.')
            sys.exit(0)

        src = args[0]

        if args[1:] == []:
            dest = src
        else:
            dest = args[1]

        if not files.isfile(src):
            colors.show('untar', 'fail', f'{src}: source archive not found.')
            sys.exit(0)

        if files.isfile(dest):
            colors.show('untar', 'fail', f'{dest}: dest is a file.')
            sys.exit(0)

        if permissions.check(files.output(src), "r", files.readall("/proc/info/su")) and permissions.check(
                files.output(dest), "w", files.readall("/proc/info/su")):
            shutil.unpack_archive(files.input(src), files.input(dest), 'tar')
        else:
            colors.show('untar', 'perm', '')
            sys.exit(0)

    # cc command #
    def cc (self,args):
        files = Files()
        colors = Colors()
        permissions = Permissions()
        if args==[]:
            colors.show('cc','fail','no inputs.')
            sys.exit(0)

        # args after checking #
        filename = args[0]
        # check file #
        if not files.isfile (filename):
            colors.show ('cc','fail',f"{filename}: file not found.")
            sys.exit(0)

        if files.isdir (filename):
            colors.show('cc','fail',f"{filename}: is a directory.")
            sys.exit(0)

        # check permission of filename to read #
        if not permissions.check(files.output(filename), "r", files.readall("/proc/info/su")):
            colors.show('cc','perm','')
            sys.exit(0)

        # compile types #
        if args[1:]==[]:
            py_compile.compile(files.input(filename),files.input(filename.replace('.py','.pyc')))
            if not permissions.check(files.output(filename.replace('.py','.pyc')), "w", files.readall("/proc/info/su")):
                colors.show('cc', 'perm', '')
                sys.exit(0)
        else:
            output = args[1]
            if not permissions.check(files.output(output), "w", files.readall("/proc/info/su")):
                colors.show('cc', 'perm', '')
                sys.exit(0)
            py_compile.compile(files.input(filename), files.input(output))


    # check command #
    def check (self,args):
        files = Files()
        colors = Colors()
        permissions = Permissions()

        filename = args[0]

        perm = permissions.get_permissions(files.output(filename))
        numperm = permissions.show_number(perm)
        r = permissions.check(files.output(filename), "r", files.readall("/proc/info/su"))
        w = permissions.check(files.output(filename), "w", files.readall("/proc/info/su"))
        x = permissions.check(files.output(filename), "x", files.readall("/proc/info/su"))


        print(f"   Seleted path: {files.output(filename)}")
        print(f"     Permission: {perm}" )
        print(f" Permission Num: {str(numperm)}" )
        if r == True:
            print("           Read: Yes")
        else:
            print("           Read: No" )

        if w == True:
            print("          Write: Yes" )
        else:
            print("          Write: No")

        if x == True:
            print("        Execute: Yes")
        else:
            print("        Execute: No")

    # chmod command #
    def chmod (self,args):
        files = Files()
        colors = Colors()
        permissions = Permissions()

        mod = args[0]
        filename = args[1]

        if args==[] or args[1:]==[]:
            colors.show("chmod", "fail", "no inputs.")
            sys.exit(0)

        perm_user = int(mod[0])
        perm_others = int(mod[1])
        perm_guest = int(mod[2])
        if permissions.check_owner(files.output(filename), files.readall("/proc/info/su")):
            owner = permissions.get_owner(files.output(filename))
            permissions.create(files.output(filename), perm_user, perm_others, perm_guest, owner)
        else:
            colors.show("chmod", "perm", "")

    def mount (self,args):
        files = Files()
        colors = Colors()
        control = Control()
        permissions = Permissions()
        commands = Commands()

        if not permissions.check_root(files.readall('/proc/info/su')):
            if not files.readall('/proc/info/su') in files.readall('/etc/sudoers'):
                colors.show("mount", "perm", "")
                sys.exit(0)

        if args==[]:
            colors.show("mount", "fail", "no inputs.")
            sys.exit(0)

        clouddrive = args[0]

        if not files.isfile(f'/dev/{clouddrive}'):
            colors.show("mount", "fail", f"{clouddrive}: cloud drive not exists.")
            sys.exit(0)

        clouddrivez = f'/dev/{clouddrive}'


        host = control.read_record('host',clouddrivez)
        password = control.read_record('password', clouddrivez)

        x = requests.post(f"{host}/check.php",data={"password":password})

        if x.text.__contains__('s: connected'):
            if files.isdir (f'/stor/{clouddrive}'):
                files.removedirs(f'/stor/{clouddrive}')

            files.mkdir(f'/stor/{clouddrive}')
            commands.cd([f'/stor/{clouddrive}'])
            files.write('/proc/info/csel',clouddrive)

            x = requests.post(f"{host}/list.php",data={"password":password})

            split_list_items = str(x.text).split('\n')
            if '' in split_list_items:
                split_list_items.remove('')

            split_list_items.reverse()

            for item in split_list_items:
                split_remove_host = item.split("/stor/")
                try:
                    myitem = split_remove_host[1]

                    if myitem.endswith ('/') and not files.isdir (f'/stor/{clouddrive}/{myitem}'):
                        files.mkdir(f'/stor/{clouddrive}/{myitem}')
                    else:
                        files.create(f'/stor/{clouddrive}/{myitem}')
                except:
                    pass

        elif 'e: wrong password' in x.text:
            colors.show("mount", "fail", f"{clouddrive}: wrong password in device database.")
        elif 'e: empty password' in x.text:
            colors.show("mount", "fail", f"{clouddrive}: empty password in device database.")
        else:
            colors.show("mount", "fail", f"{clouddrive}: cannot connect to this cloud drive.")

    def get (self,args):
        files = Files()
        colors = Colors()
        control = Control()

        if args==[]:
            colors.show("get", "fail", "no inputs.")
            sys.exit(0)

        url = args[0].split('/')
        addressz = url[0]
        try:
            dataz = url[1]
        except:
            dataz = 'index.xml'

        x = requests.post(f"{control.read_record('zone','/etc/cloud')}", data={"address": addressz,"data":dataz})

        if x.text=='e: data not found':
            colors.show('get', 'fail', f'{dataz}: data not found.')
        elif x.text=='e: address not found':
            colors.show('get', 'fail', f'{addressz}: address not found.')
        else:
            if not files.isdir(f'/srv/{addressz}'):
                files.mkdir(f'/srv/{addressz}')

            try:
                files.write(f'/srv/{addressz}/{dataz}',x.text)
            except:
                pass

    def umount (self,args):
        files = Files()
        colors = Colors()
        permissions = Permissions()
        commands = Commands()


        if not permissions.check_root(files.readall('/proc/info/su')):
            if not files.readall('/proc/info/su') in files.readall('/etc/sudoers'):
                colors.show("umount", "perm", "")
                sys.exit(0)

        if args == []:
            colors.show("umount", "fail", "no inputs.")
            sys.exit(0)

        clouddrive = args[0]

        if not files.isfile(f'/dev/{clouddrive}'):
            colors.show("umount", "fail", f"{clouddrive}: cloud drive not exists.")
            sys.exit(0)

        commands.cd (['/'])
        files.removedirs(f'/stor/{clouddrive}')

    # down mani:/Files/mani

    def down (self,args):
        files = Files()
        colors = Colors()
        control = Control()
        permissions = Permissions()


        if not permissions.check_root(files.readall('/proc/info/su')):
            if not files.readall('/proc/info/su') in files.readall('/etc/sudoers'):
                colors.show("down", "perm", "")
                sys.exit(0)

        if args == []:
            colors.show("down", "fail", "no inputs.")
            sys.exit(0)

        filename = args[0]

        clouddrive = files.readall('/proc/info/csel')
        clouddrivez = f'/dev/{clouddrive}'

        host = control.read_record('host', clouddrivez)
        password = control.read_record('password', clouddrivez)

        x = requests.post(f"{host}/download.php",data={"password":password,"filename":filename})

        if x.text == 'e: wrong password':
            colors.show("down", "fail", f"{clouddrive}: wrong password in device database.")
        elif x.text == 'e: empty password':
            colors.show("down", "fail", f"{clouddrive}: empty password in device database.")
        elif x.text == 'e: file not found':
            colors.show("down", "fail", f"{clouddrive}: {filename}: file not file in cloud drive.")
        else:
            files.write(f'/stor/{clouddrive}/{filename}',x.text)

    def rem (self,args):
        files = Files()
        colors = Colors()
        control = Control()
        permissions = Permissions()

        if not permissions.check_root(files.readall('/proc/info/su')):
            if not files.readall('/proc/info/su') in files.readall('/etc/sudoers'):
                colors.show("rem", "perm", "")
                sys.exit(0)

        if args == []:
            colors.show("rem", "fail", "no inputs.")
            sys.exit(0)

        filename = args[0]

        clouddrive = files.readall('/proc/info/csel')
        clouddrivez = f'/dev/{clouddrive}'

        host = control.read_record('host', clouddrivez)
        password = control.read_record('password', clouddrivez)

        x = requests.post(f"{host}/remove.php",data={"password":password,"filename":filename})

        if x.text == 'e: wrong password':
            colors.show("down", "fail", f"{clouddrive}: wrong password in device database.")
        elif x.text == 'e: empty password':
            colors.show("down", "fail", f"{clouddrive}: empty password in device database.")
        elif x.text == 'e: file not found':
            colors.show("down", "fail", f"{clouddrive}: {filename}: file not file in cloud drive.")
        else:
            if files.isfile (f'/stor/{clouddrive}/{filename}'):
                files.remove(f'/stor/{clouddrive}/{filename}')
            elif files.isdir(f'/stor/{clouddrive}/{filename}'):
                files.removedirs(f'/stor/{clouddrive}/{filename}')

    def mkc (self,args):
        files = Files()
        colors = Colors()
        control = Control()
        permissions = Permissions()


        if not permissions.check_root(files.readall('/proc/info/su')):
            if not files.readall('/proc/info/su') in files.readall('/etc/sudoers'):
                colors.show("mkc", "perm", "")
                sys.exit(0)

        if args == []:
            colors.show("mkc", "fail", "no inputs.")
            sys.exit(0)

        dirname = args[0]

        clouddrive = files.readall('/proc/info/csel')
        clouddrivez = f'/dev/{clouddrive}'

        host = control.read_record('host', clouddrivez)
        password = control.read_record('password', clouddrivez)

        x = requests.post(f"{host}/directory.php",data={"password":password,"dirname":dirname})

        if x.text == 'e: wrong password':
            colors.show("mkc", "fail", f"{clouddrive}: wrong password in device database.")
        elif x.text == 'e: empty password':
            colors.show("mkc", "fail", f"{clouddrive}: empty password in device database.")
        elif x.text == 'e: is a file':
            colors.show("mkc", "fail", f"{clouddrive}: {dirname}: cannot create directory; is a file.")
        else:
            x = f'/stor/{clouddrive}/{dirname}'
            if files.isfile (x):
                colors.show("mkc", "fail", f"{clouddrive}: {dirname}: cannot create directory; is a file.")
            elif not files.isdir (x):
                files.mkdir(x)

    def up (self,args):
        files = Files()
        colors = Colors()
        control = Control()
        permissions = Permissions()

        if not permissions.check_root(files.readall('/proc/info/su')):
            if not files.readall('/proc/info/su') in files.readall('/etc/sudoers'):
                colors.show("up", "perm", "")
                sys.exit(0)

        if args == []:
            colors.show("up", "fail", "no inputs.")
            sys.exit(0)

        clouddrive = files.readall('/proc/info/csel')
        filename = args[0]

        clouddrivez = f'/dev/{clouddrive}'

        host = control.read_record('host', clouddrivez)
        password = control.read_record('password', clouddrivez)

        data = files.readall(f'/stor/{clouddrive}/{filename}')

        x = requests.post(f"{host}/upload.php",data={"password":password,"filename":filename,"data":data})

        if x.text == 'e: wrong password':
            colors.show("up", "fail", f"{clouddrive}: wrong password in device database.")
        elif x.text == 'e: empty password':
            colors.show("up", "fail", f"{clouddrive}: empty password in device database.")
        elif x.text == 'e: is a directory':
            colors.show("up", "fail", f"{clouddrive}: {filename}: cannot create file; is a directory in cloud drive.")

    # chown #
    def chown (self,args):
        files = Files()
        colors = Colors()
        permissions = Permissions()
        new_owner = args[0]
        name = args[1]

        if args==[]:
            colors.show("chown", "fail", "no inputs.")
            sys.exit(0)

        if args[1:]==[]:
            new_owner = ''

        permowner = permissions.check_owner(files.output(name), files.readall("/proc/info/su"))
        perm = permissions.get_permissions(files.output(name))

        num = permissions.show_number(perm)
        num = str(num)
        user_p = int(num[0])
        others_p = int(num[1])
        guest_p = int(num[2])

        if permowner == True:
            if new_owner == "":
                permissions.create(files.output(name), user_p, others_p, guest_p, files.readall("/proc/info/su"))
            else:
                permissions.create(files.output(name), user_p, others_p, guest_p, new_owner)
        else:
            colors.show("chown", "perm", "")

    # logout #
    def logout (self,args):
        files = Files()
        process = Process()
        if files.isfile("/proc/selected"): files.remove("/proc/selected")
        process.endall()
        subprocess.call([sys.executable,'vmabr.pyc', 'login'])

    # new #
    def new (self,args):
        files = Files()
        control = Control()

        user = control.read_record("username", "/tmp/su.tmp")
        code = control.read_record ("code","/tmp/su.tmp")

        if files.isfile("/proc/selected"): files.remove("/proc/selected")
        if user == "guest":
            subprocess.call([sys.executable,'vmabr.pyc', 'user', 'guest'])
        else:
            subprocess.call([sys.executable,'vmabr.pyc', 'user', user, code])

    # det Delete Text from a line
    def det (self,args):
        files = Files()
        control = Control()
        control = Control()
        files = Files()
        for i in args:
            control.remove_item(i,files.readall('/proc/info/sel'))

    # reboot #
    def reboot (self,args):

        files = Files()
        colors = Colors()
        process = Process()

        if files.isfile("/proc/selected"): files.remove("/proc/selected")
        colors.show("kernel", "reboot", "")
        if files.isdir("/desk/guest"):
            files.removedirs("/desk/guest")
        if files.isdir("/tmp"):
            files.removedirs("/tmp")
            files.mkdir("/tmp")

        files.removedirs("/app/cache")
        files.mkdir("/app/cache")
        files.mkdir("/app/cache/gets")
        files.mkdir("/app/cache/archives")
        files.mkdir("/app/cache/archives/code")
        files.mkdir("/app/cache/archives/control")
        files.mkdir("/app/cache/archives/data")
        files.mkdir("/app/cache/archives/build")

        process.endall()

        if files.readall('/proc/info/os')=='Pyabr' and not files.isfile ('/.unlocked'):
            subprocess.call(['reboot'])
        else:
            subprocess.call([sys.executable,'vmabr.pyc'])

    # shut command #
    def shut (self,args):
        files = Files()
        process = Process()

        if files.isfile("/proc/selected"): files.remove("/proc/selected")
        process.end(int(files.readall("/proc/info/sp")))

        if files.readall("/proc/info/su") == "0":
            if files.isdir("/desk/guest"):
                files.removedirs("/desk/guest")
            if files.isdir("/tmp"):
                files.removedirs("/tmp")
                files.mkdir("/tmp")
            if files.isfile("/proc/selected"): files.remove("/proc/selected")
            process.endall()

            if files.readall('/proc/info/os') == 'Pyabr' and not files.isfile('/.unlocked'):
                subprocess.call(['poweroff'])

    # shutdown command #
    def shutdown (self,args):
        files = Files()
        process = Process()

        if files.isdir("/desk/guest"):
            files.removedirs("/desk/guest")
        if files.isdir("/tmp"):
            files.removedirs("/tmp")
            files.mkdir("/tmp")
        if files.isfile("/proc/selected"): files.remove("/proc/selected")

        files.removedirs("/app/cache")
        files.mkdir("/app/cache")
        files.mkdir("/app/cache/gets")
        files.mkdir("/app/cache/archives")
        files.mkdir("/app/cache/archives/code")
        files.mkdir("/app/cache/archives/control")
        files.mkdir("/app/cache/archives/data")
        files.mkdir("/app/cache/archives/build")

        process.endall()

        if files.readall('/proc/info/os') == 'Pyabr' and not files.isfile('/.unlocked'):
            subprocess.call(['poweroff'])


    # touch #
    def touch (self,args):
        files = Files()

        for i in args:
            files.create(i)

    # cat command #
    def cat (self,args):
        files = Files()
        colors = Colors()
        permissions = Permissions()


        cmdln = ['']
        cmdln[1:] = args

        if not cmdln[1:] == []:
            if cmdln[1] == '-r' or cmdln[1] == '-c' or cmdln[1] == '-w' or cmdln[1] == '-a' or cmdln[1]=='-l':
                option = cmdln[1]
                name = cmdln[2]
            else:
                name = cmdln[1]
                option = ''
        else:
            colors.show("cat", "fail", "no inputs.")
            sys.exit(0)

        ## Read files ##
        if option == '' or option == '-r':
            if files.isfile(name):
                if permissions.check(files.output(name), "r", files.readall("/proc/info/su")):
                    print(files.readall(name))
                else:
                    colors.show("cat", "perm", "")
            elif files.isdir(name):
                colors.show("cat", "fail", f"{name}: is a directory.")
            else:
                colors.show("cat", "fail", f"{name}: file not found.")

        ## Create files ##
        elif option == '-c':
            if files.isdir(name):
                colors.show("cat", "fail", f"{name}: is a directory.")
            else:
                if permissions.check(files.output(name), "w", files.readall("/proc/info/su")):
                    files.create(name)
                else:
                    colors.show("cat", "perm", "")

        ## Write in lines
        elif option == '-l':
            if files.isdir(name):
                colors.show("cat", "fail",  f"{name}: is a directory.")
            else:
                if permissions.check(files.output(name), "w", files.readall("/proc/info/su")):
                    strv = ''
                    for i in cmdln[3:]:
                        strv+=f' {i}'
                    files.write(name,strv[1:])
                else:
                    colors.show("cat", "perm", "")

        ## Write into files ##
        elif option == '-w':
            if files.isdir(name):
                colors.show("cat", "fail", f"{name}: is a directory.")
            else:
                if permissions.check(files.output(name), "w", files.readall("/proc/info/su")):

                    ## Set EOF
                    if cmdln[3:] == []:
                        EOF = 'EOF'
                    else:
                        EOF = cmdln[3]

                    # WRITE COMMAND LINE

                    texts = ''

                    while True:
                        cmd = input('> ')
                        if cmd == EOF:
                            break
                        else:
                            if texts == '':
                                texts = cmd
                            else:
                                texts =  f'{texts}\n{cmd}'

                    ## WRITE INTO FILE
                    files.write(cmdln[2], texts)
                else:
                    colors.show("cat", "perm", "")

        ## Write into files ##
        elif option == '-a':
            if files.isdir(name):
                colors.show("cat", "fail", f"{name}: is a directory.")
            else:
                if permissions.check(files.output(name), "w", files.readall("/proc/info/su")):

                    ## Set EOF
                    if cmdln[3:] == []:
                        EOF = 'EOF'
                    else:
                        EOF = cmdln[3]

                    # WRITE COMMAND LINE

                    texts = ''

                    while True:
                        cmd = input('> ')
                        if cmd == EOF:
                            break
                        else:
                            if texts == '':
                                texts = cmd
                            else:
                                texts = f'{texts}\n{cmd}'

                    ## WRITE INTO FILE
                    files.append(cmdln[2], texts)
                else:
                    colors.show("cat", "perm", "")

    # cd command #
    def cd (self,args):
        files = Files()
        colors = Colors()
        permissions = Permissions()
        if args==[]:
            colors.show("cd", "fail", "no inputs.")
            sys.exit (0)

        path = args[0]

        if permissions.check(files.output(path), "r", files.readall("/proc/info/su")):
            if path.startswith ('/..'):
                files.write("/proc/info/pwd", '/')
            elif path == '..':
                pwd = files.readall('/proc/info/pwd')
                pwd = pwd.split('/')
                lens = len(pwd) - 1
                pwd.pop(lens)

                strv = ''

                for i in pwd:
                    strv += f"/{i}"

                if strv.startswith('////'):
                    strv = strv.replace('////','/')
                elif strv.startswith('///'):
                    strv = strv.replace('///','/')
                elif strv.startswith('//'):
                    strv = strv.replace('//','/')

                pwd = files.output(strv)
                files.write("/proc/info/pwd", pwd)

            elif files.isdir(path):
                files.write("/proc/info/pwd", files.output(path))
            else:
                colors.show("cd", "fail", f"{path}: directory not found.")
        else:
            colors.show("cd", "perm", "")

    # clean command #
    def clean (self,args):
        files = Files()
        colors = Colors()
        permissions = Permissions()
 
        user = files.readall("/proc/info/su")
        select = files.readall("/proc/info/sel")

        if not select.startswith("/proc/"):
            if permissions.check(files.output(select), "w", user):
                files.create(select)
            else:
                colors.show("clean", "perm", "")
        else:
            files.create(select)

    # clear command #
    def clear (self,args):
        files = Files()

        osname = files.readall("/proc/info/os")
        if osname == "Windows":
            os.system("cls")
        else:
            os.system("clear")

    # cp command #
    def cp (self,args):
        files = Files()
        colors = Colors()
        control = Control()
        permissions = Permissions()


        # args #
        cmdln = ['']
        cmdln[1:] = args

        if cmdln[1:] == []:
            colors.show("cp", "fail", "no inputs.")
        if cmdln[2:] == []:
            colors.show("cp", "fail", "no inputs.")

        src = cmdln[1]
        dest = cmdln[2]



        if files.isdir(src):
            if files.isfile(dest):
                colors.show("cp", "fail", f"{dest}: dest is a file.")
            else:
                if permissions.check(files.output(src), "r", files.readall("/proc/info/su")):
                    if permissions.check(files.output(dest), "w", files.readall("/proc/info/su")):
                        perm = permissions.get_permissions(files.output(src))
                        control.write_record(files.output(dest), perm, "/etc/permtab")
                        files.copydir(src, dest)

                    else:
                        colors.show("cp", "perm", "")
                else:
                    colors.show("cp", "perm", "")
        elif files.isfile(src):
            if files.isdir(dest):
                colors.show("cp", "fail", f"{dest}: dest is a directory.")
            else:
                if permissions.check(files.output(src), "r", files.readall("/proc/info/su")):
                    if permissions.check(files.output(dest), "w", files.readall("/proc/info/su")):
                        perm = permissions.get_permissions(files.output(src))
                        control.write_record(files.output(dest), perm, "/etc/permtab")
                        files.copy(src, dest)
                    else:
                        colors.show("cp", "perm", "")
                else:
                    colors.show("cp", "perm", "")
        else:
            colors.show("cp", "fail", f"{src}: source not found.")

    # date command #
    def date (self,args):
        files = Files()

        ## Show all time and date ##
        if args == []:
            os.environ['TZ'] = files.readall("/proc/info/tz")  # https://stackoverflow.com/questions/1301493/setting-timezone-in-python
            time.tzset()
            print(datetime.datetime.now().ctime())

        ## Show utc now ##
        if args == ['utc']:
            print(datetime.datetime.utcnow().ctime())

    # getv command #
    def getv (self,args):
        files = Files()
        colors = Colors()
        control = Control()
        permissions = Permissions()

        select = files.readall("/proc/info/sel")
        if not select.startswith("/proc/"):
            if permissions.check(files.output(select), "w", files.readall("/proc/info/su")):
                listinfo = files.list("/proc/info")
                for i in listinfo:
                    control.write_record(i, files.readall(f"/proc/info/{i}"), select)
            else:
                colors.show("getv", "perm", "")
        else:
            listinfo = files.list("/proc/info")
            for i in listinfo:
                control.write_record(i, files.readall(f"/proc/info/{i}"), select)

    # help command #
    def help (self,args):
        files = Files()
        colors = Colors()

        x =  files.list ('/usr/share/helps')
        x.sort()

        if args==[]:
            
            print (f"{colored('Commands are:','cyan')}")
            for i in x:
                print(i,end=' ')
            print (f"\n{colored('Try help [command] to see more informations','cyan')}")
        else:
            if files.isfile(f"/usr/share/helps/{args[0]}"):
                print(files.readall(f"/usr/share/helps/{args[0]}"))
            else:
                print (f"{colored('Commands are:','cyan')}")
                for i in x:
                    print(i,end=' ')
                print (f"\n{colored('Try help [command] to see more informations','cyan')}")

    # read command #
    def read (self,args):

        for i in args:
            self.set([f"{i}:",input()])

    # ls command #
    def ls (self,args):
        files = Files()
        colors = Colors()
        permissions = Permissions()
        path = None
        options = None

        # check args #

        if not args == [] and args[1:] == []:
            path = files.output(args[0])
            options = ''
        elif not args == [] and not args[1:] == []:
            path = files.output(args[0])
            options = args[1]
        elif args == []:
            path = files.readall("/proc/info/pwd")
            options = ''

        if options == "":
            if files.isdir(path):
                if permissions.check(files.output(path), "r", files.readall("/proc/info/su")):
                    list = files.list(path)
                    list.sort()
                    for i in list:
                        if i.startswith ('.') and not files.readall('/etc/default/hidden_files')=='Yes':
                            list.remove(i)
                        else:
                            if files.isdir(f"{path}/{i}"):
                                print(f"{colored(f'{i}/', 'cyan')}")
                            else:
                                print(i)
                else:
                    colors.show("ls", "perm", "")
            else:
                colors.show("ls", "fail", f"{path}: directory not found.")
        elif options == "-p":
            if files.isdir(path):
                if permissions.check(files.output(path), "r", files.readall("/proc/info/su")):
                    list = files.list(path)
                    list.sort()
                    for i in list:
                        if i.startswith ('.') and not files.readall('/etc/default/hidden_files')=='Yes':
                            list.remove(i)
                        else:
                            if files.isdir(f"{path}/{i}"):
                                perm = permissions.get_permissions(files.output(f"{path}{i}"))
                                c = colored(f'{perm}\t{i}/', 'cyan')
                                print(f"{c}")
                            else:
                                perm = permissions.get_permissions(files.output(f"{path}{i}"))
                                print(f"{perm}\t{i}")
                else:
                    colors.show("ls", "perm", "")
            else:
                colors.show("ls", "fail",  f"{path}: directory not found.")
        elif options == "-n":
            if files.isdir(path):
                if permissions.check(files.output(path), "r", files.readall("/proc/info/su")):
                    list = files.list(path)
                    list.sort()
                    for i in list:
                        if i.startswith ('.') and not files.readall('/etc/default/hidden_files')=='Yes':
                            list.remove(i)
                        else:
                            if files.isdir(f"{path}/{i}"):
                                perm = permissions.get_permissions(f"{path}/{i}")
                                perm = str(permissions.show_number(perm))
                                c = colored(f'{perm}\t{i}/', 'cyan')
                                print(f"{c}")
                            else:
                                perm = permissions.get_permissions(f"{path}/{i}")
                                perm = str(permissions.show_number(perm))
                                print(f"{perm}\t{i}")
                else:
                    colors.show("ls", "perm", "")
            else:
                colors.show("ls", "fail", f"{path}: directory not found.")
    # mkdir command #
    def mkdir (self,args):
        files = Files()
        colors = Colors()
        permissions = Permissions()

        for i in args:
            if files.isfile(i):
                colors.show("mkdir", "fail", f"{i}: is a file.")
            elif files.isdir(i):
                colors.show("mkdir", "warning", f"{i}: directory exists.")
            else:
                if permissions.check(files.output(i), "w", files.readall("/proc/info/su")):
                    files.makedirs(i)
                else:
                    colors.show("mkdir", "perm", "")

    # mv command #
    def mv (self,args):
        files = Files()
        colors = Colors()
        control = Control()
        permissions = Permissions()

        # args #
        cmdln = ['']
        cmdln[1:] = args

        if cmdln[1:] == []:
            colors.show("mv", "fail", "no inputs.")
        if cmdln[2:] == []:
            colors.show("mv", "fail", "no inputs.")

        src = cmdln[1]
        dest = cmdln[2]

        if files.isdir(src):
            if files.isfile(dest):
                colors.show("mv", "fail", f"{dest}: dest is a file.")
            else:
                if permissions.check(files.output(src), "r", files.readall("/proc/info/su")) and permissions.check(
                        files.output(src), "w", files.readall("/proc/info/su")):
                    if permissions.check(files.output(dest), "w", files.readall("/proc/info/su")):
                        perm = permissions.get_permissions(files.output(src))
                        control.write_record(files.output(dest), perm, "/etc/permtab")
                        files.copydir(src, dest)
                        files.removedirs(src)
                    else:
                        colors.show("mv", "perm", "")
                else:
                    colors.show("mv", "perm", "")
        elif files.isfile(src):
            if files.isdir(dest):
                colors.show("mv", "fail", f"{dest}: dest is a directory.")
            else:
                if permissions.check(files.output(src), "r", files.readall("/proc/info/su")) and permissions.check(
                        files.output(src), "w", files.readall("/proc/info/su")):
                    if permissions.check(files.output(dest), "w", files.readall("/proc/info/su")):
                        perm = permissions.get_permissions(files.output(src))
                        control.write_record(files.output(dest), perm, "/etc/permtab")
                        files.copy(src, dest)
                        files.remove(src)
                    else:
                        colors.show("mv", "perm", "")
                else:
                    colors.show("mv", "perm", "")
        else:
            colors.show("mv", "fail", f"{src}: source not found.")

    # echo command #
    def echo (self,args):
        for i in args:
            print(
                i
                    .replace("-a", "\a")
                    .replace("-b", "\b")
                    .replace("-f", "\f")
                    .replace("-n", "\n")
                    .replace("-r", "\r")
                    .replace("-t", "\t")
                    .replace("-v", "\v"), end=' ')
        print()

    # rm command #
    def rm (self,args):
        files = Files()
        colors = Colors()
        control = Control()
        permissions = Permissions()

        for i in args:
            if files.isdir(i):
                if permissions.check(files.output(i), "w", files.readall("/proc/info/su")):
                    files.removedirs(i)
                    control.remove_record(i,'/etc/permtab')
                else:
                    colors.show("rm", "perm", "")
                    sys.exit(0)
            elif files.isfile(i):
                if permissions.check(files.output(i), "w", files.readall("/proc/info/su")):
                    files.remove(i)
                    control.remove_record(i, '/etc/permtab')
                else:
                    colors.show("rm", "perm", "")
                    sys.exit(0)
            else:
                colors.show("rm", "fail", f"{i}: file or directory not found.")
                sys.exit(0)

    ## passwd ##
    def passwd (self,args):
        files = Files()
        colors = Colors()
        control = Control()
        if args==[]:
            colors.show('passwd','fail','no inputs.')
            sys.exit(0)

        user = args[0]

        # check user exists
        if not files.isfile(f'/etc/users/{user}'):
            colors.show('passwd', 'fail', f"{user}: user not found.")
            sys.exit(0)


        if not control.read_record('code',f'/etc/users/{user}')== hashlib.sha3_512(getpass.getpass(f'Enter {user}\'s old password: ').encode()).hexdigest():
            colors.show('passwd', 'fail', f"{user}: wrong password.")
            sys.exit(0)

        newcode = getpass.getpass('Enter a new password: ')

        while True:
            confirm = getpass.getpass('Confirm the new password: ')
            if confirm==newcode: break
            else:
                print('Try agian!')

        control.write_record('code',hashlib.sha3_512(newcode.encode()).hexdigest(),f'/etc/users/{user}')

    # say command #
    def say (self,args):
        for i in args:
            print(
                i
                    .replace("-a", "\a")
                    .replace("-b", "\b")
                    .replace("-f", "\f")
                    .replace("-n", "\n")
                    .replace("-r", "\r")
                    .replace("-t", "\t")
                    .replace("-v", "\v"), end=' ')

    # sel command #
    def sel (self,args):
        files = Files()
        colors = Colors()
        permissions = Permissions()

        if args == []:
            colors.show("sel", "fail", "no inputs.")
            sys.exit(0)

        database_name = args[0]


        if files.isfile(database_name):
            if permissions.check(files.output(database_name), "r", files.readall("/proc/info/su")):
                files.write("/proc/info/sel", database_name)
                files.create("/proc/selected")
            else:
                colors.show("sel", "perm", "")
        else:
            colors.show("sel", "fail", f"{database_name}: controller not found.")

    # set command #
    def set (self,args):
        files = Files()
        colors = Colors()
        control = Control()
        permissions = Permissions()

        if args == [] or args[1:] == []:
            colors.show("set", "fail", "no inputs.")
            sys.exit(0)

        if not args[0].endswith(":"):
            colors.show("set", "fail", "wrong syntax.")
            sys.exit(0)

        name = args[0].replace(":", "")
        value = args[1]

        select = files.readall("/proc/info/sel")
        if not select.startswith("/proc/"):
            if permissions.check(files.output(select), "w", files.readall("/proc/info/su")):
                control.write_record(name, value, select)
            else:
                colors.show("set", "perm", "")
        else:
            control.write_record(name, value, select)

    # sleep command #
    def sleep (self,args):
        if args == []:
            time.sleep(3)
        else:
            timeout = float(args[0])
            time.sleep(int(timeout))

    # su command #
    def su (self,args):
        files = Files()
        colors = Colors()
        control = Control()

        if args == []:
            colors.show("su", "fail", "no inputs.")
            sys.exit(0)

        input_username = args[0]
        user = files.readall("/proc/info/su")

        if files.isfile("/proc/selected"): files.remove("/proc/selected")
        if user == input_username:
            colors.show("su", "warning", f"{user} has already switched.")
        elif input_username == "guest":
            enable_cli = control.read_record("enable_cli", "/etc/guest")
            if enable_cli == "Yes":
                subprocess.call ([sys.executable,'vmabr.pyc','user','guest'])
            else:
                colors.show(input_username, "fail", "user not found.")

        elif files.isfile(f"/etc/users/{input_username}"):

                input_password = getpass.getpass(f'Enter {input_username}\'s password: ')
                if hashlib.sha3_512(str(input_password).encode()).hexdigest() == control.read_record("code", f"/etc/users/{input_username}"):
                    subprocess.call ([sys.executable,'vmabr.pyc','user',input_username,input_password])
                else:
                    colors.show("su", "fail", f"{input_username}: wrong password.")

        else:
            colors.show("su", "fail", f"{input_username} user not found.")

    # sudo command #
    def sudo (self,args):
        files = Files()
        colors = Colors()
        permissions = Permissions()

        if args == []:
            colors.show('sudo', 'fail', 'no inputs.')
            sys.exit(0)

        if not args[0].startswith('-'):

            ## Get user name ##

            thisuser = files.readall("/proc/info/su")

            ## Check guest account ##
            if thisuser == "guest":
                colors.show("sudo", 'fail', 'cannot use sudo command in guest user.')
                sys.exit(0)

            ## Check sudoers account ##
            if not thisuser == "root":
                sudoers = files.readall('/etc/sudoers')

                if not sudoers.__contains__(thisuser):
                    colors.show('sudo', 'fail', f"{thisuser}: user isn't sudoers account.")
                    sys.exit()

            ## Send /etc/users/root to /proc/info/su username ##

            files.write("/proc/info/su", 'root')

            prompt = [sys.executable,'vmabr.pyc', 'exec']

            for i in args:
                prompt.append(i)

            subprocess.call(prompt)

            files.write("/proc/info/su", thisuser)
        elif args[0] == '-a':
            ## Check root ##
            if not permissions.check_root(files.readall("/proc/info/su")):
                colors.show("sudo", "perm", "")
                sys.exit(0)
            ## Check user exists or no ##
            if files.isfile(f'/etc/users/{args[1]}'):
                files.append('/etc/sudoers', f"{args[1]}\n")
            else:
                colors.show('sudo', 'fail', f"{args[1]}: user not found.")
        else:
            colors.show('sudo', 'fail', f"{args[1]}: option not found.")

    # uadd command #
    def uadd (self,args):
        files = Files()
        colors = Colors()
        control = Control()
        permissions = Permissions()

        if args == []:
            colors.show("uadd", "fail", "no inputs.")
            sys.exit(0)

        input_username = args[0]
        user = files.readall ("/proc/info/su")

        if permissions.check_root(user):
            ## Check exists user ##
            if files.isfile(f"/etc/users/{input_username}") or input_username == "root":
                colors.show("uadd", "fail", f"{input_username}: user exists.")
            elif input_username == "guest":
                colors.show("uadd", "fail", "cannot create user account with guest username.")
            else:
                while True:
                    password = getpass.getpass('Enter a new password: ')
                    confirm = getpass.getpass('Confirm the new password: ')
                    if password == confirm: break


                ## Informations ##
                fullname = input  ('\tFull name       []: ')
                company =    input('\tCompany name    []: ')
                birthday =   input('\tBirthday        []: ')
                gender =     input('\tGender          [Male/Female]: ')
                blood_type = input('\tBlood type      [O/A/B/AB]: ')
                phone =      input('\tPhone number    []: ')
                website =    input('\tWebsite address []: ')
                email =      input('\tEmail address   []: ')

                files.create(f"/etc/users/{input_username}")
                control.write_record("code", hashlib.sha3_512(str(password).encode()).hexdigest(), f'/etc/users/{input_username}')

                ## Add informations ##
                if not (fullname == None or fullname == ""):
                    control.write_record("fullname", fullname,f'/etc/users/{input_username}')
                if not (company == None or company == ""):
                    control.write_record("company", company, f'/etc/users/{input_username}')
                if not (birthday == None or birthday == ""):
                    control.write_record("birthday", birthday, f'/etc/users/{input_username}')
                if not (gender == None or gender == ""):
                    control.write_record("gender", gender, f'/etc/users/{input_username}')
                if not (blood_type == None or blood_type == ""):
                    control.write_record("blood_type", blood_type, f'/etc/users/{input_username}')
                if not (phone == None or phone == ""):
                    control.write_record("phone", phone, f'/etc/users/{input_username}')
                if not (website == None or website == ""):
                    control.write_record("website", website, f'/etc/users/{input_username}')
                if not (email == None or email == ""):
                    control.write_record("email", email, f'/etc/users/{input_username}')

                control.write_record(f'/desk/{input_username}',f"drwxr-x---/{input_username}",'/etc/permtab')

        else:
            colors.show("uadd", "perm", "")

    # udel command #
    def udel (self,args):
        files = Files()
        colors = Colors()
        control = Control()
        permissions = Permissions()

        if args == []:
            colors.show("udel", "fail", "no inputs.")
            sys.exit(0)

        input_username = args[0]
        user = files.readall ("/proc/info/su")

        if input_username == user:
            colors.show("udel", "fail", f"{input_username}: cannot remove switched user.")
        else:
            if permissions.check_root(user):
                if not files.isfile(f"/etc/users/{input_username}"):
                    colors.show("udel", "fail",  f"{input_username}: user not found.")
                else:
                    if input_username == "root":
                        colors.show("udel", "fail",   f"{input_username}: is a permanet user.")
                    else:
                        files.remove(f"/etc/users/{input_username}")
                        if files.isdir(f'/desk/{input_username}'):
                            files.removedirs(f"/desk/{input_username}")
                            control.remove_record(f'/desk/{input_username}','/etc/permtab')
            else:
                colors.show("udel", "perm", "")

    # uinfo command #
    def uinfo (self,args):
        files = Files()
        colors = Colors()
        control = Control()

        if args == []:
            input_username = files.readall ("/proc/info/su")
        else:
            input_username = args[0]

        enable_cli = control.read_record("enable_cli", "/etc/guest")
        if not (input_username == "guest" and enable_cli == "Yes"):
            if files.isfile(f"/etc/users/{input_username}"):
                ## Get information from user database ##
                fullname = control.read_record("fullname", f"/etc/users/{input_username}")
                company = control.read_record("company", f"/etc/users/{input_username}")
                birthday = control.read_record("birthday", f"/etc/users/{input_username}")
                gender = control.read_record("gender", f"/etc/users/{input_username}")
                blood_type = control.read_record("blood_type", f"/etc/users/{input_username}")
                phone = control.read_record("phone", f"/etc/users/{input_username}")
                website = control.read_record("website", f"/etc/users/{input_username}")
                email = control.read_record("email", f"/etc/users/{input_username}")

                ## Show it on screen ##
                if not (fullname == None or fullname == ""):  print(
                    f"\t   Full name: {fullname}")
                if not (company == None or company == ""):        print(
                    f"\t      Company: {company}" )
                if not (birthday == None or birthday == ""):      print(
                    f"\t     Birthday: {birthday}" )
                if not (gender == None or gender == ""):          print(
                    f"\t       Gender: {gender}")
                if not (blood_type == None or blood_type == ""):  print(
                    f"\t    BloodType: {blood_type}" )
                if not (phone == None or phone == ""):            print(
                    f"\t Phone number: {phone}")
                if not (website == None or website == ""):        print(
                    f"\t      Website: {website}")
                if not (email == None or email == ""):            print(
                    f"\tEmail address: {email}")
            else:
                colors.show("uinfo", "fail", f"{input_username}: user not found.")

    # unsel command #
    def unsel (self,args):
        files = Files()
        colors = Colors()

        select = files.readall("/proc/info/sel")

        if select == f'/proc/{files.readall("/proc/info/sp")}':
            colors.show("unsel", "warning", "controller has already selected.")
        else:
            files.write("/proc/info/sel", f'/proc/{files.readall("/proc/info/sp")}')
            if files.isfile("/proc/selected"): files.remove("/proc/selected")

    # upv command #
    def upv (self,args):
        files = Files()
        colors = Colors()
        control = Control()
        permissions = Permissions()

        if not permissions.check_root(files.readall("/proc/info/su")):
            colors.show("upv", "perm", "")
            sys.exit(0)

        sel = files.readall('/proc/info/sel')  ## Get selector

        ## List all controls ##

        listc = control.read_list(sel)

        for i in listc:
            if not i.__contains__(':'):
                pass
            else:
                spliter = i.split(': ')
                files.write(f'/proc/info/{spliter[0]}', spliter[1])

    # wget command #
    def wget (self,args):
        files = Files()
        colors = Colors()
        permissions = Permissions()


        # https://www.tutorialspoint.com/downloading-files-from-web-using-python

        ## Check params ##

        if args == [] and args[1:]:
            colors.show('wget', 'fail', 'no inputs.')
            sys.exit(0)

        ## Download ##

        ## Check permissions ##
        if permissions.check(files.output(args[1]), "w", files.readall("/proc/info/su")):
            wget.download(args[0],files.input(args[1]))
            print()
        else:
            colors.show("wget", "perm", "")


# package #
class Package:
    ## Clean the cache ##
    def __init__(self):
        pass

    def clean (self):

        permissions = Permissions()
        files = Files()
        colors = Colors()

        if permissions.check_root(files.readall("/proc/info/su")):
            if files.isdir("/app/cache"):
                files.removedirs("/app/cache")
                files.mkdir("/app/cache")
                files.mkdir("/app/cache/gets")
                files.mkdir("/app/cache/archives")
                files.mkdir("/app/cache/archives/code")
                files.mkdir("/app/cache/archives/control")
                files.mkdir("/app/cache/archives/data")
                files.mkdir("/app/cache/archives/build")
        else:
            colors.show("paye", "perm", "")

    ## Create .pa archive ##

    def build(self,name):
        permissions = Permissions()
        files = Files()
        colors = Colors()

        if permissions.check_root(files.readall("/proc/info/su")):
            if not files.isfile( f"{name}/control/manifest"):
                colors.show("paye", "fail", "cannot create archive package")
                self.clean()
                sys.exit(0)

            if not files.isdir(f"{name}/data"): files.mkdir(f"{name}/data")
            if not files.isdir(f"{name}/code"): files.mkdir(f"{name}/code")

            ## Remove cache archives ##
            if files.isdir('/app/cache/archives/control'): files.removedirs('/app/cache/archives/control')
            if files.isdir('/app/cache/archives/data'): files.removedirs('/app/cache/archives/data')
            if files.isdir('/app/cache/archives/code'): files.removedirs('/app/cache/archives/code')

            ## Copy dir ##
            files.copydir(f'{name}/data', '/app/cache/archives/data')
            files.copydir(f'{name}/control', '/app/cache/archives/control')
            files.copydir(f'{name}/code', '/app/cache/archives/code')

            ## Pack archives ##
            shutil.make_archive(files.input("/app/cache/archives/build/data"), "zip",
                                files.input('/app/cache/archives/data'))
            shutil.make_archive(files.input("/app/cache/archives/build/control"), "zip",
                                files.input('/app/cache/archives/control'))
            shutil.make_archive(files.input("/app/cache/archives/build/code"), "zip",
                                files.input('/app/cache/archives/code'))
            shutil.make_archive(files.input(name), "zip", files.input("/app/cache/archives/build"))

            files.cut(f"{name}.zip", f"{name}.pa")
            ## Unlock the cache ##
        else:
            colors.show("paye", "perm", "")


    ## Unpack .pa archives ##

    def unpack(self,name):
        permissions = Permissions()
        files = Files()
        control = Control()
        colors = Colors()
        commands = Commands()

        if permissions.check_root(files.readall("/proc/info/su")):

            ## unpack package ##
            shutil.unpack_archive(files.input(name), files.input("/app/cache/archives/build"), "zip")

            shutil.unpack_archive(files.input("/app/cache/archives/build/data.zip"),
                                  files.input("/app/cache/archives/data"), "zip")
            shutil.unpack_archive(files.input("/app/cache/archives/build/control.zip"),
                                  files.input("/app/cache/archives/control"), "zip")
            shutil.unpack_archive(files.input("/app/cache/archives/build/code.zip"),
                                  files.input("/app/cache/archives/code"), "zip")

            ## Get database of this package ##
            name = control.read_record("name", "/app/cache/archives/control/manifest").lower()
            unpack =control.read_record("unpack", "/app/cache/archives/control/manifest")

            ## Run preinstall script ##

            if files.isfile('/app/cache/archives/control/preinstall.sa'):
                System('/app/cache/archives/preinstall')  # Run it

                ## Copy preinstall script ##

                files.copy('/app/cache/archives/control/preinstall.sa', f"/app/packages/{name}.preinstall")

            ## Setting up ##

            if files.isfile("/app/cache/archives/control/list"): files.copy("/app/cache/archives/control/list",f"/app/packages/{name}.list")
            if files.isfile("/app/cache/archives/control/manifest"): files.copy("/app/cache/archives/control/manifest",f"/app/packages/{name}.manifest")
            if files.isfile("/app/cache/archives/control/compile"): files.copy("/app/cache/archives/control/compile",f"/app/packages/{name}.compile")

            if control.read_record('compile','/app/cache/archives/control/manifest')=='Yes':
                for i in control.read_list('/app/cache/archives/control/compile'):
                    spl = i.split(":")

                    code = f'/app/cache/archives/code/{spl[0]}'
                    dest = f"/app/cache/archives/data/{spl[1]}"

                    commands.cc([code, dest])

            ## Create data archive ##
            shutil.make_archive(files.input("/app/cache/archives/build/data"), 'zip',files.input('/app/cache/archives/data'))

            ## Unpack data again ##
            shutil.unpack_archive(files.input("/app/cache/archives/build/data.zip"), files.input(unpack), "zip")

            ## Save the source

            shutil.unpack_archive(files.input('/app/cache/archives/build/code.zip'),files.input(f'/usr/src/{name}'),'zip')

            ## After install ##

            ## Run postinstall script ##

            if files.isfile('/app/cache/archives/control/postinstall.sa'):
                System('/app/cache/archives/control/postinstall')  # Run it

                ## Copy postinstall script ##

                files.copy('/app/cache/archives/control/postinstall.sa', f'/app/packages/{name}.postinstall')

            ## Copy other scripts ##
            if files.isfile('/app/cache/archives/control/preremove.sa'):
                files.copy('/app/cache/archives/control/preremove.sa', f'/app/packages/{name}.preremove')

            if files.isfile('/app/cache/archives/control/postremove.sa'):
                files.copy('/app/cache/archives/control/postremove.sa', f'/app/packages/{name}.postremove')

            ## Unlock the cache ##
        else:
            colors.show("paye", "perm", "")

    ## Remove package ##
    def uninstall (self,name):
        permissions = Permissions()
        files = Files()
        control = Control()
        colors = Colors()
        name = name.lower()

        if permissions.check_root(files.readall("/proc/info/su")):

            location = f"/app/packages/{name}.manifest"

            if not files.isfile(location):
                colors.show("paye", "fail", f"{name}: package not found")
                self.clean()
                sys.exit(0)

            ## Database control ##


            list = f"/app/packages/{name}.list"
            compile = f'/app/packages/{name}.compile'
            preinstall = f"/app/packages/{name}.preinstall"
            postinstall = f"/app/packages/{name}.postinstall"
            preremove = f"/app/packages/{name}.preremove"
            postremove = f"/app/packages/{name}.postremove"

            ## Create preremove and postremove copies ##


            if files.isfile(preremove): files.copy(preremove, "/usr/app/preremove.sa")
            if files.isfile(postremove): files.copy(postremove, "/usr/app/postremove.sa")


            ## Run pre remove script ##

            if files.isfile ('/usr/app/preremove.sa'):
                System("/usr/app/preremove")
                files.remove('/usr/app/preremove.sa')

            ####################

            unpack = control.read_record("unpack", location)

            ## Unpacked removal ##
            filelist = control.read_list(list)

            for i in filelist:
                if files.isdir("{unpack}/{i}"):
                    files.removedirs("{unpack}/{i}")
                elif files.isfile("{unpack}/{i}"):
                    files.remove("{unpack}/{i}")


            ## Database removal ##

            if files.isfile(location): files.remove(location)
            if files.isfile(list): files.remove(list)
            if files.isfile(preinstall): files.remove(preinstall)
            if files.isfile(postinstall): files.remove(postinstall)
            if files.isfile(preremove): files.remove(preremove)
            if files.isfile(postremove): files.remove(postremove)
            if files.isfile(compile): files.remove(compile)

            ## Run postremove script ##

            if files.isfile ('/usr/app/postremove.sa'):
                System ("postremove")
                files.remove('/usr/app/postremove.sa')
        else:
            colors.show("paye", "perm", "")

    ## Download package ##

    def download(self,packname):
        permissions = Permissions()
        files = Files()
        colors = Colors()
        packname = packname.lower()

        if permissions.check_root(files.readall("/proc/info/su")):
            mirror = files.readall(f'/app/mirrors/{packname}')

            ## Download the file ##

            wget.download(mirror,files.input(f'/app/cache/gets/{packname}.pa'))
            print()

        else:
            colors.show("paye", "perm", "")

    ## Create a mirro ##
    def add (self,mirror,name):
        permissions = Permissions()
        files = Files()
        colors = Colors()
        if permissions.check_root(files.readall("/proc/info/su")):
            #endsplit = mirror.replace('https://', '').replace('http://', '')
            #endsplit = mirror.split('/')
            files.write(f"/app/mirrors/{name.replace('.pa','')}", mirror)
        else:
            colors.show("paye", "perm", "")

    # update cloud software #
    def upcloud (self):
        permissions = Permissions()
        files = Files()
        control = Control()
        colors = Colors()
        if permissions.check_root(files.readall("/proc/info/su")):

            # backup #
            shutil.make_archive(files.input('/app/cache/backups/users.bak'),'zip',files.input('/etc/users'))
            files.copy('/etc/commands','/app/cache/backups/commands.bak')
            files.copy('/etc/guest','/app/cache/backups/guest.bak')
            files.copy('/etc/gui','/app/cache/backups/gui.bak')
            files.copy('/etc/hostname','/app/cache/backups/hostname.bak')
            files.copy('/etc/interface','/app/cache/backups/interface.bak')
            files.copy('/etc/modules', '/app/cache/backups/modules.bak')
            files.copy('/etc/permtab','/app/cache/backups/permtab.bak')
            files.copy('/etc/sudoers','/app/cache/backups/sudoers.bak')
            files.copy('/etc/profile.sa','/app/cache/backups/profile.sa.bak')
            files.copy('/etc/time', '/app/cache/backups/time.bak')

            mode = control.read_record('mode','/etc/paye/sources')


            self.download(mode)
            self.unpack(f'/app/cache/gets/{mode}.pa')

            for i in files.list ('/app/packages'):
                if i.endswith ('.manifest') and files.isfile(f'/app/mirrors/{i.replace(".manifest","")}'):
                    i = i.replace('.manifest','')

                    # check version
                    old = control.read_record('version',f'/app/packages/{i}.manifest')
                    new = control.read_record('version',f'/app/mirrors/{i}.manifest')

                    if not old==new and not i=='latest':
                        self.download(i)
                        self.unpack(f'/app/cache/gets/{i}.pa')

            # backup #
            shutil.unpack_archive(files.input('/app/cache/backups/users.bak.zip'), files.input('/etc/users'), 'zip')
            files.remove('/app/cache/backups/users.bak.zip')
            files.cut('/app/cache/backups/commands.bak', '/etc/commands')
            files.cut('/app/cache/backups/guest.bak', '/etc/guest')
            files.cut('/app/cache/backups/gui.bak', '/etc/gui')
            files.cut('/app/cache/backups/hostname.bak', '/etc/hostname')
            files.cut('/app/cache/backups/interface.bak', '/etc/interface')
            files.cut('/app/cache/backups/modules.bak', '/etc/modules')
            files.cut('/app/cache/backups/permtab.bak', '/etc/permtab')
            files.cut('/app/cache/backups/sudoers.bak', '/etc/sudoers')
            files.cut('/app/cache/backups/profile.sa.bak', '/etc/profile.sa')
            files.cut('/app/cache/backups/time.bak', '/etc/time')
        else:
            colors.show("paye", "perm", "")

    ##  remove a mirror ##
    def remove (self,name):
        permissions = Permissions()
        files = Files()
        colors = Colors()
        if permissions.check_root(files.readall("/proc/info/su")):
            files.remove(f'/app/mirrors/{name}')
        else:
            colors.show("paye", "perm", "")
# res #
class Res:
    def __init__(self):
        pass
    # get app data #
    def etc (self,app,name):
        control = Control()
        return control.read_record(name,f"/usr/share/applications/{app}.desk")

    # Check lang #

    def lang (self,str):

        # en
        if str.lower().startswith ('a')\
                or str.startswith ('b')\
                or str.startswith ('c')\
                or str.startswith ('d')\
                or str.startswith ('e')\
                or str.startswith ('f')\
                or str.startswith ('g')\
                or str.startswith ('h')\
                or str.startswith ('i')\
                or str.startswith ('j')\
                or str.startswith ('k')\
                or str.startswith ('l')\
                or str.startswith ('m')\
                or str.startswith ('n')\
                or str.startswith ('o')\
                or str.startswith ('p')\
                or str.startswith ('q')\
                or str.startswith ('r')\
                or str.startswith ('s')\
                or str.startswith ('t')\
                or str.startswith ('u')\
                or str.startswith ('v')\
                or str.startswith ('w')\
                or str.startswith ('x')\
                or str.startswith ('y')\
                or str.startswith ('z'):
            return 'en'
        elif str.lower().startswith ('آ')\
                or str.startswith ('ا')\
                or str.startswith ('ب')\
                or str.startswith ('پ')\
                or str.startswith ('ت')\
                or str.startswith ('ث')\
                or str.startswith ('ج')\
                or str.startswith ('چ')\
                or str.startswith ('ح')\
                or str.startswith ('خ')\
                or str.startswith ('د')\
                or str.startswith ('ذ')\
                or str.startswith ('ر')\
                or str.startswith ('ز')\
                or str.startswith ('ژ')\
                or str.startswith ('س')\
                or str.startswith ('ش')\
                or str.startswith ('ص')\
                or str.startswith ('ض')\
                or str.startswith ('ط')\
                or str.startswith ('ظ')\
                or str.startswith ('ع')\
                or str.startswith ('غ')\
                or str.startswith ('ک')\
                or str.startswith ('گ')\
                or str.startswith ('ل')\
                or str.startswith ('م')\
                or str.startswith ('ن')\
                or str.startswith ('و')\
                or str.startswith ('ه')\
                or str.startswith ('ی'):
            return 'fa'
        else:
            # for latest update
            return 'en'

    # layout #
    def key (self,str):
        control = Control()
        files = Files()
        layout = control.read_record('layout', '/etc/gui')

        if not files.isfile(f'/usr/share/locales/{layout}.locale'):
            layout = 'en'

        data = f'/usr/share/locales/{layout}.locale'

        return str.replace ('0',control.read_record('0',data)).replace('1', control.read_record('1', data)).replace('2', control.read_record('2', data)).replace('3', control.read_record('3', data)).replace('4', control.read_record('4', data)).replace('5', control.read_record('5', data)).replace('6', control.read_record('6', data)).replace('7', control.read_record('7', data)).replace('8', control.read_record('8', data)).replace('9', control.read_record('9', data)).replace('A', control.read_record('A', data)).replace('B', control.read_record('B', data)).replace('C', control.read_record('C', data)).replace('D', control.read_record('D', data)).replace('E', control.read_record('E', data)).replace('F', control.read_record('F', data)).replace('G', control.read_record('G', data)).replace('H', control.read_record('H', data)).replace('I', control.read_record('I', data)).replace('J', control.read_record('J', data)).replace('K', control.read_record('K', data)).replace('L', control.read_record('L', data)).replace('M', control.read_record('M', data)).replace('N', control.read_record('N', data)).replace('O', control.read_record('O', data)).replace('P', control.read_record('P', data)).replace('Q', control.read_record('Q', data)).replace('R',control.read_record('R', data)).replace('S', control.read_record('S', data)).replace('T', control.read_record('T', data)).replace('U', control.read_record('U', data)).replace('V', control.read_record('V', data)).replace('W', control.read_record('W', data)).replace('X', control.read_record('X', data)).replace('Y', control.read_record('Y', data)).replace('Z', control.read_record('Z', data)).replace('a', control.read_record('a', data)).replace('b', control.read_record('b', data)).replace('c', control.read_record('c', data)).replace('d', control.read_record('d', data)).replace('e', control.read_record('e', data)).replace('f', control.read_record('f', data)).replace('g', control.read_record('g', data)).replace('h', control.read_record('h', data)).replace('i', control.read_record('i', data)).replace('j', control.read_record('j', data)).replace('k', control.read_record('k', data)).replace('l', control.read_record('l', data)).replace('m', control.read_record('m', data)).replace('n', control.read_record('n', data)).replace('o', control.read_record('o', data)).replace('p', control.read_record('p', data)).replace('q', control.read_record('q', data)).replace('r', control.read_record('r', data)).replace('s', control.read_record('s', data)).replace('t', control.read_record('t', data)).replace('u', control.read_record('u', data)).replace('v', control.read_record('v', data)).replace('w', control.read_record('w', data)).replace('x', control.read_record('x', data)).replace('y', control.read_record('y', data)).replace('z', control.read_record('z', data)).replace('~', control.read_record('~', data)).replace('`', control.read_record('`', data)).replace('!', control.read_record('!', data)).replace('@', control.read_record('@', data)).replace('#', control.read_record('#', data)).replace('$', control.read_record('$', data)).replace('%', control.read_record('%', data)).replace('^', control.read_record('^', data)).replace('&', control.read_record('&', data)).replace('*', control.read_record('*', data)).replace('(', control.read_record('(', data)).replace(')', control.read_record(')', data)).replace('-', control.read_record('-', data)).replace('_', control.read_record('_', data)).replace('+', control.read_record('+', data)).replace('=', control.read_record('=', data)).replace('{', control.read_record('{', data)).replace('}', control.read_record('}', data)).replace('[', control.read_record('[', data)).replace(']', control.read_record(']', data)).replace('\\', control.read_record('\\', data)).replace('|', control.read_record('|', data)).replace(';', control.read_record(';', data)).replace('\'', control.read_record('\'', data)).replace('"', control.read_record('"', data)).replace('<', control.read_record('<', data)).replace('>', control.read_record('>', data)).replace(',', control.read_record(',', data)).replace('.', control.read_record('.', data)).replace('/', control.read_record('/', data)).replace('?', control.read_record('?', data))

    # get translated number #
    def num (self,number):
        control = Control()
        files = Files()

        locale = control.read_record('locale','/etc/gui')

        if not files.isfile(f"/usr/share/locales/{control.read_record('locale','/etc/gui')}.locale"):
            locale = 'en'

        tnumber = ''
        for i in str(number):
            if i.isdigit():
                tnumber += i.replace(i,control.read_record(i,f'/usr/share/locales/{locale}.locale'))
            else:
                tnumber += i

        return tnumber

    # get resource #
    def get(self,filename):
        control = Control()
        files = Files()
        if not filename == None:
            filename = filename.split("/")  # @widget:barge

            share = filename[0]
            name = filename[1]

            ## Real Resource ##
            if share.startswith("@layout"):
                try:
                    return files.input(f"/usr/share/layouts/{name}.ui")
                except:
                    return ''

            elif share.startswith("@background"):
                if files.isfile(f"/usr/share/backgrounds/{name}.svg"):
                    return files.input(
                            f"/usr/share/backgrounds/{name}.svg")
                elif files.isfile(
                        f"/usr/share/backgrounds/{name}.png"):
                    return files.input(
                        f"/usr/share/backgrounds/{name}.png")
                elif files.isfile(
                        f"/usr/share/backgrounds/{name}.jpg"):
                    return files.input(
                        f"/usr/share/backgrounds/{name}.jpg")
                elif files.isfile(
                        f"/usr/share/backgrounds/{name}.jpeg"):
                    return files.input(
                       f"/usr/share/backgrounds/{name}.jpeg")
                elif files.isfile(
                        f"/usr/share/backgrounds/{name}.gif"):
                    return files.input(
                       f"/usr/share/backgrounds/{name}.gif")
                elif files.isfile(
                        f"/usr/share/backgrounds/{name}.tif"):
                    return files.input(
                       f"/usr/share/backgrounds/{name}.tif")
                else:
                    return ''

            elif share.startswith("@image"):
                if files.isfile( f"/usr/share/images/{name}.svg"):
                    return files.input(
                        f"/usr/share/images/{name}.svg")
                elif files.isfile(
                        f"/usr/share/images/{name}.png"):
                    return files.input(
                        f"/usr/share/images/{name}.png")
                elif files.isfile(
                        f"/usr/share/images/{name}.jpg"):
                    return files.input(
                        f"/usr/share/images/{name}.jpg")
                elif files.isfile(
                        f"/usr/share/images/{name}.jpeg"):
                    return files.input(
                       f"/usr/share/images/{name}.jpeg")
                elif files.isfile(
                        f"/usr/share/images/{name}.gif"):
                    return files.input(
                        f"/usr/share/images/{name}.gif")
                elif files.isfile(
                        f"/usr/share/images/{name}.tif"):
                    return files.input(
                        f"/usr/share/images/{name}.tif")
                else:
                    return ''

            elif share.startswith("@app"):
                try:
                    return files.input(f"/usr/share/applications/{name}.desk")
                except:
                    return ''

            elif share.startswith("@widget"):
                try:
                    return files.input(f"/usr/share/widgets/{name}.desk")
                except:
                    return ''

            elif share.startswith("@shell"):
                try:
                    return files.input(f"/usr/share/shells/{name}.desk")
                except:
                    return ''

            elif share.startswith("@icon"):
                if files.isfile(f"/usr/share/icons/{name}.svg"):
                    return files.input(f"/usr/share/icons/{name}.svg")
                elif files.isfile(f"/usr/share/icons/{name}.png"):
                    return files.input(f"/usr/share/icons/{name}.png")
                elif files.isfile(f"/usr/share/icons/{name}.gif"):
                    return files.input(f"/usr/share/icons/{name}.gif")
                elif files.isfile(f"/usr/share/icons/{name}.tif"):
                    return files.input(f"/usr/share/icons/{name}.tif")
                else:
                    return ''

            elif share.startswith('@temp'):
                if files.isfile(f"/usr/share/templates/{name}" ):
                    return f"/usr/share/templates/{name}"
                elif files.isdir(f"/usr/share/templates/{name}" ):
                    return f"/usr/share/templates/{name}"
                else:
                    return ''

            elif share.startswith("@string"):
                locale = control.read_record("locale", "/etc/gui")
                id = files.readall("/proc/info/id")

                ## Set default lang ##
                if locale == None: locale = "en"

                ## Get value from string ##
                result = control.read_record(f'{id.replace(".desk", "")}.{name}',
                                             f"/usr/share/locales/{locale}.locale")

                ## Find default ##
                if result == None:
                    result = control.read_record(f'{id.replace(".desk", "")}.{name}',
                                                 f"/usr/share/locales/en.locale")

                return result

            ## None Resource ##
            else:
                return ''
        else:
            return ''
# system #
class System:
    def __init__(self,cmd):
        prompt = [sys.executable,'vmabr.pyc', 'exec']
        cmdln = cmd.split(" ")

        if '' in cmdln:
            cmdln.remove('')

        for i in cmdln:
            prompt.append(i)

        subprocess.call(prompt)
# app #
class App:
    ## Start ID Process ##
    def __init__(self):
        pass
    def start(self,id):
        files = Files()

        ## Check exists ##
        if files.isfile(f'/proc/id/{id}'):
            pass


        ## Create id ##
        files.create(f"/proc/id/{id}")

        ## Check desktop shortcut ##
        if files.isfile(f"/usr/share/applications/{id}"):
            files.copy(f"/usr/share/applications/{id}.desk",
                       f"/proc/id/{id}")  # Copy all informations about this GUI application

        ## Set default id ##
        files.write("/proc/info/id", id)

    ## Check id ##
    def check(self,id):
        files = Files()

        return files.isfile(f'/proc/id/{id}')

    ## End id ##
    def end(self,id):
        files = Files()

        if files.isfile(f'/proc/id/{id}'):
            ## Remove id ##
            files.remove(f"/proc/id/{id}")

    ## Shut id ##
    def shut(self):
        files = Files()

        default = files.readall("/proc/info/id")
        if files.isfile(f"/proc/id/{default}"):
            self.end(default)

    ## Endall id ##
    def endall(self):
        files = Files()
        self.switch('desktop')
        for i in files.list("/proc/id"):
            if files.isfile(f'/proc/id/{i}'):
                files.remove(f'/proc/id/{i}')

    ## Switch id process ##
    def switch(self,id):
        files = Files()

        if files.isfile(f'/proc/id/{id}'):
            files.write("/proc/info/id", id)

    ## Check application ##
    def exists (self,app):
        files = Files()

        return files.isfile(f'/usr/share/applications/{app}.desk')

# process #

class Process:
    def __init__(self):
        pass
    def processor(self):
        files = Files()

        j = 0
        if not files.isfile(f"/proc/{str(0)}"):
            files.create(f"/proc/{str(0)}")
            j = j + 1
        else:
            list = files.list("/proc")
            list.remove('id')
            list.remove('info')

            for i in list:
                if files.isfile(f"/proc/{i}"):

                    files.create(f"/proc/{str(int(i) + 1)}")
                    j = j + 1
                else:
                    files.create(f"/proc/{i}")

        if files.isfile("/proc/1"):
            files.write("/proc/info/sp", str(j))
            return j
        else:
            files.write("/proc/info/sp", str(j - 1))
            return j - 1

    ## Check switched process ##
    def check(self,switch):
        files = Files()

        if not files.isfile(f"/proc/{str(switch)}"):
            sys.exit(0)
        else:
            if files.isfile("/proc/info/sp"): files.remove("/proc/info/sp")
            files.write("/proc/info/sp", str(switch))

    ## End switched process ##
    def end(self,switch):
        files = Files()

        if files.isfile("/proc/info/sp"): files.remove("/proc/info/sp")
        if files.isfile(f"/proc/{str(switch)}"):
            files.remove(f"/proc/{str(switch)}")
            sys.exit(0)

    ## Endall all switched processes ##
    def endall(self):
        files = Files()

        if files.isfile("/proc/info/sp"): files.remove("/proc/info/sp")
        list = files.list("/proc")
        list.remove("id")
        list.remove("info")
        for i in list:
            files.remove(f"/proc/{str(i)}")

# permissions #
class Permissions:


    def __init__(self):
        pass
    ## Create permissions ##
    def create(self,name, user, others, guest, owner):
        files = Files()
        control = Control()
        if files.isfile(name) or files.isdir(name):
            ## Learned by Guru99 2020 ##
            ## Set user permissions section
            if user == 0:
                user = "---"
            elif user == 1:
                user = "--x"
            elif user == 2:
                user = "-w-"
            elif user == 3:
                user = "-wx"
            elif user == 4:
                user = "r--"
            elif user == 5:
                user = "r-x"
            elif user == 6:
                user = "rw-"
            elif user == 7:
                user = "rwx"
            else:
                user = "rwx"

            ## Set other users permissions section
            if others == 0:
                others = "---"
            elif others == 1:
                others = "--x"
            elif others == 2:
                others = "-w-"
            elif others == 3:
                others = "-wx"
            elif others == 4:
                others = "r--"
            elif others == 5:
                others = "r-x"
            elif others == 6:
                others = "rw-"
            elif others == 7:
                others = "rwx"
            else:
                others = "rwx"

            ## Set guest user permissions section
            if guest == 0:
                guest = "---"
            elif guest == 1:
                guest = "--x"
            elif guest == 2:
                guest = "-w-"
            elif guest == 3:
                guest = "-wx"
            elif guest == 4:
                guest = "r--"
            elif guest == 5:
                guest = "r-x"
            elif guest == 6:
                guest = "rw-"
            elif guest == 7:
                guest = "rwx"
            else:
                guest = "rwx"

            if files.isdir(name):
                control.write_record(name, f"d{user}{others}{guest}/{owner}",
                                     "/etc/permtab")  # Write permissions for this directory
            else:
                control.write_record(name, f"-{user}{others}{guest}/{owner}",
                                     "/etc/permtab")  # Write permissions for this file

    def exists(self,name):
        control = Control()
        perms = control.read_record(name, "/etc/permtab")  ## get permissions
        if perms == None:
            return False
        else:
            return True

    ## This function e.g. drwxrwxrwx/root --> 777 ##
    def show_number(self,perm):

        perm = perm.split("/")
        #owner = perm[1]
        perms = perm[0]

        #dirfile = perms[0]
        user_r = perms[1]
        user_w = perms[2]
        user_x = perms[3]
        others_r = perms[4]
        others_w = perms[5]
        others_x = perms[6]
        guest_r = perms[7]
        guest_w = perms[8]
        guest_x = perms[9]

        user = f"{user_r}{user_w}{user_x}"
        others = f"{others_r}{others_w}{others_x}"
        guest = f"{guest_r}{guest_w}{guest_x}"

        if user == '---':
            user = 0
        elif user == '--x':
            user = 1
        elif user == '-w-':
            user = 2
        elif user == '-wx':
            user = 3
        elif user == 'r--':
            user = 4
        elif user == 'r-x':
            user = 5
        elif user == 'rw-':
            user = 6
        elif user == 'rwx':
            user = 7

        if others == '---':
            others = 0
        elif others == '--x':
            others = 1
        elif others == '-w-':
            others = 2
        elif others == '-wx':
            others = 3
        elif others == 'r--':
            others = 4
        elif others == 'r-x':
            others = 5
        elif others == 'rw-':
            others = 6
        elif others == 'rwx':
            others = 7

        if guest == '---':
            guest = 0
        elif guest == '--x':
            guest = 1
        elif guest == '-w-':
            guest = 2
        elif guest == '-wx':
            guest = 3
        elif guest == 'r--':
            guest = 4
        elif guest == 'r-x':
            guest = 5
        elif guest == 'rw-':
            guest = 6
        elif guest == 'rwx':
            guest = 7

        return  int(f"{str(user)}{str(others)}{str(guest)}")

    ## This function correct at all ##
    def get_permissions(self,name):
        files = Files()
        control = Control()
        perms = control.read_record(name, "/etc/permtab")  ## get permissions
        if not perms == None:
            return perms
        else:
            ## Father permtab ##
            if files.isdir(name):
                dirfile = "d"
            else:
                dirfile = "-"

            ## The most important part of father permtab ##
            names = name.split("/")

            while not self.exists(name):
                l = len(names) - 1
                names.pop(l)
                name = ""
                for i in names:
                    name += f"/{i}"
                name = name.replace("//", "/")

            perm = (control.read_record(name, "/etc/permtab")).split("/")
            owner = perm[1]
            perms = perm[0]
            user_r = perms[1]
            user_w = perms[2]
            user_x = perms[3]
            others_r = perms[4]
            others_w = perms[5]
            others_x = perms[6]
            guest_r = perms[7]
            guest_w = perms[8]
            guest_x = perms[9]
            return f"{dirfile}{user_r}{user_w}{user_x}{others_r}{others_w}{others_x}{guest_r}{guest_w}{guest_x}/{owner}"

    ## This function correct at all ##
    def check(self,name, request, user):
        files = Files()
        control = Control()

        perm = (self.get_permissions(name)).split("/")

        perms = perm[0]
        owner = perm[1]

        #dirfile = perms[0]
        user_r = perms[1]
        user_w = perms[2]
        user_x = perms[3]
        others_r = perms[4]
        others_w = perms[5]
        others_x = perms[6]
        guest_r = perms[7]
        guest_w = perms[8]
        guest_x = perms[9]

        if user == "root":
            ## Check exists user ##
            if files.isfile(f"/etc/users/{user}"):
                return True
            else:
                return False

        elif user == "guest":
            enable_cli = control.read_record("enable_cli", "/etc/guest")
            if enable_cli == "Yes":
                if owner == user:
                    if request == "r":
                        r = user_r
                        if r == "r":
                            return True
                        else:
                            return False
                    elif request == "w":
                        w = user_w
                        if w == "w":
                            return True
                        else:
                            return False
                    elif request == "x":
                        x = user_x
                        if x == "x":
                            return True
                        else:
                            return False
                    else:
                        return False
                else:
                    if request == "r":
                        r = guest_r
                        if r == "r":
                            return True
                        else:
                            return False
                    elif request == "w":
                        w = guest_w
                        if w == "w":
                            return True
                        else:
                            return False
                    elif request == "x":
                        x = guest_x
                        if x == "x":
                            return True
                        else:
                            return False
                    else:
                        return False
            else:
                return False
        else:
            ## Check exists user ##
            if files.isfile(f"/etc/users/{user}"):
                    if owner == user:
                        if request == "r":
                            r = user_r
                            if r == "r":
                                return True
                            else:
                                return False
                        elif request == "w":
                            w = user_w
                            if w == "w":
                                return True
                            else:
                                return False
                        elif request == "x":
                            x = user_x
                            if x == "x":
                                return True
                            else:
                                return False
                        else:
                            return False
                    else:
                        if request == "r":
                            r = others_r
                            if r == "r":
                                return True
                            else:
                                return False
                        elif request == "w":
                            w = others_w
                            if w == "w":
                                return True
                            else:
                                return False
                        elif request == "x":
                            x = others_x
                            if x == "x":
                                return True
                            else:
                                return False
                        else:
                            return False
            else:
                return False

    ## Get owner ##
    def get_owner(self,filename):

        perm = self.get_permissions(filename)

        return perm.split("/")[1]

    ## Check owner ##
    def check_owner(self,filename, user): 
        files = Files()
        control = Control()

        owner = self.get_owner(filename)
        if user == "guest":
            enable_cli = control.read_record("enable_cli", "/etc/guest")
            if enable_cli == "Yes":
                if owner == user:
                    return True
                else:
                    return False
            else:
                return False
        elif user == "root":
            if files.isfile(f"/etc/users/{user}"):
                return True
            else:
                return False
        else:
            if files.isfile(f"/etc/users/{user}"):
                    if owner == user:
                        return True
                    elif owner == "guest":
                        return True
                    else:
                        return False
            else:
                return False

    ## Check root ##
    def check_root(self,user):
        files = Files()

        if user == "root" and files.isfile(f"/etc/users/{user}"):
            return True
        else:
            return False
# modules #
class Modules:
    def __init__(self):
        pass

    def get_modules(self):

        file = open("etc/modules")
        strv = file.read()
        file.close()
        for i in strv.split("\n"):
            sys.path.append(f"./{i}")

    ## Import module ##
    def run_module(self,module):
        ## split ##
        m = module.split('/')
        m.pop(0)

        strv = ''

        for i in m:
            strv += i

        importlib.import_module(strv)

# files #
class Files:
    def __init__(self):
        pass

    def input(self, filename):
        f = open ('proc/info/pwd','r')
        pwd = f.read()
        f.close()

        if filename.startswith("/"):
            return f"./{filename}"
        else:
            return f"./{pwd}/{filename}"

    def input_exec(self,filename):
        x = self.input(filename.replace("./", "")).replace(".//", "").replace("/", ".")

        if x.startswith('.////'):
            x = x.replace('.////', '/')

        return x

    def output(self,filename):
        if filename.startswith ('/'):
            return filename
        else:
            x = self.input(filename)

            if x.startswith ('./'):
                x = x.replace ('./','/')

            if x.startswith ('////'):
                x = x.replace ('////','/')
            elif x.startswith ('///'):
                x = x.replace ('///','/')
            elif x.startswith ('//'):
                x = x.replace ('//','/')
            elif x.startswith ('/'):
                x = x.replace ('/','/')
                
            return x


    def create(self,filename):
        open(self.input(filename), "w")

    def readall(self,filename):
        file = open(self.input(filename), "rb")
        check_bin = file.read().decode('latin-1')
        file.close()
        if check_bin.__contains__("\00"):
            return check_bin
        else:
            file = open(self.input(filename), "r", encoding='utf-8')
            strv = file.read()
            file.close()
            return strv

    def write(self,filename, text):
        file = open(self.input(filename), "w")
        file.write(text)
        file.close()

    def append(self,filename, text):
        file = open(self.input(filename), "a")
        file.write(text)
        file.close()

    def isfile(self,filename):
        return os.path.isfile(self.input(filename))

    def isdir(self,dirname):
        return os.path.isdir(self.input(dirname))

    def mkdir(self,dirname):
        os.mkdir(self.input(dirname))

    def makedirs(self,dirname):
        os.makedirs(self.input(dirname))

    def remove(self,filename):
        os.remove(self.input(filename))

    def rmdir(self,dirname):
        os.rmdir(self.input(dirname))

    def removedirs(self,dirname):
        shutil.rmtree(self.input(dirname))

    def copy(self,src, dest):
        shutil.copyfile(self.input(src), self.input(dest))

    def cut(self,src, dest):
        shutil.copyfile(self.input(src), self.input(dest))
        os.remove(self.input(src))

    def copydir(self,src, dest):
        shutil.copytree(self.input(src), self.input(dest))

    def cutdir(self,src, dest):
        shutil.copytree(self.input(src), self.input(dest))
        shutil.rmtree(self.input(src))

    def list(self,path):
        if not path.startswith ('/..'):
            return os.listdir(self.input(path))
        else:
            return os.listdir(self.input(self.readall('/proc/info/pwd')))

    def parentdir(self,filename):
        file = self.input(filename)  ## Get file name

        file = file.split('/')
        file.pop(len(file) - 1)

        strv = ''
        for i in file:
            strv += f'/{i}'

        return strv

    def filename(self,path):
        file = (self.input(path)).split('/')

        return file[len(file) - 1]
# control #
class Control:

    def __init__(self):
        pass

    def read_record(self,name, filename):
        files = Files()
        for i in (files.readall(filename)).split("\n"):
            if i.startswith(name):
                i = i.split(": ")
                if i[0] == (name):
                    return i[1]

    def read_list(self,filename):
        files = Files()
        return (files.readall(filename)).split("\n")

    def write_record(self,name, value, filename):
        files = Files()
        all = files.readall(filename)
        record = self.read_record(name, filename)
        files.remove(filename)
        if not (record == None):
            all = all.replace(f"\n{name}: {record}", "")

        files.write(filename, f"{all}\n{name}: {value}")

    def remove_record(self,name, filename):
        files = Files()
        all = files.readall(filename)
        record = self.read_record(name, filename)
        files.remove(filename)
        if not (record == None):
            all = all.replace(f"{name}: {record}", "")
            
        files.write(filename, all)

    def remove_item(self,name, filename):
        files = Files()
        strv = ""
        for i in self.read_list(filename):
            if i == name:
                strv += "\n"
            else:
                strv += "\n{i}"
        files.write(filename, strv)

# colors #
class Colors:
    def __init__(self):
        pass

    def show(self,process_name, process_type, process_message):
        if process_type == "fail":
            print(f'{colored(f"{process_name}: error: {process_message}","red")}')
        elif process_type == "perm":
            print(f'{colored(f"{process_name}: error: Permission denied.","red")}')
        elif process_type == "warning":
            print(f'{colored(f"{process_name}: warning: {process_message}","yellow")}')

class Message:
    def __init__(self):
        pass

    def send (self,giver,message):
        colors = Colors()
        files = Files()
        control = Control()

        user = files.readall('/etc/hostname')
        password = files.readall('/etc/shadow')

        x = requests.post(control.read_record('send','/etc/cloud'),data={"sender":user,"password":password,"giver":giver,"message":message})

        if x.text == 'e: unknown sender':
            colors.show('send','fail',f'{user}: unknown sender')
        elif x.text == 'e: wrong password':
            colors.show('send','fail',f'{user}: wrong password')
        elif x.text == 'e: unknown giver':
            colors.show('send','fail',f'{user}: unknown giver')
        else:
            '''
            try:
                files.makedirs(f'/app/messages/{giver}')
            except:
                pass

            try:
                files.write (f'/app/messages/{giver}/{str(datetime.datetime.now()).strftime("%Y,%m,%d,%H,%M,%S")}.me',message)
            except:
                pass
            '''

    def receive (self):
        colors = Colors()
        control = Control()
        files = Files()

        user = files.readall('/etc/hostname')
        shadow = files.readall('/etc/shadow')

        x = requests.post(control.read_record('receive','/etc/cloud'),data={"giver":user,"password":shadow})

        if x.text == 'e: unknown giver':
            colors.show('receive','fail',f'{user}: unknown giver')
        elif x.text == 'e: wrong password':
            colors.show('receive','fail',f'{user}: wrong password')
        else:
            files.write ('/app/inbox',x.text)

            file = open (files.input('/app/inbox'),"r")
            listm = (file.read()).split("@xsms@")
            file.close()

            if '' in listm:
                listm.remove('')

            files.remove('/app/inbox')

            for i in listm:
                splitor = i.split('@sms@')
                head = splitor[0]
                file = splitor[1]
                data = splitor[2]

                sender = head.split('/')[0]
                giver = head.split('/')[2]
                
                try:
                    files.makedirs(f'/app/messages/{sender}')
                except:
                    pass

                try:
                    files.write(f'/app/messages/{sender}/{file}',data)
                except:
                    pass
