#!/bin/bash
# Build Dependencies of Pyabr
# Please use this script in your guest virtual fresh Debian
# Use Slax scripts

# Install firmwares
apt update
apt install --yes --no-install-recommends \
   firmware-linux-free \
   firmware-linux-nonfree \
   firmware-atheros \
   firmware-iwlwifi \
   firmware-zd1211 \
   firmware-realtek \
   firmware-bnx2 \
   firmware-brcm80211 \
   firmware-cavium \
   firmware-ipw2x00 \
   firmware-libertas \
   firmware-ti-connectivity \
   firmware-b43-installer

# Install GUI
apt-get update
apt-get install --yes --no-install-recommends \
    xserver-xorg xserver-xorg-video-all xserver-xorg-video-intel \
    xinit \
    konsole \
    openbox \
    libxcursor1 \
    breeze-cursor-theme \
    x11-utils \
    wmctrl \
    xdotool \
    libdrm-intel1 \
    libgl1-mesa-dri \
    libglu1-mesa

# Set setuid bit on xorg binary, so it can be started by guest user
chmod u+s /usr/lib/xorg/Xorg

cd /tmp
apt-get download x11-xserver-utils
dpkg -x x11-xserver-utils*.deb /tmp/x11utils
cd /tmp/x11utils
cp -aR * /

update-alternatives --set x-terminal-emulator /usr/bin/konsole

apt-get update
apt-get install --yes --no-install-recommends \
    python3-wget \
    python3-cryptoghraphy \
    python3-requests \
    python3-termcolor \
    python3-pyqt5 \
    python3-pyqt5.qtsvg \
    python3-pyqt5.qtquick \
    chromium \
    mpv \
    scrot