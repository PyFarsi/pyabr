#######################################################################################
#  In the name of God, the Compassionate, the Merciful
#  Pyabr (c) 2020 Mani Jamali. GNU General Public License v3.0
#
#  Official Website: 		http://pyabr.rf.gd
#  Programmer & Creator:    Mani Jamali <manijamali2003@gmail.com>
#  Gap channel: 			@pyabr
#  Gap group:   			@pyabr_community
#  Git source:              github.com/PyFarsi/pyabr
#
#######################################################################################

import importlib, shutil, os, sys, hashlib, subprocess,time,datetime,getpass,py_compile,wget,requests

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
        all = all.replace("\n"+name + ": " + record, "")
    file = open(filename,'w')
    file.write(all + "\n" + name + ": " + value)
    file.close()

# script #
class Script:
    def __init__(self,filename):
        self.permissions = Permissions()
        self.colors = Colors()
        self.files = Files()
        self.control = Control()

        # check perms #
        if not self.permissions.check(self.files.output(filename) + '.sa', "x", self.files.readall("/proc/info/su")):
            self.colors.show(filename, "perm", "")
            sys.exit(0)

        k = 0

        for cmd in  self.control.read_list(filename + '.sa'):
            k = k + 1
            ## Create cmdln with variables ##

            cmdln = cmd.split(" ")

            strcmdln = ""

            for i in cmdln:
                if str(i).startswith("$"):
                    select = self.files.readall("/proc/info/sel")
                    var = self.control.read_record(str(i).replace("$", ""), select)
                    if var == None:
                        strcmdln = strcmdln + " " + i
                    else:
                        strcmdln = strcmdln + " " + var
                else:
                    strcmdln = strcmdln + " " + i

            cmdln = strcmdln.split(" ")
            cmdln.remove('')

            cmd = ""
            for j in cmdln:
                cmd = cmd + " " + j

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
        self.files = Files()
        self.colors = Colors()
        self.process = Process()
        self.control = Control()
        self.permissions = Permissions()
        self.res = Res()
        self.app = App()

    # start #
    
    def start (self,args):
        if args==[]:
            self.colors.show ('start','fail','no inputs.')
            sys.exit(0)
        if self.files.isfile (f'/usr/share/applications/{args[0]}.desk'):
            self.files.write('/tmp/start.tmp',args[0])
        else:
            self.colors.show('start', 'fail', f'{args[0]}: application not found.')

    def cl (self,args):

        if args==[]:
            self.colors.show ('cl','fail','no inputs.')
            sys.exit(0)

        self.files.write('/tmp/cloud.tmp',args[0])

    # kill process #
    def kill (self,args):

        for i in args:
            if self.app.check(i):
                self.app.end(i)
            else:
                self.colors.show ('kill','fail',f'{i}: id process not found.')

    # un set a variable
    def unset(self,args):
        for name in args:
            if not (self.files.readall("/proc/info/sel")).startswith("/proc/"):
                if self.permissions.check(self.files.output(self.files.readall("/proc/info/sel")), "w", self.files.readall("/proc/info/su")):
                    self.control.remove_record(name, self.files.readall("/proc/info/sel"))
                else:
                    self.colors.show("unset", "perm", "")
            else:
                self.control.remove_record(name, self.files.readall("/proc/info/sel"))

    # pause
    def pause (self,args):
        self.sleep(['1000000'])

    # add controller data base
    def add (self,args):
        for i in args:
            x = (self.files.readall(i)).split('\n')
            for j in x:
                if j.__contains__(': '):
                    s = j.split(': ')
                    self.set([s[0]+":",s[1]])
    # zip #
    def zip (self, args):

        if args==[]:
            self.colors.show ('zip','fail','no inputs.')
            sys.exit(0)

        src = args[0]

        if args[1:]==[]:
            dest = src
        else:
            dest = args[1]

        if not self.files.isdir (src):
            self.colors.show('zip', 'fail', f'{src}: source directory not found.')
            sys.exit(0)

        if self.files.isdir (dest+".zip"):
            self.colors.show('zip', 'fail', f'{dest+".zip"}: dest is not a archive file.')
            sys.exit(0)

        if self.files.isfile (dest+".zip"):
            self.colors.show('zip', 'warning', f'{dest+".zip"}: dest archives exists.')

        if self.permissions.check(self.files.output(src), "r", self.files.readall("/proc/info/su")) and self.permissions.check(self.files.output(dest+'.zip'), "w", self.files.readall("/proc/info/su")):
            shutil.make_archive(self.files.input(dest),'zip',self.files.input(src))
        else:
            self.colors.show('zip', 'perm', '')
            sys.exit(0)

    # zip #
    def tar (self, args):
        if args==[]:
            self.colors.show ('tar','fail','no inputs.')
            sys.exit(0)

        src = args[0]

        if args[1:]==[]:
            dest = src
        else:
            dest = args[1]

        if not self.files.isdir (src):
            self.colors.show('tar', 'fail', f'{src}: source directory not found.')
            sys.exit(0)

        if self.files.isdir (dest+".tar"):
            self.colors.show('tar', 'fail', f'{dest+".tar"}: dest is not a archive file.')
            sys.exit(0)

        if self.files.isfile (dest+".tar"):
            self.colors.show('tar', 'warning', f'{dest+".tar"}: dest archives exists.')

        if self.permissions.check(self.files.output(src), "r", self.files.readall("/proc/info/su")) and self.permissions.check(self.files.output(dest+'.tar'), "w", self.files.readall("/proc/info/su")):
            shutil.make_archive(self.files.input(dest),'tar',self.files.input(src))
        else:
            self.colors.show('tar', 'perm', '')
            sys.exit(0)

    # pwd #
    def pwd (self,args):
        print (self.files.readall('/proc/info/pwd'))

    # zip #
    def xzip (self, args):
        if args==[]:
            self.colors.show ('xzip','fail','no inputs.')
            sys.exit(0)

        src = args[0]

        if args[1:]==[]:
            dest = src
        else:
            dest = args[1]

        if not self.files.isdir (src):
            self.colors.show('xzip', 'fail', f'{src}: source directory not found.')
            sys.exit(0)

        if self.files.isdir (dest+".tar.xz"):
            self.colors.show('xzip', 'fail', f'{dest+".tar.xz"}: dest is not a archive file.')
            sys.exit(0)

        if self.files.isfile (dest+".tar.xz"):
            self.colors.show('xzip', 'warning', f'{dest+".tar.xz"}: dest archives exists.')

        if self.permissions.check(self.files.output(src), "r", self.files.readall("/proc/info/su")) and self.permissions.check(self.files.output(dest+'.tar.xz'), "w", self.files.readall("/proc/info/su")):
            shutil.make_archive(self.files.input(dest),'xztar',self.files.input(src))
        else:
            self.colors.show('xzip', 'perm', '')
            sys.exit(0)

    # zip #
    def gzip (self, args):
        if args==[]:
            self.colors.show ('gzip','fail','no inputs.')
            sys.exit(0)

        src = args[0]

        if args[1:]==[]:
            dest = src
        else:
            dest = args[1]

        if not self.files.isdir (src):
            self.colors.show('gzip', 'fail', f'{src}: source directory not found.')
            sys.exit(0)

        if self.files.isdir (dest+".tar.gz"):
            self.colors.show('gzip', 'fail', f'{dest+".tar.gz"}: dest is not a archive file.')
            sys.exit(0)

        if self.files.isfile (dest+".tar.gz"):
            self.colors.show('gzip', 'warning', f'{dest+".tar.gz"}: dest archive exists.')

        if self.permissions.check(self.files.output(src), "r", self.files.readall("/proc/info/su")) and self.permissions.check(self.files.output(dest+'.tar.gz'), "w", self.files.readall("/proc/info/su")):
            shutil.make_archive(self.files.input(dest),'gztar',self.files.input(src))
        else:
            self.colors.show('gzip', 'perm', '')
            sys.exit(0)

    # zip #
    def bzip (self, args):
        if args==[]:
            self.colors.show ('bzip','fail','no inputs.')
            sys.exit(0)

        src = args[0]

        if args[1:]==[]:
            dest = src
        else:
            dest = args[1]

        if not self.files.isdir (src):
            self.colors.show('bzip', 'fail', f'{src}: source directory not found.')
            sys.exit(0)

        if self.files.isdir (dest+".tar.bz2"):
            self.colors.show('bzip', 'fail', f'{dest+".tar.bz2"}: dest is not a archive file.')
            sys.exit(0)

        if self.files.isfile (dest+".tar.bz"):
            self.colors.show('bzip', 'warning', f'{dest+".tar.bz2"}: dest archive exists.')

        if self.permissions.check(self.files.output(src), "r", self.files.readall("/proc/info/su")) and self.permissions.check(self.files.output(dest+'.tar.bz2'), "w", self.files.readall("/proc/info/su")):
            shutil.make_archive(self.files.input(dest),'bztar',self.files.input(src))
        else:
            self.colors.show('bzip', 'perm', '')
            sys.exit(0)

    def unzip (self,args):

        if args == []:
            self.colors.show('unzip', 'fail', 'no inputs.')
            sys.exit(0)

        src = args[0]

        if args[1:]==[]:
            dest = src
        else:
            dest = args[1]

        if not self.files.isfile (src):
            self.colors.show('unzip', 'fail', f'{src}: source archive not found.')
            sys.exit(0)

        if self.files.isfile (dest):
            self.colors.show('unzip', 'fail', f'{dest}: dest is a file.')
            sys.exit(0)

        if self.permissions.check(self.files.output(src), "r", self.files.readall("/proc/info/su")) and self.permissions.check(self.files.output(dest), "w", self.files.readall("/proc/info/su")):
            shutil.unpack_archive(self.files.input(src),self.files.input(dest),'zip')
        else:
            self.colors.show('unzip', 'perm', '')
            sys.exit(0)

    def xunzip (self, args):

        if args == []:
            self.colors.show('xunzip', 'fail', 'no inputs.')
            sys.exit(0)

        src = args[0]

        if args[1:] == []:
            dest = src
        else:
            dest = args[1]

        if not self.files.isfile(src):
            self.colors.show('xunzip', 'fail', f'{src}: source archive not found.')
            sys.exit(0)

        if self.files.isfile(dest):
            self.colors.show('xunzip', 'fail', f'{dest}: dest is a file.')
            sys.exit(0)

        if self.permissions.check(self.files.output(src), "r", self.files.readall("/proc/info/su")) and self.permissions.check(
                self.files.output(dest), "w", self.files.readall("/proc/info/su")):
            shutil.unpack_archive(self.files.input(src), self.files.input(dest), 'xztar')
        else:
            self.colors.show('xunzip', 'perm', '')
            sys.exit(0)

    def gunzip(self, args):

        if args == []:
            self.colors.show('gunzip', 'fail', 'no inputs.')
            sys.exit(0)

        src = args[0]

        if args[1:] == []:
            dest = src
        else:
            dest = args[1]

        if not self.files.isfile(src):
            self.colors.show('gunzip', 'fail', f'{src}: source archive not found.')
            sys.exit(0)

        if self.files.isfile(dest):
            self.colors.show('gunzip', 'fail', f'{dest}: dest is a file.')
            sys.exit(0)

        if self.permissions.check(self.files.output(src), "r", self.files.readall("/proc/info/su")) and self.permissions.check(
                self.files.output(dest), "w", self.files.readall("/proc/info/su")):
            shutil.unpack_archive(self.files.input(src), self.files.input(dest), 'gztar')
        else:
            self.colors.show('gunzip', 'perm', '')
            sys.exit(0)

    def bunzip(self, args):


        if args == []:
            self.colors.show('bunzip', 'fail', 'no inputs.')
            sys.exit(0)

        src = args[0]

        if args[1:] == []:
            dest = src
        else:
            dest = args[1]

        if not self.files.isfile(src):
            self.colors.show('bunzip', 'fail', f'{src}: source archive not found.')
            sys.exit(0)

        if self.files.isfile(dest):
            self.colors.show('bunzip', 'fail', f'{dest}: dest is a file.')
            sys.exit(0)

        if self.permissions.check(self.files.output(src), "r", self.files.readall("/proc/info/su")) and self.permissions.check(
                self.files.output(dest), "w", self.files.readall("/proc/info/su")):
            shutil.unpack_archive(self.files.input(src), self.files.input(dest), 'bztar')
        else:
            self.colors.show('bunzip', 'perm', '')
            sys.exit(0)

    def untar(self, args):

        if args == []:
            self.colors.show('untar', 'fail', 'no inputs.')
            sys.exit(0)

        src = args[0]

        if args[1:] == []:
            dest = src
        else:
            dest = args[1]

        if not self.files.isfile(src):
            self.colors.show('untar', 'fail', f'{src}: source archive not found.')
            sys.exit(0)

        if self.files.isfile(dest):
            self.colors.show('untar', 'fail', f'{dest}: dest is a file.')
            sys.exit(0)

        if self.permissions.check(self.files.output(src), "r", self.files.readall("/proc/info/su")) and self.permissions.check(
                self.files.output(dest), "w", self.files.readall("/proc/info/su")):
            shutil.unpack_archive(self.files.input(src), self.files.input(dest), 'tar')
        else:
            self.colors.show('untar', 'perm', '')
            sys.exit(0)

    # cc command #
    def cc (self,args):

        if args==[]:
            colors.show('cc','fail','no inputs.')
            sys.exit(0)

        # args after checking #
        filename = args[0]
        # check file #
        type = None

        # check file #
        if not self.files.isfile (filename):
            self.colors.show ('cc','fail',filename+": file not found.")
            sys.exit(0)

        if self.files.isdir (filename):
            self.colors.show('cc','fail',filename+": is a directory.")
            sys.exit(0)

        # check permission of filename to read #
        if not self.permissions.check(self.files.output(filename), "r", self.files.readall("/proc/info/su")):
            self.colors.show('cc','perm','')
            sys.exit(0)

        if filename.endswith ('.c'):
            type = 'c'
        elif filename.endswith ('.cpp') or filename.endswith('.c++') or filename.endswith('.cxx'):
            type = 'c++'
        elif filename.endswith ('.py'):
            type = 'python'
        elif filename.endswith ('.java'):
            type = 'java'

        # compile types #
        if type=='python':
            if args[1:]==[]:
                py_compile.compile(self.files.input(filename),self.files.input(filename.replace('.py','.pyc')))
                if not self.permissions.check(self.files.output(filename.replace('.py','.pyc')), "w", self.files.readall("/proc/info/su")):
                    self.colors.show('cc', 'perm', '')
                    sys.exit(0)
            else:
                output = args[1]
                if not self.permissions.check(self.files.output(output), "w", self.files.readall("/proc/info/su")):
                    self.colors.show('cc', 'perm', '')
                    sys.exit(0)
                py_compile.compile(self.files.input(filename), self.files.input(output))


        elif type=='c':
            if args[1:] == []:
                output = filename.replace('.c','.out')
            else:
                output = args[1]+'.out'

            if not self.permissions.check(self.files.output(output), "w", self.files.readall("/proc/info/su")):
                self.colors.show('cc', 'perm', '')
                sys.exit(0)

            strv = self.control.read_record('exec.c','/etc/compiler').replace ("{src}",self.files.input(filename)).replace ("{dest}",self.files.input(output))

            strv = strv.split(" ")

            subprocess.call(strv)


        elif type=='c++':
            if args[1:] == []:
                output = filename.replace('.cpp','.out').replace('.cxx','.out').replace('.c++','.out')
            else:
                output = args[1]+'.out'

            if not self.permissions.check(self.files.output(output), "w", self.files.readall("/proc/info/su")):
                self.colors.show('cc', 'perm', '')
                sys.exit(0)

            strv = self.control.read_record('exec.c++', '/etc/compiler').replace("{src}", self.files.input(filename)).replace(
                "{dest}", self.files.input(output)).split (" ")

            subprocess.call(strv)

        elif type=='java':
            if not self.permissions.check(self.files.output(filename.replace('.java','.class')), "w", self.files.readall("/proc/info/su")):
                self.colors.show('cc', 'perm', '')
                sys.exit(0)
            strv = (self.control.read_record('class.java', '/etc/compiler').replace("{src}", self.files.input(filename).replace('.//',''))).split (' ')
            subprocess.call(strv)

        else:
            self.colors.show('cc','fail','not supported programing language.')

    # check command #
    def check (self,args):
        filename = args[0]

        perm = self.permissions.get_permissions(self.files.output(filename))
        numperm = self.permissions.show_number(perm)
        r = self.permissions.check(self.files.output(filename), "r", self.files.readall("/proc/info/su"))
        w = self.permissions.check(self.files.output(filename), "w", self.files.readall("/proc/info/su"))
        x = self.permissions.check(self.files.output(filename), "x", self.files.readall("/proc/info/su"))

        bold = self.colors.color(1, self.colors.get_bgcolor(), self.colors.get_fgcolor())

        print("   Seleted path: " + bold + self.files.output(filename) + self.colors.get_colors())
        print("     Permission: " + bold + perm + self.colors.get_colors())
        print(" Permission Num: " + bold + str(numperm) + self.colors.get_colors())
        if r == True:
            print("           Read: " + bold + self.colors.get_ok() + "Yes" + self.colors.get_colors())
        else:
            print("           Read: " + bold + self.colors.get_fail() + "No" + self.colors.get_colors())

        if w == True:
            print("          Write: " + bold + self.colors.get_ok() + "Yes" + self.colors.get_colors())
        else:
            print("          Write: " + bold + self.colors.get_fail() + "No" + self.colors.get_colors())

        if x == True:
            print("        Execute: " + bold + self.colors.get_ok() + "Yes" + self.colors.get_colors())
        else:
            print("        Execute: " + bold + self.colors.get_fail() + "No" + self.colors.get_colors())

    # chmod command #
    def chmod (self,args):

        mod = args[0]
        filename = args[1]

        if args==[] or args[1:]==[]:
            self.colors.show("chmod", "fail", "no inputs.")
            sys.exit(0)

        perm_user = int(mod[0])
        perm_others = int(mod[1])
        perm_guest = int(mod[2])
        if self.permissions.check_owner(self.files.output(filename), self.files.readall("/proc/info/su")):
            owner = self.permissions.get_owner(self.files.output(filename))
            self.permissions.create(self.files.output(filename), perm_user, perm_others, perm_guest, owner)
        else:
            self.colors.show("chmod", "perm", "")

    def mount (self,args):
        if not self.permissions.check_root(self.files.readall('/proc/info/su')):
            if not self.files.readall('/proc/info/su') in self.files.readall('/etc/sudoers'):
                self.colors.show("mount", "perm", "")
                sys.exit(0)

        if args==[]:
            self.colors.show("mount", "fail", "no inputs.")
            sys.exit(0)

        clouddrive = args[0]

        if not self.files.isfile(f'/dev/{clouddrive}'):
            self.colors.show("mount", "fail", f"{clouddrive}: cloud drive not exists.")
            sys.exit(0)

        clouddrivez = f'/dev/{clouddrive}'


        host = self.control.read_record('host',clouddrivez)
        password = self.control.read_record('password', clouddrivez)

        x = requests.post(f"{host}/{self.control.read_record('index',clouddrivez)}",data={"password":password})

        if x.text=='s: connected':
            if self.files.isdir (f'/stor/{clouddrive}'):
                self.files.removedirs(f'/stor/{clouddrive}')

            self.files.mkdir(f'/stor/{clouddrive}')
            self.commands.cd([f'/stor/{clouddrive}'])
            self.files.write('/proc/info/csel',clouddrive)

            x = requests.post(f"{host}/{self.control.read_record('list',clouddrivez)}",data={"password":password})

            split_list_items = str(x.text).split('\n')
            if '' in split_list_items:
                split_list_items.remove('')

            split_list_items.reverse()

            for item in split_list_items:
                split_remove_host = item.split("/stor/")
                myitem = split_remove_host[1]

                if myitem.endswith ('/') and not self.files.isdir (f'/stor/{clouddrive}/{myitem}'):
                    self.files.mkdir(f'/stor/{clouddrive}/{myitem}')
                else:
                    self.files.create(f'/stor/{clouddrive}/{myitem}')

        elif x.text=='e: wrong password':
            self.colors.show("mount", "fail", f"{clouddrive}: wrong password in device database.")
        elif x.text=='e: empty password':
            self.colors.show("mount", "fail", f"{clouddrive}: empty password in device database.")
        else:
            self.colors.show("mount", "fail", f"{clouddrive}: cannot connect to this cloud drive.")

    def get (self,args):


        if args==[]:
            colors.show("get", "fail", "no inputs.")
            sys.exit(0)

        url = args[0].split('/')
        addressz = url[0]
        try:
            dataz = url[1]
        except:
            dataz = 'index.xml'

        host = self.control.read_record('host', '/etc/abr')
        cloud = self.control.read_record('cloud', '/etc/abr')

        x = requests.post(f"{host}/{cloud}", data={"address": addressz,"data":dataz})

        if x.text=='e: data not found':
            self.colors.show('get', 'fail', f'{dataz}: data not found.')
        elif x.text=='e: address not found':
            self.colors.show('get', 'fail', f'{addressz}: address not found.')
        else:
            if not self.files.isdir(f'/srv/{addressz}'):
                self.files.mkdir(f'/srv/{addressz}')

            try:
                self.files.write(f'/srv/{addressz}/{dataz}',x.text)
            except:
                pass

    def umount (self,args):


        if not self.permissions.check_root(self.files.readall('/proc/info/su')):
            if not self.files.readall('/proc/info/su') in self.files.readall('/etc/sudoers'):
                self.colors.show("umount", "perm", "")
                sys.exit(0)

        if args == []:
            self.colors.show("umount", "fail", "no inputs.")
            sys.exit(0)

        clouddrive = args[0]

        if not self.files.isfile(f'/dev/{clouddrive}'):
            self.colors.show("umount", "fail", f"{clouddrive}: cloud drive not exists.")
            sys.exit(0)

        self.commands.cd (['/'])
        self.files.removedirs(f'/stor/{clouddrive}')

    # down mani:/Files/mani

    def down (self,args):

        if not self.permissions.check_root(self.files.readall('/proc/info/su')):
            if not self.files.readall('/proc/info/su') in self.files.readall('/etc/sudoers'):
                self.colors.show("down", "perm", "")
                sys.exit(0)

        if args == []:
            self.colors.show("down", "fail", "no inputs.")
            sys.exit(0)

        filename = args[0]

        clouddrive = self.files.readall('/proc/info/csel')
        clouddrivez = f'/dev/{clouddrive}'

        host = self.control.read_record('host', clouddrivez)
        password = self.control.read_record('password', clouddrivez)

        x = requests.post(f"{host}/{self.control.read_record('download',clouddrivez)}",data={"password":password,"filename":filename})

        if x.text == 'e: wrong password':
            self.colors.show("down", "fail", f"{clouddrive}: wrong password in device database.")
        elif x.text == 'e: empty password':
            self.colors.show("down", "fail", f"{clouddrive}: empty password in device database.")
        elif x.text == 'e: file not found':
            self.colors.show("down", "fail", f"{clouddrive}: {filename}: file not file in cloud drive.")
        else:
            self.files.write(f'/stor/{clouddrive}/{filename}',x.text)

    def rem (self,args):

        if not self.permissions.check_root(self.files.readall('/proc/info/su')):
            if not self.files.readall('/proc/info/su') in self.files.readall('/etc/sudoers'):
                self.colors.show("rem", "perm", "")
                sys.exit(0)

        if args == []:
            self.colors.show("rem", "fail", "no inputs.")
            sys.exit(0)

        filename = args[0]

        clouddrive = self.files.readall('/proc/info/csel')
        clouddrivez = f'/dev/{clouddrive}'

        host = self.control.read_record('host', clouddrivez)
        password = self.control.read_record('password', clouddrivez)

        x = requests.post(f"{host}/{self.control.read_record('remove',clouddrivez)}",data={"password":password,"filename":filename})

        if x.text == 'e: wrong password':
            self.colors.show("down", "fail", f"{clouddrive}: wrong password in device database.")
        elif x.text == 'e: empty password':
            self.colors.show("down", "fail", f"{clouddrive}: empty password in device database.")
        elif x.text == 'e: file not found':
            self.colors.show("down", "fail", f"{clouddrive}: {filename}: file not file in cloud drive.")
        else:
            if self.files.isfile (f'/stor/{clouddrive}/{filename}'):
                self.files.remove(f'/stor/{clouddrive}/{filename}')
            elif self.files.isdir(f'/stor/{clouddrive}/{filename}'):
                self.files.removedirs(f'/stor/{clouddrive}/{filename}')

    def mkc (self,args):

        if not self.permissions.check_root(self.files.readall('/proc/info/su')):
            if not self.files.readall('/proc/info/su') in self.files.readall('/etc/sudoers'):
                self.colors.show("mkc", "perm", "")
                sys.exit(0)

        if args == []:
            self.colors.show("mkc", "fail", "no inputs.")
            sys.exit(0)

        dirname = args[0]

        clouddrive = self.files.readall('/proc/info/csel')
        clouddrivez = f'/dev/{clouddrive}'

        host = self.control.read_record('host', clouddrivez)
        password = self.control.read_record('password', clouddrivez)

        x = requests.post(f"{host}/{self.control.read_record('directory',clouddrivez)}",data={"password":password,"dirname":dirname})

        if x.text == 'e: wrong password':
            self.colors.show("mkc", "fail", f"{clouddrive}: wrong password in device database.")
        elif x.text == 'e: empty password':
            self.colors.show("mkc", "fail", f"{clouddrive}: empty password in device database.")
        elif x.text == 'e: is a file':
            self.colors.show("mkc", "fail", f"{clouddrive}: {dirname}: cannot create directory; is a file.")
        else:
            x = f'/stor/{clouddrive}/{dirname}'
            if self.files.isfile (x):
                self.colors.show("mkc", "fail", f"{clouddrive}: {dirname}: cannot create directory; is a file.")
            elif not self.files.isdir (x):
                self.files.mkdir(x)

    def up (self,args):

        if not self.permissions.check_root(self.files.readall('/proc/info/su')):
            if not self.files.readall('/proc/info/su') in self.files.readall('/etc/sudoers'):
                self.colors.show("up", "perm", "")
                sys.exit(0)

        if args == []:
            self.colors.show("up", "fail", "no inputs.")
            sys.exit(0)

        clouddrive = self.files.readall('/proc/info/csel')
        filename = args[0]

        clouddrivez = f'/dev/{clouddrive}'

        host = self.control.read_record('host', clouddrivez)
        password = self.control.read_record('password', clouddrivez)

        data = self.files.readall(f'/stor/{clouddrive}/{filename}')

        x = requests.post(f"{host}/{self.control.read_record('upload',clouddrivez)}",data={"password":password,"filename":filename,"data":data})

        if x.text == 'e: wrong password':
            self.colors.show("up", "fail", f"{clouddrive}: wrong password in device database.")
        elif x.text == 'e: empty password':
            self.colors.show("up", "fail", f"{clouddrive}: empty password in device database.")
        elif x.text == 'e: is a directory':
            self.colors.show("up", "fail", f"{clouddrive}: {filename}: cannot create file; is a directory in cloud drive.")

    # chown #
    def chown (self,args):
        new_owner = args[0]
        name = args[1]

        if args==[]:
            self.colors.show("chown", "fail", "no inputs.")
            sys.exit(0)

        if args[1:]==[]:
            new_owner = ''

        permowner = self.permissions.check_owner(self.files.output(name), self.files.readall("/proc/info/su"))
        perm = self.permissions.get_permissions(self.files.output(name))

        num = self.permissions.show_number(perm)
        num = str(num)
        user_p = int(num[0])
        others_p = int(num[1])
        guest_p = int(num[2])

        if permowner == True:
            if new_owner == "":
                self.permissions.create(self.files.output(name), user_p, others_p, guest_p, self.files.readall("/proc/info/su"))
            else:
                self.permissions.create(self.files.output(name), user_p, others_p, guest_p, new_owner)
        else:
            self.colors.show("chown", "perm", "")

    # logout #
    def logout (self,args):

        if self.files.isfile("/proc/selected"): self.files.remove("/proc/selected")
        self.process.endall()
        subprocess.call([sys.executable,self.files.readall("/proc/info/boot"), 'login'])

    # new #
    def new (self,args):

        boot = self.files.readall("/proc/info/boot")

        user = self.control.read_record("username", "/tmp/su.tmp")
        code = self.control.read_record ("code","/tmp/su.tmp")

        if self.files.isfile("/proc/selected"): self.files.remove("/proc/selected")
        if user == "guest":
            subprocess.call([sys.executable,boot, 'user', 'guest'])
        else:
            subprocess.call([sys.executable,boot, 'user', user, code])

    # det Delete Text from a line
    def det (self,args):
        control = Control()
        files = Files()
        for i in args:
            control.remove_item(i,files.readall('/proc/info/sel'))

    # reboot #
    def reboot (self,args):


        if self.files.isfile("/proc/selected"): self.files.remove("/proc/selected")
        self.colors.show("kernel", "reboot", "")
        if self.files.isdir("/desk/guest"):
            self.files.removedirs("/desk/guest")
        if self.files.isdir("/tmp"):
            self.files.removedirs("/tmp")
            self.files.mkdir("/tmp")

        self.files.removedirs("/app/cache")
        self.files.mkdir("/app/cache")
        self.files.mkdir("/app/cache/gets")
        self.files.mkdir("/app/cache/archives")
        self.files.mkdir("/app/cache/archives/code")
        self.files.mkdir("/app/cache/archives/control")
        self.files.mkdir("/app/cache/archives/data")
        self.files.mkdir("/app/cache/archives/build")

        self.process.endall()

        if self.files.readall('/proc/info/os')=='Pyabr' and not self.files.isfile ('/.unlocked'):
            subprocess.call(['reboot'])
        else:
            subprocess.call([sys.executable,self.files.readall("/proc/info/boot")])

    # shut command #
    def shut (self,args):

        if self.files.isfile("/proc/selected"): self.files.remove("/proc/selected")
        self.process.end(int(self.files.readall("/proc/info/sp")))

        if self.files.readall("/proc/info/su") == "0":
            if self.files.isdir("/desk/guest"):
                self.files.removedirs("/desk/guest")
            if self.files.isdir("/tmp"):
                self.files.removedirs("/tmp")
                self.files.mkdir("/tmp")
            if self.files.isfile("/proc/selected"): self.files.remove("/proc/selected")
            self.process.endall()

            if self.files.readall('/proc/info/os') == 'Pyabr' and not self.files.isfile('/.unlocked'):
                subprocess.call(['poweroff'])

    # shutdown command #
    def shutdown (self,args):

        if self.files.isdir("/desk/guest"):
            self.files.removedirs("/desk/guest")
        if self.files.isdir("/tmp"):
            self.files.removedirs("/tmp")
            self.files.mkdir("/tmp")
        if self.files.isfile("/proc/selected"): self.files.remove("/proc/selected")

        self.files.removedirs("/app/cache")
        self.files.mkdir("/app/cache")
        self.files.mkdir("/app/cache/gets")
        self.files.mkdir("/app/cache/archives")
        self.files.mkdir("/app/cache/archives/code")
        self.files.mkdir("/app/cache/archives/control")
        self.files.mkdir("/app/cache/archives/data")
        self.files.mkdir("/app/cache/archives/build")

        self.process.endall()

        if self.files.readall('/proc/info/os') == 'Pyabr' and not self.files.isfile('/.unlocked'):
            subprocess.call(['poweroff'])


    # touch #
    def touch (self,args):
        for i in args:
            self.files.create(i)

    # cat command #
    def cat (self,args):
        ## args ##

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
            self.colors.show("cat", "fail", "no inputs.")
            sys.exit(0)

        ## Read files ##
        if option == '' or option == '-r':
            if self.files.isfile(name):
                if self.permissions.check(self.files.output(name), "r", self.files.readall("/proc/info/su")):
                    print(self.files.readall(name))
                else:
                    self.colors.show("cat", "perm", "")
            elif self.files.isdir(name):
                self.colors.show("cat", "fail", name + ": is a directory.")
            else:
                self.colors.show("cat", "fail", name + ": file not found.")

        ## Create files ##
        elif option == '-c':
            if self.files.isdir(name):
                self.colors.show("cat", "fail", name + ": is a directory.")
            else:
                if self.permissions.check(self.files.output(name), "w", self.files.readall("/proc/info/su")):
                    self.files.create(name)
                else:
                    self.colors.show("cat", "perm", "")

        ## Write in lines
        elif option == '-l':
            if self.files.isdir(name):
                self.colors.show("cat", "fail", name + ": is a directory.")
            else:
                if self.permissions.check(self.files.output(name), "w", self.files.readall("/proc/info/su")):
                    strv = ''
                    for i in cmdln[3:]:
                        strv+=' '+i
                    self.files.write(name,strv[1:])
                else:
                    self.colors.show("cat", "perm", "")

        ## Write into files ##
        elif option == '-w':
            if self.files.isdir(name):
                self.colors.show("cat", "fail", name + ": is a directory.")
            else:
                if self.permissions.check(self.files.output(name), "w", self.files.readall("/proc/info/su")):

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
                                texts = texts + '\n' + cmd

                    ## WRITE INTO FILE
                    self.files.write(cmdln[2], texts)
                else:
                    self.colors.show("cat", "perm", "")

        ## Write into files ##
        elif option == '-a':
            if self.files.isdir(name):
                self.colors.show("cat", "fail", name + ": is a directory.")
            else:
                if self.permissions.check(self.files.output(name), "w", self.files.readall("/proc/info/su")):

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
                                texts = texts + '\n' + cmd

                    ## WRITE INTO FILE
                    self.files.append(cmdln[2], texts)
                else:
                    self.colors.show("cat", "perm", "")

    # cd command #
    def cd (self,args):
        if args==[]:
            self.colors.show("cd", "fail", "no inputs.")
            sys.exit (0)

        path = args[0]

        if self.permissions.check(self.files.output(path), "r", self.files.readall("/proc/info/su")):
            if path.startswith ('/..'):
                self.files.write("/proc/info/pwd", '/')
            elif path == '..':
                pwd = self.files.readall('/proc/info/pwd')
                pwd = pwd.split('/')
                lens = len(pwd) - 1
                pwd.pop(lens)

                strv = ''

                for i in pwd:
                    strv += "/" + i

                if strv.startswith('////'):
                    strv = strv.replace('////','/')
                elif strv.startswith('///'):
                    strv = strv.replace('///','/')
                elif strv.startswith('//'):
                    strv = strv.replace('//','/')

                pwd = self.files.output(strv)
                self.files.write("/proc/info/pwd", pwd)

            elif self.files.isdir(path):
                self.files.write("/proc/info/pwd", self.files.output(path))
            else:
                self.colors.show("cd", "fail", path + ": directory not found.")
        else:
            self.colors.show("cd", "perm", "")

    # clean command #
    def clean (self,args):

        user = self.files.readall("/proc/info/su")
        select = self.files.readall("/proc/info/sel")

        if not select.startswith("/proc/"):
            if self.permissions.check(self.files.output(select), "w", user):
                self.files.create(select)
            else:
                self.colors.show("clean", "perm", "")
        else:
            self.files.create(select)

    # clear command #
    def clear (self,args):

        osname = self.files.readall("/proc/info/os")
        if osname == "Windows":
            os.system("cls")
        else:
            os.system("clear")

    # cp command #
    def cp (self,args):

        # args #
        cmdln = ['']
        cmdln[1:] = args

        if cmdln[1:] == []:
            self.colors.show("cp", "fail", "no inputs.")
        if cmdln[2:] == []:
            self.colors.show("cp", "fail", "no inputs.")

        src = cmdln[1]
        dest = cmdln[2]



        if self.files.isdir(src):
            if self.files.isfile(dest):
                self.colors.show("cp", "fail", dest + ": dest is a file.")
            else:
                if self.permissions.check(self.files.output(src), "r", self.files.readall("/proc/info/su")):
                    if self.permissions.check(self.files.output(dest), "w", self.files.readall("/proc/info/su")):
                        perm = self.permissions.get_permissions(self.files.output(src))
                        self.control.write_record(self.files.output(dest), perm, "/etc/permtab")
                        self.files.copydir(src, dest)

                    else:
                        self.colors.show("cp", "perm", "")
                else:
                    self.colors.show("cp", "perm", "")
        elif self.files.isfile(src):
            if self.files.isdir(dest):
                self.colors.show("cp", "fail", dest + ": dest is a directory.")
            else:
                if self.permissions.check(self.files.output(src), "r", self.files.readall("/proc/info/su")):
                    if self.permissions.check(self.files.output(dest), "w", self.files.readall("/proc/info/su")):
                        perm = self.permissions.get_permissions(self.files.output(src))
                        self.control.write_record(self.files.output(dest), perm, "/etc/permtab")
                        self.files.copy(src, dest)
                    else:
                        self.colors.show("cp", "perm", "")
                else:
                    self.colors.show("cp", "perm", "")
        else:
            self.colors.show("cp", "fail", src + ": source not found.")

    # date command #
    def date (self,args):
        ## Show all time and date ##
        if args == []:
            os.environ['TZ'] = self.files.readall("/proc/info/tz")  # https://stackoverflow.com/questions/1301493/setting-timezone-in-python
            time.tzset()
            print(datetime.datetime.now().ctime())

        ## Show utc now ##
        if args == ['utc']:
            print(datetime.datetime.utcnow().ctime())

    # getv command #
    def getv (self,args):
        select = self.files.readall("/proc/info/sel")
        if not select.startswith("/proc/"):
            if self.permissions.check(self.files.output(select), "w", self.files.readall("/proc/info/su")):
                listinfo = self.files.list("/proc/info")
                for i in listinfo:
                    self.control.write_record(i, self.files.readall("/proc/info/" + i), select)
            else:
                self.colors.show("getv", "perm", "")
        else:
            listinfo = self.files.list("/proc/info")
            for i in listinfo:
                self.control.write_record(i, self.files.readall("/proc/info/" + i), select)

    # help command #
    def help (self,args):

        if args==[]:
            print(self.files.readall("/usr/share/helps/cmdall.txt"))
        else:
            if self.files.isfile("/usr/share/helps/" + args[0] + ".txt"):
                print(self.files.readall("/usr/share/helps/" + args[0] + ".txt"))
            else:
                print(self.files.readall("/usr/share/helps/cmdall.txt"))

    # read command #
    def read (self,args):
        for i in args:
            self.set([i+":",input()])

    # ls command #
    def ls (self,args):

        path = None
        options = None

        # check args #

        if not args == [] and args[1:] == []:
            path = self.files.output(args[0])
            options = ''
        elif not args == [] and not args[1:] == []:
            path = self.files.output(args[0])
            options = args[1]
        elif args == []:
            path = self.files.readall("/proc/info/pwd")
            options = ''

        if options == "":
            if self.files.isdir(path):
                if self.permissions.check(self.files.output(path), "r", self.files.readall("/proc/info/su")):
                    list = self.files.list(path)
                    list.sort()
                    for i in list:
                        if self.files.isdir(path + "/" + i):
                            print(self.colors.get_path() + i + "/" + self.colors.get_colors())
                        else:
                            print(i)
                else:
                    self.colors.show("ls", "perm", "")
            else:
                self.colors.show("ls", "fail", path + ": directory not found.")
        elif options == "-p":
            if self.files.isdir(path):
                if self.permissions.check(self.files.output(path), "r", self.files.readall("/proc/info/su")):
                    list = self.files.list(path)
                    list.sort()
                    for i in list:
                        if self.files.isdir(path + "/" + i):
                            perm = self.permissions.get_permissions(self.files.output(path + i))
                            print(perm + "\t" + self.colors.get_path() + i + "/" + self.colors.get_colors())
                        else:
                            perm = self.permissions.get_permissions(self.files.output(path + i))
                            print(perm + "\t" + i)
                else:
                    self.colors.show("ls", "perm", "")
            else:
                self.colors.show("ls", "fail", path + ": directory not found.")
        elif options == "-n":
            if self.files.isdir(path):
                if self.permissions.check(self.files.output(path), "r", self.files.readall("/proc/info/su")):
                    list = self.files.list(path)
                    list.sort()
                    for i in list:
                        if self.files.isdir(path + "/" + i):
                            perm = self.permissions.get_permissions(path + "/" + i)
                            perm = str(self.permissions.show_number(perm))
                            print(perm + "\t" + self.colors.get_path() + i + "/" + self.colors.get_colors())
                        else:
                            perm = self.permissions.get_permissions(path + "/" + i)
                            perm = str(self.permissions.show_number(perm))
                            print(perm + "\t" + i)
                else:
                    self.colors.show("ls", "perm", "")
            else:
                self.colors.show("ls", "fail", path + ": directory not found.")
    # mkdir command #
    def mkdir (self,args):

        for i in args:
            if self.files.isfile(i):
                self.colors.show("mkdir", "fail", i + ": is a file.")
            elif self.files.isdir(i):
                self.colors.show("mkdir", "warning", i + ": directory exists.")
            else:
                if self.permissions.check(self.files.output(i), "w", self.files.readall("/proc/info/su")):
                    self.files.makedirs(i)
                else:
                    self.colors.show("mkdir", "perm", "")

    # mv command #
    def mv (self,args):

        # args #
        cmdln = ['']
        cmdln[1:] = args

        if cmdln[1:] == []:
            self.colors.show("mv", "fail", "no inputs.")
        if cmdln[2:] == []:
            self.colors.show("mv", "fail", "no inputs.")

        src = cmdln[1]
        dest = cmdln[2]

        if self.files.isdir(src):
            if self.files.isfile(dest):
                self.colors.show("mv", "fail", dest + ": dest is a file.")
            else:
                if self.permissions.check(self.files.output(src), "r", self.files.readall("/proc/info/su")) and self.permissions.check(
                        self.files.output(src), "w", self.files.readall("/proc/info/su")):
                    if self.permissions.check(self.files.output(dest), "w", self.files.readall("/proc/info/su")):
                        perm = self.permissions.get_permissions(self.files.output(src))
                        self.control.write_record(self.files.output(dest), perm, "/etc/permtab")
                        self.files.copydir(src, dest)
                        self.files.removedirs(src)
                    else:
                        self.colors.show("mv", "perm", "")
                else:
                    self.colors.show("mv", "perm", "")
        elif self.files.isfile(src):
            if self.files.isdir(dest):
                self.colors.show("mv", "fail", dest + ": dest is a directory.")
            else:
                if self.permissions.check(self.files.output(src), "r", self.files.readall("/proc/info/su")) and self.permissions.check(
                        self.files.output(src), "w", self.files.readall("/proc/info/su")):
                    if self.permissions.check(self.files.output(dest), "w", self.files.readall("/proc/info/su")):
                        perm = self.permissions.get_permissions(self.files.output(src))
                        self.control.write_record(self.files.output(dest), perm, "/etc/permtab")
                        self.files.copy(src, dest)
                        self.files.remove(src)
                    else:
                        self.colors.show("mv", "perm", "")
                else:
                    self.colors.show("mv", "perm", "")
        else:
            self.colors.show("mv", "fail", src + ": source not found.")

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
        for i in args:
            if self.files.isdir(i):
                if self.permissions.check(self.files.output(i), "w", self.files.readall("/proc/info/su")):
                    self.files.removedirs(i)
                    self.control.remove_record(i,'/etc/permtab')
                else:
                    self.colors.show("rm", "perm", "")
                    sys.exit(0)
            elif self.files.isfile(i):
                if self.permissions.check(self.files.output(i), "w", self.files.readall("/proc/info/su")):
                    self.files.remove(i)
                    self.control.remove_record(i, '/etc/permtab')
                else:
                    self.colors.show("rm", "perm", "")
                    sys.exit(0)
            else:
                self.colors.show("rm", "fail", i + ": file or directory not found.")
                sys.exit(0)

    ## passwd ##
    def passwd (self,args):

        if args==[]:
            colors.show('passwd','fail','no inputs.')
            sys.exit(0)

        user = args[0]

        # check user exists
        if not self.files.isfile('/etc/users/'+user):
            self.colors.show('passwd', 'fail', user+": user not found.")
            sys.exit(0)

        # check user exists with hashname

        username = self.control.read_record('username','/etc/users/'+user)
        hashname = hashlib.sha3_256(user.encode()).hexdigest()

        if not username==hashname:
            self.colors.show('passwd', 'fail', user + ": user not found.")
            sys.exit(0)

        # old password

        code = self.control.read_record('code','/etc/users/'+user)

        oldcode = hashlib.sha3_512(getpass.getpass('Enter '+user+"'s old password: ").encode()).hexdigest()

        if not code==oldcode:
            self.colors.show('passwd', 'fail', user + ": wrong password.")
            sys.exit(0)

        newcode = getpass.getpass('Enter a new password: ')

        while True:
            confirm = getpass.getpass('Confirm the new password: ')
            if confirm==newcode: break
            else:
                print('Try agian!')

        self.control.write_record('code',hashlib.sha3_512(newcode.encode()).hexdigest(),'/etc/users/'+user)

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

        if args == []:
            self.colors.show("sel", "fail", "no inputs.")
            sys.exit(0)

        database_name = args[0]


        if self.files.isfile(database_name):
            if self.permissions.check(self.files.output(database_name), "r", self.files.readall("/proc/info/su")):
                self.files.write("/proc/info/sel", database_name)
                self.files.create("/proc/selected")
            else:
                self.colors.show("sel", "perm", "")
        else:
            self.colors.show("sel", "fail", database_name + ": controller not found.")

    # set command #
    def set (self,args):
        if args == [] or args[1:] == []:
            self.colors.show("set", "fail", "no inputs.")
            sys.exit(0)

        if not args[0].endswith(":"):
            self.colors.show("set", "fail", "wrong syntax.")
            sys.exit(0)

        name = args[0].replace(":", "")
        value = args[1]

        select = self.files.readall("/proc/info/sel")
        if not select.startswith("/proc/"):
            if self.permissions.check(self.files.output(select), "w", self.files.readall("/proc/info/su")):
                self.control.write_record(name, value, select)
            else:
                self.colors.show("set", "perm", "")
        else:
            self.control.write_record(name, value, select)

    # sleep command #
    def sleep (self,args):
        if args == []:
            time.sleep(3)
        else:
            timeout = float(args[0])
            time.sleep(int(timeout))

    # su command #
    def su (self,args):

        if args == []:
            self.colors.show("su", "fail", "no inputs.")
            sys.exit(0)

        input_username = args[0]
        user = self.files.readall("/proc/info/su")

        if self.files.isfile("/proc/selected"): self.files.remove("/proc/selected")
        if user == input_username:
            self.colors.show("su", "warning", user + " has already switched.")
        elif input_username == "guest":
            enable_cli = self.control.read_record("enable_cli", "/etc/guest")
            if enable_cli == "Yes":
                subprocess.call ([sys.executable,self.files.readall("/proc/info/boot"),'user','guest'])
            else:
                self.colors.show(input_username, "fail", "user not found.")

        elif self.files.isfile("/etc/users/" + input_username):
            hashname = hashlib.sha3_256(str(input_username).encode()).hexdigest()
            username = self.control.read_record("username", "/etc/users/" + input_username)
            if hashname == username:
                input_password = getpass.getpass('Enter ' + input_username + '\'s password: ')
                hashcode = hashlib.sha3_512(str(input_password).encode()).hexdigest()
                password = self.control.read_record("code", "/etc/users/" + input_username)
                if hashcode == password:
                    subprocess.call ([sys.executable,self.files.readall("/proc/info/boot"),'user',input_username,input_password])
                else:
                    self.colors.show("su", "fail", input_username + ": wrong password.")
            else:
                self.colors.show("su", "fail", input_username + " user not found.")
        else:
            self.colors.show("su", "fail", input_username + " user not found.")

    # sudo command #
    def sudo (self,args):

        if args == []:
            self.colors.show('sudo', 'fail', 'no inputs.')
            sys.exit(0)

        if not args[0].startswith('-'):

            ## Get user name ##

            thisuser = self.files.readall("/proc/info/su")

            ## Check guest account ##
            if thisuser == "guest":
                self.colors.show("sudo", 'fail', 'cannot use sudo command in guest user.')
                sys.exit(0)

            ## Check sudoers account ##
            if not thisuser == "root":
                sudoers = self.files.readall('/etc/sudoers')

                if not sudoers.__contains__(thisuser):
                    self.colors.show('sudo', 'fail', thisuser + ": user isn't sudoers account.")
                    sys.exit()

            ## Send /etc/users/root to /proc/info/su username ##

            self.files.write("/proc/info/su", 'root')

            prompt = [sys.executable,self.files.readall('/proc/info/boot'), 'exec']

            for i in args:
                prompt.append(i)

            subprocess.call(prompt)

            self.files.write("/proc/info/su", thisuser)
        elif args[0] == '-a':
            ## Check root ##
            if not self.permissions.check_root(self.files.readall("/proc/info/su")):
                colors.show("sudo", "perm", "")
                sys.exit(0)
            ## Check user exists or no ##
            if self.files.isfile('/etc/users/' + args[1]):
                hashname = hashlib.sha3_256(args[1].encode()).hexdigest()
                username = self.control.read_record('username', '/etc/users/' + args[1])

                if hashname == username:
                    self.files.append('/etc/sudoers', args[1] + "\n")
                else:
                    self.colors.show('sudo', 'fail', args[1] + ": user not found.")
            else:
                self.colors.show('sudo', 'fail', args[1] + ": user not found.")
        else:
            self.colors.show('sudo', 'fail', args[1] + ": option not found.")

    # uadd command #
    def uadd (self,args):

        if args == []:
            self.colors.show("uadd", "fail", "no inputs.")
            sys.exit(0)

        input_username = args[0]
        user = self.files.readall ("/proc/info/su")

        if self.permissions.check_root(user):
            ## Check exists user ##
            if self.files.isfile("/etc/users/" + input_username) or input_username == "root":
                self.colors.show("uadd", "fail", input_username + ": user exists.")
            elif input_username == "guest":
                self.colors.show("uadd", "fail", "cannot create user account with guest username.")
            else:
                while True:
                    password = getpass.getpass('Enter a new password: ')
                    confirm = getpass.getpass('Confirm the new password: ')
                    if password == confirm: break

                ## Informations ##
                fullname = input('\tFull name      []: ')
                company =    input('\tCompany name    []: ')
                birthday =   input('\tBirthday        []: ')
                gender =     input('\tGender          [Male/Female]: ')
                blood_type = input('\tBlood type      [O/A/B/AB]: ')
                phone =      input('\tPhone number    []: ')
                website =    input('\tWebsite address []: ')
                email =      input('\tEmail address   []: ')

                hashname = hashlib.sha3_256(str(input_username).encode()).hexdigest()
                hashcode = hashlib.sha3_512(str(password).encode()).hexdigest()

                self.files.create("/etc/users/" + input_username)
                self.control.write_record("username", hashname, '/etc/users/' + input_username)
                self.control.write_record("code", hashcode, '/etc/users/' + input_username)

                ## Add informations ##
                if not (fullname == None or fullname == ""):
                    self.control.write_record("fullname", fullname, '/etc/users/' + input_username)
                if not (company == None or company == ""):
                    self.control.write_record("company", company, '/etc/users/' + input_username)
                if not (birthday == None or birthday == ""):
                    self.control.write_record("birthday", birthday, '/etc/users/' + input_username)
                if not (gender == None or gender == ""):
                    self.control.write_record("gender", gender, '/etc/users/' + input_username)
                if not (blood_type == None or blood_type == ""):
                    self.control.write_record("blood_type", blood_type, '/etc/users/' + input_username)
                if not (phone == None or phone == ""):
                    self.control.write_record("phone", phone, '/etc/users/' + input_username)
                if not (website == None or website == ""):
                    self.control.write_record("website", website, '/etc/users/' + input_username)
                if not (email == None or email == ""):
                    self.control.write_record("email", email, '/etc/users/' + input_username)

                self.control.write_record('/desk/'+input_username,"drwxr-x---/"+input_username,'/etc/permtab')

        else:
            self.colors.show("uadd", "perm", "")

    # udel command #
    def udel (self,args):

        if args == []:
            self.colors.show("udel", "fail", "no inputs.")
            sys.exit(0)

        input_username = args[0]
        user = self.files.readall ("/proc/info/su")

        if input_username == user:
            self.colors.show("udel", "fail", input_username + ": cannot remove switched user.")
        else:
            if self.permissions.check_root(user):
                if not self.files.isfile("/etc/users/" + input_username):
                    self.colors.show("udel", "fail", input_username + ": user not found.")
                else:
                    if input_username == "root":
                        self.colors.show("udel", "fail", input_username + ": is a permanet user.")
                    else:
                        hashname = hashlib.sha3_256(str(input_username).encode()).hexdigest()  ## Create hashname
                        username = self.control.read_record("username", "/etc/users/" + input_username)

                        if not hashname == username:
                            self.colors.show("udel", "fail", input_username + ": user not found.")
                        else:
                            self.files.remove("/etc/users/" + input_username)
                            if self.files.isdir('/desk/' + input_username):
                                self.files.removedirs("/desk/" + input_username)
                                self.control.remove_record('/desk/'+input_username,'/etc/permtab')
            else:
                self.colors.show("udel", "perm", "")

    # uinfo command #
    def uinfo (self,args):

        if args == []:
            input_username = self.files.readall ("/proc/info/su")
        else:
            input_username = args[0]

        enable_cli = self.control.read_record("enable_cli", "/etc/guest")
        if not (input_username == "guest" and enable_cli == "Yes"):
            if self.files.isfile("/etc/users/" + input_username):
                ## Get information from user database ##
                fullname = self.control.read_record("fullname", "/etc/users/" + input_username)
                company = self.control.read_record("company", "/etc/users/" + input_username)
                birthday = self.control.read_record("birthday", "/etc/users/" + input_username)
                gender = self.control.read_record("gender", "/etc/users/" + input_username)
                blood_type = self.control.read_record("blood_type", "/etc/users/" + input_username)
                phone = self.control.read_record("phone", "/etc/users/" + input_username)
                website = self.control.read_record("website", "/etc/users/" + input_username)
                email = self.control.read_record("email", "/etc/users/" + input_username)

                ## Show it on screen ##
                bold = self.colors.color(1, self.colors.get_bgcolor(), self.colors.get_fgcolor())
                if not (fullname == None or fullname == ""):  print(
                    "\t   Full name: " + bold + fullname + self.colors.get_colors())
                if not (company == None or company == ""):        print(
                    "\t      Company: " + bold + company + self.colors.get_colors())
                if not (birthday == None or birthday == ""):      print(
                    "\t     Birthday: " + bold + birthday + self.colors.get_colors())
                if not (gender == None or gender == ""):          print(
                    "\t       Gender: " + bold + gender + self.colors.get_colors())
                if not (blood_type == None or blood_type == ""):  print(
                    "\t    BloodType: " + bold + blood_type + self.colors.get_colors())
                if not (phone == None or phone == ""):            print(
                    "\t Phone number: " + bold + phone + self.colors.get_colors())
                if not (website == None or website == ""):        print(
                    "\t      Website: " + bold + website + self.colors.get_colors())
                if not (email == None or email == ""):            print(
                    "\tEmail address: " + bold + email + self.colors.get_colors())
            else:
                self.colors.show("uinfo", "fail", input_username + ": user not found.")

    # unsel command #
    def unsel (self,args):
        select = self.files.readall("/proc/info/sel")

        if select == "/proc/" + self.files.readall("/proc/info/sp"):
            self.colors.show("unsel", "warning", "controller has already selected.")
        else:
            self.files.write("/proc/info/sel", "/proc/" + self.files.readall("/proc/info/sp"))
            if self.files.isfile("/proc/selected"): self.files.remove("/proc/selected")

    # upv command #
    def upv (self,args):

        if not self.permissions.check_root(self.files.readall("/proc/info/su")):
            self.colors.show("upv", "perm", "")
            sys.exit(0)

        sel = self.files.readall('/proc/info/sel')  ## Get selector

        ## List all controls ##

        listc = self.control.read_list(sel)

        for i in listc:
            if not i.__contains__(':'):
                pass
            else:
                spliter = i.split(': ')
                self.files.write('/proc/info/' + spliter[0], spliter[1])

    # wget command #
    def wget (self,args):

        # https://www.tutorialspoint.com/downloading-files-from-web-using-python

        ## Check params ##

        if args == [] and args[1:]:
            self.colors.show('wget', 'fail', 'no inputs.')
            sys.exit(0)

        ## Download ##

        ## Check permissions ##
        if self.permissions.check(self.files.output(args[1]), "w", self.files.readall("/proc/info/su")):
            wget.download(args[0],self.files.input(args[1]))
            print()
        else:
            self.colors.show("wget", "perm", "")


# package #
class Package:
    ## Clean the cache ##
    def __init__(self):
        self.permissions = Permissions()
        self.files = Files()
        self.control = Control()
        self.commands = Commands()
        self.colors = Colors()

    def clean (self):

        if self.permissions.check_root(self.files.readall("/proc/info/su")):
            if self.files.isdir("/app/cache"):
                self.files.removedirs("/app/cache")
                self.files.mkdir("/app/cache")
                self.files.mkdir("/app/cache/gets")
                self.files.mkdir("/app/cache/archives")
                self.files.mkdir("/app/cache/archives/code")
                self.files.mkdir("/app/cache/archives/control")
                self.files.mkdir("/app/cache/archives/data")
                self.files.mkdir("/app/cache/archives/build")
        else:
            self.colors.show("paye", "perm", "")

    ## Create .pa archive ##

    def build(self,name):

        if self.permissions.check_root(self.files.readall("/proc/info/su")):
            if not self.files.isfile(name + "/control/manifest"):
                self.colors.show("paye", "fail", "cannot create archive package")
                self.clean()
                sys.exit(0)

            if not self.files.isdir(name + "/data"): self.files.mkdir(name + "/data")
            if not self.files.isdir(name + "/code"): self.files.mkdir(name + "/code")

            ## Remove cache archives ##
            if self.files.isdir('/app/cache/archives/control'): self.files.removedirs('/app/cache/archives/control')
            if self.files.isdir('/app/cache/archives/data'): self.files.removedirs('/app/cache/archives/data')
            if self.files.isdir('/app/cache/archives/code'): self.files.removedirs('/app/cache/archives/code')

            ## Copy dir ##
            self.files.copydir(name + '/data', '/app/cache/archives/data')
            self.files.copydir(name + '/control', '/app/cache/archives/control')
            self.files.copydir(name + '/code', '/app/cache/archives/code')

            ## Pack archives ##
            shutil.make_archive(self.files.input("/app/cache/archives/build/data"), "zip",
                                self.files.input('/app/cache/archives/data'))
            shutil.make_archive(self.files.input("/app/cache/archives/build/control"), "zip",
                                self.files.input('/app/cache/archives/control'))
            shutil.make_archive(self.files.input("/app/cache/archives/build/code"), "zip",
                                self.files.input('/app/cache/archives/code'))
            shutil.make_archive(self.files.input(name), "zip", self.files.input("/app/cache/archives/build"))

            self.files.cut(name + ".zip", name + ".pa")
            ## Unlock the cache ##
        else:
            self.colors.show("paye", "perm", "")


    ## Unpack .pa archives ##

    def unpack(self,name):

        if self.permissions.check_root(self.files.readall("/proc/info/su")):

            ## unpack package ##
            shutil.unpack_archive(self.files.input(name), self.files.input("/app/cache/archives/build"), "zip")

            shutil.unpack_archive(self.files.input("/app/cache/archives/build/data.zip"),
                                  self.files.input("/app/cache/archives/data"), "zip")
            shutil.unpack_archive(self.files.input("/app/cache/archives/build/control.zip"),
                                  self.files.input("/app/cache/archives/control"), "zip")
            shutil.unpack_archive(self.files.input("/app/cache/archives/build/code.zip"),
                                  self.files.input("/app/cache/archives/code"), "zip")

            ## Get database of this package ##
            name = self.control.read_record("name", "/app/cache/archives/control/manifest").lower()
            unpack =self.control.read_record("unpack", "/app/cache/archives/control/manifest")
            depends = self.control.read_record("depends", "/app/cache/archives/control/manifest")

            if not (depends == None):
                depends.split(",")

            ## Search for tree dependency ##

            if not depends == None:
                for i in depends:
                    if not self.files.isfile("/app/packages/" + i + ".manifest"):
                        System ('paye -i ' + name)

            ## Write dependency ##

            if not depends == None:
                for i in depends:
                    self.files.create("/app/packages/" + i + ".depends")
                    self.files.write("/app/packages/" + i + ".depends", name + "\n")

            ## Run preinstall script ##

            if self.files.isfile('/app/cache/archives/control/preinstall.sa'):
                System('/app/cache/archives/preinstall')  # Run it

                ## Copy preinstall script ##

                self.files.copy('/app/cache/archives/control/preinstall.sa', '/app/packages/' + name + ".preinstall")

            ## Setting up ##

            if self.files.isfile("/app/cache/archives/control/list"): self.files.copy("/app/cache/archives/control/list","/app/packages/" + name + ".list")
            if self.files.isfile("/app/cache/archives/control/manifest"): self.files.copy("/app/cache/archives/control/manifest","/app/packages/" + name + ".manifest")
            if self.files.isfile("/app/cache/archives/control/compile"): self.files.copy("/app/cache/archives/control/compile","/app/packages/" + name + ".compile")

            if self.control.read_record('compile','/app/cache/archives/control/manifest')=='Yes':
                for i in self.control.read_list('/app/cache/archives/control/compile'):
                    spl = i.split(":")

                    code = '/app/cache/archives/code/' + spl[0]
                    dest = "/app/cache/archives/data/" + spl[1]

                    self.commands.cc([code, dest])

            ## Create data archive ##
            shutil.make_archive(self.files.input("/app/cache/archives/build/data"), 'zip',self.files.input('/app/cache/archives/data'))

            ## Unpack data again ##
            shutil.unpack_archive(self.files.input("/app/cache/archives/build/data.zip"), self.files.input(unpack), "zip")

            ## Save the source

            shutil.unpack_archive(self.files.input('/app/cache/archives/build/code.zip'),self.files.input('/usr/src/'+name),'zip')

            ## After install ##

            ## Run postinstall script ##

            if self.files.isfile('/app/cache/archives/control/postinstall.sa'):
                System('/app/cache/archives/control/postinstall')  # Run it

                ## Copy postinstall script ##

                self.files.copy('/app/cache/archives/control/postinstall.sa', '/app/packages/' + name + ".postinstall")

            ## Copy other scripts ##
            if self.files.isfile('/app/cache/archives/control/preremove.sa'):
                self.files.copy('/app/cache/archives/control/preremove.sa', '/app/packages/' + name + ".preremove")

            if self.files.isfile('/app/cache/archives/control/postremove.sa'):
                self.files.copy('/app/cache/archives/control/postremove.sa', '/app/packages/' + name + ".postremove")

            ## Unlock the cache ##
        else:
            self.colors.show("paye", "perm", "")

    ## Remove package ##
    def uninstall (self,name):
        name = name.lower()

        if self.permissions.check_root(self.files.readall("/proc/info/su")):

            location = "/app/packages/" + name + ".manifest"

            if not self.files.isfile(location):
                self.colors.show("paye", "fail", name + ": package not found")
                self.clean()
                sys.exit(0)

            ## Database control ##


            list = "/app/packages/" + name + ".list"
            compile = '/app/packages/'+name+".compile"
            preinstall = "/app/packages/" + name + ".preinstall"
            postinstall = "/app/packages/" + name + ".postinstall"
            preremove = "/app/packages/" + name + ".preremove"
            postremove = "/app/packages/" + name + ".postremove"
            depends = "/app/packages/" + name+ ".depends"


            ## Create preremove and postremove copies ##


            if self.files.isfile(preremove): self.files.copy(preremove, "/usr/app/preremove.sa")
            if self.files.isfile(postremove): self.files.copy(postremove, "/usr/app/postremove.sa")


            ## Run pre remove script ##

            if self.files.isfile ('/usr/app/preremove.sa'):
                System("/usr/app/preremove")
                self.files.remove('/usr/app/preremove.sa')

            ## Remove depends ##

            if self.files.isfile(depends):
                depends = self.control.read_list(depends)
                for i in depends:
                    self.remove(i)

            ####################

            unpack = self.control.read_record("unpack", location)

            ## Unpacked removal ##
            filelist = self.control.read_list(list)

            for i in filelist:
                if self.files.isdir(unpack + "/" + i):
                    self.files.removedirs(unpack + "/" + i)
                elif self.files.isfile(unpack + "/" + i):
                    self.files.remove(unpack + "/" + i)


            ## Database removal ##

            if self.files.isfile(location): self.files.remove(location)
            if self.files.isfile(list): self.files.remove(list)
            if self.files.isfile(preinstall): self.files.remove(preinstall)
            if self.files.isfile(postinstall): self.files.remove(postinstall)
            if self.files.isfile(preremove): self.files.remove(preremove)
            if self.files.isfile(postremove): self.files.remove(postremove)
            if self.files.isfile(depends): self.files.remove(depends)
            if self.files.isfile(compile): self.files.remove(compile)


            ## Remove the source code ##

            if self.files.isdir ('/usr/src/'+name): self.files.removedirs('/usr/src/'+name)

            ## Run postremove script ##

            if self.files.isfile ('/usr/app/postremove.sa'):
                System ("postremove")
                self.files.remove('/usr/app/postremove.sa')
        else:
            self.colors.show("paye", "perm", "")

    ## Download package ##

    def download(self,packname):

        packname = packname.lower()

        if self.permissions.check_root(self.files.readall("/proc/info/su")):
            mirror = self.files.readall('/app/mirrors/' + packname)

            ## Download the file ##

            wget.download(mirror,self.files.input(f'/app/cache/gets/{packname}.pa'))
            print()

        else:
            self.colors.show("paye", "perm", "")

    ## Create a mirro ##
    def add (self,mirror,name):

        if self.permissions.check_root(self.files.readall("/proc/info/su")):
            #endsplit = mirror.replace('https://', '').replace('http://', '')
            #endsplit = mirror.split('/')
            self.files.write('/app/mirrors/' + name.replace('.pa',''), mirror)
        else:
            self.colors.show("paye", "perm", "")

    # update cloud software #
    def upcloud (self):

        if self.permissions.check_root(self.files.readall("/proc/info/su")):

            # backup #
            shutil.make_archive(self.files.input('/app/cache/backups/users.bak'),'zip',self.files.input('/etc/users'))
            self.files.copy('/etc/color','/app/cache/backups/color.bak')
            self.files.copy('/etc/compiler','/app/cache/backups/compiler.bak')
            self.files.copy('/etc/exec','/app/cache/backups/exec.bak')
            self.files.copy('/etc/guest','/app/cache/backups/guest.bak')
            self.files.copy('/etc/gui','/app/cache/backups/gui.bak')
            self.files.copy('/etc/hostname','/app/cache/backups/hostname.bak')
            self.files.copy('/etc/interface','/app/cache/backups/interface.bak')
            self.files.copy('/etc/modules', '/app/cache/backups/modules.bak')
            self.files.copy('/etc/permtab','/app/cache/backups/permtab.bak')
            self.files.copy('/etc/time', '/app/cache/backups/time.bak')

            mode = self.control.read_record('mode','/etc/paye/sources')


            self.download(mode)
            self.unpack(f'/app/cache/gets/{mode}.pa')

            for i in self.files.list ('/app/packages'):
                if i.endswith ('.manifest') and self.files.isfile(f'/app/mirrors/{i.replace(".manifest","")}'):
                    i = i.replace('.manifest','')

                    # check version
                    old = self.control.read_record('version',f'/app/packages/{i}.manifest')
                    new = self.control.read_record('version',f'/app/mirrors/{i}.manifest')

                    if not old==new and not i=='latest':
                        self.download(i)
                        self.unpack(f'/app/cache/gets/{i}.pa')

            # backup #
            shutil.unpack_archive(self.files.input('/app/cache/backups/users.bak.zip'), self.files.input('/etc/users'), 'zip')
            self.files.remove('/app/cache/backups/users.bak.zip')
            self.files.cut('/app/cache/backups/color.bak', '/etc/color')
            self.files.cut('/app/cache/backups/compiler.bak', '/etc/compiler')
            self.files.cut('/app/cache/backups/exec.bak', '/etc/exec')
            self.files.cut('/app/cache/backups/guest.bak', '/etc/guest')
            self.files.cut('/app/cache/backups/gui.bak', '/etc/gui')
            self.files.cut('/app/cache/backups/hostname.bak', '/etc/hostname')
            self.files.cut('/app/cache/backups/interface.bak', '/etc/interface')
            self.files.cut('/app/cache/backups/modules.bak', '/etc/modules')
            self.files.cut('/app/cache/backups/permtab.bak', '/etc/permtab')
            self.files.cut('/app/cache/backups/time.bak', '/etc/time')
        else:
            self.colors.show("paye", "perm", "")

    ## install from git source ##
    def gitinstall (self,name):

        if self.permissions.check_root(self.files.readall("/proc/info/su")):
            self.download(name.lower())

            ## unpack pyabr ##
            shutil.unpack_archive(self.files.input('/app/cache/gets/'+name.lower()+'.pa'), self.files.input('/tmp'), 'zip')

            self.build('/tmp/'+name+'-master/packs/'+name.lower())
            self.unpack('/tmp/'+name+'-master/packs/'+name.lower()+".pa")
            self.files.removedirs('/tmp/'+name+"-master")
        else:
            self.colors.show("paye", "perm", "")

    ##  remove a mirror ##
    def remove (self,name):
        if self.permissions.check_root(self.files.readall("/proc/info/su")):
            self.files.remove('/app/mirrors/' + name)
        else:
            self.colors.show("paye", "perm", "")
# res #
class Res:
    def __init__(self):
        self.control = Control()
        self.files = Files()
    # get app data #
    def etc (self,app,name):
        return self.control.read_record(name,f"/usr/share/applications/{app}.desk")

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

        layout = self.control.read_record('layout', '/etc/gui')

        if not self.files.isfile('/usr/share/locales/' + layout + ".locale"):
            layout = 'en'

        data = f'/usr/share/locales/{layout}.locale'

        return str.replace ('0',self.control.read_record('0',data)).replace('1', self.control.read_record('1', data)).replace('2', self.control.read_record('2', data)).replace('3', self.control.read_record('3', data)).replace('4', self.control.read_record('4', data)).replace('5', self.control.read_record('5', data)).replace('6', self.control.read_record('6', data)).replace('7', self.control.read_record('7', data)).replace('8', self.control.read_record('8', data)).replace('9', self.control.read_record('9', data)).replace('A', self.control.read_record('A', data)).replace('B', self.control.read_record('B', data)).replace('C', self.control.read_record('C', data)).replace('D', self.control.read_record('D', data)).replace('E', self.control.read_record('E', data)).replace('F', self.control.read_record('F', data)).replace('G', self.control.read_record('G', data)).replace('H', self.control.read_record('H', data)).replace('I', self.control.read_record('I', data)).replace('J', self.control.read_record('J', data)).replace('K', self.control.read_record('K', data)).replace('L', self.control.read_record('L', data)).replace('M', self.control.read_record('M', data)).replace('N', self.control.read_record('N', data)).replace('O', self.control.read_record('O', data)).replace('P', self.control.read_record('P', data)).replace('Q', self.control.read_record('Q', data)).replace('R',self.control.read_record('R', data)).replace('S', self.control.read_record('S', data)).replace('T', self.control.read_record('T', data)).replace('U', self.control.read_record('U', data)).replace('V', self.control.read_record('V', data)).replace('W', self.control.read_record('W', data)).replace('X', self.control.read_record('X', data)).replace('Y', self.control.read_record('Y', data)).replace('Z', self.control.read_record('Z', data)).replace('a', self.control.read_record('a', data)).replace('b', self.control.read_record('b', data)).replace('c', self.control.read_record('c', data)).replace('d', self.control.read_record('d', data)).replace('e', self.control.read_record('e', data)).replace('f', self.control.read_record('f', data)).replace('g', self.control.read_record('g', data)).replace('h', self.control.read_record('h', data)).replace('i', self.control.read_record('i', data)).replace('j', self.control.read_record('j', data)).replace('k', self.control.read_record('k', data)).replace('l', self.control.read_record('l', data)).replace('m', self.control.read_record('m', data)).replace('n', self.control.read_record('n', data)).replace('o', self.control.read_record('o', data)).replace('p', self.control.read_record('p', data)).replace('q', self.control.read_record('q', data)).replace('r', self.control.read_record('r', data)).replace('s', self.control.read_record('s', data)).replace('t', self.control.read_record('t', data)).replace('u', self.control.read_record('u', data)).replace('v', self.control.read_record('v', data)).replace('w', self.control.read_record('w', data)).replace('x', self.control.read_record('x', data)).replace('y', self.control.read_record('y', data)).replace('z', self.control.read_record('z', data)).replace('~', self.control.read_record('~', data)).replace('`', self.control.read_record('`', data)).replace('!', self.control.read_record('!', data)).replace('@', self.control.read_record('@', data)).replace('#', self.control.read_record('#', data)).replace('$', self.control.read_record('$', data)).replace('%', self.control.read_record('%', data)).replace('^', self.control.read_record('^', data)).replace('&', self.control.read_record('&', data)).replace('*', self.control.read_record('*', data)).replace('(', self.control.read_record('(', data)).replace(')', self.control.read_record(')', data)).replace('-', self.control.read_record('-', data)).replace('_', self.control.read_record('_', data)).replace('+', self.control.read_record('+', data)).replace('=', self.control.read_record('=', data)).replace('{', self.control.read_record('{', data)).replace('}', self.control.read_record('}', data)).replace('[', self.control.read_record('[', data)).replace(']', self.control.read_record(']', data)).replace('\\', self.control.read_record('\\', data)).replace('|', self.control.read_record('|', data)).replace(';', self.control.read_record(';', data)).replace('\'', self.control.read_record('\'', data)).replace('"', self.control.read_record('"', data)).replace('<', self.control.read_record('<', data)).replace('>', self.control.read_record('>', data)).replace(',', self.control.read_record(',', data)).replace('.', self.control.read_record('.', data)).replace('/', self.control.read_record('/', data)).replace('?', self.control.read_record('?', data))

    # get translated number #
    def num (self,number):

        if not self.files.isfile('/usr/share/locales/'+ self.control.read_record('locale','/etc/gui')+".locale"):
            locale = 'en'

        tnumber = ''
        for i in number:
            if i.isdigit():
                tnumber += i.replace(i,self.control.read_record(i,'/usr/share/locales/'+self.control.read_record('locale','/etc/gui')+".locale"))
            else:
                tnumber += i

        return tnumber

    # get resource #
    def get(self,filename):
        if not filename == None:
            filename = filename.split("/")  # @widget:barge

            share = filename[0]
            name = filename[1]

            ## Real Resource ##
            if share.startswith("@layout"):
                try:
                    return self.files.input("/usr/share/" + share.replace("@layout", "layouts") + "/" + name + ".ui")
                except:
                    return ''

            elif share.startswith("@background"):
                if self.files.isfile("/usr/share/backgrounds/" + name + ".svg"):
                    return self.files.input(
                            "/usr/share/backgrounds/" + name + ".svg")
                elif self.files.isfile(
                        "/usr/share/backgrounds/" + name + ".png"):
                    return self.files.input(
                        "/usr/share/backgrounds/" + name + ".png")
                elif self.files.isfile(
                        "/usr/share/backgrounds/" + name + ".jpg"):
                    return self.files.input(
                        "/usr/share/backgrounds/" + name + ".jpg")
                elif self.files.isfile(
                        "/usr/share/backgrounds/" + name + ".jpeg"):
                    return self.files.input(
                        "/usr/share/backgrounds/" + name + ".jpeg")
                elif self.files.isfile(
                        "/usr/share/backgrounds/" + name + ".gif"):
                    return self.files.input(
                        "/usr/share/backgrounds/" + name + ".gif")
                else:
                    return ''

            elif share.startswith("@image"):
                if self.files.isfile("/usr/share/images/" + name + ".svg"):
                    return self.files.input(
                        "/usr/share/images/" + name + ".svg")
                elif self.files.isfile(
                        "/usr/share/images/" + name + ".png"):
                    return self.files.input(
                        "/usr/share/images/" + name + ".png")
                elif self.files.isfile(
                        "/usr/share/images/" + name + ".jpg"):
                    return self.files.input(
                        "/usr/share/images/" + name + ".jpg")
                elif self.files.isfile(
                        "/usr/share/images/" + name + ".jpeg"):
                    return self.files.input(
                        "/usr/share/images/" + name + ".jpeg")
                elif self.files.isfile(
                        "/usr/share/images/" + name + ".gif"):
                    return self.files.input(
                        "/usr/share/images/" + name + ".gif")
                else:
                    return ''

            elif share.startswith("@app"):
                try:
                    return self.files.input("/usr/share/" + share.replace("@app", "applications") + "/" + name + ".desk")
                except:
                    return ''

            elif share.startswith("@widget"):
                try:
                    return self.files.input("/usr/share/" + share.replace("@widget", "widgets") + "/" + name + ".desk")
                except:
                    return ''

            elif share.startswith("@shell"):
                try:
                    return self.files.input("/usr/share/" + share.replace("@shell", "shells") + "/" + name + ".desk")
                except:
                    return ''

            elif share.startswith("@icon"):
                if self.files.isfile("/usr/share/" + share.replace("@icon", "icons") + "/" + name + ".svg"):
                    return self.files.input("/usr/share/" + share.replace("@icon", "icons") + "/" + name + ".svg")
                elif self.files.isfile("/usr/share/" + share.replace("@icon", "icons") + "/" + name + ".png"):
                    return self.files.input("/usr/share/" + share.replace("@icon", "icons") + "/" + name + ".png")
                elif self.files.isfile("/usr/share/" + share.replace("@icon", "icons") + "/" + name + ".gif"):
                    return self.files.input("/usr/share/" + share.replace("@icon", "icons") + "/" + name + ".gif")
                else:
                    return ''

            elif share.startswith('@temp'):
                if self.files.isfile("/usr/share/" + share.replace("@temp", "templates") + "/" + name ):
                    return "/usr/share/" + share.replace("@temp", "templates") + "/" + name
                elif self.files.isdir("/usr/share/" + share.replace("@temp", "templates") + "/" + name ):
                    return "/usr/share/" + share.replace("@temp", "templates") + "/" + name
                else:
                    return ''

            elif share.startswith("@string"):
                locale = self.control.read_record("locale", "/etc/gui")
                id = self.files.readall("/proc/info/id")

                ## Set default lang ##
                if locale == None: locale = "en"

                ## Get value from string ##
                result = self.control.read_record(id.replace(".desk", "") + "." + name,
                                             "/usr/share/locales/" + locale + ".locale")

                ## Find default ##
                if result == None:
                    result = self.control.read_record(id.replace(".desk", "") + "." + name,
                                                 "/usr/share/locales/" + 'en' + ".locale")

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
        self.files = Files()
        self.control = Control()

    def start(self,id):

        ## Check exists ##
        if self.files.isfile('/proc/id/' + id):
            pass


        ## Create id ##
        self.files.create("/proc/id/" + id)

        ## Check desktop shortcut ##
        if self.files.isfile("/usr/share/applications/" + id):
            self.files.copy("/usr/share/applications/" + id + ".desk",
                       "/proc/id/" + id)  # Copy all informations about this GUI application

        ## Set default id ##
        self.files.write("/proc/info/id", id)

    ## Check id ##
    def check(self,id):

        return self.files.isfile('/proc/id/' + id)

    ## End id ##
    def end(self,id):
        if self.files.isfile('/proc/id/' + id):
            ## Remove id ##
            self.files.remove("/proc/id/" + id)

    ## Shut id ##
    def shut(self):

        default = self.files.readall("/proc/info/id")
        if self.files.isfile("/proc/id/" + default):
            self.end(default)

    ## Endall id ##
    def endall(self):
        self.switch('desktop')
        for i in self.files.list("/proc/id"):
            if self.files.isfile('/proc/id/' + i):
                self.files.remove('/proc/id/' + i)

    ## Switch id process ##
    def switch(self,id):

        if self.files.isfile('/proc/id/' + id):
            self.files.write("/proc/info/id", id)

    ## Check application ##
    def exists (self,app):
        return self.files.isfile('/usr/share/applications/'+app+".desk")

# process #

class Process:
    def __init__(self):
        self.files = Files()
        self.control = Control()

    def processor(self):

        j = 0
        if not self.files.isfile("/proc/" + str(0)):
            self.files.create("/proc/" + str(0))
            j = j + 1
        else:
            list = self.files.list("/proc")
            list.remove('id')
            list.remove('info')

            for i in list:
                if self.files.isfile("/proc/" + i):

                    self.files.create("/proc/" + str(int(i) + 1))
                    j = j + 1
                else:
                    self.files.create("/proc/" + i)

        if self.files.isfile("/proc/1"):
            self.files.write("/proc/info/sp", str(j))
            return j
        else:
            self.files.write("/proc/info/sp", str(j - 1))
            return j - 1

    ## Check switched process ##
    def check(self,switch):

        if not self.files.isfile("/proc/" + str(switch)):
            sys.exit(0)
        else:
            if self.files.isfile("/proc/info/sp"): self.files.remove("/proc/info/sp")
            self.files.write("/proc/info/sp", str(switch))

    ## End switched process ##
    def end(self,switch):

        if self.files.isfile("/proc/info/sp"): self.files.remove("/proc/info/sp")
        if self.files.isfile("/proc/" + str(switch)):
            self.files.remove("/proc/" + str(switch))
            sys.exit(0)

    ## Endall all switched processes ##
    def endall(self):
        if self.files.isfile("/proc/info/sp"): self.files.remove("/proc/info/sp")
        list = self.files.list("/proc")
        list.remove("id")
        list.remove("info")
        for i in list:
            self.files.remove("/proc/" + str(i))

# permissions #
class Permissions:


    def __init__(self):
        self.files = Files()
        self.control = Control()
    ## Create permissions ##
    def create(self,name, user, others, guest, owner):
        if self.files.isfile(name) or self.files.isdir(name):
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

            if self.files.isdir(name):
                self.control.write_record(name, "d" + user + others + guest + "/" + owner,
                                     "/etc/permtab")  # Write permissions for this directory
            else:
                self.control.write_record(name, "-" + user + others + guest + "/" + owner,
                                     "/etc/permtab")  # Write permissions for this file

    def exists(self,name):

        perms = self.control.read_record(name, "/etc/permtab")  ## get permissions
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

        user = user_r + user_w + user_x
        others = others_r + others_w + others_x
        guest = guest_r + guest_w + guest_x

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

        return  int(str(user) + str(others) + str(guest))

    ## This function correct at all ##
    def get_permissions(self,name):

        perms = self.control.read_record(name, "/etc/permtab")  ## get permissions
        if not perms == None:
            return perms
        else:
            ## Father permtab ##
            if self.files.isdir(name):
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
                    name = name + "/" + i
                name = name.replace("//", "/")

            perm = (self.control.read_record(name, "/etc/permtab")).split("/")
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
            return dirfile + user_r + user_w + user_x + others_r + others_w + others_x + guest_r + guest_w + guest_x + "/" + owner

    ## This function correct at all ##
    def check(self,name, request, user):
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
            if self.files.isfile("/etc/users/" + user):
                if (hashlib.sha3_256(str("root").encode()).hexdigest() == self.control.read_record("username", "/etc/users/root")):
                    return True
                else:
                    return False
            else:
                return False

        elif user == "guest":
            enable_cli = self.control.read_record("enable_cli", "/etc/guest")
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
            if self.files.isfile("/etc/users/" + user):
                if ( hashlib.sha3_256(str(user).encode()).hexdigest() == self.control.read_record("username", "/etc/users/" + user)):
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
            else:
                return False

    ## Get owner ##
    def get_owner(self,filename):
        perm = self.get_permissions(filename)

        return perm.split("/")[1]

    ## Check owner ##
    def check_owner(self,filename, user):

        owner = self.get_owner(filename)
        if user == "guest":
            enable_cli = self.control.read_record("enable_cli", "/etc/guest")
            if enable_cli == "Yes":
                if owner == user:
                    return True
                else:
                    return False
            else:
                return False
        elif user == "root":
            if self.files.isfile("/etc/users/" + user):
                if (hashlib.sha3_256(str(user).encode()).hexdigest() == self.control.read_record("username", "/etc/users/" + user)):
                    return True
                else:
                    return False
            else:
                return False
        else:
            if self.files.isfile("/etc/users/" + user):
                if (hashlib.sha3_256(str(user).encode()).hexdigest() == self.control.read_record("username", "/etc/users/" + user)):
                    if owner == user:
                        return True
                    elif owner == "guest":
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False

    ## Check root ##
    def check_root(self,user):
        if user == "root" and self.files.isfile("/etc/users/" + user) and (hashlib.sha3_256(str(user).encode()).hexdigest() == self.control.read_record("username", "/etc/users/" + user)):
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
            sys.path.append("./" + i)

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
            return "./"+ filename
        else:
            return "./"+ pwd + "/" + filename

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
            strv += '/'+ i

        return strv

    def filename(self,path):
        file = (self.input(path)).split('/')

        return file[len(file) - 1]
# control #
class Control:

    def __init__(self):
        self.files = Files()

    def read_record(self,name, filename):
        for i in (self.files.readall(filename)).split("\n"):
            if i.startswith(name):
                i = i.split(": ")
                if i[0] == (name):
                    return i[1]

    def read_list(self,filename):
        return (self.files.readall(filename)).split("\n")

    def write_record(self,name, value, filename):
        all = self.files.readall(filename)
        record = self.read_record(name, filename)
        self.files.remove(filename)
        if not (record == None):
            all = all.replace("\n"+name + ": " + record, "")

        self.files.write(filename, all + "\n" + name + ": " + value)

    def remove_record(self,name, filename):
        all = self.files.readall(filename)
        record = self.read_record(name, filename)
        self.files.remove(filename)
        if not (record == None):
            all = all.replace(name + ": " + record, "")
        self.files.write(filename, all)

    def remove_item(self,name, filename):
        strv = ""
        for i in self.read_list(filename):
            if i == name:
                strv += "\n"
            else:
                strv += "\n" + i
        self.files.write(filename, strv)

# colors #
class Colors:
    def __init__(self):
        self.files = Files()
        self.control = Control()
    argv = 'kernel'

    black = 30
    red = 31
    green = 32
    yellow = 33
    blue = 34
    purple = 35
    cyan = 36
    white = 37

    style_none = 0
    style_bold = 1
    style_underline = 2
    style_negative1 = 3
    style_negative2 = 5

    bg_black = 40
    bg_red = 41
    bg_green = 42
    bg_yellow = 43
    bg_blue = 44
    bg_purple = 45
    bg_cyan = 46
    bg_white = 47

    def show(self,process_name, process_type, process_message):
        if process_type == "fail":
            print(self.get_fail() + process_name + ": error: " + process_message + self.get_colors())
        elif process_type == "perm":
            print(self.get_fail() + process_name + ": error: " + "Permission denied." + self.get_colors())
        elif process_type == "warning":
            print(self.get_warning() + process_name + ": warning: " + process_message + self.get_colors())
        elif process_type == "fail-start":
            print("[ " + self.get_fail() + "FAIL " + self.get_colors() + "] Fail to start " + process_name + " process.")
        elif process_type == "fail-switch":
            print("[ " + self.get_fail() + "FAIL " + self.get_colors() + "] Fail to switch " + process_name + " process.")
        elif process_type == "stop":
            print("[ " + self.get_fail() + "STOP" + self.get_colors() + " ] Stop the " + process_name)
        elif process_type == "fail-show":
            print("[ " + self.get_fail() + "FAIL" + self.get_colors() + " ] " + process_message)

    def color(self,style, text, background):
        if not self.files.isfile("/proc/id/desktop"):
            return "\033[" + str(style) + ";" + str(text) + ";" + str(background) + "m"
        else:
            return ""

    def get_colors(self):
        if not self.files.isfile("/proc/id/desktop"):
            return "\033[" + str(self.control.read_record("fgcolor", "/etc/color")) + ";" + str( self.control.read_record("bgcolor", "/etc/color")) + ";" + str(self.control.read_record("style", "/etc/color")) + "m"
        else:
            return ""

    def get_style(self):
        if not self.files.isfile("/proc/id/desktop"):
            return self.control.read_record("style", "/etc/color")
        else:
            return ""

    def get_fgcolor(self):

        if not self.files.isfile("/proc/id/desktop"):
            return self.control.read_record("fgcolor", "/etc/color")
        else:
            return ""

    def get_bgcolor(self):
        if not self.files.isfile("/proc/id/desktop"):
            return  self.control.read_record("bgcolor", "/etc/color")
        else:
            return ""

    def get_warning(self):

        if not self.files.isfile("/proc/id/desktop"):
            return "\033[" + str(self.control.read_record("warning_style", "/etc/color")) + ";" + str(self.control.read_record("warning_fgcolor", "/etc/color")) + ";" + str(self.control.read_record("warning_bgcolor", "/etc/color")) + "m"
        else:
            return ""

    def get_path(self):

        if not self.files.isfile("/proc/id/desktop"):
            return "\033[" + str(self.control.read_record("path_style", "/etc/color")) + ";" + str(self.control.read_record("path_fgcolor", "/etc/color")) + ";" + str(self.control.read_record("path_bgcolor", "/etc/color")) + "m"
        else:
            return ""

    def get_prompt(self):

        if not self.files.isfile("/proc/id/desktop"):
            return "\033[" + str(self.control.read_record("prompt_style", "/etc/color")) + ";" + str(self.control.read_record("prompt_fgcolor", "/etc/color")) + ";" + str( self.control.read_record("prompt_bgcolor", "/etc/color")) + "m"
        else:
            return ""

    def get_fail(self):

        if not self.files.isfile("/proc/id/desktop"):
            return "\033[" + str(self.control.read_record("fail_style", "/etc/color")) + ";" + str(self.control.read_record("fail_fgcolor", "/etc/color")) + ";" + str( self.control.read_record("fail_bgcolor", "/etc/color")) + "m"
        else:
            return ""

    def get_ok(self):
        if not self.files.isfile("/proc/id/desktop"):
            return "\033[" + str(self.control.read_record("ok_style", "/etc/color")) + ";" + str(self.control.read_record("ok_fgcolor", "/etc/color")) + ";" + str( self.control.read_record("ok_bgcolor", "/etc/color")) + "m"
        else:
            return ""

    def get_hide(self):
        if not self.files.isfile("/proc/id/desktop"):
            return "\033[" + str(self.control.read_record("style", "/etc/color")) + ";" + str(int(self.control.read_record("bgcolor", "/etc/color")) + 10) + ";" + str( self.control.read_record("bgcolor", "/etc/color")) + "m"
        else:
            return ""