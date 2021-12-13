#!/bin/bash
# This script makes from your image a compressed backup

mkdir backup
mv pyabr.img backup
mksquashfs backup backup.squashfs -comp xz -b 1024K -always-use-fragments -noappend
rmdir backup
