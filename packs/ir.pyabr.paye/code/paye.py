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

import sys, subprocess, os

from pyabr.core import *
from termcolor import colored

## Check root ##
if not permissions.check_root (files.readall("/proc/info/su")):
    colors.show ("paye","perm","")
    sys.exit(0)

## Check inputs ##
if sys.argv[1:]==[]:
    colors.show ("paye","fail","no inputs.")
    sys.exit(0)

if sys.argv[1]=="cl":
    package.clean()

elif sys.argv[1]=="pak" or sys.argv[1]=="pack":
    if files.isfile ("/app/cache/lock"):
        colors.show ("paye","fail","cache has already locked.")
        sys.exit(0)
    else:
        files.create ("/app/cache/lock")

    if sys.argv[2:]==[]:
        colors.show("paye", "fail", "no inputs.")
        sys.exit(0)

    dir = sys.argv[2:]

    for i in dir:
        print(f"Building {i.lower()} ...")
        package.build(i)

    package.clean()


elif sys.argv[1]=="upak" or sys.argv[1]=="unpack":
    if files.isfile ("/app/cache/lock"):
        colors.show ("paye","fail","cache has already locked.")
        sys.exit(0)
    else:
        files.create ("/app/cache/lock")

    if sys.argv[1:]==[]:
        colors.show("paye", "fail", "no inputs.")
        sys.exit(0)

    archive = sys.argv[2:]

    if not archive[1:]==[]:
        strv = ''
        for i in archive:
            strv+=f',{i}'

    for i in archive:
        if files.isfile(i):
            print(f"Unpacking {i.lower()} ...")
            package.unpack(i)
        else:
            colors.show("paye", "fail",  f"{i}: archive not found.")

    package.clean()

elif sys.argv[1]=="rm" or sys.argv[1]=="remove" or sys.argv[1]=="uninstall" or sys.argv[1]=="-r":
    if files.isfile ("/app/cache/lock"):
        colors.show ("paye","fail","cache has already locked.")
        sys.exit(0)
    else:
        files.create ("/app/cache/lock")

    if sys.argv[2]==[]:
        colors.show("paye", "fail", "no inputs.")
        sys.exit(0)

    list = control.read_list('/etc/paye/permanetly_applications')

    if not (sys.argv[2:])[1:] == []:
        strv = ''
        for i in (sys.argv[2:]):
            strv +=f',{i}'

    for i in (sys.argv[2:]):
        if not i in list:
            print(f"Uninstalling {i.lower()} ...")
            package.uninstall(i.lower())
        else:
            colors.show ('paye','fail',f"{i}: is a permanetly application that cannot be removed.")

    app.signal ('dock')
    app.signal ('apps')

    package.clean()

elif sys.argv[1]=="get" or sys.argv[1]=="download" or sys.argv[1]=="-d":

    if sys.argv[2]==[]:
        colors.show("paye", "fail", "no inputs.")
        sys.exit(0)


    if not (sys.argv[2:])[1:] == []:
        strv = ''
        for i in sys.argv[2:]:
            strv += f',{i}'
    for i in sys.argv[2:]:
        print(f"Downloading {i.lower()} ...")
        package.download (i.lower())

elif sys.argv[1]=="in" or sys.argv[1]=="it" or sys.argv[1]=="install" or sys.argv[1]=="-i":
    if files.isfile ("/app/cache/lock"):
        colors.show ("paye","fail","cache has already locked.")
        sys.exit(0)
    else:
        files.create ("/app/cache/lock")

    if sys.argv[2]==[]:
        colors.show("paye", "fail", "no inputs.")
        sys.exit(0)


    source = files.readall('/etc/paye/sources')

    if not (sys.argv[2:])[1:]==[]:
        strv = ''
        for i in sys.argv[2:]:
            strv+=f',{i}'

    for i in sys.argv[2:]:
        if files.isfile(f'/app/packages/{i.lower()}.manifest'):
            old = control.read_record('version', f'/app/packages/{i}.manifest')
            new = control.read_record('version', f'/app/mirrors/{i}.manifest')
            if not i==source and old == new and not old=='current':
                colors.show('paye','warning',f'{i}: package is up to date.')
            else:
                print(f"Downloading {i.lower()} ...")
                package.download(i.lower())
        else:
            print(f"Downloading {i.lower()} ...")
            package.download(i.lower())

    for j in sys.argv[2:]:
        if files.isfile(f'/app/packages/{j.lower()}.manifest'):
            old = control.read_record('version', f'/app/packages/{j}.manifest')
            new = control.read_record('version', f'/app/mirrors/{j}.manifest')
            if not i==source and old == new and not old=='current':
                pass
            else:
                package.unpack(f"/app/cache/gets/{j.lower()}.pa")
        else:
            package.unpack(f"/app/cache/gets/{j.lower()}.pa")

    # update desktop signals

    app.signal ('dock')
    app.signal ('apps')

    package.clean()

elif sys.argv[1]=="info" or sys.argv[1]=="-v":
    if sys.argv[2:]==[]:
        colors.show ('paye','fail','no inputs.')
        sys.exit(0)

    pack = f"/app/packages/{sys.argv[2]}.manifest"
    if files.isfile(pack):

        name = control.read_record ("name",pack)
        build = control.read_record("build", pack)
        version = control.read_record("version", pack)
        unpack = control.read_record("unpack", pack)
        description = control.read_record("description", pack)
        depends = control.read_record("depends", pack)
        license = control.read_record("license", pack)
        copyright = control.read_record("copyright", pack)

        if not (name == None or name == ""):  print(
            f"\t      Package name: {name}" )
        if not (version == None or version == ""):  print(
            f"\t   Package version: {version}" )
        if not (build == None or build == ""):  print(
            f"\t        Build date: {build}" )
        if not (copyright == None or copyright == ""):  print(
            f"\t         Copyright: {copyright}"   )
        if not (license == None or license == ""):  print(
            f"\t          License: {license}"   )
        if not (description == None or description == ""):  print(
            f"\t       Description: {description}"   )
        if not (unpack == None or unpack == ""):  print(
            f"\t      Installed in: {unpack}"   )
    else:
        colors.show ("paye","fail",f"{sys.argv[2]}: package has not already installed.")

elif sys.argv[1]=="ls" or sys.argv[1]=="list" or sys.argv[1]=="-l":
    list = files.list ("/app/mirrors")
    list.sort()
    for i in list:
        if i.endswith (".manifest"):
            try:
                name = control.read_record("name", f"/app/mirrors/{i}")
                build = control.read_record("build", f"/app/mirrors/{i}")
                version = control.read_record("version", f"/app/mirrors/{i}")
                if files.isfile (f'/app/packages/{i}'):
                    print (f"{colored(name,'green')}/{colored(version,'cyan')}/{colored(build,'cyan')} (installed)")
                else:
                    print (f"{colored(name,'green')}/{colored(version,'cyan')}/{colored(build,'cyan')}")
            except:
                pass
    print()

elif sys.argv[1]=='add':
    if sys.argv[2:]==[] or sys.argv[3:]==[]:
        colors.show ('paye','fail','no inputs.')
        sys.exit(0)

    package.add (sys.argv[2],sys.argv[3])

elif sys.argv[1]=='del' or sys.argv[1]=="delete":
    if sys.argv[2:]==[]:
        colors.show ('paye','fail','no inputs.')
        sys.exit(0)

    package.remove (sys.argv[2])

elif sys.argv[1]=='up' or sys.argv[1]=="update":
    System (f'sudo paye cl')
    System (f'sudo paye in ir.pyabr.updates')

    # backup files

    files.copy ('/etc/gui','/tmp/gui')
    files.copy ('/etc/hostname','/tmp/hostname')
    files.copy ('/etc/users/root','/tmp/root')
    files.copy ('/etc/time','/tmp/time')
    files.copy ('/etc/sudoers','/tmp/sudoers')
    files.copy ('/etc/permtab','/tmp/permtab')
    files.copy ('/etc/profile.sa','/tmp/profile.sa')
    files.copy ('/etc/cloud','/tmp/cloud')
    files.copy ('/etc/channel','/tmp/channel')
    files.copy ('/etc/default/hidden_files','/tmp/hidden_files')

    packages = files.list('/app/packages')
    
    for i in packages:
        if i.endswith ('.manifest'):
            System (f'sudo paye cl')
            System (f'sudo paye in {i.replace(".manifest","")}')
    
    files.cut ('/tmp/gui','/etc/gui')
    files.cut ('/tmp/hostname','/etc/hostname')
    files.cut ('/tmp/root','/etc/users/root')
    files.cut ('/tmp/time','/etc/time')
    files.cut ('/tmp/sudoers','/etc/sudoers')
    files.cut ('/tmp/permtab','/etc/permtab')
    files.cut ('/tmp/profile.sa','/etc/profile.sa')
    files.cut ('/tmp/cloud','/etc/cloud')
    files.cut ('/tmp/channel','/etc/channel')
    files.cut ('/tmp/hidden_files','/etc/default/hidden_files')

elif sys.argv[1]=='crt' or sys.argv[1]=="create":
    if sys.argv[2:]==[]:
        colors.show ('paye','fail','no inputs.')
        sys.exit(0)

    crtype = sys.argv[2]

    if sys.argv[3:]==[]:
        crname = 'untitled'
    else:
        crname = sys.argv[3]

    try:
        if crtype == 'python-console':
            files.copydir(res.get('@sample/python-console'), crname)
        elif crtype == 'python-qt':
            files.copydir(res.get('@sample/python-qt'), crname)
        elif crtype == 'python-quick':
            files.copydir(res.get('@sample/python-quick'), crname)
        elif crtype == 'python-webapp':
            files.copydir(res.get('@sample/python-webapp'), crname)
        elif crtype == 'pashmak-console':
            files.copydir(res.get('@sample/pashmak-console'), crname)
        elif crtype == 'saye-console':
            files.copydir(res.get('@sample/saye-console'), crname)
        else:
            files.copydir(res.get('@sample/python-console'), crtype)
    except:
        colors.show('paye','fail',f'cannot create project with {crname} name.')
else:
    colors.show ("paye","fail",f"{sys.argv[1]}: option not found.")