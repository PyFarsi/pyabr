import subprocess
from pyabr.core import *

if files.readall('/proc/info/su')=='root':
    user = f'/stor/root'
else:
    user = f'/stor/desk/{files.readall("/proc/info/su")}'

if files.isfile('/usr/share/persepolis/data.sb'):
    subprocess.call('unsquashfs /stor/usr/share/persepolis/data.sb && cp -r squashfs-root/* / && rm -rf squashfs-root && rm /stor/usr/share/persepolis/*',shell=True)
subprocess.call(f'cd /stor/usr/app && python3 -m persepolis',shell=True)