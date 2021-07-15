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

# In the name of God, the Compassionte, the Merciful
# pyabr kernel (wet) written in Python
# Virtual Memory Abr Kernel (vmabr)
# (c) 2020 Mani Jamali All rights reserved.
import subprocess
import sys, platform, hashlib, os, getpass, subprocess as sub, importlib

## @variables ##

user = ""
code = ""

## Configure kernel ###############################################################################

################## Module configure ##########################

sys.path.append("usr/app")

from libabr import Modules, Files, Control, Colors, Process, Permissions, System, App, Commands, Script

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
    interface = files.readall("/etc/interface").upper()

    if interface.startswith("CLI"):
        sys.argv[1:] = ['kernel']
    elif interface.startswith("GUI"):
        sys.argv[1:] = ['gui']
    else:
        colors.show("interface", "fail-start", "")
        colors.show("kernel", "stop", "")
        sys.exit(0)

## @core/params-check ##

if not (sys.argv[1:][0] == "kernel" or
        sys.argv[1:][0] == "gui" or
        sys.argv[1:][0] == "user" or
        sys.argv[1:][0] == "login" or
        sys.argv[1:][0] == "gui-splash" or
        sys.argv[1:][0] == "gui-login" or
        sys.argv[1:][0] == 'gui-enter' or
        sys.argv[1:][0] == 'gui-desktop' or
        sys.argv[1:][0] == 'gui-unlock' or
        sys.argv[1:][0] == "exec"):
    colors.show("params-check", "fail-start", "")
    colors.show("kernel", "stop", "")
    sys.exit(0)
else:
    if sys.argv[1:][0] == 'kernel' or sys.argv[1:][0] == 'gui':
        if files.isfile("/proc/0"):
            colors.show("params-check", "fail-start", "")
            colors.show("kernel", "stop", "")
            sys.exit(0)

colors.argv = sys.argv[1:][0]  ## Set color argv

## @core/exec ##

if sys.argv[1:][0] == 'exec':

    if (sys.argv[1:][1:] == [] or
            sys.argv[1:][1] == "" or
            sys.argv[1:][1] == " " or
            sys.argv[1:][1].startswith(";")
    ):
        print(end='')

    elif sys.argv[1:][1].__contains__("/"):

        if files.isfile(sys.argv[1:][1] + ".pyc") and control.read_record('outside', '/etc/exec') == 'Yes':
            if permissions.check(files.output(sys.argv[1:][1]) + ".pyc", "x", files.readall("/proc/info/su")):
                ## Set args ##
                sys.argv = sys.argv[1:][1:]

                appname = sys.argv[1:][1]

                parent = files.parentdir(files.output(appname))[1:]

                sys.path.append(parent)
                __import__(files.filename(appname))
                sys.path.remove(parent)

                # remove pycache
                if files.isdir(files.output('./__pycache__')): files.removedirs(files.output('./__pycache__'))
            else:
                colors.show(sys.argv[1:][1], "perm", "")

        elif files.isfile(sys.argv[1:][1] + ".out") and control.read_record('portable', '/etc/exec') == 'Yes':
            if permissions.check(files.output(sys.argv[1:][1] + ".out"), "x", files.readall("/proc/info/su")):
                ## command ##
                command = [files.input(sys.argv[1:][1] + ".out")]

                for i in sys.argv[1:][2:]:
                    command.append(i)

                sub.call(command)
            else:
                colors.show(sys.argv[1:][1], "perm", "")

        elif files.isfile(sys.argv[1:][1] + '.sa') and control.read_record('script', '/etc/exec') == 'Yes':
            if permissions.check(files.output(sys.argv[1:][1]) + '.sa', "x", files.readall("/proc/info/su")):
                Script(sys.argv[1:][1])
            else:
                colors.show(sys.argv[1:][1], "perm", "")
        else:
            colors.show(sys.argv[1:][1], "fail", "command not found.")
    else:
        ## Library execute in path ##
        if hasattr(commands, sys.argv[1:][1]) and control.read_record('inside', '/etc/exec') == 'Yes':
            result = getattr(commands, sys.argv[1:][1])(sys.argv[1:][
                                                2:])  # https://stackoverflow.com/questions/3061/calling-a-function-of-a-module-by-using-its-name-a-string

        elif files.isfile("/usr/app/" + sys.argv[1:][1] + ".pyc") and control.read_record('outside', '/etc/exec') == 'Yes':
            if permissions.check("/usr/app/" + files.output(sys.argv[1:][1]) + ".pyc", "x", files.readall("/proc/info/su")):
                ## Set args ##
                sys.argv = sys.argv[1:][1:]

                __import__(sys.argv[1:][1])
            else:
                colors.show(sys.argv[1:][1], "perm", "")

        elif files.isfile('/usr/app/' + sys.argv[1:][1] + ".out") and control.read_record('portable', '/etc/exec') == 'Yes':
            if permissions.check("/usr/app/" + files.output(sys.argv[1:][1] + ".out"), "x", files.readall("/proc/info/su")):
                ## command ##
                command = [files.input('/usr/app/' + sys.argv[1:][1] + ".out")]

                for i in sys.argv[1:][2:]:
                    command.append(i)

                sub.call(command)
            else:
                colors.show(sys.argv[1:][1], "perm", "")

        elif files.isfile('/usr/app/' + sys.argv[1:][1] + '.sa') and control.read_record('script', '/etc/exec') == 'Yes':
            if permissions.check(files.output('/usr/app/' + sys.argv[1:][1] + '.sa'), "x", files.readall("/proc/info/su")):
                Script('/usr/app/' + sys.argv[1:][1])
            else:
                colors.show(sys.argv[1:][1], "perm", "")

        elif not control.read_record('command.' + sys.argv[1:][1], '/etc/exec') == None:

            command = [sys.argv[1:][1]]

            args = control.read_record(f'command.{sys.argv[1:][1]}.args', '/etc/exec')
            perm = control.read_record(f'command.{sys.argv[1:][1]}.perm', '/etc/exec')

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

colors.show("", "poweron", "")
if app.check('desktop'):
    app.end('desktop')

################## Switch configure ##########################

switch = process.processor()  # Switch the process
process.check(switch)  # Check the switched process

if switch == None:
    switch = 0

files.write("/proc/info/sel", "/proc/" + str(switch))

####################################################################################################
## @core/hostname ##

if files.isfile("/etc/hostname"):
    files.copy("/etc/hostname", "/proc/info/host")
else:
    colors.show("hostname", "fail-start", "")
    colors.show("kernel", "stop", "")
    sys.exit(0)

## @core/distro ##

if files.isfile("/etc/distro"):
    files.write("/proc/info/cs", control.read_record("name", "/etc/distro"))
    files.write("/proc/info/cd", control.read_record("code", "/etc/distro"))
    files.write("/proc/info/ver",  control.read_record("version", "/etc/distro"))
    files.write("/proc/info/bl", control.read_record("build", "/etc/distro"))
else:
    colors.show("distro", "fail-start", "")
    colors.show("kernel", "stop", "")
    sys.exit(0)

## @core/mount ##
files.write("/proc/info/kname", 'vmabr')
files.write("/proc/info/kver", '2.0.0')

if sys.argv[1:][0] == "kernel":
    interface = "CLI"
else:
    interface = "GUI"
if os.path.isfile('/etc/issue.net'):
    f = open('/etc/issue.net', 'r')
    s = f.read();f.close()
    files.write("/proc/info/os", s)
else:
    files.write("/proc/info/os", platform.system())

files.write("/proc/info/arch", platform.architecture()[0])
files.write("/proc/info/os_su", getpass.getuser())
files.write("/proc/info/os_host", platform.node())
files.write("/proc/info/inter", interface)
files.write("/proc/info/tz", control.read_record("format", "/etc/time"))
files.write("/proc/info/sweek", control.read_record("start-week", "/etc/time"))
files.write("/proc/info/boot", 'vmabr.pyc')
files.write('/proc/info/py', sys.executable)

## @core/dirs ##

for i in control.read_list("/etc/fhs"):
    if not files.isdir(i) and not files.isfile(i):
        files.mkdir(i)

## @core/welcome ##

if sys.argv[1:][0] == "kernel":
    print()
    print("Welcome to " + control.read_record("name", "/etc/distro") + " " +  control.read_record("version", "/etc/distro") + " (" + control.read_record("code", "/etc/distro") + ") cloud software.")
    print()

## @core/issue ##

if (sys.argv[1:][0] == "kernel") and files.isfile("/etc/issue"):
    print()
    print(files.readall("/etc/issue"))
    print()

## @core/gui ##

if sys.argv[1:][0] == "gui":
    desktop = control.read_record('desktop', '/etc/gui')

    from PyQt5.QtCore import *
    from PyQt5.QtWidgets import *

    ## Main entry ##
    application = QApplication(sys.argv)
    app.start('desktop')
    ## https://www.cdog.pythonlibrary.org/2015/08/18/getting-your-screen-resolution-with-python/ Get screen model ##
    screen_resolution = application.desktop().screenGeometry()
    width, height = screen_resolution.width(), screen_resolution.height()

    files.write('/tmp/width', str(width))
    files.write('/tmp/height', str(height))

    if not desktop == None:
        w = importlib.import_module(desktop).Backend()
    else:
        colors.show('gui', 'fail-start', '')
        colors.show('kernel', 'stop', '')

    sys.exit(application.exec_())

## @core/gui-splash ##

if sys.argv[1:][0] == "gui-splash":
    desktop = control.read_record('desktop', '/etc/gui')
    control.write_record('params', 'splash', '/etc/gui')

    from PyQt5.QtCore import *
    from PyQt5.QtWidgets import *

    ## Main entry ##
    application = QApplication(sys.argv)
    app.start('desktop')
    ## https://www.cdog.pythonlibrary.org/2015/08/18/getting-your-screen-resolution-with-python/ Get screen model ##
    screen_resolution = application.desktop().screenGeometry()
    width, height = screen_resolution.width(), screen_resolution.height()

    files.write('/tmp/width', str(width))
    files.write('/tmp/height', str(height))

    if not desktop == None:
        w = importlib.import_module(desktop).Backend()
    else:
        colors.show('gui-splash', 'fail-start', '')
        colors.show('kernel', 'stop', '')
    sys.exit(application.exec_())

## @core/gui-login ##

if sys.argv[1:][0] == "gui-login":
    desktop = control.read_record('desktop', '/etc/gui')
    control.write_record('params', 'login', '/etc/gui')

    from PyQt5.QtCore import *
    from PyQt5.QtWidgets import *

    ## Main entry ##
    application = QApplication(sys.argv)
    app.start('desktop')
    ## https://www.cdog.pythonlibrary.org/2015/08/18/getting-your-screen-resolution-with-python/ Get screen model ##
    screen_resolution = application.desktop().screenGeometry()
    width, height = screen_resolution.width(), screen_resolution.height()

    files.write('/tmp/width', str(width))
    files.write('/tmp/height', str(height))

    if not desktop == None:
        w = importlib.import_module(desktop).Backend()
    else:
        colors.show('gui-login', 'fail-start', '')
        colors.show('kernel', 'stop', '')
    sys.exit(application.exec_())

## @core/gui-enter ##

if sys.argv[1:][0] == "gui-enter":
    if sys.argv[1:][1:] == [] or sys.argv[1:][1] == 'guest' or not files.isfile('/etc/users/' + sys.argv[1:][1]):
        colors.show('gui-enter', 'fail-start', '')
        colors.show('kernel', 'stop', '')
        sys.exit(0)

    if not hashlib.sha3_256(sys.argv[1:][1].encode()).hexdigest() == control.read_record('username', '/etc/users/' + sys.argv[1:][1]):
        colors.show('gui-enter', 'fail-start', '')
        colors.show('kernel', 'stop', '')
        sys.exit(0)

    # do the job #
    desktop = control.read_record('desktop', '/etc/gui')

    from PyQt5.QtCore import *
    from PyQt5.QtWidgets import *

    ## Main entry ##
    application = QApplication(sys.argv)
    app.start('desktop')
    ## https://www.cdog.pythonlibrary.org/2015/08/18/getting-your-screen-resolution-with-python/ Get screen model ##
    screen_resolution = application.desktop().screenGeometry()
    width, height = screen_resolution.width(), screen_resolution.height()

    files.write('/tmp/width', str(width))
    files.write('/tmp/height', str(height))

    control.write_record('params', 'enter', '/etc/gui')
    control.write_record('username', sys.argv[1:][1], '/etc/gui')
    if not desktop == None:
        w = importlib.import_module(desktop).Backend()
    else:
        colors.show('gui-enter', 'fail-start', '')
        colors.show('kernel', 'stop', '')
    sys.exit(application.exec_())

if sys.argv[1:][0] == "gui-unlock":
    if sys.argv[1:][1:] == [] or sys.argv[1:][1] == 'guest' or not files.isfile('/etc/users/' + sys.argv[1:][1]):
        colors.show('gui-unlock', 'fail-start', '')
        colors.show('kernel', 'stop', '')
        sys.exit(0)

    if not hashlib.sha3_256(sys.argv[1:][1].encode()).hexdigest() == control.read_record('username', '/etc/users/' + sys.argv[1:][1]):
        colors.show('gui-unlock', 'fail-start', '')
        colors.show('kernel', 'stop', '')
        sys.exit(0)

    # do the job #
    desktop = control.read_record('desktop', '/etc/gui')

    from PyQt5.QtCore import *
    from PyQt5.QtWidgets import *

    ## Main entry ##
    application = QApplication(sys.argv)
    app.start('desktop')
    ## https://www.cdog.pythonlibrary.org/2015/08/18/getting-your-screen-resolution-with-,thon/ Get screen model ##
    screen_resolution = application.desktop().screenGeometry()
    width, height = screen_resolution.width(), screen_resolution.height()

    files.write('/tmp/width', str(width))
    files.write('/tmp/height', str(height))

    control.write_record('params', 'unlock', '/etc/gui')
    control.write_record('username', sys.argv[1:][1], '/etc/gui')
    if not desktop == None:
        w = importlib.import_module(desktop).Backend()
    else:
        colors.show('gui-unlock', 'fail-start', '')
        colors.show('kernel', 'stop', '')

    sys.exit(application.exec_())

## @core/gui-desktop ##

if sys.argv[1:][0] == "gui-desktop":
    if sys.argv[1:][1:] == [] or sys.argv[1:][2:] == [] or sys.argv[1:][1] == 'guest' or not files.isfile('/etc/users/' + sys.argv[1:][1]):
        colors.show('gui-desktop', 'fail-start', '')
        colors.show('kernel', 'stop', '')
        sys.exit(0)

    if not hashlib.sha3_256(sys.argv[1:][1].encode()).hexdigest() == control.read_record('username', '/etc/users/' + sys.argv[1:][1]):
        colors.show('gui-desktop', 'fail-start', '')
        colors.show('kernel', 'stop', '')
        sys.exit(0)

    hashcode = hashlib.sha3_512(sys.argv[1:][2].encode()).hexdigest()
    password = control.read_record('code', '/etc/users/' + sys.argv[1:][1])

    if not hashcode == password:
        colors.show('gui-desktop', 'fail-start', '')
        colors.show('kernel', 'stop', '')
        sys.exit(0)

    desktop = control.read_record('desktop', '/etc/gui')

    from PyQt5.QtCore import *
    from PyQt5.QtWidgets import *

    ## Main entry ##
    application = QApplication(sys.argv)
    app.start('desktop')
    ## https://www.cdog.pythonlibrary.org/2015/08/18/getting-your-screen-resolution-with-python/ Get screen model ##
    screen_resolution = application.desktop().screenGeometry()
    width, height = screen_resolution.width(), screen_resolution.height()

    files.write('/tmp/width', str(width))
    files.write('/tmp/height', str(height))

    control.write_record('params',
                         'desktop',
                         '/etc/gui')
    control.write_record('username', sys.argv[1:][1], '/etc/gui')
    control.write_record('password', sys.argv[1:][2], '/etc/gui')

    if not desktop == None:
        w = importlib.import_module(desktop).Backend()
    else:
        colors.show('gui-desktop', 'fail-start', '')
        colors.show('kernel', 'stop', '')
    sys.exit(application.exec_())


## @lib/shell ##

def shell():

    if files.isfile(f'/etc/profile.sa'):
        Script('/etc/profile')

    if user == "root":
        files.write("/proc/info/pwd", "/root")
        if files.isfile(f'/root/profile.sa'):
            Script('/root/profile')
    else:
        files.write("/proc/info/pwd", "/desk/" + user)
        if files.isfile(f'/desk/{user}/profile.sa'):
            Script(f'/desk/{user}/profile')

    if files.isfile(f'/tmp/exec.sa'):
        Script('/tmp/exec')


    while True:
        if not files.isfile("/proc/selected"):
            files.write("/proc/info/sel", "/proc/" + str(switch))  ## Write this controller
        ## Check the switched process ##
        process.check(switch)  # Check the switched process

        files.write("/proc/info/sp", str(switch))  # Write switched process

        if files.isfile("/tmp/su.tmp"): files.remove("/tmp/su.tmp")

        ## User configure check ##
        files.write("/proc/info/su", user)  # Write user name in info processor
        if not user == "guest":
            if not (hashlib.sha3_256(str(user).encode()).hexdigest() == control.read_record("username", "/etc/users/" + user)) and not ( hashlib.sha3_512(str(code).encode()).hexdigest() == control.read_record("code", "/etc/users/" + user)):
                colors.show("shell", "fail-start", "")
                colors.show("kernel", "stop", "")
                sys.exit(0)
        ## PWD path setting up at all ##
        if not user == "root":
            if not files.isdir("/desk/" + user): files.mkdir("/desk/" + user)  # Create home folder

        ## Prompt data base ##

        ## Setting up prompt data base 2 ##

        if user == "root":
            prompt_symbol = control.read_record("root", "/etc/prompt")
            color_uh = colors.get_colors()
            color_path = colors.get_colors()
        else:
            prompt_symbol = control.read_record("user", "/etc/prompt")
            color_uh = colors.get_ok()
            color_path = colors.get_path()

        ## Setting up space of prompt ##

        if control.read_record("show_username", "/etc/prompt") == "Yes":
            space_username = user
        else:
            space_username = ""

        if control.read_record("show_hostname", "/etc/prompt") == "Yes":
            space_hostname = files.readall("/etc/hostname")
        else:
            space_hostname = ""

        if control.read_record("show_path", "/etc/prompt") == "Yes":
            space_path = files.readall("/proc/info/pwd")
        else:
            space_path = ""

        if control.read_record("show_hostname", "/etc/prompt") == "Yes" and control.read_record("show_username", "/etc/prompt") == "Yes":
            space1 = "@"
        else:
            space1 = ""

        if (control.read_record("show_hostname", "/etc/prompt") == "Yes" or control.read_record("show_username", "/etc/prompt") == "Yes") and control.read_record("show_path", "/etc/prompt") == "Yes":
            space2 = ":"
        else:
            space2 = ""

        ## Shell prompt ##

        cmd = input(
            color_uh + space_username + space1 + space_hostname + colors.get_colors() + space2 + color_path + space_path + colors.get_colors() + prompt_symbol + " ")

        cmdln = cmd.split(" ")

        strcmdln = ""

        for i in cmdln:
            if str(i).startswith("$"):
                var = control.read_record(str(i).replace("$", ""), files.readall("/proc/info/sel"))
                if var == None:
                    strcmdln = strcmdln + " " + i
                else:
                    strcmdln = strcmdln + " " + var
            else:
                strcmdln = strcmdln + " " + i

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
            prompt = [
                sys.executable, 'vmabr.pyc',
                'exec',
                cmdln[0]
            ]

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
            ## Set variables ##
            user = "guest"
            code = "*"
            ## Create info ##
            files.write("/proc/info/su", sys.argv[1:][1])
            shell()
            sys.exit(0)
        else:
            colors.show(sys.argv[1:][1], "fail", "user not found.")
    else:
        if files.isfile("/etc/users/" + sys.argv[1:][1]):
            if  control.read_record("username", "/etc/users/" + sys.argv[1:][1]) == hashlib.sha3_256(str(sys.argv[1:][1]).encode()).hexdigest() and control.read_record("code", "/etc/users/" + sys.argv[1:][1]) == hashlib.sha3_512(str(sys.argv[1:][2]).encode()).hexdigest():
                ## Set variables ##
                user = sys.argv[1:][1]
                code = sys.argv[1:][2]
                ## Create info ##
                files.write("/proc/info/su", sys.argv[1:][1])
                permissions.user = user
                permissions.code = code
                shell()
                sys.exit(0)
            else:
                colors.show("user", "fail-start", "")
                colors.show("kernel", "stop", "")
                sys.exit(0)
        else:
            colors.show("user", "fail-start", "")
            colors.show("kernel", "stop", "")
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
                ## Set variables ##
                user = "guest"
                code = "*"
                ## Create info ##
                files.write("/proc/info/su", input_username)
                permissions.user = user
                permissions.code = code
                shell()
                sys.exit(0)
            else:
                colors.show(input_username, "fail", "user not found.")
        elif files.isfile("/etc/users/" + input_username):
            hashname =  hashlib.sha3_256(str(input_username).encode()).hexdigest()# Hashname creator from input_username
            username = control.read_record("username", "/etc/users/" + input_username)
            if not files.readall("/etc/hostname") == input_username:
                input_password = getpass.getpass("Enter " + input_username + "'s password: ")
                hashcode = hashlib.sha3_512(
                    str(input_password).encode()).hexdigest()  # Hashcode creator from input_password
                password = control.read_record("code", "/etc/users/" + input_username)
                if hashcode == password:
                    ## Set variables ##
                    user = input_username
                    code = input_password
                    ## Create info ##
                    files.write("/proc/info/su", input_username)
                    permissions.user = user
                    permissions.code = code
                    shell()
                    sys.exit(0)
                else:
                    colors.show(input_username, "fail", "wrong password.")
            else:
                colors.show(input_username, "fail", "user not found.")
        else:
            colors.show(input_username, "fail", "user not found.")