import json
import subprocess
import sys
import hashlib

if sys.argv[1:]==[]:
    name = input('Enter a new name: ')
else:
    name = sys.argv[1]

f = open(f'Etc/Users/{name}.json','r')
config = json.loads(f.read())
f.close()

# Booting #
print('Booting Pyabr Hard Disk ...')
subprocess.call(['qemu-system-x86_64','-enable-kvm','-hda',f'Disks/{config["name"]}.img','-m',config["ram"],'-smp',config["smp"]])