import os.path
import shutil

from pyabr.core import *

if not os.path.isdir('/usr/share/themes/Luna'):
    shutil.copytree('/stor/usr/share/themes/gtk/example','/usr/share/themes/example')

openbox = files.readall('/etc/default/openbox.xml.bak').replace('Win10','example')
files.write('/etc/default/openbox.xml',openbox)