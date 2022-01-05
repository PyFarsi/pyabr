import subprocess, os

name = input('Enter an exists name: ')
ram  = input('RAM for launch [e.g. 4000]: ')
ip   = input('Enter remote device ip: ')
if os.path.isfile(f'Disks/{name}.img'):
    subprocess.call(f'export DISPLAY={ip}:0\nexport PULSE_SERVER=tcp:{ip}:4713\nqemu-system-x86_64 -m {ram} -enable-kvm -hda Disks/{name}.img',shell=True)
else:
    print(f'{name}: disk not found.')