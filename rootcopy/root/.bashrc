if [ -d /usr/share/defaults/etc/profile.d ] ; then
    for script in /usr/share/defaults/etc/profile.d/*.sh
    do
      source $script
    done
    unset script
fi

if [ -d /etc/profile.d ] ; then
    for script in /etc/profile.d/*.sh
    do
      source $script
    done
    unset script
fi

cd /stor
python3 vmabr.pyc login