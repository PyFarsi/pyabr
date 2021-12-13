#!/bin/bash
# Run your built Pyabr
MEMORY=4000

qemu-system-i386 -m $MEMORY -enable-kvm -cdrom pyabr-i386.iso