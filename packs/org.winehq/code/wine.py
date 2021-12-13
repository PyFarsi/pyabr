import subprocess,sys,os
from pyabr.core import *
from pyabr.quick import *

if not sys.argv[1:]==[]:
    subprocess.call(f'wine "{files.input(sys.argv[1])}"',shell=True)
elif not os.path.isfile ('/usr/bin/wine'):
    app = QApplication([])
    w = DataInstaller ('wine','https://dl.pyabr.ir/07-wine.sb','07-wine.sb')
    app.exec()
else:
    subprocess.call(f'winecfg',shell=True)