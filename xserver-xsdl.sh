export DISPLAY=$1:0
export PULSE_SERVER=tcp:$1:4713
python3 geniso.py