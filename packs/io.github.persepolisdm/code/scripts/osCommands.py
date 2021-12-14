# -*- coding: utf-8 -*-

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.


from persepolis.constants import OS
import subprocess
import platform
import shutil
import os

os_type = platform.system()
home_address = os.path.expanduser("~")


# this method finds file manager in linux
def findFileManager():
    pipe = subprocess.check_output(['xdg-mime',
                                    'query',
                                    'default',
                                    'inode/directory'])
    file_manager = pipe.decode('utf-8').strip().lower()

    return file_manager


def touch(file_path):
    if not(os.path.isfile(file_path)):
        f = open(file_path, 'w')
        f.close()

# xdgOpen opens files or folders
def xdgOpen(file_path, f_type='file', path='file'):

    # we have a file path and we want to open it's directory.
    # highlit(select) file in file manager after opening.
    # it's help to find file easier :)
    if f_type == 'folder' and path == 'file':
        highlight = True
    else:
        highlight = False

    # for linux and bsd
    if os_type in OS.UNIX_LIKE:

        file_manager = findFileManager()
        # check default file manager.
        # some file managers wouldn't support highlighting.
        if highlight:

            # dolphin is kde plasma's file manager
            if 'dolphin' in file_manager:

                subprocess.Popen(['dolphin',
                                  '--select', file_path],
                                 stderr=subprocess.PIPE,
                                 stdout=subprocess.PIPE,
                                 stdin=subprocess.PIPE,
                                 shell=False)

            # dde-file-manager is deepin's file manager
            elif 'dde-file-manager' in file_manager:

                subprocess.Popen(['dde-file-manager',
                                  '--show-item', file_path],
                                 stderr=subprocess.PIPE,
                                 stdout=subprocess.PIPE,
                                 stdin=subprocess.PIPE,
                                 shell=False)

            # if file manager is nautilus or nemo or pantheon-file-manager
            elif file_manager in ['org.gnome.nautilus.desktop', 'nemo.desktop', 'io.elementary.files.desktop']:

                # nautilus is gnome's file manager.
                if 'nautilus' in file_manager:
                    file_manager = 'nautilus'

                # pantheon-files is pantheon's file manager(elementary OS).
                elif 'elementary' in file_manager:
                    file_manager = 'io.elementary.files'

                # nemo is cinnamon's file manager.
                elif 'nemo' in file_manager:
                    file_manager = 'nemo'

                subprocess.Popen([file_manager,
                                  file_path],
                                 stderr=subprocess.PIPE,
                                 stdout=subprocess.PIPE,
                                 stdin=subprocess.PIPE,
                                 shell=False)

            else:
                # find folder path
                file_name = os.path.basename(str(file_path))

                file_path_split = file_path.split(file_name)

                del file_path_split[-1]

                folder_path = file_name.join(file_path_split)

                subprocess.Popen(['xdg-open', folder_path],
                                 stderr=subprocess.PIPE,
                                 stdout=subprocess.PIPE,
                                 stdin=subprocess.PIPE,
                                 shell=False)

        else:

            subprocess.Popen(['xdg-open', file_path],
                             stderr=subprocess.PIPE,
                             stdout=subprocess.PIPE,
                             stdin=subprocess.PIPE,
                             shell=False)

    # for Mac OS X
    elif os_type == OS.OSX:
        if highlight:

            subprocess.Popen(['open', '-R', file_path],
                             stderr=subprocess.PIPE,
                             stdout=subprocess.PIPE,
                             stdin=subprocess.PIPE,
                             shell=False)

        else:

            subprocess.Popen(['open', file_path],
                             stderr=subprocess.PIPE,
                             stdout=subprocess.PIPE,
                             stdin=subprocess.PIPE,
                             shell=False)

    # for MS Windows
    elif os_type == OS.WINDOWS:
        CREATE_NO_WINDOW = 0x08000000

        if highlight:
            subprocess.Popen(['explorer.exe', '/select,',  file_path],
                             stderr=subprocess.PIPE,
                             stdout=subprocess.PIPE,
                             stdin=subprocess.PIPE,
                             shell=False,
                             creationflags=CREATE_NO_WINDOW)

        else:

            subprocess.Popen(['cmd', '/C', 'start', file_path,  file_path],
                             stderr=subprocess.PIPE,
                             stdout=subprocess.PIPE,
                             stdin=subprocess.PIPE,
                             shell=False,
                             creationflags=CREATE_NO_WINDOW)

# remove file with path of file_path
def remove(file_path): 
    if os.path.isfile(file_path):
        try:
            # function returns  ok, if operation was successful
            os.remove(file_path)
            return 'ok'

        except:
            # function returns this, if operation was not successful
            return 'cant'

    else:
        # function returns this , if file is not existed
        return 'no'

# removeDir removes folder : folder_path
def removeDir(folder_path):

    # check folder_path existence
    if os.path.isdir(folder_path):
        try:
            # remove folder
            shutil.rmtree(folder_path)
            return 'ok'

        except:
            # return 'cant' if removing was not successful
            return 'cant'
    else:
        # return 'no' if file didn't existed
        return 'no'

# make directory 
def makeDirs(folder_path, hidden=False):

    if hidden:

        # create hidden attribute directory.
        if os_type == OS.WINDOWS:

            os.makedirs(folder_path, exist_ok=True)

            # in MS Windows "attrib +h" command hidden directory.
            CREATE_NO_WINDOW = 0x08000000
            subprocess.Popen(['attrib', '+h', folder_path],
                             stderr=subprocess.PIPE,
                             stdout=subprocess.PIPE,
                             stdin=subprocess.PIPE,
                             shell=False,
                             creationflags=CREATE_NO_WINDOW)
        else:

            # In linux and bsd a dot character must be added in the start of the directory's name
            dir_name = os.path.basename(folder_path)
            dir_name = '.' + dir_name 
            folder_path = os.path.join(os.path.dirname(folder_path), dir_name)

            os.makedirs(folder_path, exist_ok=True)

    else:
        os.makedirs(folder_path, exist_ok=True)

    return folder_path
    
# this function returns mount point
def findMountPoint(path):

    while not os.path.ismount(path):
        path = os.path.dirname(path)

    return path

# this function creates temporary download folder in mount point of given path
def makeTempDownloadDir(path):

    # if path and home_address are in the same partition,
    # create temp folder in default settings address.
    if os.lstat(path).st_dev == os.lstat(home_address):

        if os_type != OS.WINDOWS:
            download_path_temp = os.path.join(home_address, '.persepolis')
        else:
            download_path_temp = os.path.join(
                home_address, 'AppData', 'Local', 'persepolis')

        # create directory
        download_path_temp = makeDirs(download_path_temp)

    else:
        # Find mount point and create temp folder there!
        mount_point = findMountPoint(path)
        download_path_temp = os.path.join(mount_point, 'persepolis')

        # Create folder and give new temp address from makeDirs function.
        # Please checkout osCommands.py for more information.
        download_path_temp = makeDirs(download_path_temp, hidden=True)


    return download_path_temp

# move downloaded file to another destination.
def moveFile(old_file_path, new_path, new_path_type='folder'):

    # new_path_type can be file or folder
    # if it's folder so we have folder path
    # else we have new file path that includes file name
    if os.path.isfile(old_file_path):

        if new_path_type == 'folder':

            # check availability of directory
            check_path = os.path.isdir(new_path)

        else:

            check_path = True

        if check_path:

            try:
                # move file to new_path
                shutil.move(old_file_path, new_path)
                return True

            except:

                return False
        else:

            return False

    else:

        return False
