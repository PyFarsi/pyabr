import subprocess, os
from pyabr.core import *
from pyabr.quick import *

if files.readall('/proc/info/su')=='root':
    user = f'/stor/root'
else:
    user = f'/stor/desk/{files.readall("/proc/info/su")}'
    
os.environ['HOME'] = user+"/Projects"

if os.path.isfile ('/usr/bin/code'):
    subprocess.call(f'mkdir -p {user}/vscode',shell=True)
    subprocess.call(f'code --user-data-dir={user}/vscode --no-sandbox',shell=True)
else:
    app = QGuiApplication ([])
    w = DataInstaller ('vscode','https://dl.pyabr.ir/06-vscode.sb','06-vscode.sb')
    app.exec()