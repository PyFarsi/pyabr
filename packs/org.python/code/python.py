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
from pyabr.core import *
app.launchedlogo(res.get('@string/python'), res.etc('python', 'logo'))
app.launchedlogo(res.get('@string/python')+" — Konsole",res.etc('python','logo'))
app.terminal (res.get('@string/python'),'/stor/usr/share/icons/python.svg','/usr/bin/python3')