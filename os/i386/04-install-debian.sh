#!/bin/bash
# This part for installing debian

MEMORY=4000

qemu-system-x86_64 -m $MEMORY -enable-kvm -cdrom cd.iso -hda pyabr.img