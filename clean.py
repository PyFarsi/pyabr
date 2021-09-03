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

import os, shutil,sys
from buildlibs import  control


def clean():
    if os.path.isdir ('app'):                                           shutil.rmtree('app')
    if os.path.isdir ('build-packs'):                                   shutil.rmtree('build-packs')
    if os.path.isdir('wheel/src'):                                      shutil.rmtree('wheel/src')
    if os.path.isdir('wheel/setup'):                                    shutil.rmtree('wheel/setup')
    if os.path.isfile('pyabr.zip'):                                     os.remove    ('pyabr.zip')
    if os.path.isdir('sb'): shutil.rmtree('sb')

    for i in os.listdir ('/stor'):
        if os.path.isfile (f'/stor/{i}'):
            os.remove (f'/stor/{i}')
        else:
            shutil.rmtree (f'/stor/{i}')

if sys.argv[0]=='clean.py':
    clean()
