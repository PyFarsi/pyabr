#!/bin/bash
# Run your fresh Debian 11

MEMORY=4000

qemu-system-x86_64 -m $MEMORY -enable-kvm -hda pyabr.img