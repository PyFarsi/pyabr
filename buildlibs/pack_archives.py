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

import shutil, os, sys,glob, platform,py_compile,hashlib
from buildlibs import control

def compile (src,dest):
    py_compile.compile(src,dest)

## Build ##
def build(name):
    if not ("packs/"+name + "/code") and ("packs/"+name + "/data") and (
            "packs/"+name + "/control") and ("packs/"+name + "/control/manifest"):
        exit(0)

    shutil.make_archive("app/cache/archives/build/data", "zip",    "packs/"+name + "/data")
    shutil.make_archive("app/cache/archives/build/code", "zip",    "packs/"+name + "/code")
    shutil.make_archive("app/cache/archives/build/control", "zip", "packs/"+ name + "/control")
    shutil.make_archive(name, "zip", "app/cache/archives/build")
    os.rename (name+".zip","build-packs/"+name+".pa")
    clean()

def build_extra(name):
    if not ("packs-extra/"+name + "/code") and ("packs-extra/"+name + "/data") and (
            "packs-extra/"+name + "/control") and ("packs-extra/"+name + "/control/manifest"):
        exit(0)

    shutil.make_archive("app/cache/archives/build/data", "zip",    "packs-extra/"+name + "/data")
    shutil.make_archive("app/cache/archives/build/code", "zip",    "packs-extra/"+name + "/code")
    shutil.make_archive("app/cache/archives/build/control", "zip", "packs-extra/"+ name + "/control")
    shutil.make_archive(name, "zip", "app/cache/archives/build")
    os.rename (name+".zip","build-packs/"+name+".pa")
    clean()

def manifest(name):
    if not ("packs/"+name + "/code") and ("packs/"+name + "/data") and (
            "packs/"+name + "/control") and ("packs/"+name + "/control/manifest"):
        exit(0)

    f = open ('build-date.txt','r',encoding='utf-8')
    control.write_record('build',f.read(),f'packs/{name}/control/manifest')
    f.close()

    f = open ('mirror.txt','r',encoding='utf-8')
    control.write_record('mirror',f.read(),f'packs/{name}/control/manifest')
    f.close()
    shutil.copyfile('packs/'+name+'/control/manifest',f'packs/ir.pyabr.updates/data/{name}.manifest')

def manifest_extra(name):
    if not ("packs-extra/"+name + "/code") and ("packs-extra/"+name + "/data") and (
            "packsextra/"+name + "/control") and ("packs-extra/"+name + "/control/manifest"):
        exit(0)

    f = open ('build-date.txt','r',encoding='utf-8')
    control.write_record('build',f.read(),f'packs-extra/{name}/control/manifest')
    f.close()

    f = open ('mirror.txt','r',encoding='utf-8')
    control.write_record('mirror',f.read(),f'packs-extra/{name}/control/manifest')
    f.close()
    shutil.copyfile('packs-extra/'+name+'/control/manifest',f'packs/ir.pyabr.updates/data/{name}.manifest')

## Clean the cache ##
def clean():
    shutil.rmtree("app/cache")
    os.mkdir("app/cache")
    os.mkdir("app/cache/gets")
    os.mkdir("app/cache/archives")
    os.mkdir("app/cache/archives/code")
    os.mkdir("app/cache/archives/control")
    os.mkdir("app/cache/archives/data")
    os.mkdir("app/cache/archives/build")

## Unpack .pa archives ##

def unpack (name):
    shutil.unpack_archive("build-packs/"+name+".pa","app/cache/archives/build","zip")
    shutil.unpack_archive("app/cache/archives/build/data.zip","app/cache/archives/data","zip")
    shutil.unpack_archive("app/cache/archives/build/code.zip","app/cache/archives/code", "zip")
    shutil.unpack_archive("app/cache/archives/build/control.zip","app/cache/archives/control", "zip")

    name = control.read_record ("name","app/cache/archives/control/manifest")
    unpack = control.read_record ("unpack","app/cache/archives/control/manifest")

    ## Setting up ##

    if os.path.isfile ("app/cache/archives/control/manifest"): shutil.copyfile("app/cache/archives/control/manifest","stor/app/packages/"+name+".manifest")
    if os.path.isfile("app/cache/archives/control/list"): shutil.copyfile("app/cache/archives/control/list","stor/app/packages/" + name + ".list")
    if os.path.isfile("app/cache/archives/control/compile"): shutil.copyfile("app/cache/archives/control/compile","stor/app/packages/" + name + ".compile")
    if os.path.isfile("app/cache/archives/control/preremove.sa"): shutil.copyfile("app/cache/archives/control/preremove.sa",
                                                                             "stor/app/packages/" + name + ".preremove")
    if os.path.isfile("app/cache/archives/control/postremove.sa"): shutil.copyfile("app/cache/archives/control/postremove.sa",
                                                                             "stor/app/packages/" + name + ".postremove")
    if os.path.isfile("app/cache/archives/control/preinstall.sa"): shutil.copyfile("app/cache/archives/control/preinstall.sa",
                                                                             "stor/app/packages/" + name + ".preinstall")
    if os.path.isfile("app/cache/archives/control/postinstall.sa"): shutil.copyfile("app/cache/archives/control/postinstall.sa",
                                                                             "stor/app/packages/" + name + ".postinstall.sa")

    ## Compile codes ##
    if os.path.isfile ("app/cache/archives/control/compile"):
        listcodes = control.read_list("app/cache/archives/control/compile")
        for i in listcodes:
            i = i.split(":")

            compile('app/cache/archives/code/'+i[0], 'app/cache/archives/data/'+i[1])


    ## Archive data again ##
    shutil.make_archive("app/cache/archives/build/data","zip","app/cache/archives/data")

    ## Unpack data again ##
    shutil.unpack_archive("app/cache/archives/build/data.zip","stor/"+unpack,"zip")

def install ():
    list = os.listdir('packs')
    for i in list:
        if os.path.isdir('packs/'+i):
            build(i)
            unpack(i)

    try:
        list = os.listdir('packs-extra')
        for i in list:
            if os.path.isdir('packs-extra/' + i):
                build_extra(i)
                unpack(i)
    except:
        pass

def genisoinstall ():
    list = os.listdir('packs')
    for i in list:
        if os.path.isdir('packs/'+i):
            build(i)
            unpack(i)

def linuxinstall ():
    list = [
        'ir.pyabr',
        'ir.pyabr.baad',
        'ir.pyabr.barf',
        'ir.pyabr.barge',
        'ir.pyabr.calculator',
        'ir.pyabr.calendar',
        'ir.pyabr.chat',
        'ir.pyabr.clock',
        'ir.pyabr.controls',
        'ir.pyabr.files',
        'ir.pyabr.help',
        'ir.pyabr.nama',
        'ir.pyabr.paye',
        'ir.pyabr.pyket',
        'ir.pyabr.pysys',
        'ir.pyabr.runapp',
        'ir.pyabr.sample',
        'ir.pyabr.sysinfo',
        'ir.pyabr.updates',
    ]
    for i in list:
        if os.path.isdir('packs/'+i):
            build(i)
            unpack(i)

def inst (pack):
    build(pack)
    unpack(pack)

def buildpacks ():
    list = os.listdir('packs')
    list.remove('ir.pyabr.updates')
    for i in list:
        if os.path.isdir('packs/'+i):
            manifest(i)
            build(i)

    try:
        list = os.listdir('packs-extra')
        for i in list:
            if os.path.isdir('packs-extra/' + i):
                manifest_extra(i)
                build_extra(i)
    except:
        pass

    manifest('ir.pyabr.updates')
    build('ir.pyabr.updates')