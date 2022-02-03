import subprocess, os,sys ,json, hashlib

if sys.argv[1:]==[]:
    name = input('Enter a new name: ')
else:
    name = sys.argv[1]

name = hashlib.md5(name.encode()).hexdigest()

if sys.argv[2:]==[]:
    ip = input('Enter remote device ip: ')
else:
    ip = sys.argv[2]

f = open(f'Etc/Users/{name}.json','r')
config = json.loads(f.read())
f.close()


if os.path.isfile(f'Disks/{name}.img'):
    subprocess.call(f'export DISPLAY={ip}:0\nexport PULSE_SERVER=tcp:{ip}:4713\nqemu-system-x86_64 -m {config["ram"]} -enable-kvm -hda Disks/{name}.img -smp {config["smp"]}',shell=True)
else:
    print(f'{name}: disk not found.')