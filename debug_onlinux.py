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

import os,shutil,subprocess,sys,platform
from buildlibs import pack_archives as pack

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
pack.linuxinstall()

subprocess.call(['sudo','cp','-rf','stor','/'])
subprocess.call(['sudo','chmod','-R','777','/stor'])
subprocess.call(f'echo "#!/bin/bash\ncd /stor\npython3 vmabr.pyc gui-desktop root toor" > ~/.local/bin/pyabr\nchmod +x ~/.local/bin/pyabr',shell=True)
subprocess.call([sys.executable,'-m','pip','uninstall','pyabr'])

print("Run: `pyabr` to launch Pyabr Platform")

subprocess.call(f'cd /stor && python3 vmabr.pyc {sys.argv[1]}',shell=True)