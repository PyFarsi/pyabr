from pyabr.core import *
from pyabr.quick import *

import subprocess,sys,os

if files.readall('/proc/info/su')=='root':
    user = f'/stor/root'
else:
    user = f'/stor/desk/{files.readall("/proc/info/su")}'
    
os.environ['HOME'] = user

if not os.path.isfile ('/usr/bin/libreoffice'):
    app = QApplication([])
    w = DataInstaller ('libreoffice','https://dl.pyabr.ir/08-libreoffice.sb','08-libreoffice.sb')
    app.exec()
elif sys.argv[1:]==[]:
    subprocess.call(['libreoffice','--draw'])
else:
    subprocess.call(['libreoffice','--draw',files.input(sys.argv[1])])