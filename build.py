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

from buildlibs import pack_archives as pack
from buildlibs import control
from pathlib import Path
import shutil, os, sys, hashlib,getpass,subprocess,platform
## pre build ##

if not os.path.isdir ("app"):
	os.mkdir ("app")
	os.mkdir ("app/cache")
	os.mkdir ("app/cache/archives")
	os.mkdir ("app/cache/archives/data")
	os.mkdir ("app/cache/archives/control")
	os.mkdir ("app/cache/archives/code")
	os.mkdir ("app/cache/archives/build")
	os.mkdir ("app/cache/gets")

if not os.path.isdir ("stor"):
	os.mkdir ("stor")
	os.mkdir ("stor/app")
	os.mkdir ("stor/app/packages")

if not os.path.isdir ("build-packs"): os.mkdir ("build-packs")

# build #

pack.install()
pack.inst('baran')

# run #
if os.path.isfile ('stor/proc/0'):  os.remove ('stor/proc/0')
if os.path.isfile ('stor/proc/id/desktop'): os.remove('stor/proc/id/desktop')
if not os.path.isdir('stor/proc/id'): os.mkdir('stor/proc/id')
if os.path.isdir('/stor'): shutil.rmtree('/stor')
shutil.copytree('stor/','/stor')

if platform.node()=='localhost':
	auto = input ('Do you want to run Pyabr in Termux automatically? [Y/n]: ')

	f = open ('pyabr.py','w')
	f.write('''import subprocess,sys
subprocess.call (f'cd stor && {sys.executable} vmabr.pyc login',shell=True)
''')
	f.close()

	if auto.lower()=='y':
		f.write('.bashrc','w')
		f.write(f'{sys.executable} pyabr.py')
		f.close()
	else:
		print ('For run Pyabr use `python pyabr.py`')

elif platform.system()=='Linux':
	f = open('/usr/bin/pyabr','w')
	f.write('''#!/bin/bash
cd /stor
python3 vmabr.pyc''')
	f.close()
	subprocess.call(['chmod','777','-R','/stor'])
	subprocess.call(['chmod','+x','/usr/bin/pyabr'])

	f = open('/usr/share/applications/pyabr.desktop','w')
	f.write('''[Desktop Entry]
Type=Application
Name=Pyabr
GenericName=Pyabr
X-GNOME-FullName=Pyabr
Exec=/usr/bin/pyabr %u
Icon=/stor/usr/share/icons/breeze-cloud.svg
Terminal=false
TryExec=pyabr
Name[fa_IR]=پای ابر''')
	f.close()
elif platform.system()=="Windows":
	f = open(f'{str(Path.home())}/pyabr.bat','w')
	f.write('''@echo off
cd /stor
python vmabr.pyc''')
	f.close()
import clean