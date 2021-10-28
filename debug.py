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

import subprocess, os, sys, shutil,clean

# configure #

RAM = 4000
Name = "Pyabr"
ISO = "pyabr-x86_64.iso"
genisoimage = " C:\\cygwin64\\bin\\genisoimage"
QEMU = "C:\\Program Files\\qemu\\qemu-system-x86_64"
SB = "C:\\cygwin64\\squashfs\\mksquashfs"
USB = "C:\\cygwin64\\squashfs\\unsquashfs"
# Remove unused files #
list = ['packs','buildlibs','osinstaller.py','clean.py']

# Root copy #
if not os.path.isdir('sb'):
    shutil.copytree('rootcopy','sb')
else:
    list.remove('sb')

for i in list:
    if os.path.isdir(i):
        shutil.copytree(i,'sb/'+i)
    else:
        shutil.copyfile(i, 'sb/'+i)

# Create ISO #

if os.path.isfile ('pyabr-amd64/pyabr/modules/stor.sb'): os.remove('pyabr-amd64/pyabr/modules/stor.sb')
subprocess.call([SB,'sb','pyabr-amd64/pyabr/modules/stor.sb','-comp','xz'])
clean.clean()
subprocess.call(f'cd pyabr-amd64 && {genisoimage} -o ../{ISO} -v -J -R -D -A pyabr -V pyabr -no-emul-boot -boot-info-table -boot-load-size 4 -b pyabr/boot/isolinux.bin -c pyabr/boot/isolinux.boot .',shell=True)
#subprocess.call(f'"{QEMU}" -m {str(RAM)} -accel hax -cdrom {ISO} -name {Name} ',shell=True)
