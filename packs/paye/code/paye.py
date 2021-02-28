#######################################################################################
#  In the name of God, the Compassionate, the Merciful
#  Pyabr (c) 2020 Mani Jamali. GNU General Public License v3.0
#
#  Official Website: 		http://pyabr.rf.gd
#  Programmer & Creator:    Mani Jamali <manijamali2003@gmail.com>
#  Gap channel: 			@pyabr
#  Gap group:   			@pyabr_community
#  Git source:              github.com/manijamali2003/pyabr
#
#######################################################################################

import sys, subprocess

from libabr import Files, Control, Permissions, Colors, Process, Modules, Package, Commands, Res

modules = Modules()
files = Files()
control = Control()
colors = Colors()
process = Process()
permissions = Permissions()
pack = Package()
cmd = Commands()
res = Res()

## Check root ##
if not permissions.check_root (files.readall("/proc/info/su")):
    colors.show ("paye","perm","")
    sys.exit(0)

## Check inputs ##
if sys.argv[1:]==[]:
    colors.show ("paye","fail","no inputs.")
    sys.exit(0)

option = sys.argv[1]

if option=="cl":
    pack.clean()

elif option=="pak":
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
        pack.build(i)

    pack.clean()


elif option=="upak":
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
            strv+=','+i

    for i in archive:
        if files.isfile(i):
            print (f'Unpacking \'{i}\' archive package ...')
            pack.unpack(i)
        else:
            colors.show("paye", "fail", i + ": archive not found.")

    pack.clean()

elif option=="rm":
    if files.isfile ("/app/cache/lock"):
        colors.show ("paye","fail","cache has already locked.")
        sys.exit(0)
    else:
        files.create ("/app/cache/lock")

    if sys.argv[2]==[]:
        colors.show("paye", "fail", "no inputs.")
        sys.exit(0)

    package = sys.argv[2:]

    list = control.read_list('/etc/paye/permanetly_applications')

    if not package[1:] == []:
        strv = ''
        for i in package:
            strv += ',' + i

    for i in package:
        if not i in list:
            print (f"Uninstalling {i} package ... ")
            pack.uninstall(i.lower())
        else:
            colors.show ('paye','fail',f"{i}: is a permanetly application that cannot be removed.")

    pack.clean()

elif option=="get":

    if sys.argv[2]==[]:
        colors.show("paye", "fail", "no inputs.")
        sys.exit(0)

    package = sys.argv[2:]

    if not package[1:] == []:
        strv = ''
        for i in package:
            strv += ',' + i
    for i in package:
        print (f'Downloading {i} archive package ... ')
        pack.download (i.lower())

elif option=="in":
    if files.isfile ("/app/cache/lock"):
        colors.show ("paye","fail","cache has already locked.")
        sys.exit(0)
    else:
        files.create ("/app/cache/lock")

    if sys.argv[2]==[]:
        colors.show("paye", "fail", "no inputs.")
        sys.exit(0)

    package = sys.argv[2:]

    if not package[1:]==[]:
        strv = ''
        for i in package:
            strv+=','+i

    for i in package:
        if files.isfile(f'/app/packages/{i.lower()}.manifest'):
            old = control.read_record('version', f'/app/packages/{i}.manifest')
            new = control.read_record('version', f'/app/mirrors/{i}.manifest')
            if not i=='latest' and old == new:
                colors.show('paye','warning',f'{i}: package is up to date.')
            else:
                print(f'Downloading {i} archive package ... ')
                pack.download(i.lower())
        else:
            print(f'Downloading {i} archive package ... ')
            pack.download(i.lower())

    for j in package:
        if files.isfile(f'/app/packages/{j.lower()}.manifest'):
            old = control.read_record('version', f'/app/packages/{j}.manifest')
            new = control.read_record('version', f'/app/mirrors/{j}.manifest')
            if not i=='latest' and old == new:
                pass
            else:
                print(f'Installing {i} archive package ... ')
                pack.unpack("/app/cache/gets/" + j.lower() + ".pa")
        else:
            print(f'Installing {i} archive package ... ')
            pack.unpack("/app/cache/gets/" + j.lower() + ".pa")

    pack.clean()

elif option=="info":
    if sys.argv[2:]==[]:
        colors.show ('paye','fail','no inputs.')
        sys.exit(0)

    pack = "/app/packages/"+sys.argv[2]+".manifest"
    if files.isfile(pack):

        name = control.read_record ("name",pack)
        build = control.read_record("build", pack)
        version = control.read_record("version", pack)
        unpack = control.read_record("unpack", pack)
        description = control.read_record("description", pack)
        depends = control.read_record("depends", pack)
        license = control.read_record("license", pack)
        copyright = control.read_record("copyright", pack)

        bold = colors.color(1, colors.get_bgcolor(), colors.get_fgcolor())
        if not (name == None or name == ""):  print(
            "\t      Package name: " + bold + name + colors.get_colors())
        if not (version == None or version == ""):  print(
            "\t   Package version: " + bold + version + colors.get_colors())
        if not (build == None or build == ""):  print(
            "\t        Build date: " + bold + build + colors.get_colors())
        if not (copyright == None or copyright == ""):  print(
            "\t         Copyright: " + bold + copyright + colors.get_colors())
        if not (license == None or license == ""):  print(
            "\t          Licensce: " + bold + license + colors.get_colors())
        if not (description == None or description == ""):  print(
            "\t       Description: " + bold + description + colors.get_colors())
        if not (depends == None or depends == ""):  print(
            "\t   Package depends: " + bold + depends + colors.get_colors())
        if not (unpack == None or unpack == ""):  print(
            "\t      Installed in: " + bold + unpack + colors.get_colors())
    else:
        colors.show ("paye","fail",sys.argv[2]+": package has not already installed.")

elif option=="ls":
    list = files.list ("/app/packages")
    bold = colors.color(1, colors.get_bgcolor(), colors.green)
    for i in list:
        if i.endswith (".manifest"):
            name = control.read_record("name", "/app/packages/"+i)
            build = control.read_record("build", "/app/packages/"+i)
            version = control.read_record("version", "/app/packages/"+i)
            print (bold+name+colors.get_colors()+"/"+colors.get_path()+version+colors.get_colors()+"/"+build)

elif option=='add':
    if sys.argv[2:]==[] or sys.argv[3:]==[]:
        colors.show ('paye','fail','no inputs.')
        sys.exit(0)

    pack.add (sys.argv[2],sys.argv[3])

elif option=='del':
    if sys.argv[2:]==[]:
        colors.show ('paye','fail','no inputs.')
        sys.exit(0)

    pack.remove (sys.argv[2])

elif option=='git':
    if sys.argv[2:]==[]:
        colors.show ('paye','fail','no inputs.')
        sys.exit(0)

    print(f'Cloning {sys.argv[2]} archive package ... ')
    pack.gitinstall (sys.argv[2])

elif option=='up':
    pack.upcloud ()

elif option=='pip':
    argsv = [files.readall('/proc/info/py'),'-m','pip']
    for i in sys.argv[2:]:
        argsv.append(i)
    subprocess.call(argsv)

elif option=='latest':
    print('Downloading the latest repo ... ')
    pack.download('latest')
    pack.unpack('/app/cache/gets/latest.pa')

elif option=='stable':
    print('Downloading the stable repo ... ')
    pack.download('stable')
    pack.unpack('/app/cache/gets/stable.pa')

elif option=='crt':
    if sys.argv[2:]==[]:
        colors.show ('paye','fail','no inputs.')
        sys.exit(0)

    crtype = sys.argv[2]

    if sys.argv[3:]==[]:
        crname = 'untitled'
    else:
        crname = sys.argv[3]

    if not files.isdir(crname):
        files.mkdir(crname)

    print(f'Creating {crname} project ... ',end='')
    if crtype=='gui':
        cmd.unzip ([res.get('@temp/simple-gui-project.zip'),crname])
    elif crtype=='web':
        cmd.unzip([res.get('@temp/simple-web-project.zip'), crname])
    else:
        cmd.unzip([res.get('@temp/simple-project.zip'), crname])
    print('done')
else:
    colors.show ("paye","fail",option+": option not found.")