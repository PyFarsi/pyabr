import subprocess

list = subprocess.check_output('xdotool search "."',shell=True).decode('utf-8').split('\n')
#listb = subprocess.check_output('xdotool search "baran"',shell=True).decode('utf-8').split('\n')
listp = subprocess.check_output('xdotool search "Pyabr OS"',shell=True).decode('utf-8').split('\n')

for i in listp:
    try:
        list.remove(i)
    except:
        pass

for i in list:
    if not 'vmabr' in i:
        subprocess.call(f'xdotool windowunmap {i}',shell=True)

for i in list:
    if not 'vmabr' in i:
        subprocess.call(f'xdotool windowmap {i}',shell=True)

#subprocess.call("xdotool search '.*' windowunmap %@",shell=True)
#subprocess.call("xdotool search '.*' windowmap %@",shell=True)