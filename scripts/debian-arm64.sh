#!/usr/bin/env bash
# This script used for creating the environment of Pyabr in Debian 11
# Do not run script in Host OS
# Run it in Virtual Machines

echo "If your os is a virtual machine please press [Enter]"
read

apt update
apt upgrade

echo 'Installing firmwares ...'
apt install --no-install-recommends \
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

echo 'Install Xorg environment ...'
apt-get install --yes --no-install-recommends \
    xserver-xorg \
    xserver-xorg-video-all \
    xserver-xorg-video-intel \
    xinit \
    xterm \
    openbox \
    libxcursor1 \
    breeze-cursor-theme \
    x11-utils \
    wmctrl \
    xdotool \
    libdrm-intel1 \
    libgl1-mesa-dri \
    libglu1-mesa

echo 'Setting up Xorg ...'
chmod u+s /usr/lib/xorg/Xorg
rm -Rf /usr/share/icons/breeze_cursors
mv /usr/share/icons/Breeze_Snow /usr/share/icons/breeze_cursors

cat >> /etc/systemd/system/display-manager.service << EOF
[Unit]
Description=X-Window
ConditionKernelCommandLine=!text
After=systemd-user-sessions.service

[Service]
ExecStart=/bin/su --login -c "/usr/bin/startx -- :0 vt7 -ac -nolisten tcp"
EOF

cp /etc/systemd/system/display-manager.service /usr/lib/systemd/system/xorg.service
cd /tmp
apt-get download x11-xserver-utils
dpkg -x x11-xserver-utils*.deb /tmp/x11utils
cd /tmp/x11utils
cp -aR * /
update-alternatives --set x-terminal-emulator /usr/bin/xterm

echo 'Installing Pyabr dependencies ...'
apt install --no-install-recommends \
  python3-pyqt5 \
  python3-pyqt5.qtsvg \
  python3-pyqt5.qtwebengine \
  python3-wheel \
  python3-pip \
  python3-pyqt5.qtquick \
  qml-module-qtquick* \
  qml-module-qtwebengine \
  sudo \
  chromium \
  mpv \
  python3-cryptography \
  python3-wget \
  python3-psutil \
  python3-requests \
  pulseaudio \
  squashfs-tools \
  python3-alsaaudio \
  python3-pocketsphinx \
  python3-pyaudio \
  espeak \

pip3 install aiml

wget https://dl.pyabr.ir/stor.sb
mount stor.sb /mnt
cp -r /mnt/* /
umount /mnt
rm -rf stor.sb
chmod 777 -R /stor

echo 'Cleaning up ...'
rm -Rf /tmp/*
rm -f /etc/apt/sources.list~
rm -Rf /etc/systemd/system/timers.target.wants
rm -f /etc/systemd/system/multi-user.target.wants/ssh.service
rm -f /etc/systemd/system/multi-user.target.wants/dnsmasq.service
rm -f /etc/ssh/ssh_host*
rm -f /var/backups/*
rm -f /var/cache/ldconfig/*
rm -f /var/cache/debconf/*
rm -f /var/cache/fontconfig/*
rm -f /var/lib/apt/extended_states
rm -f /var/lib/systemd/random-seed
rm -f /var/lib/apt/lists/deb.*
rm -Rf /root/.local/share/mc
rm -Rf /root/.cache
rm -f /root/.wget-hsts
rm -f /var/lib/dpkg/*-old
rm -f /var/log/*
rm -f /var/log/*/*
rm -f /var/log/*/*/*
rm -f /var/cache/apt/archives/*.deb
rm -f /var/cache/apt/*.bin
rm -f /var/cache/debconf/*-old
rm -f /var/lib/dhcp/dhclient.leases
rm -f /root/.bash_history
rm -f /root/.wget-hsts
rm -Rf /usr/share/doc/*
rm -Rf /usr/share/info/*
rm -f /usr/share/images/fluxbox/debian-squared.jpg
rm -Rf /usr/share/fluxbox/nls/??*
rm -Rf /usr/share/gnome/help
rm -Rf /usr/share/locale/??
rm -Rf /usr/share/locale/??_*
rm -Rf /usr/share/locale/??@*
rm -Rf /usr/share/locale/???
rm -Rf /usr/share/i18n/locales/*_*
rm -Rf /usr/share/man/??
rm -Rf /usr/share/man/*_*
rm -Rf /usr/share/icons/elementaryXubuntu-dark
rm -Rf /usr/share/icons/gnome/256x256
rm -Rf /usr/share/applications/*
rm -Rf /stor/tmp/*

uncompress_files()
{
   local LINK LINE

   find "$1" -type l -name "*.gz" | while read LINE; do
      LINK="$(readlink "$LINE" | sed -r 's/.gz$//')"
      FILE="$(echo "$LINE" | sed -r 's/.gz$//')"
      ln -sfn "$LINK" "$FILE"
      rm -f "$LINE"
   done
   find "$1" -type f -name "*.gz" | xargs -r gunzip
}

uncompress_files /etc/alternatives
uncompress_files /usr/share/man

remove_broken_links()
{
   find "$1" -type l -exec test ! -e {} \; -print | xargs rm -vf
}

remove_broken_links /etc/alternatives
remove_broken_links /usr/share/man

echo 'Installaction complete Press [Enter] to reboot ...'
read
reboot