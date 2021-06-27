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

import shutil, os, sys,py_compile
import base64

if not os.path.isdir ("build-packs"): os.mkdir ("build-packs")
if not os.path.isdir ("wheel/src"): os.mkdir("wheel/src")
shutil.unpack_archive('wheel/setup.zip','wheel/setup','zip') # Unpack setup wheel package

## Copy all files and dirs in wheel/setup/src ##

list = os.listdir('.')
list.remove('.idea')
list.remove('.git')
list.remove('wheel')
list.remove('.gitignore')
list.remove('clouddrive')
list.remove('AUTHERS')
list.remove('build.py')
list.remove('build-packs.py')
list.remove('debug.py')
list.remove('debug_apps')
list.remove('debug_params')
list.remove('installer.ui')
list.remove('LICENSE')
list.remove('pack.py')
list.remove('pack-wheel.py')
list.remove('README.md')
list.remove('requirments.txt')

for i in list:
    if os.path.isdir(i):
        shutil.copytree(i,'wheel/src/'+i)
    else:
        shutil.copyfile(i, 'wheel/src/'+i)


shutil.copyfile('LICENSE','wheel/setup/LICENSE')
shutil.copyfile('README.md','wheel/setup/README.md')
shutil.copyfile('wheel/setup-pack.py','wheel/setup/setup.py')
shutil.copyfile('wheel/setup-installer.py','wheel/setup/pyabr/setup.py')
file = open ("wheel/setup/pyabr/__main__.py","w");file.write('from pyabr import setup');file.close()

## Pack src to setup ##
shutil.make_archive('wheel/setup/pyabr/pyabr','zip','wheel/src')

## Build wheel package and save it to build-packs ##

os.system ("cd wheel/setup && \""+sys.executable+"\" setup.py bdist_wheel")

C = input('Do you want to clean the cache? [Y/n]: ')
if C.lower()=='y':
    import clean