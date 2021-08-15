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

# In the name of God, the Compassionte, the Merciful
# pyabr kernel (wet) written in Python
# Virtual Memory Abr Kernel (vmabr)
# (c) 2020 Mani Jamali All rights reserved.
import subprocess,time
import sys, platform, hashlib, os, getpass, subprocess as sub, importlib,multiprocessing

## Configure kernel ###############################################################################

################## Module configure ##########################

sys.path.append("usr/app")

from libabr import Modules, Files, Control, Colors, Process, Permissions, System, App, Commands, Script
from termcolor import colored
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

################## Interface configure ##########################

modules = Modules()
files = Files()
control = Control()
colors = Colors()
process = Process()
permissions = Permissions()
app = App()
commands = Commands()

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

        elif not control.read_record( sys.argv[1:][1], '/etc/commands') == None:

            command = [sys.argv[1:][1]]

            args = control.read_record(f'{sys.argv[1:][1]}.args', '/etc/commands')
            perm = control.read_record(f'{sys.argv[1:][1]}.perm', '/etc/commands')

            # args check #
            if not args == None:
                if args == 'Yes':
                    args = True
                else:
                    args = False
            else:
                args = True

            # perm check #
            if perm == None:
                perm = 3

            if files.readall('/proc/info/su') == 'guest' and int(perm) < 3:
                colors.show(sys.argv[1:][1], 'perm', '')
                sys.exit(0)
            elif not files.readall('/proc/info/su') == 'root' and int(perm) < 2:
                colors.show(sys.argv[1:][1], 'perm', '')
                sys.exit(0)

            if args:
                for i in sys.argv[1:][2:]:
                    command.append(i)

            sub.call(command)
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

## @core/mount ##
files.write("/proc/info/kname", 'vmabr')
files.write("/proc/info/kver", '2.0.0')

if os.path.isfile('/etc/issue.net'):
    f = open('/etc/issue.net', 'r')
    s = f.read();f.close()
    files.write("/proc/info/os", s)
else:
    files.write("/proc/info/os", platform.system())

files.write("/proc/info/arch", platform.architecture()[0])
files.write("/proc/info/os_su", getpass.getuser())
files.write("/proc/info/os_host", platform.node())
files.write("/proc/info/inter", sys.argv[1:][0])
files.write("/proc/info/tz", control.read_record("format", "/etc/time"))
files.write("/proc/info/sweek", control.read_record("start-week", "/etc/time"))
files.write("/proc/info/boot", 'vmabr.pyc')
files.write('/proc/info/host',files.readall('/etc/hostname'))
files.write('/proc/info/py', sys.executable)

## @core/dirs ##

for i in control.read_list("/etc/fhs"):
    if not files.isdir(i) and not files.isfile(i):
        files.mkdir(i)

## @core/welcome ##

if sys.argv[1:][0] == "kernel":
    print(f'\nWelcome to {control.read_record("name", "/etc/distro")} {control.read_record("version", "/etc/distro")} ({control.read_record("code", "/etc/distro")}) cloud software.\n')
    print(f'\n{files.readall("/etc/issue")}\n')

    if not files.isfile('/proc/info/sym'):
        for j in control.read_list('/etc/symlinks'):

            if not files.isdir(j) and not files.isfile(j):
                subprocess.call(f'ln -sv {(j.split(":")[0])} /stor/{(j.split(":")[1])}', shell=True)

        files.create('/proc/info/sym')

## @core/gui ##

def gui():
    try:
        ## Main entry ##
        application = QApplication(sys.argv)
        app.start('desktop')
        ## https://www.cdog.pythonlibrary.org/2015/08/18/getting-your-screen-resolution-with-python/ Get screen model ##

        files.write('/tmp/width', str((application.desktop().screenGeometry()).width()))
        files.write('/tmp/height', str((application.desktop().screenGeometry()).height()))

        if not control.read_record('desktop', '/etc/gui') == None:
            w = importlib.import_module(control.read_record('desktop', '/etc/gui')).Backend()

        sys.exit(application.exec_())
    except:
        pass

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
    try:
        control.write_record('params', 'splash', '/etc/gui')

        ## Main entry ##
        application = QApplication(sys.argv)
        app.start('desktop')
        ## https://www.cdog.pythonlibrary.org/2015/08/18/getting-your-screen-resolution-with-python/ Get screen model ##

        files.write('/tmp/width', str((application.desktop().screenGeometry()).width()))
        files.write('/tmp/height', str((application.desktop().screenGeometry()).height()))

        if not control.read_record('desktop', '/etc/gui') == None:
            w = importlib.import_module(control.read_record('desktop', '/etc/gui')).Backend()
        sys.exit(application.exec_())
    except:
        pass

if sys.argv[1:][0] == "gui-splash":
    p1 = multiprocessing.Process(target=windows_manager)
    p2 = multiprocessing.Process(target=gui_splash)

    p1.start()
    p2.start()

## @core/gui-login ##

def gui_login():
    try:
        control.write_record('params', 'login', '/etc/gui')
        ## Main entry ##
        application = QApplication(sys.argv)
        app.start('desktop')
        ## https://www.cdog.pythonlibrary.org/2015/08/18/getting-your-screen-resolution-with-python/ Get screen model ##
        files.write('/tmp/width', str((application.desktop().screenGeometry()).width()))
        files.write('/tmp/height', str((application.desktop().screenGeometry()).height()))

        if not  control.read_record('desktop', '/etc/gui') == None:
            w = importlib.import_module( control.read_record('desktop', '/etc/gui')).Backend()
        sys.exit(application.exec_())
    except:
        pass

if sys.argv[1:][0] == "gui-login":
    p1 = multiprocessing.Process(target=windows_manager)
    p2 = multiprocessing.Process(target=gui_login)

    p1.start()
    p2.start()
## @core/gui-enter ##

def gui_enter():
    try:
        if sys.argv[1:][1:] == [] or sys.argv[1:][1] == 'guest' or not files.isfile(f'/etc/users/{sys.argv[1:][1]}'):
            sys.exit(0)

        ## Main entry ##
        application = QApplication(sys.argv)
        app.start('desktop')
        ## https://www.cdog.pythonlibrary.org/2015/08/18/getting-your-screen-resolution-with-python/ Get screen model ##
        files.write('/tmp/width', str((application.desktop().screenGeometry()).width()))
        files.write('/tmp/height', str((application.desktop().screenGeometry()).height()))

        control.write_record('params', 'enter', '/etc/gui')
        control.write_record('username', sys.argv[1:][1], '/etc/gui')
        if not control.read_record('desktop', '/etc/gui') == None:
            w = importlib.import_module(control.read_record('desktop', '/etc/gui')).Backend()
        sys.exit(application.exec_())
    except:
        pass

if sys.argv[1:][0] == "gui-enter":
    p1 = multiprocessing.Process(target=windows_manager)
    p2 = multiprocessing.Process(target=gui_enter)

    p1.start()
    p2.start()

def gui_unlock():
    try:
        if sys.argv[1:][1:] == [] or sys.argv[1:][1] == 'guest' or not files.isfile(f'/etc/users/{sys.argv[1:][1]}'):
            sys.exit(0)

        ## Main entry ##
        application = QApplication(sys.argv)
        app.start('desktop')
        ## https://www.cdog.pythonlibrary.org/2015/08/18/getting-your-screen-resolution-with-,thon/ Get screen model ##
        files.write('/tmp/width', str((application.desktop().screenGeometry()).width()))
        files.write('/tmp/height', str((application.desktop().screenGeometry()).height()))

        control.write_record('params', 'unlock', '/etc/gui')
        control.write_record('username', sys.argv[1:][1], '/etc/gui')
        if not control.read_record('desktop', '/etc/gui') == None:
            w = importlib.import_module(control.read_record('desktop', '/etc/gui')).Backend()

        sys.exit(application.exec_())
    except:
        pass

if sys.argv[1:][0] == "gui-unlock":
    p1 = multiprocessing.Process(target=windows_manager)
    p2 = multiprocessing.Process(target=gui_unlock)

    p1.start()
    p2.start()

def gui_desktop():
    try:
        if sys.argv[1:][1:] == [] or sys.argv[1:][2:] == [] or sys.argv[1:][1] == 'guest' or not files.isfile(f'/etc/users/{sys.argv[1:][1]}'):
            sys.exit(0)


        if not hashlib.sha3_512(sys.argv[1:][2].encode()).hexdigest() == control.read_record('code', f'/etc/users/{sys.argv[1:][1]}'):
            sys.exit(0)


        ## Main entry ##
        application = QApplication(sys.argv)
        app.start('desktop')
        ## https://www.cdog.pythonlibrary.org/2015/08/18/getting-your-screen-resolution-with-python/ Get screen model ##
        files.write('/tmp/width', str((application.desktop().screenGeometry()).width()))
        files.write('/tmp/height', str((application.desktop().screenGeometry()).height()))

        control.write_record('params',
                            'desktop',
                            '/etc/gui')
        control.write_record('username', sys.argv[1:][1], '/etc/gui')
        control.write_record('password', sys.argv[1:][2], '/etc/gui')

        if not control.read_record('desktop', '/etc/gui') == None:
            w = importlib.import_module(control.read_record('desktop', '/etc/gui')).Backend()
        sys.exit(application.exec_())
    except:
        pass

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
            col = ['white','white']
        else:
            prompt = '>'
            col = ['green','cyan']

        hosti = colored(f"{user}@{hostname}",col[0])
        pathi = colored(f"{files.readall('/proc/info/pwd')}",col[1])

        cmd = input(f"{hosti}:{pathi}{prompt} ")
        cmdln = cmd.split(" ")

        strcmdln = ""

        for i in cmdln:
            if str(i).startswith("$"):
                var = control.read_record(str(i).replace("$", ""), files.readall("/proc/info/sel"))
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

        ## New command ##
        if cmdln[0] == "new":
            files.create("/tmp/su.tmp")
            control.write_record("username", user, "/tmp/su.tmp")
            control.write_record("code", code, "/tmp/su.tmp")

        ## Other commands ##
        if (cmdln == [] or
                cmdln[0] == "" or
                cmdln[0] == " " or
                cmd.startswith("#")
        ):
            continue
        else:
            ## Prompt ##
            prompt = [sys.executable,'vmabr.pyc','exec',cmdln[0]]

            ## Arguments ##
            for i in cmdln[1:]:
                prompt.append(i)

            ## Call the kernel ##
            sub.call(prompt)


## @core/user ##

if sys.argv[1:][0] == "user":
    if sys.argv[1:][1] == "guest":
        enable_cli = control.read_record("enable_cli", "/etc/guest")
        if enable_cli == "Yes":
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
            enable_cli = control.read_record("enable_cli", "/etc/guest")
            if enable_cli == "Yes":
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