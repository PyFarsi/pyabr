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

import sys, subprocess
from pyabr.core import *

if sys.argv[1:]==[]:
    subprocess.call([sys.executable,'usr/app/pashmak_core.pyc'])

elif sys.argv[1].startswith('-') or sys.argv[1].startswith('@'):
    subprocess.call([sys.executable,'usr/app/pashmak_core.pyc',sys.argv[1]])
else:
    subprocess.call([sys.executable,'usr/app/pashmak_core.pyc',files.input(sys.argv[1])])

if files.isdir ('__pashmam__'):
    files.removedirs ('__pashmam__')

if files.isdir ('/__pashmam__'):
    files.removedirs ('/__pashmam__')