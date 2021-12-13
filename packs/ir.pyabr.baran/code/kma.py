import subprocess

list = subprocess.check_output('xdotool search "."',shell=True).decode('utf-8').split('\n')
listb = subprocess.check_output('xdotool search "baran"',shell=True).decode('utf-8').split('\n')
listp = subprocess.check_output('xdotool search "Pyabr OS"',shell=True).decode('utf-8').split('\n')

for i in listb:
    try:
        list.remove(i)
    except:
        pass

for i in listp:
    try:
        list.remove(i)
    except:
        pass

for i in list:
    subprocess.call(f'xdotool windowkill {i}',shell=True)