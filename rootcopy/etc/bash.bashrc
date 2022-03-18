# ~/.bashrc: executed by bash(1) for non-login shells.

# Note: PS1 and umask are already set in /etc/profile. You should not
# need this unless you want different defaults for root.
# PS1='${debian_chroot:+($debian_chroot)}\h:\w\$ '
# umask 022

export EDITOR=mcedit
export LS_OPTIONS='--color=auto'
eval "`dircolors`"

apt-get()
{
   if [ -e /var/cache/apt/pkgcache.bin ]; then
      /usr/bin/apt-get "$@"
   else
      /usr/bin/apt-get update
      /usr/bin/apt-get "$@"
   fi
}

apt()
{
   if [ -e /var/cache/apt/pkgcache.bin ]; then
      /usr/bin/apt "$@"
   else
      /usr/bin/apt update
      /usr/bin/apt "$@"
   fi
}

export -f apt-get
export -f apt
exec="python3 vmabr.pyc exec"
alias add="$exec add"
alias bunzip="$exec bunzip"
alias bzip="$exec bzip"
alias cat="$exec cat"
alias cc="$exec cc"
alias cd="$exec cd"
alias check="$exec check"
alias chmod="$exec chmod"
alias chown="$exec chown"
alias clean="$exec clean"
alias clear="$exec clear"
alias cp="$exec cp"
alias date="$exec date"
alias det="$exec det"
alias down="$exec down"
alias echo="$exec echo"
alias getv="$exec getv"
alias gunzip="$exec gunzip"
alias gzip="$exec gzip"
alias link="$exec link"
alias logout="$exec logout"
alias ls="$exec ls"
alias mkdir="$exec mkdir"
alias mv="$exec mv"
alias new="$exec new"
alias passwd="$exec passwd"
alias pause="$exec pause"
alias paye="$exec paye"
alias push="$exec pwd"
alias push="$exec push"
alias read="$exec read"
alias reboot="$exec reboot"
alias rm="$exec rm"
alias say="$exec say"
alias sel="$exec sel"
alias set="$exec set"
alias shut="$exec shut"
alias shutdown="$exec shutdown"
alias sleep="$exec sleep"
alias su="$exec su"
alias sudo="$exec sudo"
alias tar="$exec tar"
alias touch="$exec touch"
alias uadd="$exec uadd"
alias udel="$exec udel"
alias uinfo="$exec uinfo"
alias unlink="$exec unlink"
alias unsel="$exec unsel"
alias unset="$exec unset"
alias untar="$exec untar"
alias unzip="$exec unzip"
alias up="$exec up"
alias upv="$exec upv"
alias ver="$exec ver"
alias view="$exec view"
alias wget="$exec wget"
alias xunzip="$exec xunzip"
alias xzip="$exec xzip"
alias zero="$exec zero"
alias zip="$exec zip"
alias exec="$exec"

# linux commands #
alias useradd="$exec uadd"
alias adduser="$exec uadd"
alias userdel="$exec udel"

export PS1="Bash # "