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

import subprocess, os, shutil,clean
from buildlibs import pack_archives as pack

# configure #
if not os.path.isdir ("app"):
	os.mkdir ("app")
	os.mkdir ("app/cache")
	os.mkdir ("app/cache/archives")
	os.mkdir ("app/cache/archives/data")
	os.mkdir ("app/cache/archives/control")
	os.mkdir ("app/cache/archives/code")
	os.mkdir ("app/cache/archives/build")
	os.mkdir ("app/cache/gets")

if not os.path.isdir ('stor'):		os.mkdir ('stor')
if not os.path.isdir ("stor/app"):	os.mkdir ("stor/app")
if not os.path.isdir ("stor/app/packages"): os.mkdir ("stor/app/packages")
if not os.path.isdir ('build-packs'): os.mkdir('build-packs')
pack.genisoinstall()

if not os.path.isdir ('sb'): os.mkdir ('sb')
shutil.copytree ('stor','sb/stor')
os.mkdir('sb/root')
os.makedirs('sb/usr/bin')
os.mkdir('sb/etc')
os.makedirs('sb/usr/lib')
f = open('sb/root/.xinitrc','w')
f.write('pyabr')
f.close()

f = open('sb/usr/bin/pyabr','w')
f.write('''#!/usr/bin/python3
import subprocess
f = open ('/stor/proc/info/su','w')
f.write('root')
f.close()
subprocess.call ('cd /stor && QTWEBENGINE_DISABLE_SANDBOX=1 python3 vmabr.pyc',shell=True)''')
f.close()

f = open('sb/etc/os-release','w')
f.write('''PRETTY_NAME="Pyabr 2.3.0"
NAME="Pyabr"
VERSION_ID="2.3.0"
VERSION="2.3.0 (Zayande Road)"
VERSION_CODENAME=zayanderoad
ID=pyabr
ID_LIKE=debian
HOME_URL="https://pyabr.ir/"''')
f.close()

f = open('sb/usr/lib/os-release','w')
f.write('''PRETTY_NAME="Pyabr 2.3.0"
NAME="Pyabr"
VERSION_ID="2.3.0"
VERSION="2.3.0 (Zayande Road)"
VERSION_CODENAME=zayanderoad
ID=pyabr
ID_LIKE=debian
HOME_URL="https://pyabr.ir/"''')
f.close()

f = open('sb/etc/issue','w')
f.write('Pyabr 2.3.0 \l \\n\n')
f.close()

f = open('sb/etc/issue.net','w')
f.write('Pyabr 2.3.0')
f.close()

subprocess.call(['chmod','+x','sb/usr/bin/pyabr'])

# Create ISO #

subprocess.call(['mksquashfs','sb','stor.sb','-comp','xz','-b','1024K','-always-use-fragments','-noappend'])
clean.clean()