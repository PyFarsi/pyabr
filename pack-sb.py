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
try:
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
    list.remove('requirements.txt')
    list.remove('rootcopy')
    list.remove('.circleci')
    list.remove('debug.py')
    list.remove('.gitignore')
    list.remove('pyabr-amd64')
    list.remove('gen.sh')
    list.remove('run.sh')
    list.remove('pyabr-x86_64.iso')
    list.remove('mark_updates')
    list.remove('build-date.txt')
    list.remove('CONTRIBUTING.md')
    list.remove('debug_params')
    list.remove('debug_apps')
except:
    pass

if '__pycache__' in list:
    list.remove('__pycache__')

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