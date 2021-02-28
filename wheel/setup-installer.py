#######################################################################################
#  In the name of God, the Compassionate, the Merciful
#  Pyabr (c) 2020 Mani Jamali. GNU General Public License v3.0
#
#  Official Website: 		http://pyabr.rf.gd
#  Programmer & Creator:    Mani Jamali <manijamali2003@gmail.com>
#  Gap channel: 			@pyabr
#  Gap group:   			@pyabr_community
#  Git source:              github.com/manijamali2003/pyabr
#
#######################################################################################

import site, shutil, os, sys

#print(site.getusersitepackages()) # https://stackoverflow.com/questions/122327/how-do-i-find-the-location-of-my-python-site-packages-directory

s = site.getusersitepackages()
shutil.copyfile(s+"/pyabr/pyabr.zip","pyabr.zip")
shutil.unpack_archive("pyabr.zip","pyabr-install","zip")
os.system("cd pyabr-install && \""+sys.executable+"\" setup.py")
shutil.rmtree("pyabr-install")
os.remove("pyabr.zip")