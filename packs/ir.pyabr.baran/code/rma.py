import subprocess

list = subprocess.check_output('/usr/bin/xdotool search "."',shell=True).decode('utf-8').split('\n')
#listb = subprocess.check_output('xdotool search "baran"',shell=True).decode('utf-8').split('\n')
listp = subprocess.check_output('/usr/bin/xdotool search "Pyabr OS"',shell=True).decode('utf-8').split('\n')

for i in listp:
    try:
        list.remove(i)
    except:
        pass

listp = subprocess.check_output('/usr/bin/xdotool search "vmabr.pyc"',shell=True).decode('utf-8').split('\n')

for i in listp:
    try:
        list.remove(i)
    except:
        pass

listp = subprocess.check_output('/usr/bin/xdotool search "Qt Selection*"',shell=True).decode('utf-8').split('\n')

for i in listp:
    try:
        list.remove(i)
    except:
        pass

for i in list:
    subprocess.call(f'/usr/bin/xdotool windowunmap {i}',shell=True)

for i in list:
    subprocess.call(f'/usr/bin/xdotool windowmap {i}',shell=True)