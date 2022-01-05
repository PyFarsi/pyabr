export DISPLAY=$1:0
export PULSE_SERVER=tcp:$1:4713
qemu-system-x86_64 -m 4000 -smp 4 -enable-kvm -cdrom pyabr-x86_64.iso