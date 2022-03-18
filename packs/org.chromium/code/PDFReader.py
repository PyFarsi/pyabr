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
   sys.exit(0)
else:
   if sys.argv[1].endswith('.pdf'):
      subprocess.call(['chromium','--no-sandbox',f'--app={files.input_qml(sys.argv[1])}'])
   else:
      sys.exit(0)