#######################################################################################
#  In the name of God, the Compassionate, the Merciful
#  Pyabr (c) 2020 Mani Jamali. GNU General Public License v3.0
#
#  Official Website: 		http://pyabr.rf.gd
#  Programmer & Creator:    Mani Jamali <manijamali2003@gmail.com>
#  Gap channel: 			@pyabr
#  Gap group:   			@pyabr_community
#  Git source:              github.com/manijamali2003/pyabr
#
#######################################################################################
import os

def read_record (name,filename):
    file = open (filename,"r")
    strv = file.read()
    file.close()
    strv = strv.split("\n")

    for i in strv:
        if i.startswith(name):
            i = i.split(": ")
            if i[0]==(name):
                return i[1]

def read_list (filename):
    file = open (filename,"r")
    strv = file.read()
    file.close()
    strv = strv.split("\n")
    return strv

def write_record(name, value, filename):
    file = open (filename,'r')
    all = file.read()
    file.close()
    record = read_record(name, filename)
    os.remove(filename)
    if not (record == None):
        all = all.replace("\n"+name + ": " + record, "")
    file = open(filename,'w')
    file.write(all + "\n" + name + ": " + value)
    file.close()