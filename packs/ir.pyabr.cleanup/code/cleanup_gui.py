'''
    Pyabr OS

    Python Cloud Operating System Platform (c) 2021 PyFarsi. Free Software GNU General Public License v3.0

    - Informations

    * Name:             Pyabr
    * Founder:          Mani Jamali
    * Developers:       PyFarsi Community
    * Package Manager:  Paye, PyPI
    * License:          GNU General Publice License v3.0

    - Official Website

    * Persian Page:     https://pyabr.ir
    * English Page:     https://en.pyabr.ir
'''

from pyabr.core import *
from pyabr.quick import *
import  subprocess

class MainApp (MainApp):
    def preclick_(self):
        self.pro.setProperty('indeterminate', True)
        QTimer.singleShot(3000,self.preclick1_)

    def preclick1_(self):
        self.pro.setProperty('indeterminate', False)
        QTimer.singleShot(1000, self.prog1_)

    def prog1_ (self):
        self.pro.setProperty('value', 0.1)
        try:
            list = subprocess.check_output('cd / && find -iname __pycache__', shell=True).decode('utf-8').split('\n')
            for i in list:
                subprocess.call(['rm', '-rf', i])
        except:
            pass

        QTimer.singleShot(1000, self.prog2_)

    def prog2_(self):
        self.pro.setProperty('value', 0.2)

        try:
            list = subprocess.check_output('cd / && find -iname *.log', shell=True).decode('utf-8').split('\n')
            for i in list:
                subprocess.call(['rm', '-rf', i])
        except:
            pass

        QTimer.singleShot(1000, self.prog3_)


    def prog3_(self):
        self.pro.setProperty('value', 0.3)

        try:
            list = subprocess.check_output('cd / && find -iname *wh.*', shell=True).decode('utf-8').split('\n')
            for i in list:
                subprocess.call(['rm', '-rf', i])
        except:
            pass

        QTimer.singleShot(1000, self.prog4_)

    def prog4_(self):
        self.pro.setProperty('value', 0.4)

        try:
            list = subprocess.check_output('cd / && find -iname *.tmp', shell=True).decode('utf-8').split('\n')
            for i in list:
                subprocess.call(['rm', '-rf', i])
        except:
            pass

        QTimer.singleShot(1000, self.prog5_)

    def prog5_(self):
        self.pro.setProperty('value', 0.5)

        try:
            list = subprocess.check_output('cd / && find -iname *.temp', shell=True).decode('utf-8').split('\n')
            for i in list:
                subprocess.call(['rm', '-rf', i])
        except:
            pass

        QTimer.singleShot(1000, self.prog6_)

    def prog6_(self):
        self.pro.setProperty('value', 0.6)

        subprocess.call('''rm -f /etc/fstab
                rm -f /etc/mtab
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
                remove_broken_links /usr/share/man''', shell=True)

        self.pro.setProperty('value', 1)

    def __init__(self):
        super(MainApp, self).__init__()

        self.load (res.get('@layout/cleanup'))

        self.btnCleanup = self.findChild ('btnCleanup')
        self.pro = self.findChild('pro')
        self.btnCleanup.clicked.connect (self.preclick_)

application = QtGui.QGuiApplication([])
application.setWindowIcon (QIcon(res.get(res.etc('cleanup','logo'))))

w = MainApp()
application.exec()