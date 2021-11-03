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

import subprocess

from buildlibs import pack_archives as pack
from buildlibs import control
import shutil, os, sys, hashlib,getpass

os.chdir('/')

if os.path.isfile('/stor/vmabr.pyc'):

	if os.path.isdir('/stor/pyabr-master'):
		shutil.rmtree('/stor/pyabr-master')

	if os.path.isfile ('/stor/master.zip'):
		os.remove('/stor/master.zip')

	if os.path.isfile('/stor/proc/0'):  os.remove('/stor/proc/0')
	if os.path.isfile('/stor/proc/id/desktop'): os.remove('/stor/proc/id/desktop')
	if not os.path.isdir('/stor/proc/id'): os.mkdir('/stor/proc/id')

	os.system(f'cd /stor && "{sys.executable}" vmabr.pyc')
else:
	## pre build ##

	if not os.path.isdir("/app"):
		os.mkdir("/app")
		os.mkdir("/app/cache")
		os.mkdir("/app/cache/archives")
		os.mkdir("/app/cache/archives/data")
		os.mkdir("/app/cache/archives/control")
		os.mkdir("/app/cache/archives/code")
		os.mkdir("/app/cache/archives/build")
		os.mkdir("/app/cache/gets")

	if not os.path.isdir("/stor"):
		os.mkdir("/stor")
		os.mkdir("/stor/app")
		os.mkdir("/stor/app/packages")
	else:
		try:
			shutil.rmtree('/stor')
			os.mkdir("/stor")
		except:
			pass
		if not os.path.isdir("/stor/app"): os.mkdir("/stor/app")
		if not os.path.isdir("/stor/app/packages"): os.mkdir("/stor/app/packages")

	if not os.path.isdir("/build-packs"): os.mkdir("/build-packs")

	# build #

	pack.install()


	f = open('/stor/etc/suapp', 'w')
	f.write ('setup')
	f.close()

	from PyQt6.QtCore import *
	from PyQt6.QtWidgets import *

	control.write_record('width','1920','/stor/etc/gui')
	control.write_record('height','1080', '/stor/etc/gui')

	try:
		subprocess.call('ln -sf /usr/share/zoneinfo/Asia/Tehran /etc/localtime',shell=True)
		subprocess.call('hwclock --systohc --localtime',shell=True)
	except: pass

	os.system(f'cd /stor && "{sys.executable}" vmabr.pyc gui-desktop root toor')

if not os.path.isfile('/stor/testing'):
	os.system('poweroff')