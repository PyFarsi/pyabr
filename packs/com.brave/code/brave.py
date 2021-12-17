import subprocess,os,sys
from pyabr.core import *

# Set home folder

if files.readall('/proc/info/su')=='root':
    user = f'/stor/root'
else:
    user = f'/stor/desk/{files.readall("/proc/info/su")}'

os.environ['HOME'] = user
# Running Chromium

if sys.argv[1:]==[] or sys.argv[1:]==['']:
    subprocess.call(['brave-browser','--no-sandbox'])
else:
    subprocess.call(['brave-browser','--no-sandbox',f'--app={sys.argv[1]}'])