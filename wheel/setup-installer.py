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

import  shutil, os, sys,pyabr, subprocess

location  = str(pyabr.__file__).replace ("__init__.py","").replace ("__main__.py","").replace ("setup.py","")
shutil.unpack_archive(f'{location}/pyabr.zip',f"{location}/pyabr-install","zip")
os.chdir (f'{location}/pyabr-install')
subprocess.call([sys.executable,'install.py'])