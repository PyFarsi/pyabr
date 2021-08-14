'''
    Pyabr OS

    Python Cloud Operating System Platform (c) 2021 PyFarsi. Free Software GNU General Public License v3.0

    - Informations

    * Name:             Pyabr
    * Founder:          Mani Jamali
    * Developers:       PyFarsi Community
    * Package Manager:  Paye, Apt, Dpkg, PyPI
    * License:          GNU General Publice License v3.0

    * Source code:      https://github.com/PyFarsi/pyabr
    * PyPI:             https://pypi.org/project/pyabr

    - Download Pyabr OS

    * AMD64, Intel64:   https://dl.pyabr.ir/pyabr-x86_64.iso     
    * ARM64:            https://dl.pyabr.ir/pyabr-arm64.img
    * Platform:         https://dl.pyabr.ir/stor.sb
    * Wheel Package:    https://dl.pyabr.ir/pyabr.whl
    
    - Channels:

    * Official Website: https://pyabr.ir
    * Telegram Channel: https://t.me/pyfarsi
    * Gap Channel:      https://gap.im/pyabr
    * Sorosh Channel:   https://splus.ir/pyabr
    * Instagram:        https://instagram.com/pyabrir
    * Hoorsa:           https://hoorsa.com/pyabr
    * Aparat:           https://aparat.com/pyabr

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

subprocess.call(['mksquashfs','sb','pyabr-amd64/pyabr/modules/stor.sb','-comp','xz'])
import clean