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
pack.install()

if not os.path.isdir ('sb'): os.mkdir ('sb')
shutil.copytree ('stor','sb/stor')

# Create ISO #

arch = input("Choose your debug arch [ 1. amd64 , 2. i386 ]: ")
subprocess.call(['mksquashfs','sb','os/stor.squashfs','-comp','xz'])
shutil.copyfile ('os/stor.squashfs','os/amd64/live-cd/live/stor.squashfs')
shutil.copyfile ('os/stor.squashfs','os/arm/live-cd/live/stor.squashfs')
shutil.copyfile ('os/stor.squashfs','os/arm64/live-cd/live/stor.squashfs')
shutil.copyfile ('os/stor.squashfs','os/i386/live-cd/live/stor.squashfs')
os.remove('os/stor.squashfs')

if arch=='1':
	subprocess.call('cd os/amd64 && sh 09-generate-iso.sh && sh 10-run-iso.sh',shell=True)
elif arch=='2':
	subprocess.call('cd os/i386 && sh 09-generate-iso.sh && sh 10-run-iso.sh',shell=True)
clean.clean()