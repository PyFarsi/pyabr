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
from buildlibs import pack_archives as pack
# configure #

RAM = 4000
Name = "Pyabr"
ISO = "pyabr-x86_64.iso"
genisoimage = " genisoimage"
QEMU = "qemu-system-x86_64"
SB = "mksquashfs"
USB = "unsquashfs"

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

if not os.path.isdir ('sb'): os.mkdir ('sb')
shutil.copytree ('stor','sb/stor')

# Create ISO #

subprocess.call([SB,'sb','os/stor.squashfs','-comp','xz'])
clean.clean()
subprocess.call(f'cd pyabr-amd64 && {genisoimage} -o ../{ISO} -v -J -R -D -A pyabr -V pyabr -no-emul-boot -boot-info-table -boot-load-size 4 -b pyabr/boot/isolinux.bin -c pyabr/boot/isolinux.boot .',shell=True)