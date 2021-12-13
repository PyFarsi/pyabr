#!/bin/bash
# This script used for creating fresh Disk with 2G
SIZE=20G # Should be upper than 8GB
qemu-img create disk pyabr.img $SIZE