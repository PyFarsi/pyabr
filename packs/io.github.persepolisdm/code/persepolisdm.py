import subprocess
from pyabr.core import *

if files.readall('/proc/info/su')=='root':
    user = f'/stor/root'
else:
    user = f'/stor/desk/{files.readall("/proc/info/su")}'

subprocess.call(f'cd /stor/usr/app && python3 -m persepolis"',shell=True)