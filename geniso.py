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

import subprocess, os, shutil,clean
from buildlibs import pack_archives as pack

# configure #
if not os.path.isdir ("app"):
	os.mkdir ("app")
	os.mkdir ("app/cache")
	os.mkdir ("app/cache/archives")
	os.mkdir ("app/cache/archives/data")
	os.mkdir ("app/cache/archives/control")
	os.mkdir ("app/cache/archives/code")
	os.mkdir ("app/cache/archives/build")
	os.mkdir ("app/cache/gets")

if not os.path.isdir ('stor'):		os.mkdir ('stor')
if not os.path.isdir ("stor/app"):	os.mkdir ("stor/app")
if not os.path.isdir ("stor/app/packages"): os.mkdir ("stor/app/packages")
if not os.path.isdir ('build-packs'): os.mkdir('build-packs')
pack.genisoinstall()

shutil.copytree("rootcopy","sb")
shutil.copytree ('stor','sb/stor')

# Create ISO #

subprocess.call(['mksquashfs','sb','os/pyabr/modules/stor.sb','-comp','xz','-b','1024K','-always-use-fragments','-noappend'])
subprocess.call('cd os && genisoimage -o ../pyabr-x86_64.iso -v -J -R -D -A pyabr -V pyabr -no-emul-boot -boot-info-table -boot-load-size 4 -b pyabr/boot/isolinux.bin -c pyabr/boot/isolinux.boot .',shell=True)
os.remove('os/pyabr/modules/stor.sb')
clean.clean()

subprocess.call('qemu-system-x86_64 -m 4000 -enable-kvm -cdrom pyabr-x86_64.iso -smp 4',shell=True)
