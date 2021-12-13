import subprocess,os,sys
from pyabr.core import *

# Set home folder

if files.readall('/proc/info/su')=='root':
    user = f'/stor/root'
else:
    user = f'/stor/desk/{files.readall("/proc/info/su")}'

subprocess.call(['unsquashfs','/stor/usr/share/gerdoo/gerdoo.sb'])
subprocess.call(['rm','-rf',f'{user}/.config/chromium'])
subprocess.call(['mkdir','-v',f'{user}/.config/chromium'])
subprocess.call(f'cp -rf squashfs-root/* {user}/.config/chromium',shell=True)
subprocess.call('rm -rf squashfs-root',shell=True)
    
os.environ['HOME'] = user
# Running Chromium

subprocess.call(['chromium','--no-sandbox','https://gerdoo.me'])