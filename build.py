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

from buildlibs import pack_archives as pack
from buildlibs import control
import shutil, os, sys, hashlib,getpass

import shutil, os

## pre build ##

if not os.path.isdir ("app"):
	os.mkdir ("app")
	os.mkdir ("app/cache")
	os.mkdir ("app/cache/archives")
	os.mkdir ("app/cache/archives/data")
	os.mkdir ("app/cache/archives/control")
	os.mkdir ("app/cache/archives/code")
	os.mkdir ("app/cache/archives/build")
	os.mkdir ("app/cache/gets")

if not os.path.isdir ("stor"):
	os.mkdir ("stor")
	os.mkdir ("stor/app")
	os.mkdir ("stor/app/packages")

if not os.path.isdir ("build-packs"): os.mkdir ("build-packs")

# build #

pack.install()
pack.inst('baran')

# run #
if os.path.isfile ('stor/proc/0'):  os.remove ('stor/proc/0')
if os.path.isfile ('stor/proc/id/desktop'): os.remove('stor/proc/id/desktop')
if not os.path.isdir('stor/proc/id'): os.mkdir('stor/proc/id')

shutil.make_archive('stor','zip','stor')
import clean