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

import  shutil, os, sys,pyabr, subprocess

location  = str(pyabr.__file__).replace ("__init__.py","").replace ("__main__.py","").replace ("setup.py","")
shutil.unpack_archive(f'{location}/pyabr.zip',f"{location}/pyabr-install","zip")
os.chdir (f'{location}/pyabr-install')
subprocess.call([sys.executable,'build.py'])
shutil.rmtree (f"{location}/pyabr-install")