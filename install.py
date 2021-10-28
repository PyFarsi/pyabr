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

import os,shutil,subprocess,sys,platform

if platform.system()=='Linux':
    subprocess.call('cp -i pyabr-x86_64.iso vm/Linux/opt/pyabr/image.iso',shell=True)
    subprocess.call('cp -i packs/ir.pyabr.breeze-theme/data/usr/share/icons/breeze-cloud.svg vm/Linux/opt/pyabr/logo.svg',shell=True)
    subprocess.call('cp -r vm/Linux/* /',shell=True)
    subprocess.call('chmod 777 -R /opt/pyabr',shell=True)
    subprocess.call('chmod +x /usr/bin/pyabr',shell=True)