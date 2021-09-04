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

import subprocess, os, sys, shutil

list = os.listdir('.')

for i in list:
    if i=='packs' or i=='buildlibs' or i=='osinstaller.py' or i=='clean.py':
        pass
    else:
        list.remove(i)

if not os.path.isdir('sb'):
    shutil.copytree('rootcopy','sb')
else:
    list.remove('sb')

for i in list:
    if os.path.isdir(i):
        shutil.copytree(i,'sb/'+i)
    else:
        shutil.copyfile(i, 'sb/'+i)

if os.path.isfile ('pyabr-amd64/pyabr/modules/stor.sb'): os.remove('pyabr-amd64/pyabr/modules/stor.sb')
subprocess.call(['mksquashfs','sb','pyabr-amd64/pyabr/modules/stor.sb','-comp','xz'])
subprocess.call(['sh','gen.sh'])
subprocess.call(['sh','run.sh'])
import clean