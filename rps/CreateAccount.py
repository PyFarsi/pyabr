import subprocess, json, os, hashlib
from termcolor import colored

# Asks
config = {'name':'','size':'','ram':'','smp':''}

config['name'] = input(colored('Enter a new name: ','cyan'))
config['size'] = input(colored('Enter the size of Pyabr Disk (e.g. 1G): ','cyan'))
config['ram']  = input(colored('RAM for install [e.g. 4000]: ','cyan'))
config['smp']  = input(colored('SMP Cores [e.g. 1]: ','cyan'))

# Checking #
if os.path.isfile(f'Etc/Users/{config["name"]}.json'):
    print(colored('User alreay exists','red'))
    exit(0)

# User config #
#help me https://moonbooks.org/Articles/How-to-save-a-dictionary-in-a-json-file-with-python-/
with open(f'Etc/Users/{config["name"]}.json', 'w') as fp:
    json.dump(config, fp)

# Creating Disk #
if config["size"]=='' or not config["size"].endswith('G'):
    size='2G'
if config["ram"]=='':
    ram='4000'

print('Creating disk ...')
subprocess.call(['qemu-img','create',f'Disks/{config["name"]}.img',config["size"]])

# Booting #
print('Booting Pyabr ISO on this disk ...')
print('Please copy Pyabr with copydisk in current disk and shutdown it')
subprocess.call(['qemu-system-x86_64','-enable-kvm','-hda',f'Disks/{config["name"]}.img','-cdrom','../pyabr-x86_64.iso','-m',config["ram"],'-smp',config["smp"]])