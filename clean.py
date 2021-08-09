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

import os, shutil
from buildlibs import  control


def clean():
    if os.path.isdir ('app'):                                           shutil.rmtree('app')
    if os.path.isdir ('build-packs'):                                   shutil.rmtree('build-packs')
    if os.path.isdir ('stor'):                                          shutil.rmtree('stor')
    if os.path.isdir('wheel/src'):                                      shutil.rmtree('wheel/src')
    if os.path.isdir('wheel/setup'):                                    shutil.rmtree('wheel/setup')
    if os.path.isfile('pyabr.zip'):                                     os.remove    ('pyabr.zip')
    if os.path.isdir('sb'): shutil.rmtree('sb')
clean()
