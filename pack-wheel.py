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

import shutil, os, sys,py_compile
import base64

if not os.path.isdir ("build-packs"): os.mkdir ("build-packs")
if not os.path.isdir ("wheel/src"): os.mkdir("wheel/src")
shutil.unpack_archive('wheel/setup.zip','wheel/setup','zip') # Unpack setup wheel package

## Copy all files and dirs in wheel/setup/src ##

list = os.listdir('.')
for i in list:
    if i=='packs' or i=='buildlibs' or i=='build.py' or i=='clean.py':
        pass
    else:
        list.remove(i)

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
    clean.clean()