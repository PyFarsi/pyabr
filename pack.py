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

import os, shutil
from buildlibs import control

name = control.read_record('name','packs/pyabr/data/etc/distro')
version = control.read_record('version','packs/pyabr/data/etc/distro')
build = control.read_record('build','packs/pyabr/data/etc/distro')

if os.path.isdir ('pack-release'):
    shutil.rmtree('pack-release')

os.mkdir('pack-release')

list = os.listdir('.')
list.remove('.git')
list.remove('.idea')
list.remove('pack-release')

for i in list:
    if os.path.isdir(i):
        shutil.copytree(i,'pack-release/'+i)
    else:
        shutil.copyfile(i, 'pack-release/'+i)

shutil.make_archive(name+"-"+version+"-"+build,'zip','pack-release')
shutil.rmtree('pack-release')
