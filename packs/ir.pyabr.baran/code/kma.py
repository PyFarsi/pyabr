import subprocess

list = subprocess.check_output('/usr/bin/xdotool search "."',shell=True).decode('utf-8').split('\n')
listp = subprocess.check_output('/usr/bin/xdotool search "Pyabr OS"',shell=True).decode('utf-8').split('\n')

for i in listp:
    try:
        list.remove(i)
    except:
        pass

for i in list:
    subprocess.call(f'/usr/bin/xdotool windowkill {i}',shell=True)