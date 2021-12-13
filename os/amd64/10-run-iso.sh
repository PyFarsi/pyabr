#!/bin/bash
# Run your built Pyabr
MEMORY=4000

qemu-system-x86_64 -m $MEMORY -enable-kvm -cdrom pyabr-amd64.iso