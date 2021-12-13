#!/bin/bash
# This script used for installing dependencies thant your host system should have to generate Pyabr
# Your host should be Debian base

sudo apt update
sudo apt install \
 qemu \
 qemu-system-x86 \
 genisoimage \
 squashfs-tools
sudo apt clean