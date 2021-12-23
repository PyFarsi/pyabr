import subprocess, os
from pyabr.core import *

lista = subprocess.check_output(['wmctrl','-l']).decode('utf-8').split('\n')
list2 = []
for i in lista:
    try:
        list2.append(i.split('  0 pyabr ')[1])
    except:
        pass

list2 = list(dict.fromkeys(list2))

