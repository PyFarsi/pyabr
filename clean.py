#######################################################################################
#  In the name of God, the Compassionate, the Merciful
#  Pyabr (c) 2020 Mani Jamali. GNU General Public License v3.0
#
#  Official Website: 		https://pyabr.ir
#  Programmer & Creator:    Mani Jamali <manijamali2003@gmail.com>
#  Gap channel: 			@pyabr
#  Gap group:   			@pyabr_community
#  Git source:              github.com/PyFarsi/pyabr
#
#######################################################################################

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
