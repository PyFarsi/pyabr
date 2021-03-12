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

import sys, platform, hashlib, os, getpass, subprocess as sub, importlib
## @variables ##

hostname = ""
distro_name = ""
distro_code = ""
distro_version = ""
distro_build = ""
ip = ""
arch = ""
os_user = ""
kernel_name = "vmabr"
kernel_version = "1.2.3"
user = ""
code = ""
argv = sys.argv[1:] # kernel parameters

if platform.node() == 'localhost':
    osname = 'Android'
    kernel_file = 'vmabr.py'
else:
    if os.path.isfile ('/etc/issue.net'):
        f = open('/etc/issue.net','r')
        osname = f.read()
        f.close()
    else:
        osname = platform.system()
    kernel_file = 'vmabr.pyc'

select = ""
tz = ""
cpu = ''
cpuc = ''
ram = ''
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

if argv == []:
    interface = files.readall ("/etc/interface").upper()

    if interface.startswith("CLI"):
        argv = ['kernel']
    elif interface.startswith("GUI"):
        argv = ['gui']
    else:
        colors.show("interface", "fail-start", "")
        colors.show("kernel", "stop", "")
        sys.exit(0)

## @core/params-check ##

if not (argv[0] == "kernel" or
    argv[0] == "gui" or
    argv[0] == "user" or
    argv[0] == "login" or
    argv[0] == "gui-splash" or
    argv[0] == "gui-login" or
    argv[0] == 'gui-enter' or
    argv[0] == 'gui-desktop' or
    argv[0] == "exec" ):
    colors.show("params-check", "fail-start", "")
    colors.show("kernel", "stop", "")
    sys.exit(0)
else:
    if argv[0]=='kernel' or argv[0]=='gui':
        if files.isfile ("/proc/0"):
            colors.show("params-check", "fail-start", "")
            colors.show("kernel", "stop", "")
            sys.exit(0)

colors.argv = argv[0] ## Set color argv

## @core/exec ##

if argv[0]=='exec':
    user = files.readall("/proc/info/su")

    inside = control.read_record('inside','/etc/exec')
    outside = control.read_record('outside', '/etc/exec')
    script = control.read_record('script', '/etc/exec')
    portable = control.read_record('portable', '/etc/exec')
    mirror = control.read_record('mirror','/etc/exec')

    if (argv[1:] == [] or
            argv[1] == "" or
            argv[1] == " " or
            argv[1].startswith(";")
    ):
        print(end='')

    elif argv[1].__contains__("/"):
        if files.isfile(argv[1]+".pyc") and outside=='Yes':
            if permissions.check(files.output(argv[1])+".pyc", "x", user):
                ## Set args ##
                sys.argv = argv[1:]

                appname = argv[1]

                parent = files.parentdir(files.output(appname))[1:]

                sys.path.append(parent)
                __import__(files.filename(appname))
                sys.path.remove (parent)

                # remove pycache
                if files.isdir (files.output('./__pycache__')): files.removedirs (files.output('./__pycache__'))
            else:
                colors.show(argv[1], "perm", "")

        elif files.isfile(argv[1]+".py") and outside=='Yes':
            if permissions.check(files.output(argv[1])+".py", "x", user):
                ## Set args ##
                sys.argv = argv[1:]

                appname = argv[1]

                parent = files.parentdir(files.output(appname))[1:]
                sys.path.append(parent)
                __import__(files.filename(appname))
                sys.path.remove (parent)

                if files.isdir (files.output('./__pycache__')): files.removedirs (files.output('./__pycache__'))
            else:
                colors.show(argv[1], "perm", "")

        elif files.isfile(argv[1]+".jar") and portable=='Yes':
            if permissions.check(files.output(argv[1]+".jar"), "x", user):
                ## command ##
                command = ["java",'--jar',files.input(argv[1]+".jar")]

                for i in argv[2:]:
                    command.append(i)

                sub.call(command)
            else:
                colors.show(argv[1], "perm", "")

        elif files.isfile(argv[1]+".exe") and portable=='Yes':
            if permissions.check(files.output(argv[1]+".exe"), "x", user):
                ## command ##
                command = [files.input(argv[1])+".exe"]

                for i in argv[2:]:
                    command.append(i)

                sub.call(command)
            else:
                colors.show(argv[1], "perm", "")

        elif files.isfile(argv[1]) and portable=='Yes':
            if permissions.check(files.output(argv[1]), "x", user):
                ## command ##
                command = [files.input(argv[1])]

                for i in argv[2:]:
                    command.append(i)

                sub.call(command)
            else:
                colors.show(argv[1], "perm", "")

        elif files.isfile(argv[1]+'.sa') and script == 'Yes':
            if permissions.check(files.output(argv[1])+'.sa', "x", user):
                Script (argv[1])
            else:
                colors.show(argv[1], "perm", "")
        else:
            colors.show(argv[1], "fail", "command not found.")
    else:
        ## Library execute in path ##
        if hasattr(commands,argv[1]) and inside=='Yes':
            result = getattr(commands, argv[1])(argv[2:]) # https://stackoverflow.com/questions/3061/calling-a-function-of-a-module-by-using-its-name-a-string

        elif files.isfile("/usr/app/"+argv[1]+".pyc") and outside=='Yes':
            if permissions.check("/usr/app/"+files.output(argv[1])+".pyc", "x", user):
                ## Set args ##
                sys.argv = argv[1:]

                __import__(argv[1])
            else:
                colors.show(argv[1], "perm", "")

        elif files.isfile("/usr/app/"+argv[1]+".py") and outside=='Yes':
            if permissions.check("/usr/app/"+files.output(argv[1])+".py", "x", user):
                ## Set args ##
                sys.argv = argv[1:]

                __import__(argv[1])

                if files.isdir (files.output('./__pycache__')): files.removedirs (files.output('./__pycache__'))
            else:
                colors.show(argv[1], "perm", "")

        elif files.isfile('/usr/app/'+argv[1]+".jar") and portable=='Yes':
            if permissions.check('/usr/app/'+files.output(argv[1]+".jar"), "x", user):
                ## command ##
                command = ["java",'--jar',files.input('/usr/app/'+argv[1]+".jar")]

                for i in argv[2:]:
                    command.append(i)

                sub.call(command)
            else:
                colors.show(argv[1], "perm", "")

        elif files.isfile ('/usr/app/'+argv[1]+'.exe') and portable=='Yes':
            if permissions.check("/usr/app/" + files.output(argv[1])+".exe", "x", user):
                ## command ##
                command = [files.input ('/usr/app/'+argv[1])+".exe"]

                for i in argv[2:]:
                    command.append(i)

                sub.call(command)
            else:
                colors.show(argv[1], "perm", "")

        elif files.isfile ('/usr/app/'+argv[1]) and portable=='Yes':
            if permissions.check("/usr/app/" + files.output(argv[1]), "x", user):
                ## command ##
                command = [files.input ('/usr/app/'+argv[1])]

                for i in argv[2:]:
                    command.append(i)

                sub.call(command)
            else:
                colors.show(argv[1], "perm", "")

        elif files.isfile('/usr/app/'+argv[1]+'.sa') and script=='Yes':
            if permissions.check(files.output('/usr/app/'+argv[1]+'.sa'), "x", user):
                Script ('/usr/app/'+argv[1])
            else:
                colors.show(argv[1], "perm", "")
        elif files.isfile ('/app/mirrors/'+argv[1]) and mirror=='Yes':
            if files.isfile ('/app/mirrors/'+argv[1]+".try"):
                print (files.readall('/app/mirrors/'+argv[1]+".try"))
            else:
                print ("Run `sudo paye in "+argv[1]+'`')
        elif argv[1]=='python' or argv[1]=='py':
            sub.call([files.readall('/proc/info/py')])
        elif argv[1]=='pip':
            argsv = [files.readall('/proc/info/py'), '-m', 'pip']
            for i in sys.argv[3:]:
                argsv.append(i)
            sub.call(argsv)
        elif argv[1]=='apt':
            argsv = ['apt']
            for i in sys.argv[3:]:
                argsv.append(i)
            sub.call(argsv)
        else:
            colors.show(argv[1], "fail", "command not found.")

    sys.exit()

###################################################################################

colors.show ("","poweron","")
if app.check('desktop'):
    app.end('desktop')

################## Switch configure ##########################

switch = process.processor() # Switch the process
process.check (switch) # Check the switched process

if switch == None:
    switch = 0

files.write("/proc/info/sel","/proc/"+str(switch))
select = files.readall("/proc/info/sel")


####################################################################################################

## @core/hostname ##

if files.isfile("/etc/hostname"):
    files.copy("/etc/hostname", "/proc/info/host")
    hostname = files.readall("/etc/hostname")
else:
    colors.show("hostname", "fail-start", "")
    colors.show("kernel", "stop", "")
    sys.exit(0)


## @core/distro ##

if files.isfile("/etc/distro"):
    distro_name = control.read_record("name", "/etc/distro")
    distro_code = control.read_record("code", "/etc/distro")
    distro_version = control.read_record("version", "/etc/distro")
    distro_build = control.read_record("build", "/etc/distro")
    files.write("/proc/info/cs", distro_name)
    files.write("/proc/info/cd", distro_code)
    files.write("/proc/info/ver", distro_version)
    files.write("/proc/info/bl", distro_build)
else:
    colors.show("distro", "fail-start", "")
    colors.show("kernel", "stop", "")
    sys.exit(0)

## @core/mount ##
if platform.system()=='Linux' and argv[0]=='gui':
    if not (files.isdir('/stor') and files.isfile('/stor')):
        os.system('ln -s /media stor')

    if not (files.isdir('/usr/share/fonts') and files.isfile('/usr/share/fonts')):
        os.system('ln -s /usr/share/fonts usr/share/fonts')

## @core/removeinstaller ##

if not (argv[0]=='user' or argv[0]=='login'):
    if files.isfile('/master.zip'): files.remove('/master.zip')
    if files.isfile('/pyabr-master.zip'): files.remove('/pyabr-master.zip')
    if files.isfile('/pyabr.zip'): files.remove('/pyabr.zip')
    if files.isdir('/pyabr-master'): files.removedirs('/pyabr-master')

## @core/kernel-info ##

    files.write("/proc/info/kname", kernel_name)
    files.write("/proc/info/kver", kernel_version)
## @core/system-info ##

    arch = platform.architecture()[0]
    os_user = getpass.getuser()
    os_host = platform.node()
    tz = control.read_record("format", "/etc/time")
    sweek = control.read_record("start-week", "/etc/time")
    py = sys.executable
    #mac = getmac.getmac.get_mac_address()

    if argv[0] == "kernel":
        interface = "CLI"
    else:
        interface = "GUI"

    files.write("/proc/info/os", osname)
    files.write("/proc/info/arch", arch)
    files.write("/proc/info/os_su", os_user)
    files.write("/proc/info/os_host", os_user)
    files.write("/proc/info/inter", interface)
    files.write("/proc/info/tz", tz)
    files.write("/proc/info/sweek", sweek)
    files.write("/proc/info/boot", kernel_file)
    files.write('/proc/info/py',py)

## @core/dirs ##

fhs = control.read_list ("/etc/fhs")
for i in fhs:
    if not files.isdir (i) and not files.isfile (i):
        files.mkdir (i)

## @core/welcome ##

if argv[0]=="kernel":
    print ()
    print ("Welcome to "+distro_name+" "+distro_version+" ("+distro_code+") cloud software.")
    print()

## @core/issue ##

if (argv[0]=="kernel") and files.isfile ("/etc/issue"):
    print ()
    print (files.readall("/etc/issue"))
    print ()

## @core/gui ##

if argv[0]=="gui":
    desktop = control.read_record('desktop','/etc/gui')

    from PyQt5.QtCore import *
    from PyQt5.QtWidgets import *

    try:
        from PyQt5.QtWebEngineWidgets import *
    except:
        pass

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

if argv[0]=="gui-splash":
    desktop = control.read_record('desktop', '/etc/gui')
    control.write_record('params','splash','/etc/gui')

    from PyQt5.QtCore import *
    from PyQt5.QtWidgets import *

    try:
        from PyQt5.QtWebEngineWidgets import *
    except:
        pass

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

if argv[0]=="gui-login":
    desktop = control.read_record('desktop', '/etc/gui')
    control.write_record('params','login','/etc/gui')

    from PyQt5.QtCore import *
    from PyQt5.QtWidgets import *

    try:
        from PyQt5.QtWebEngineWidgets import *
    except:
        pass

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

if argv[0]=="gui-enter":
    if argv[1:]==[] or argv[1]=='guest' or not files.isfile ('/etc/users/'+argv[1]):
        colors.show('gui-enter', 'fail-start', '')
        colors.show('kernel', 'stop', '')
        sys.exit(0)

    hashname = hashlib.sha3_256(argv[1].encode()).hexdigest()
    username = control.read_record('username','/etc/users/'+argv[1])

    if not hashname==username:
        colors.show('gui-enter', 'fail-start', '')
        colors.show('kernel', 'stop', '')
        sys.exit(0)

    # do the job #
    desktop = control.read_record('desktop', '/etc/gui')

    from PyQt5.QtCore import *
    from PyQt5.QtWidgets import *

    try:
        from PyQt5.QtWebEngineWidgets import *
    except:
        pass

    ## Main entry ##
    application = QApplication(sys.argv)
    app.start('desktop')
    ## https://www.cdog.pythonlibrary.org/2015/08/18/getting-your-screen-resolution-with-python/ Get screen model ##
    screen_resolution = application.desktop().screenGeometry()
    width, height = screen_resolution.width(), screen_resolution.height()

    files.write('/tmp/width', str(width))
    files.write('/tmp/height', str(height))

    control.write_record('params', 'enter', '/etc/gui')
    control.write_record('username',argv[1],'/etc/gui')
    if not desktop == None:
        w = importlib.import_module(desktop).Backend()
    else:
        colors.show('gui-enter', 'fail-start', '')
        colors.show('kernel', 'stop', '')
    sys.exit(application.exec_())

## @core/gui-desktop ##

if argv[0]=="gui-desktop":
    if argv[1:] == [] or argv[2:]==[] or argv[1] == 'guest' or not files.isfile('/etc/users/' + argv[1]):
        colors.show('gui-desktop', 'fail-start', '')
        colors.show('kernel', 'stop', '')
        sys.exit(0)

    hashname = hashlib.sha3_256(argv[1].encode()).hexdigest()
    username = control.read_record('username', '/etc/users/' + argv[1])

    if not hashname == username:
        colors.show('gui-desktop', 'fail-start', '')
        colors.show('kernel', 'stop', '')
        sys.exit(0)

    hashcode = hashlib.sha3_512(argv[2].encode()).hexdigest()
    password = control.read_record('code','/etc/users/'+argv[1])

    if not hashcode==password:
        colors.show('gui-desktop', 'fail-start', '')
        colors.show('kernel', 'stop', '')
        sys.exit(0)

    desktop = control.read_record('desktop', '/etc/gui')

    from PyQt5.QtCore import *
    from PyQt5.QtWidgets import *

    try:
        from PyQt5.QtWebEngineWidgets import *
    except:
        pass

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
    control.write_record('username',argv[1],'/etc/gui')
    control.write_record('password', argv[2], '/etc/gui')

    if not desktop == None:
        w = importlib.import_module(desktop).Backend()
    else:
        colors.show('gui-desktop', 'fail-start', '')
        colors.show('kernel', 'stop', '')
    sys.exit(application.exec_())

## @lib/shell ##

def shell():
    print()

    if files.isfile(f'/etc/profile.sa'):
        Script ('/etc/profile')

    if user=="root":
        files.write("/proc/info/pwd","/root")
        if files.isfile(f'/root/profile.sa'):
            Script('/root/profile')
    else:
        files.write("/proc/info/pwd","/desk/"+user)
        if files.isfile(f'/desk/{user}/profile.sa'):
            Script(f'/desk/{user}/profile')

    if files.isfile(f'/tmp/exec.sa'):
        Script('/tmp/exec')

    select = files.readall ("/proc/info/sel")  # Change selected database

    while True:
        if not files.isfile ("/proc/selected"):
            files.write("/proc/info/sel", "/proc/" + str(switch))  ## Write this controller
        ## Check the switched process ##
        process.check(switch)  # Check the switched process

        files.write("/proc/info/sp", str(switch))  # Write switched process

        if files.isfile ("/tmp/su.tmp"): files.remove ("/tmp/su.tmp")

        ## User configure check ##
        files.write("/proc/info/su",user) # Write user name in info processor
        if not user=="guest":
            hashname = hashlib.sha3_256(str(user).encode()).hexdigest()
            username = control.read_record("username","/etc/users/"+user)
            hashcode = hashlib.sha3_512(str(code).encode()).hexdigest()
            password = control.read_record("code","/etc/users/"+user)

            if not (hostname==username) and not (password==hashcode):
                colors.show("shell","fail-start","")
                colors.show("kernel","stop","")
                sys.exit(0)
        ## PWD path setting up at all ##
        if not user == "root":
            if not files.isdir("/desk/" + user): files.mkdir("/desk/" + user)  # Create home folder

        ## Prompt data base ##

        show_username = control.read_record("show_username", "/etc/prompt")
        show_hostname = control.read_record("show_hostname", "/etc/prompt")
        show_path = control.read_record("show_path", "/etc/prompt")
        root_symbol = control.read_record("root","/etc/prompt")
        user_symbol = control.read_record("user", "/etc/prompt")

        ## Setting up prompt data base 2 ##

        color_uh = ""
        color_path = ""
        prompt_symbol = ""

        if user=="root":
            prompt_symbol = root_symbol
            color_uh = colors.get_colors()
            color_path = colors.get_colors()
        else:
            prompt_symbol = user_symbol
            color_uh = colors.get_ok()
            color_path = colors.get_path()

        ## Setting up space of prompt ##

        if show_username == "Yes":
            space_username = user
        else:
            space_username = ""

        if show_hostname == "Yes":
            space_hostname = hostname
        else:
            space_hostname = ""

        if show_path == "Yes":
            space_path = files.readall("/proc/info/pwd")
        else:
            space_path = ""

        if show_hostname == "Yes" and show_username == "Yes":
            space1 = "@"
        else:
            space1 = ""

        if (show_hostname == "Yes" or show_username == "Yes") and show_path == "Yes":
            space2 = ":"
        else:
            space2 = ""

        ## Shell prompt ##

        cmd = input(color_uh + space_username + space1 + space_hostname + colors.get_colors() + space2 + color_path + space_path + colors.get_colors() + prompt_symbol + " ")

        cmdln = cmd.split(" ")


        strcmdln = ""

        for i in cmdln:
            if str(i).startswith("$"):
                select = files.readall("/proc/info/sel")
                var = control.read_record(str(i).replace("$",""),select)
                if var==None:
                    strcmdln = strcmdln + " " + i
                else:
                    strcmdln = strcmdln + " " + var
            else:
                strcmdln = strcmdln + " " + i

        ## Command line ##
        cmdln = strcmdln.split(" ")
        cmdln.remove ('')

        ## All commands run in here ##

        ## New command ##
        if cmdln[0]=="new":
            files.create ("/tmp/su.tmp")
            control.write_record ("username",user,"/tmp/su.tmp")
            control.write_record ("code",code,"/tmp/su.tmp")


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
                sys.executable, kernel_file,
                'exec',
                cmdln[0]
            ]

            ## Arguments ##
            for i in cmdln[1:]:
                prompt.append(i)

            ## Call the kernel ##
            sub.call(prompt)
## @core/user ##

if argv[0]=="user":
    input_username = argv[1]
    if input_username=="guest":
        enable_cli = control.read_record("enable_cli", "/etc/guest")
        if enable_cli == "Yes":
            ## Set variables ##
            user = "guest"
            code = "*"
            ## Create info ##
            files.write("/proc/info/su", input_username)
            shell()
            sys.exit(0)
        else:
            colors.show(input_username, "fail", "user not found.")
    else:
        input_password = argv[2]
        hashname = hashlib.sha3_256(str(input_username).encode()).hexdigest()
        hashcode = hashlib.sha3_512(str(input_password).encode()).hexdigest()

        if files.isfile ("/etc/users/"+input_username):
            username = control.read_record("username","/etc/users/"+input_username)
            password = control.read_record("code","/etc/users/"+input_username)
            if username==hashname and password==hashcode:
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
                colors.show("user", "fail-start", "")
                colors.show("kernel", "stop", "")
                sys.exit(0)
        else:
            colors.show ("user","fail-start","")
            colors.show ("kernel","stop","")
            sys.exit(0)

## @core/login ##

if argv[0]=="kernel" or argv[0]=="login":
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
            hashname = hashlib.sha3_256(
                str(input_username).encode()).hexdigest()  # Hashname creator from input_username
            username = control.read_record("username", "/etc/users/" + input_username)
            if not hostname == input_username:
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
