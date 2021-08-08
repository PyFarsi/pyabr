#######################################################################################
#  In the name of God, the Compassionate, the Merciful
#  Pyabr (c) 2020 Mani Jamali. GNU General Public License v3.0
#
#  Official Website: 		https://pyabr.ir
#  Programmer & Creator:    Mani Jamali <manijamali2003@gmail.com>
#  Gap channel: 			@pyabr
#  Gap group:   			@pyabr_community
#  Git source:              github.com/PyFarsi/pyabr
#
#######################################################################################

import subprocess, os, sys, shutil

list = os.listdir('.')
list.remove('.git')
list.remove('.idea')
list.remove('wheel')
list.remove('build.py')
list.remove('pack-sb.py')
list.remove('build-packs.py')
list.remove('LICENSE')
list.remove('upgrade.sa')
list.remove('pack-wheel.py')
list.remove('README.md')
list.remove('clouddrive')
list.remove('requirments.txt')
list.remove('.gitignore')
list.remove('mark_updates')
list.remove('build-date.txt')
list.remove('CONTRIBUTING.md')
list.remove('debug_params')
list.remove('debug_apps')

if '__pycache__' in list:
    list.remove('__pycache__')

if not os.path.isdir('sb'):
    os.mkdir('sb')
    os.mkdir('sb/stor')
    os.mkdir('sb/root')
    os.mkdir('sb/etc')

    f = open('sb/etc/issue.net', 'w')
    f.write('Pyabr')
    f.close()

    f = open('sb/etc/issue', 'w')
    f.write('Pyabr \\n \\l')
    f.close()

    f = open('sb/etc/os-release','w')
    f.write('''PRETTY_NAME="Pyabr 2 (Aras)"
NAME="Pyabr"
VERSION_ID="2"
VERSION="2 (Aras)"
VERSION_CODENAME=aras
ID=pyabr''')
    f.close()

    f = open('sb/root/.xinitrc','w')
    f.write('pyabr')
    f.close()

    f = open('sb/etc/hosts','w')
    f.write('''127.0.0.1	localhost
127.0.1.1	pyabr

# The following lines are desirable for IPv6 capable hosts
::1     localhost ip6-localhost ip6-loopback
ff02::1 ip6-allnodes
ff02::2 ip6-allrouters''')
    f.close()

    f = open('sb/etc/hostname','w')
    f.write('pyabr')
    f.close()

    f = open ('sb/etc/timezone','w')
    f.write('Asia/Tehran')
    f.close()
else:
    list.remove('sb')

for i in list:
    if os.path.isdir(i):
        shutil.copytree(i,'sb/'+i)
    else:
        shutil.copyfile(i, 'sb/'+i)

subprocess.call(['mksquashfs','sb','stor.sb','-comp','xz'])
import clean