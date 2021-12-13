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
import os

def read_record (name,filename):
    file = open (filename,"r",encoding='utf-8')
    strv = file.read()
    file.close()
    strv = strv.split("\n")

    for i in strv:
        if i.startswith(name):
            i = i.split(": ")
            if i[0]==(name):
                return i[1]

def read_list (filename):
    file = open (filename,"r",encoding='utf-8')
    strv = file.read()
    file.close()
    strv = strv.split("\n")
    return strv

def write_record(name, value, filename):
    file = open (filename,'r',encoding='utf-8')
    all = file.read()
    file.close()
    record = read_record(name, filename)
    os.remove(filename)
    if not (record == None):
        all = all.replace("\n"+name + ": " + record, "")
    file = open(filename,'w',encoding='utf-8')
    file.write(all + "\n" + name + ": " + value)
    file.close()