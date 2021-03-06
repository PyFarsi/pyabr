#######################################################################################
#  In the name of God, the Compassionate, the Merciful
#  Pyabr (c) 2020 Mani Jamali. GNU General Public License v3.0
#
#  Official Website: 		http://pyabr.rf.gd
#  Programmer & Creator:    Mani Jamali <manijamali2003@gmail.com>
#  Gap channel: 			@pyabr
#  Gap group:   			@pyabr_community
#  Git source:              github.com/PyFarsi/pyabr
#
#######################################################################################

import  shutil, os, sys,pyabr, subprocess

location  = str(pyabr.__file__).replace ("__init__.py","pyabr.zip")
shutil.unpack_archive(location,"pyabr-install","zip")
os.chdir ('pyabr-install')
subprocess.call([sys.executable,'setup.py'])
shutil.rmtree ("pyabr-install")