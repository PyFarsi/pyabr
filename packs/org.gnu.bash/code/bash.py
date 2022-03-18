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

import subprocess, os
from pyabr.core import *

app.launchedlogo(res.get('@string/bash'),res.etc('bash','logo'))
app.launchedlogo("Konsole",res.etc('bash','logo'))
app.terminal (res.get('@string/bash'),'/stor/usr/share/icons/breeze-commento.svg','/usr/bin/bash')
