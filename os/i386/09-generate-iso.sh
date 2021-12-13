#!/bin/bash
# ISO Generator

cd live-cd && genisoimage -o ../pyabr-i386.iso -v -J -R -D -A pyabr -V pyabr -no-emul-boot -boot-info-table -boot-load-size 4 -b isolinux/isolinux.bin -c isolinux/boot.cat .