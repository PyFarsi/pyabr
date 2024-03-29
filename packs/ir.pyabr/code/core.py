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
import importlib, shutil, os, sys, hashlib, subprocess,time,datetime,getpass,py_compile,wget,requests,random,multiprocessing
from requests.models import requote_uri
from termcolor import colored
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from rich.console import Console
from rich.markdown import Markdown

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

def startId():
    files = Files()
    res = Res()
    if files.isfile('/proc/info/ext'):
        System (f"{res.etc(files.readall('/proc/info/id'),'exec')} {files.readall('/proc/info/ext')}")
    else:
        System (res.etc(files.readall('/proc/info/id'),'exec'))

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
                if str(i).startswith(":"):
                    select = files.readall("/proc/info/sel")
                    var = control.read_record(str(i).replace(":", ""), select)
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
            elif cmdln[0]=='>' or cmdln[0]=='>>' or cmdln[0]=='>>>':
                cmdln.pop(0)
                scmd = ''
                for i in cmdln:
                    if scmd=='':
                        scmd+=i
                    else:
                        scmd+=f' {i}'

                strcmd = f"\"{sys.executable}\" -c \""
                strcmd2 = scmd.replace('"','\\"')
                strcmd = f"{strcmd}{strcmd2}\""
                subprocess.call(strcmd,shell=True)
            elif hasattr(Commands, cmdln[0]):
                cmd = Commands()
                getattr(cmd, cmdln[0])(cmdln[1:])
            else:
                System(cmd)

# commands #
class Commands:
    def __init__(self):
        pass

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

        if filename.endswith('.py'):
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

        elif filename.endswith('.c'):
            if args[1:]==[]:
                subprocess.call(['/usr/bin/gcc',files.input(filename),'-o',files.input('a.out')])
                if not permissions.check(files.output('a.out'), "w", files.readall("/proc/info/su")):
                    colors.show('cc', 'perm', '')
                    sys.exit(0)
            else:
                output = args[1]
                if not permissions.check(files.output(output), "w", files.readall("/proc/info/su")):
                    colors.show('cc', 'perm', '')
                    sys.exit(0)

                if output.endswith('.so'):
                    subprocess.call(['/usr/bin/gcc','-shared','-o',files.input(output),'-fPIC',files.input(filename)])
                else:
                    subprocess.call(['/usr/bin/gcc',files.input(filename),'-o',files.input(output)])

        elif filename.endswith('.has'):
            if args[1:]==[]:
                System (f"hascal {files.input(filename)} {files.input('a.out')}")
                if not permissions.check(files.output('a.out'), "w", files.readall("/proc/info/su")):
                    colors.show('cc', 'perm', '')
                    sys.exit(0)
            else:
                output = args[1]
                if not permissions.check(files.output(output), "w", files.readall("/proc/info/su")):
                    colors.show('cc', 'perm', '')
                    sys.exit(0)
                
                System (f"hascal {files.input(filename)} {files.input(output)}")

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
            print(f"           Read: {colored('Yes','green')}")
        else:
            print(f"           Read: {colored('No','red')}" )

        if w == True:
            print(f"          Write: {colored('Yes','green')}" )
        else:
            print(f"          Write: {colored('No','red')}")

        if x == True:
            print(f"        Execute: {colored('Yes','green')}")
        else:
            print(f"        Execute: {colored('No','red')}")

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
        app.start('commento','')

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

        subprocess.call(['/usr/bin/reboot'])

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

            subprocess.call(['/usr/bin/poweroff'])

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

        subprocess.call(['/usr/bin/poweroff'])


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

    # view command #
    def view (self,args):
        if args==[]:
            colors.show("view", "fail", "no inputs.")
            sys.exit (0)

        viewname = args[0]

        if permissions.check(files.output(viewname), "r", files.readall("/proc/info/su")):
            if files.isfile (viewname):
                if viewname.endswith('.qml'):
                    files.copy (viewname,'/usr/share/layouts/debug.qml')
                    app.start('debug','')
                else:
                    colors.show("view", "fail", f"{viewname}: is not a QML file.")
            else:
                colors.show("view", "fail", f"{viewname}: QML file not found.")
        else:
            colors.show("view", "perm", "")

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
                files.write("/proc/info/pwd", files.output(pwd))

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

        x =  files.list ('/usr/share/docs/commands')
        x.sort()

        if args==[]:
            
            print (f"{colored('Commands are:','cyan')}")
            for i in x:
                print(i.replace(".md",""),end=' ')
            print (f"\n{colored('Try `help [command]` to see more informations','cyan')}")
        else:
            if files.isfile(f"/usr/share/docs/commands/{args[0]}.md"):
                console = Console()
                md = Markdown(files.readall(f"/usr/share/docs/commands/{args[0]}.md"))
                console.print(md)
                pass
            else:
                print (f"{colored('Commands are:','cyan')}")
                for i in x:
                    print(i.replace(".md",""),end=' ')
                print (f"\n{colored('Try `help [command]` to see more informations','cyan')}")

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
                        if (i.startswith ('.') or i=='__pycache__') and not files.readall('/etc/default/hidden_files')=='No':
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
                control.remove_record(name,select)
                control.write_record(name, value, select)
            else:
                colors.show("set", "perm", "")
        else:
            control.remove_record(name,select)
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
            if files.readall('/etc/guest') == "enable":
                files.create('/proc/info/pause')
                subprocess.call ([sys.executable,'vmabr.pyc','user','guest'])
            else:
                colors.show(input_username, "fail", "user not found.")

        elif files.isfile(f"/etc/users/{input_username}"):

                input_password = getpass.getpass(f'Enter {input_username}\'s password: ')
                if hashlib.sha3_512(str(input_password).encode()).hexdigest() == control.read_record("code", f"/etc/users/{input_username}"):
                    files.create('/proc/info/pause')
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
            files.create("/proc/info/sudo")
            files.create("/proc/info/pause")

            #prompt = [sys.executable,'vmabr.pyc', 'exec']
            prompt = f'"{sys.executable}" vmabr.pyc exec '

            for i in args:
                prompt+=f" {i}"

            files.remove ('/proc/info/sudo')
            subprocess.call(prompt,shell=True)

            files.write("/proc/info/su", thisuser)

            try:
                files.remove ("/proc/info/pause")
            except:
                pass
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

                files.create(f"/etc/users/{input_username}")
                control.write_record("code", hashlib.sha3_512(str(password).encode()).hexdigest(), f'/etc/users/{input_username}')

                ## Add informations ##
                if not (fullname == None or fullname == ""):
                    control.write_record("fullname", fullname,f'/etc/users/{input_username}')
                
                if not files.isdir (f'/desk/{input_username}'):
                    files.mkdir(f'/desk/{input_username}')

                if not files.isdir (f'/etc/key/{input_username}'):
                    files.mkdir(f'/etc/key/{input_username}')

                k = Key(input_username) # create public key and private key for created user

                control.write_record(f'/desk/{input_username}',f"drwxr-x---/{input_username}",'/etc/permtab')
                control.write_record('profile','@icon/breeze-users',f'/etc/users/{input_username}')
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

        if not (input_username == "guest" and files.readall('/etc/guest') == "enable"):
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

        if args == []:
            colors.show('wget', 'fail', 'no inputs.')
            sys.exit(0)
        elif args[1:]==[]:
            args [1] = max(args[0].split('.'))

        ## Download ##

        ## Check permissions ##
        if permissions.check(files.output(args[1]), "w", files.readall("/proc/info/su")):
            wget.download(args[0],files.input(args[1]))
            print()
        else:
            colors.show("wget", "perm", "")

commands = Commands()
# package #
class Package:
    ## Clean the cache ##
    def __init__(self):
        pass

    def listfiles(self,package):
        list2 = subprocess.check_output(f'cd {files.input(package)}/data && find . -type f', shell=True).decode('utf-8').split('\n')
        list2.remove('')

        f = open(f'{files.input(package)}/control/list', 'w')
        for i in list2:
            try:
                f.write(f"{i.replace('./','')}\n")
            except:
                pass
        f.close()

        try:
            f = open(f'{files.input(package)}/control/compile', 'r')
            list3 = f.read().split('\n')
            f.close()

            f = open(f'{files.input(package)}/control/list', 'a')
            for i in list3:
                if not i=='':
                    f.write(i.split(":")[1] + "\n")
            f.close()
        except:
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

            self.listfiles(name)

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
                System('/app/cache/archives/control/preinstall')  # Run it

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
                if files.isfile(f"{unpack}/{i}"):
                    files.remove(f"{unpack}/{i}")


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
            mirror = control.read_record('mirror',f'/app/mirrors/{packname}.manifest')+'/'+packname+'.pa'
            try:
                wget.download(mirror,files.input(f'/app/cache/gets/{packname}.pa'))
            except:
                colors.show("paye","fail",f"{packname}: package not found.")
                
            print()

        else:
            colors.show("paye", "perm", "")

    ## Create a mirro ##
    def add (self,mirror,name):
        permissions = Permissions()
        files = Files()
        colors = Colors()
        if permissions.check_root(files.readall("/proc/info/su")):
            files.create(f"/app/mirrors/{name}.manifest")
            control.write_record('name',name,f'/app/mirrors/{name}.manifest')
            control.write_record('mirror',mirror,f'/app/mirrors/{name}.manifest')
        else:
            colors.show("paye", "perm", "")

    ##  remove a mirror ##
    def remove (self,name):
        permissions = Permissions()
        files = Files()
        colors = Colors()
        if permissions.check_root(files.readall("/proc/info/su")):
            try:
                files.remove(f'/app/mirrors/{name}.manifest')
            except:
                pass
        else:
            colors.show("paye", "perm", "")

package = Package()
# res #
class Res:
    def __init__(self):
        pass

    def getuserdata (self,name):
        try:
            x = control.read_record(name,f'/etc/users/{files.readall("/proc/info/su")}')
            if x=='' or x==None:
                x = self.getdata(name)
        except:
            x = self.getdata(name)

        return x
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

    def qmlget (self,filename):
        control = Control()
        files = Files()
        if not filename == None:
            filename = filename.split("/")  # @widget:barge

            share = filename[0]
            name = filename[1]

            ## Real Resource ##
            if share.startswith("@layout"):
                try:
                    shell_theme = self.getdata("shell-theme")
                    if shell_theme == None:
                        shell_theme = "barf"

                    if files.isfile(f"/usr/share/layouts/{shell_theme}-{name}.qml"):
                        return files.input_qml(f"/usr/share/layouts/{shell_theme}-{name}.qml")
                    elif files.isfile(f"/usr/share/layouts/barf-{name}.qml"):
                        return files.input_qml(f"/usr/share/layouts/barf-{name}.qml")
                    else:
                        return files.input_qml(f"/usr/share/layouts/{name}.qml")
                except:
                    return ''

            elif share.startswith("@background"):
                if files.isfile(f"/usr/share/backgrounds/{name}.svg"):
                    return files.input_qml(
                        f"/usr/share/backgrounds/{name}.svg")
                elif files.isfile(
                        f"/usr/share/backgrounds/{name}.png"):
                    return files.input_qml(
                        f"/usr/share/backgrounds/{name}.png")
                elif files.isfile(
                        f"/usr/share/backgrounds/{name}.jpg"):
                    return files.input_qml(
                        f"/usr/share/backgrounds/{name}.jpg")
                elif files.isfile(
                        f"/usr/share/backgrounds/{name}.jpeg"):
                    return files.input_qml(
                        f"/usr/share/backgrounds/{name}.jpeg")
                elif files.isfile(
                        f"/usr/share/backgrounds/{name}.gif"):
                    return files.input_qml(
                        f"/usr/share/backgrounds/{name}.gif")
                elif files.isfile(
                        f"/usr/share/backgrounds/{name}.tif"):
                    return files.input_qml(
                        f"/usr/share/backgrounds/{name}.tif")
                else:
                    return ''

            elif share.startswith("@image"):
                if files.isfile(f"/usr/share/images/{name}.svg"):
                    return files.input_qml(
                        f"/usr/share/images/{name}.svg")
                elif files.isfile(
                        f"/usr/share/images/{name}.png"):
                    return files.input_qml(
                        f"/usr/share/images/{name}.png")
                elif files.isfile(
                        f"/usr/share/images/{name}.jpg"):
                    return files.input_qml(
                        f"/usr/share/images/{name}.jpg")
                elif files.isfile(
                        f"/usr/share/images/{name}.jpeg"):
                    return files.input_qml(
                        f"/usr/share/images/{name}.jpeg")
                elif files.isfile(
                        f"/usr/share/images/{name}.gif"):
                    return files.input_qml(
                        f"/usr/share/images/{name}.gif")
                elif files.isfile(
                        f"/usr/share/images/{name}.tif"):
                    return files.input_qml(
                        f"/usr/share/images/{name}.tif")
                else:
                    return ''

            elif share.startswith("@app"):
                try:
                    return files.input_qml(f"/usr/share/applications/{name}.desk")
                except:
                    return ''

            elif share.startswith("@widget"):
                try:
                    return files.input_qml(f"/usr/share/widgets/{name}.desk")
                except:
                    return ''

            elif share.startswith("@shell"):
                try:
                    return files.input_qml(f"/usr/share/shells/{name}.desk")
                except:
                    return ''

            elif share.startswith("@icon"):
                theme = self.getdata('icon-theme')
                if theme == None:
                    theme = 'breeze'

                if files.isfile(f"/usr/share/icons/{theme}-{name}.svg"):
                    return files.input_qml(f"/usr/share/icons/{theme}-{name}.svg")
                elif files.isfile(f"/usr/share/icons/{theme}-{name}.png"):
                    return files.input_qml(f"/usr/share/icons/{theme}-{name}.png")
                elif files.isfile(f"/usr/share/icons/{theme}-{name}.gif"):
                    return files.input_qml(f"/usr/share/icons/{theme}-{name}.gif")
                elif files.isfile(f"/usr/share/icons/{theme}-{name}.tif"):
                    return files.input_qml(f"/usr/share/icons/{theme}-{name}.tif")
                else:
                    if name.startswith ('file-'):
                        if files.isfile(f'/usr/share/icons/{theme}-file.svg'):
                            return files.input_qml(f'/usr/share/icons/{theme}-file.svg')
                        elif files.isfile(f'/usr/share/icons/{theme}-file.png'):
                            return files.input_qml(f'/usr/share/icons/{theme}-file.png')
                        elif files.isfile(f'/usr/share/icons/{theme}-file.gif'):
                            return files.input_qml(f'/usr/share/icons/{theme}-file.gif')
                        elif files.isfile(f'/usr/share/icons/{theme}-file.tif'):
                            return files.input_qml(f'/usr/share/icons/{theme}-file.tif')
                        else:
                            return files.input_qml(f'/usr/share/icons/breeze-file.png')
                    else:
                        if files.isfile(f"/usr/share/icons/breeze-{name}.svg"):
                            return files.input_qml(f"/usr/share/icons/breeze-{name}.svg")
                        elif files.isfile(f"/usr/share/icons/breeze-{name}.png"):
                            return files.input_qml(f"/usr/share/icons/breeze-{name}.png")
                        elif files.isfile(f"/usr/share/icons/breeze-{name}.gif"):
                            return files.input_qml(f"/usr/share/icons/breeze-{name}.gif")
                        elif files.isfile(f"/usr/share/icons/breeze-{name}.tif"):
                            return files.input_qml(f"/usr/share/icons/breeze-{name}.tif")
                        else:
                            if files.isfile(f"/usr/share/icons/{name}.svg"):
                                return files.input_qml(f"/usr/share/icons/{name}.svg")
                            elif files.isfile(f"/usr/share/icons/{name}.png"):
                                return files.input_qml(f"/usr/share/icons/{name}.png")
                            elif files.isfile(f"/usr/share/icons/{name}.gif"):
                                return files.input_qml(f"/usr/share/icons/{name}.gif")
                            elif files.isfile(f"/usr/share/icons/{name}.tif"):
                                return files.input_qml(f"/usr/share/icons/{name}.tif")
                            else:
                                return ''
            else:
                return ''

    def getdata (self,name):
        return control.read_record(name,'/etc/gui')

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
                    shell_theme = self.getdata("shell-theme")
                    if shell_theme==None:
                        shell_theme="barf"

                    if files.isfile (f"/usr/share/layouts/{shell_theme}-{name}.qml"):
                        return files.input(f"/usr/share/layouts/{shell_theme}-{name}.qml")
                    elif files.isfile(f"/usr/share/layouts/barf-{name}.qml"):
                        return files.input(f"/usr/share/layouts/barf-{name}.qml")
                    else:
                        return files.input(f"/usr/share/layouts/{name}.qml")
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
                theme = self.getdata('icon-theme')
                if theme == None:
                    theme = 'breeze'

                if files.isfile(f"/usr/share/icons/{theme}-{name}.svg"):
                    return files.input(f"/usr/share/icons/{theme}-{name}.svg")
                elif files.isfile(f"/usr/share/icons/{theme}-{name}.png"):
                    return files.input(f"/usr/share/icons/{theme}-{name}.png")
                elif files.isfile(f"/usr/share/icons/{theme}-{name}.gif"):
                    return files.input(f"/usr/share/icons/{theme}-{name}.gif")
                elif files.isfile(f"/usr/share/icons/{theme}-{name}.tif"):
                    return files.input(f"/usr/share/icons/{theme}-{name}.tif")
                else:
                    if name.startswith ('file-'):
                        if files.isfile(f'/usr/share/icons/{theme}-file.svg'):
                            return files.input(f'/usr/share/icons/{theme}-file.svg')
                        elif files.isfile(f'/usr/share/icons/{theme}-file.png'):
                            return files.input(f'/usr/share/icons/{theme}-file.png')
                        elif files.isfile(f'/usr/share/icons/{theme}-file.gif'):
                            return files.input(f'/usr/share/icons/{theme}-file.gif')
                        elif files.isfile(f'/usr/share/icons/{theme}-file.tif'):
                            return files.input(f'/usr/share/icons/{theme}-file.tif')
                        else:
                            return files.input(f'/usr/share/icons/breeze-file.png')
                    else:
                        if files.isfile(f"/usr/share/icons/breeze-{name}.svg"):
                            return files.input(f"/usr/share/icons/breeze-{name}.svg")
                        elif files.isfile(f"/usr/share/icons/breeze-{name}.png"):
                            return files.input(f"/usr/share/icons/breeze-{name}.png")
                        elif files.isfile(f"/usr/share/icons/breeze-{name}.gif"):
                            return files.input(f"/usr/share/icons/breeze-{name}.gif")
                        elif files.isfile(f"/usr/share/icons/breeze-{name}.tif"):
                            return files.input(f"/usr/share/icons/breeze-{name}.tif")
                        else:
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

            elif share.startswith('@sample'):
                if files.isfile(f"/usr/share/samples/{name}" ):
                    return f"/usr/share/samples/{name}"
                elif files.isdir(f"/usr/share/samples/{name}" ):
                    return f"/usr/share/samples/{name}"
                else:
                    return ''

            elif share.startswith("@string"):
                locale = control.read_record("locale", "/etc/gui")

                ## Set default lang ##
                if locale == None: locale = "en"

                ## Get value from string ##
                result = control.read_record(f'{name}',
                                             f"/usr/share/locales/{locale}.locale")

                ## Find default ##
                if result == None:
                    result = control.read_record(f'{name}',
                                                 f"/usr/share/locales/en.locale")

                return result

            ## None Resource ##
            else:
                return ''
        else:
            return ''

    def getname (self,app):
        locale = control.read_record("locale", "/etc/gui")

                ## Set default lang ##
        result =  self.etc (app,f'name[{locale}]')
        if result==None:
            result = self.etc (app,f'name[en]')

        return result

res = Res()
# system #
class System:
    def __init__(self,cmd):
        prompt = f'\"{sys.executable}\" vmabr.pyc exec '
        cmdln = cmd.split(" ")

        if '' in cmdln:
            cmdln.remove('')

        for i in cmdln:
            prompt+=f" {i}"

        subprocess.call(prompt,shell=True)
# app #
class App:
    ## Start ID Process ##
    def __init__(self):
        pass

    def terminal (self,title,icon,command):
        subprocess.call(f'''{files.readall(f"/etc/default/terminals/{control.read_record('external-terminal','/etc/gui')}")} {command}'''.replace('{0}',title).replace('{1}',icon),shell=True)

    def browser (self,url):
        if importlib.util.find_spec("PyQt5.QtWebEngineWidgets") is not None:
            System (f'webapp {url}')
        else:
            self.start(files.readall('/etc/default/browser'),url)

    def browser (self,url,icon):
        if importlib.util.find_spec("PyQt5.QtWebEngineWidgets") is not None:
            System (f'webapp {url} "{icon}"')
        else:
            self.start(files.readall('/etc/default/browser'),url)

    def browser (self,url,icon,title):
        if importlib.util.find_spec("PyQt5.QtWebEngineWidgets") is not None:
            System (f'webapp {url} "{icon}" "{title}"')
        else:
            self.start(files.readall('/etc/default/browser'),url)

    # start app
    def start(self,id,external):
        files = Files()

        ## Create id ##
        files.create(f"/proc/id/{id}.desk")

        ## Check desktop shortcut ##
        if files.isfile(f"/usr/share/applications/{id}.desk"):
            files.copy(f"/usr/share/applications/{id}.desk",
                       f"/proc/id/{id}.desk")  # Copy all informations about this GUI application

        ## Set default id ##
        files.write("/proc/info/id", id)

        if not (external=='' or external==None): files.write('/proc/info/ext',external)

        try:
            proc = multiprocessing.Process(target=startId)
            proc.start()
        except:
            pass

    ## Check id ##
    def check(self,id):
        files = Files()
        return files.isfile(f'/proc/id/{id}.desk')

    ## End id ##
    def end(self,id):
        files = Files()

        files.remove(f"/proc/id/{id}.desk")

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

        if files.isfile(f'/proc/id/{id}.desk'):
            files.write("/proc/info/id", id)

    ## Check application ##
    def exists (self,app):
        files = Files()

        return files.isfile(f'/usr/share/applications/{app}.desk')

    ## Signal ##
    def signal (self,sig):
        files = Files()
        files.write('/proc/info/sig',sig)

    def launchedlogo(self,title,logo):
        correctname = title.replace('\n', '').replace('(', '').replace(')', '').replace('0',
                                                                                                        '').replace('1',
                                                                                                                    '').replace(
            '2', '').replace('3', '').replace('4', '').replace('5', '').replace('6', '').replace('7', '').replace('8',
                                                                                                                  '').replace(
            '9', '')

        control.write_record(correctname,logo,'/etc/launched/logo.list')

app = App()
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
process = Process()
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
            try:
                names = name.split("/")

                while not self.exists(name):
                    l = len(names) - 1
                    names.pop(l)
                    name = ""
                    for i in names:
                        name += f"/{i}"
                    name = name.replace("//", "/")
            except:
                name = '/'

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
            if files.readall('/etc/guest') == "enable":
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
            if files.readall('/etc/guest') == "enable":
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
permissions = Permissions()
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

modules = Modules()

# files #
class Files:
    def __init__(self):
        pass

    def input_qml (self,filename):
        if filename.startswith("/"):
            return f"file:///stor/{filename}"

    def size (self,filename):
        return os.stat(self.input(filename)).st_size

    def input(self, filename):
        f = open ('proc/info/pwd','r')
        pwd = f.read()
        f.close()

        if filename.startswith("/"):
            return f"./{filename}"
        else:
            return f"./{pwd}/{filename}"

    def input_exec(self,filename):
        x = self.input(filename.replace("./", "")).replace(".//", "").replace("/", ".").replace('\\','/')

        if x.startswith('.////'):
            x = x.replace('.////', '/')

        return x

    def output(self,filename):
        #x = subprocess.check_output(f'readlink -f "{self.input(filename)}"',shell=True).decode('utf-8').replace('\n','').replace('/stor','')
        x = os.path.realpath (self.input(filename)).replace('/stor','').replace('C:\\stor\\','/').replace('C:\\stor','')
        if x=='':
            return '/'
        else:
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

files = Files()
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

    def read_in (self,name, filename):
        files = Files()
        for i in (files.readall(filename)).split("\n"):
            if i.__contains__(name):
                i = i.split(": ")
                if i[0].__contains__(name):
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
control = Control()
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
colors = Colors()

class Key:
    # create keys for wallet or bank
    def __init__(self,su):
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
            backend=default_backend()
        )
        public_key = private_key.public_key()

        private = private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        )
        
        f = open(files.input(f'/etc/key/{su}/Private Key.pem'), 'wb')
        f.write(private)
        f.close()

        public = public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )

        f = open(files.input(f'/etc/key/{su}/Public Key.pem'),'wb')
        f.write(public)
        f.close()

class Message:
    text = ''
    def __init__(self):
        super(Message, self).__init__()

    def Write (self,text):
        self.text+=text+"\n"

    def Save (self):
        self.user = files.readall('/proc/info/su')
        self.keydir = f'/etc/key/{self.user}'
        message = self.text.encode()

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

        f = open(files.input(f'/etc/external-key/Message.bin'), 'wb')
        f.write(encrypted)
        f.close()

    def Read (self):
        self.user = files.readall('/proc/info/su')
        with open(files.input(f'/etc/key/{self.user}/Private Key.pem'), "rb") as key_file:
            private_key = serialization.load_pem_private_key(
                key_file.read(),
                password=None,
                backend=default_backend()
            )

        f = open(files.input(f'/etc/key/{self.user}/Message.bin'), 'rb')
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
