import subprocess
name = input('Enter a new name: ')
size = input('Enter the size of Pyabr Disk (e.g. 1G): ')
ram  = input('RAM for install [e.g. 4000]: ')
if size=='' or not size.endswith('G'):
    size='2G'
if ram=='':
    ram='4000'

print('Creating disk ...')
subprocess.call(['qemu-img','create',f'Disks/{name}.img',size])
print('Booting Pyabr ISO on this disk ...')
print('Please copy Pyabr with copydisk in current disk and shutdown it')
subprocess.call(['qemu-system-x86_64','-enable-kvm','-hda',f'Disks/{name}.img','-cdrom','../pyabr-x86_64.iso','-m',ram])