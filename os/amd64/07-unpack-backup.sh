#!/bin/bash
# This script used for unpacking 'backup.squashfs'

unsquashfs backup.squashfs
mv squashfs-root/* .
rmdir squashfs-root