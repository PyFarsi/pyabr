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

import subprocess,time
import sys, platform, hashlib, os, getpass, subprocess as sub, importlib,multiprocessing

## Configure kernel ###############################################################################

################## Module configure ##########################

sys.path.append("usr/app")

from pyabr.core import *
from pyabr.quick import *
from pyabr.cloud import *
from pyabr.chat import *

from termcolor import colored

################## Interface configure ##########################

modules.get_modules()

## @core/interface ##

if sys.argv[1:] == []:
    sys.argv[1:] = [files.readall('/etc/interface').lower()]

## @core/exec ##

if sys.argv[1:][0] == 'exec':

    if (sys.argv[1:][1:] == [] or
            sys.argv[1:][1] == "" or
            sys.argv[1:][1] == " " or
            sys.argv[1:][1].startswith(";")
    ):
        print(end='')

    elif sys.argv[1:][1].__contains__("/"):

        if files.isfile(f"{sys.argv[1:][1]}.pyc"):
            if permissions.check(f"{files.output(sys.argv[1:][1])}.pyc", "x", files.readall("/proc/info/su")):
                ## Set args ##
                sys.argv = sys.argv[1:][1:]

                appname = (sys.argv)[0]

                parent = files.parentdir(files.output(appname))[1:]

                sys.path.append(parent)
                __import__(files.filename(appname))
                sys.path.remove(parent)
            else:
                colors.show(sys.argv[1:][1], "perm", "")

        elif files.isfile(f'{sys.argv[1:][1]}.sa'):
            if permissions.check(f'{files.output(sys.argv[1:][1])}.sa', "x", files.readall("/proc/info/su")):
                Script(sys.argv[1:][1])
            else:
                colors.show(sys.argv[1:][1], "perm", "")
        else:
            colors.show(sys.argv[1:][1], "fail", "command not found.")
    else:
        ## Library execute in path ##
        if hasattr(commands, sys.argv[1:][1]):
            result = getattr(commands, sys.argv[1:][1])(sys.argv[1:][
                                                2:])  # https://stackoverflow.com/questions/3061/calling-a-function-of-a-module-by-using-its-name-a-string

        elif files.isfile(f"/usr/app/{sys.argv[1:][1]}.pyc"):
            if permissions.check(f"/usr/app/{files.output(sys.argv[1:][1])}.pyc", "x", files.readall("/proc/info/su")):
                ## Set args ##
                sys.argv = sys.argv[2:]
                __import__(sys.argv[0])
            else:
                colors.show(sys.argv[1:][1], "perm", "")

        elif files.isfile(f'/usr/app/{sys.argv[1:][1]}.sa') :
            if permissions.check(files.output(f'/usr/app/{sys.argv[1:][1]}.sa'), "x", files.readall("/proc/info/su")):
                Script(f'/usr/app/{sys.argv[1:][1]}')
            else:
                colors.show(sys.argv[1:][1], "perm", "")
        else:
            colors.show(sys.argv[1:][1], "fail", "command not found.")

    sys.exit()

###################################################################################

#if app.check('desktop'):
#    app.end('desktop')

################## Switch configure ##########################

switch = process.processor()  # Switch the process
process.check(switch)  # Check the switched process

if switch == None:
    switch = 0

files.write("/proc/info/sel", f"/proc/{str(switch)}")

####################################################################################################

## @core/distro ##

files.write("/proc/info/cs", control.read_record("name", "/etc/distro"))
files.write("/proc/info/cd", control.read_record("code", "/etc/distro"))
files.write("/proc/info/ver",  control.read_record("version", "/etc/distro"))
files.write("/proc/info/bl", control.read_record("build", "/etc/distro"))



# @core/os ##
if platform.system()=='Linux':
    files.write("/proc/info/kname", os.uname()[0])
    files.write("/proc/info/kver", os.uname()[2])
elif platform.system()=='Windows':
    files.write("/proc/info/kname", 'Kernel')
    files.write('/proc/info/kver','32')
else:
    files.write("/proc/info/kname", 'Unknown')
    files.write('/proc/info/kver','0.0')


## @core/tz ##

if os.path.isfile('/etc/issue.net'):
    f = open('/etc/issue.net', 'r')
    s = f.read();f.close()
    files.write("/proc/info/os", s.replace('\n',''))
else:
    files.write("/proc/info/os", platform.system())

try:
    files.write("/proc/info/arch", os.uname()[4])
except:
    files.write("/proc/info/arch",platform.architecture()[1])
files.write("/proc/info/os_su", getpass.getuser())
files.write("/proc/info/os_host", platform.node())
files.write("/proc/info/inter", sys.argv[1:][0])
files.write("/proc/info/tz", control.read_record("format", "/etc/time"))
files.write("/proc/info/sweek", control.read_record("start-week", "/etc/time"))
files.write("/proc/info/boot", 'vmabr.pyc')
files.write('/proc/info/host',files.readall('/etc/hostname'))
files.write('/proc/info/py', sys.executable)
files.write('/proc/info/de',res.getdata('desktop'))
files.write('/proc/info/gui',res.getdata('gui'))
## @core/dirs ##

for i in control.read_list("/etc/fhs"):
    if not files.isdir(i) and not files.isfile(i):
        files.mkdir(i)

## @core/welcome ##

if sys.argv[1:][0] == "kernel":
    print(f'\nWelcome to {control.read_record("name", "/etc/distro")} {control.read_record("version", "/etc/distro")} ({control.read_record("code", "/etc/distro")}) cloud software.\n')
    print(f'\n{files.readall("/etc/issue")}\n')

## @core/setup ##
if files.isfile ('/app/packages/ir.pyabr.setup.manifest') and sys.argv[1:][0]=='gui':
    files.write ('/etc/suapp','setup')
    sys.argv[1:]=['gui-desktop','root','toor']
    
## @core/gui ##

def gui():
    if not control.read_record('desktop', '/etc/gui') == None:
        os.environ['QT_QUICK_CONTROLS_STYLE'] = 'material'
        subprocess.call([sys.executable,'vmabr.pyc','exec',control.read_record('desktop','/etc/gui')])
def windows_manager ():
    try:
        subprocess.call([control.read_record('external-windows-manager','/etc/gui')])
    except:
        pass

if sys.argv[1:][0] == "gui":
    p1 = multiprocessing.Process(target=windows_manager)
    p2 = multiprocessing.Process(target=gui)

    p1.start()
    p2.start()

## @core/gui-splash ##

def gui_splash ():
    control.write_record('params', 'splash', '/etc/gui')

    if not control.read_record('desktop', '/etc/gui') == None:
        os.environ['QT_QUICK_CONTROLS_STYLE'] = 'material'
        subprocess.call([sys.executable,'vmabr.pyc','exec',control.read_record('desktop','/etc/gui')])

if sys.argv[1:][0] == "gui-splash":
    p1 = multiprocessing.Process(target=windows_manager)
    p2 = multiprocessing.Process(target=gui_splash)

    p1.start()
    p2.start()

## @core/gui-login ##

def gui_login():
    try:
        control.write_record('params', 'login', '/etc/gui')

        if not  control.read_record('desktop', '/etc/gui') == None:
            subprocess.call([sys.executable,'vmabr.pyc','exec',control.read_record('desktop','/etc/gui')])
    except:
        pass

if sys.argv[1:][0] == "gui-login":
    p1 = multiprocessing.Process(target=windows_manager)
    p2 = multiprocessing.Process(target=gui_login)

    p1.start()
    p2.start()
## @core/gui-enter ##

def gui_enter():
        if sys.argv[1:][1:] == [] or sys.argv[1:][1] == 'guest' or not files.isfile(f'/etc/users/{sys.argv[1:][1]}'):
            sys.exit(0)
        control.write_record('params', 'enter', '/etc/gui')
        control.write_record('username', sys.argv[1:][1], '/etc/gui')
        if not control.read_record('desktop', '/etc/gui') == None:
            os.environ['QT_QUICK_CONTROLS_STYLE'] = 'material'
            subprocess.call([sys.executable,'vmabr.pyc','exec',control.read_record('desktop','/etc/gui')])
if sys.argv[1:][0] == "gui-enter":
    p1 = multiprocessing.Process(target=windows_manager)
    p2 = multiprocessing.Process(target=gui_enter)

    p1.start()
    p2.start()

def gui_unlock():
        if sys.argv[1:][1:] == [] or sys.argv[1:][1] == 'guest' or not files.isfile(f'/etc/users/{sys.argv[1:][1]}'):
            sys.exit(0)
        control.write_record('params', 'unlock', '/etc/gui')
        control.write_record('username', sys.argv[1:][1], '/etc/gui')
        if not control.read_record('desktop', '/etc/gui') == None:
            os.environ['QT_QUICK_CONTROLS_STYLE'] = 'material'
            subprocess.call([sys.executable,'vmabr.pyc','exec',control.read_record('desktop','/etc/gui')])

if sys.argv[1:][0] == "gui-unlock":
    p1 = multiprocessing.Process(target=windows_manager)
    p2 = multiprocessing.Process(target=gui_unlock)

    p1.start()
    p2.start()

def gui_desktop():
        if sys.argv[1:][1:] == [] or sys.argv[1:][2:] == [] or sys.argv[1:][1] == 'guest' or not files.isfile(f'/etc/users/{sys.argv[1:][1]}'):
            sys.exit(0)


        if not hashlib.sha3_512(sys.argv[1:][2].encode()).hexdigest() == control.read_record('code', f'/etc/users/{sys.argv[1:][1]}'):
            sys.exit(0)

        control.write_record('params',
                            'desktop',
                            '/etc/gui')
        control.write_record('username', sys.argv[1:][1], '/etc/gui')
        control.write_record('password', sys.argv[1:][2], '/etc/gui')

        if not control.read_record('desktop', '/etc/gui') == None:
            os.environ['QT_QUICK_CONTROLS_STYLE'] = 'material'
            subprocess.call([sys.executable,'vmabr.pyc','exec',control.read_record('desktop','/etc/gui')])
## @core/gui-desktop ##

if sys.argv[1:][0] == "gui-desktop":
    p1 = multiprocessing.Process(target=windows_manager)
    p2 = multiprocessing.Process(target=gui_desktop)

    p1.start()
    p2.start()

## @lib/shell ##

def shell(user,code):

    if files.isfile(f'/etc/profile.sa'):
        Script('/etc/profile')

    if user == "root":
        files.write("/proc/info/pwd", "/root")
        if files.isfile(f'/root/profile.sa'):
            Script('/root/profile')
    else:
        files.write("/proc/info/pwd", f"/desk/{user}")
        if files.isfile(f'/desk/{user}/profile.sa'):
            Script(f'/desk/{user}/profile')

    if files.isfile(f'/tmp/exec.sa'):
        Script('/tmp/exec')

    hostname = files.readall('/proc/info/host')

    while True:
        if not files.isfile("/proc/selected"):
            files.write("/proc/info/sel", f"/proc/{str(switch)}")  ## Write this controller
        ## Check the switched process ##
        process.check(switch)  # Check the switched process

        files.write("/proc/info/sp", str(switch))  # Write switched process

        if files.isfile("/tmp/su.tmp"): files.remove("/tmp/su.tmp")

        ## User configure check ##
        files.write("/proc/info/su", user)  # Write user name in info processor

        if user=='root':
            prompt = '#'
            col = ['magenta','cyan']
        else:
            prompt = '>'
            col = ['magenta','cyan']

        hosti = colored(f"{user}@{hostname}",col[0])
        pathi = colored(f"{files.readall('/proc/info/pwd')}",col[1])

        cmd = input(f"{hosti}:{pathi}{prompt} ")
        cmdln = cmd.split(" ")

        strcmdln = ""

        for i in cmdln:
            if str(i).startswith(":"):
                var = control.read_record(str(i).replace(":", ""), files.readall("/proc/info/sel"))
                if var == None:
                    strcmdln += f" {i}"
                else:
                    strcmdln += f" {var}"
            else:
                strcmdln += f" {i}"

        ## Command line ##
        cmdln = strcmdln.split(" ")
        cmdln.remove('')

        ## All commands run in here ##

        ## Other commands ##
        if (cmdln == [] or
                cmdln[0] == "" or
                cmdln[0] == " " or
                cmd.startswith("#")
        ):
            continue
        elif cmdln[0]=='>' or cmdln[0]=='>>' or cmdln[0]=='>>>':
            cmdln.pop(0)
            scmd = ''
            for i in cmdln:
                if scmd=='':
                    scmd+=i
                else:
                    scmd+=f' {i}'

            strcmd = f"{sys.executable} -c \""
            strcmd2 = scmd.replace('"','\\"')
            strcmd = f"{strcmd}{strcmd2}\""
            subprocess.call(strcmd,shell=True)
        else:
            ## Prompt ##
            prompt = f'{sys.executable} vmabr.pyc exec'

            ## Arguments ##
            for i in cmdln[0:]:
                prompt+=f" {i}"

            ## Call the kernel ##
            sub.call(prompt,shell=True)


## @core/user ##

if sys.argv[1:][0] == "user":
    if sys.argv[1:][1] == "guest":
        if files.readall('/etc/guest') == "enable":
            ## Create info ##
            files.write("/proc/info/su", sys.argv[1:][1])
            shell('guest','*')
        else:
            colors.show(sys.argv[1:][1], "fail", "user not found.")
    else:
        if files.isfile(f"/etc/users/{sys.argv[1:][1]}"):
            files.write("/proc/info/su", sys.argv[1:][1])
            shell(sys.argv[1:][1],sys.argv[1:][2])
        else:
            sys.exit(0)

## @core/login ##

if sys.argv[1:][0] == "kernel" or sys.argv[1:][0] == "login":
    while True:
        print()

        process.check(switch)  # Check the switched process

        input_username = input("Enter an username: ")
        if input_username == "" or input_username == " ":
            continue
        elif input_username == "guest":
            if files.readall('/etc/guest') == "Yes":
                files.write("/proc/info/su", input_username)
                shell('guest','*')
            else:
                colors.show(input_username, "fail", "user not found.")
        elif files.isfile(f"/etc/users/{input_username}"):
                input_password = getpass.getpass(f"Enter {input_username}'s password: ")
                if hashlib.sha3_512(
                    str(input_password).encode()).hexdigest() == control.read_record("code", f"/etc/users/{input_username}"):
                    files.write("/proc/info/su", input_username)
                    shell(input_username,input_password)
                else:
                    colors.show(input_username, "fail", "wrong password.")
        else:
            colors.show(input_username, "fail", "user not found.")