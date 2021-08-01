#!/bin/sh
# In the name of God, the Compassionate, the Merciful
# Pyabr master installer script

echo 'Help of copydisk for Pyabr: '
echo "1. n"
echo "2. p"
echo '3. 1'
echo "4. 2048"
echo "5. "
echo '6. a'
echo '7. w'

fdisk /dev/sda
mkfs.vfat -F 32 -v /dev/sda1
mount /dev/sda1 /mnt
cp -r /run/initramfs/memory/data/pyabr /mnt
sh /mnt/pyabr/boot/bootinst.sh
reboot