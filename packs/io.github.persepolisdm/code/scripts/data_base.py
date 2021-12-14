# -*- coding: utf-8 -*-
"""
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

from persepolis.scripts.useful_tools import determineConfigFolder
from persepolis.scripts import logger
from time import sleep
import traceback
import sqlite3
import random
import ast
import os

# download manager config folder .
config_folder = determineConfigFolder()

# persepolis tmp folder path
persepolis_tmp = os.path.join(config_folder, 'persepolis_tmp')


# This class manages TempDB
# TempDB contains gid of active downloads in every session.
class TempDB():
    def __init__(self):
        # temp_db saves in RAM
        # temp_db_connection

        self.temp_db_connection = sqlite3.connect(':memory:', check_same_thread=False)

        # temp_db_cursor
        self.temp_db_cursor = self.temp_db_connection.cursor()

        # create a lock for data base
        self.lock = False

    # this method locks data base.
    # this is pervent accessing data base simultaneously.
    def lockCursor(self):
        while self.lock:
            rand_float = random.uniform(0, 0.5)
            sleep(rand_float)

        self.lock = True

    # temp_db_table contains gid of active downloads.

    def createTables(self):
        # lock data base
        self.lockCursor()
        self.temp_db_cursor.execute("""CREATE TABLE IF NOT EXISTS single_db_table(
                                                                                ID INTEGER,
                                                                                gid TEXT PRIMARY KEY,
                                                                                status TEXT,
                                                                                shutdown TEXT
                                                                                )""")

        self.temp_db_cursor.execute("""CREATE TABLE IF NOT EXISTS queue_db_table(
                                                                                ID INTEGER,
                                                                                category TEXT PRIMARY KEY,
                                                                                shutdown TEXT
                                                                                )""")

        self.temp_db_connection.commit()
        self.lock = False

    # insert new item in single_db_table
    def insertInSingleTable(self, gid):
        # lock data base
        self.lockCursor()
        self.temp_db_cursor.execute("""INSERT INTO single_db_table VALUES(
                                                                NULL,
                                                                '{}',
                                                                'active',
                                                                NULL)""".format(gid))

        self.temp_db_connection.commit()
        self.lock = False

    # insert new item in queue_db_table

    def insertInQueueTable(self, category):
        # lock data base
        self.lockCursor()
        self.temp_db_cursor.execute("""INSERT INTO queue_db_table VALUES(
                                                                NULL,
                                                                '{}',
                                                                NULL)""".format(category))

        self.temp_db_connection.commit()
        self.lock = False

    # this method updates single_db_table

    def updateSingleTable(self, dict):
        # lock data base
        self.lockCursor()
        keys_list = ['gid',
                     'shutdown',
                     'status'
                     ]

        for key in keys_list:
            # if a key is missed in dict,
            # then add this key to the dict and assign None value for the key.
            if key not in dict.keys():
                dict[key] = None

        # update data base if value for the keys is not None
        self.temp_db_cursor.execute("""UPDATE single_db_table SET shutdown = coalesce(:shutdown, shutdown),
                                                                status = coalesce(:status, status)
                                                                WHERE gid = :gid""", dict)

        self.temp_db_connection.commit()

        self.lock = False

    # this method updates queue_db_table
    def updateQueueTable(self, dict):
        # lock data base
        self.lockCursor()
        keys_list = ['category',
                     'shutdown']

        for key in keys_list:
            # if a key is missed in dict,
            # then add this key to the dict and assign None value for the key.
            if key not in dict.keys():
                dict[key] = None

        # update data base if value for the keys is not None
        self.temp_db_cursor.execute("""UPDATE queue_db_table SET shutdown = coalesce(:shutdown, shutdown)
                                                                WHERE category = :category""", dict)

        self.temp_db_connection.commit()

        self.lock = False

    # this method returns gid of active downloads
    def returnActiveGids(self):
        # lock data base
        self.lockCursor()

        self.temp_db_cursor.execute("""SELECT gid FROM single_db_table WHERE status = 'active'""")

        list = self.temp_db_cursor.fetchall()

        self.lock = False
        gid_list = []

        for tuple in list:
            gid = tuple[0]
            gid_list.append(gid)

        return gid_list

    # this method returns shutdown value for specific gid
    def returnGid(self, gid):
        # lock data base
        self.lockCursor()
        self.temp_db_cursor.execute("""SELECT shutdown, status FROM single_db_table WHERE gid = '{}'""".format(gid))

        list = self.temp_db_cursor.fetchall()

        self.lock = False

        tuple = list[0]

        dict = {'shutdown': str(tuple[0]),
                'status': tuple[1]}

        return dict

    # This method returns values of columns for specific category

    def returnCategory(self, category):
        # lock data base
        self.lockCursor()
        self.temp_db_cursor.execute("""SELECT shutdown FROM queue_db_table WHERE category = '{}'""".format(category))

        list = self.temp_db_cursor.fetchall()

        self.lock = False

        tuple = list[0]

        dict = {'shutdown': tuple[0]}

        return dict

    def resetDataBase(self):
        # lock data base
        self.lockCursor()

        # delete all items
        self.temp_db_cursor.execute("""DELETE FROM single_db_table""")
        self.temp_db_cursor.execute("""DELETE FROM queue_db_table""")

        # release lock
        self.lock = False

    # close connections

    def closeConnections(self):
        # lock data base
        self.lockCursor()
        self.temp_db_cursor.close()
        self.temp_db_connection.close()
        self.lock = False


# plugins.db is store links, when browser plugins are send new links.
# This class is managing plugin.db
class PluginsDB():
    def __init__(self):
        # plugins.db file path
        plugins_db_path = os.path.join(persepolis_tmp, 'plugins.db')

        # plugins_db_connection
        self.plugins_db_connection = sqlite3.connect(plugins_db_path, check_same_thread=False)

        # plugins_db_cursor
        self.plugins_db_cursor = self.plugins_db_connection.cursor()

        # create a lock for data base
        self.lock = False

    # this method locks data base.
    # this is pervent accessing data base simultaneously.
    def lockCursor(self):
        while self.lock:
            rand_float = random.uniform(0, 0.5)
            sleep(rand_float)

        self.lock = True

    # plugins_db_table contains links that sends by browser plugins.

    def createTables(self):
        # lock data base
        self.lockCursor()

        self.plugins_db_cursor.execute("""CREATE TABLE IF NOT EXISTS plugins_db_table(
                                                                                ID INTEGER PRIMARY KEY,
                                                                                link TEXT,
                                                                                referer TEXT,
                                                                                load_cookies TEXT,
                                                                                user_agent TEXT,
                                                                                header TEXT,
                                                                                out TEXT,
                                                                                status TEXT
                                                                                )""")
        self.plugins_db_connection.commit()

        # release lock
        self.lock = False

    # insert new items in plugins_db_table
    def insertInPluginsTable(self, list):
        # lock data base
        self.lockCursor()

        for dict in list:
            self.plugins_db_cursor.execute("""INSERT INTO plugins_db_table VALUES(
                                                                        NULL,
                                                                        :link,
                                                                        :referer,
                                                                        :load_cookies,
                                                                        :user_agent,
                                                                        :header,
                                                                        :out,
                                                                        'new'
                                                                            )""", dict)

        self.plugins_db_connection.commit()
        # release lock
        self.lock = False

# this method returns all new links in plugins_db_table
    def returnNewLinks(self):
        # lock data base
        self.lockCursor()

        self.plugins_db_cursor.execute("""SELECT link, referer, load_cookies, user_agent, header, out
                                            FROM plugins_db_table
                                            WHERE status = 'new'""")

        list = self.plugins_db_cursor.fetchall()

        # chang all rows status to 'old'
        self.plugins_db_cursor.execute("""UPDATE plugins_db_table SET status = 'old'
                                            WHERE status = 'new'""")

        # commit changes
        self.plugins_db_connection.commit()

        # release lock
        self.lock = False

        # create new_list
        new_list = []

        # put the information in tuples in dictionary format and add it to new_list
        for tuple in list:
            dict = {'link': tuple[0],
                    'referer': tuple[1],
                    'load_cookies': tuple[2],
                    'user_agent': tuple[3],
                    'header': tuple[4],
                    'out': tuple[5]
                    }

            new_list.append(dict)

        # return results in list format!
        # every member of this list is a dictionary.
        # every dictionary contains download information
        return new_list

    # delete old links from data base
    def deleteOldLinks(self):
        # lock data base
        self.lockCursor()

        self.plugins_db_cursor.execute("""DELETE FROM plugins_db_table WHERE status = 'old'""")
        # commit changes
        self.plugins_db_connection.commit()

        # release lock
        self.lock = False

    # close connections
    def closeConnections(self):
        # lock data base
        self.lockCursor()

        self.plugins_db_cursor.close()
        self.plugins_db_connection.close()

        # release lock
        self.lock = False


# persepolis main data base contains downloads information
# This class is managing persepolis.db
class PersepolisDB():
    def __init__(self):
        # persepolis.db file path
        persepolis_db_path = os.path.join(config_folder, 'persepolis.db')

        # persepolis_db_connection
        self.persepolis_db_connection = sqlite3.connect(persepolis_db_path, check_same_thread=False)

        # turn FOREIGN KEY Support on!
        self.persepolis_db_connection.execute('pragma foreign_keys=ON')

        # persepolis_db_cursor
        self.persepolis_db_cursor = self.persepolis_db_connection.cursor()

        # Create a lock for data base
        self.lock = False

    # this method locks data base.
    # this is pervent accessing data base simultaneously.
    def lockCursor(self):

        while self.lock:
            rand_float = random.uniform(0, 0.5)
            sleep(rand_float)

        self.lock = True

    # queues_list contains name of categories and category settings
    def createTables(self):

        # lock data base
        self.lockCursor()
        # Create category_db_table and add 'All Downloads' and 'Single Downloads' to it
        self.persepolis_db_cursor.execute("""CREATE TABLE IF NOT EXISTS category_db_table(
                                                                category TEXT PRIMARY KEY,
                                                                start_time_enable TEXT,
                                                                start_time TEXT,
                                                                end_time_enable TEXT,
                                                                end_time TEXT,
                                                                reverse TEXT,
                                                                limit_enable TEXT,
                                                                limit_value TEXT,
                                                                after_download TEXT,
                                                                gid_list TEXT
                                                                            )""")

        # download table contains download table download items information
        self.persepolis_db_cursor.execute("""CREATE TABLE IF NOT EXISTS download_db_table(
                                                                                    file_name TEXT,
                                                                                    status TEXT,
                                                                                    size TEXT,
                                                                                    downloaded_size TEXT,
                                                                                    percent TEXT,
                                                                                    connections TEXT,
                                                                                    rate TEXT,
                                                                                    estimate_time_left TEXT,
                                                                                    gid TEXT PRIMARY KEY,
                                                                                    link TEXT,
                                                                                    first_try_date TEXT,
                                                                                    last_try_date TEXT,
                                                                                    category TEXT,
                                                                                    FOREIGN KEY(category) REFERENCES category_db_table(category)
                                                                                    ON UPDATE CASCADE
                                                                                    ON DELETE CASCADE
                                                                                         )""")

        # addlink_db_table contains addlink window download information
        self.persepolis_db_cursor.execute("""CREATE TABLE IF NOT EXISTS addlink_db_table(
                                                                                ID INTEGER PRIMARY KEY,
                                                                                gid TEXT,
                                                                                out TEXT,
                                                                                start_time TEXT,
                                                                                end_time TEXT,
                                                                                link TEXT,
                                                                                ip TEXT,
                                                                                port TEXT,
                                                                                proxy_user TEXT,
                                                                                proxy_passwd TEXT,
                                                                                download_user TEXT,
                                                                                download_passwd TEXT,
                                                                                connections TEXT,
                                                                                limit_value TEXT,
                                                                                download_path TEXT,
                                                                                referer TEXT,
                                                                                load_cookies TEXT,
                                                                                user_agent TEXT,
                                                                                header TEXT,
                                                                                after_download TEXT,
                                                                                FOREIGN KEY(gid) REFERENCES download_db_table(gid) 
                                                                                ON UPDATE CASCADE 
                                                                                ON DELETE CASCADE 
                                                                                    )""")

        # video_finder_db_table contains addlink window download information
        self.persepolis_db_cursor.execute("""CREATE TABLE IF NOT EXISTS video_finder_db_table(
                                                                                ID INTEGER PRIMARY KEY,
                                                                                video_gid TEXT,
                                                                                audio_gid TEXT,
                                                                                video_completed TEXT,
                                                                                audio_completed TEXT,
                                                                                muxing_status TEXT,
                                                                                checking TEXT,
                                                                                download_path TEXT,
                                                                                FOREIGN KEY(video_gid) REFERENCES download_db_table(gid)
                                                                                ON DELETE CASCADE,
                                                                                FOREIGN KEY(audio_gid) REFERENCES download_db_table(gid)
                                                                                ON DELETE CASCADE
                                                                                    )""")

        self.persepolis_db_connection.commit()

        # job is done! open the lock
        self.lock = False

        # add 'All Downloads' and 'Single Downloads' to the category_db_table if they wasn't added.
        answer = self.searchCategoryInCategoryTable('All Downloads')

        if not(answer):
            all_downloads_dict = {'category': 'All Downloads',
                                  'start_time_enable': 'no',
                                  'start_time': '0:0',
                                  'end_time_enable': 'no',
                                  'end_time': '0:0',
                                  'reverse': 'no',
                                  'limit_enable': 'no',
                                  'limit_value': '0K',
                                  'after_download': 'no',
                                  'gid_list': '[]'
                                  }

            single_downloads_dict = {'category': 'Single Downloads',
                                     'start_time_enable': 'no',
                                     'start_time': '0:0',
                                     'end_time_enable': 'no',
                                     'end_time': '0:0',
                                     'reverse': 'no',
                                     'limit_enable': 'no',
                                     'limit_value': '0K',
                                     'after_download': 'no',
                                     'gid_list': '[]'
                                     }

            self.insertInCategoryTable(all_downloads_dict)
            self.insertInCategoryTable(single_downloads_dict)

        # add default queue with the name 'Scheduled Downloads'
        answer = self.searchCategoryInCategoryTable('Scheduled Downloads')
        if not(answer):
            scheduled_downloads_dict = {'category': 'Scheduled Downloads',
                                        'start_time_enable': 'no',
                                        'start_time': '0:0',
                                        'end_time_enable': 'no',
                                        'end_time': '0:0',
                                        'reverse': 'no',
                                        'limit_enable': 'no',
                                        'limit_value': '0K',
                                        'after_download': 'no',
                                        'gid_list': '[]'
                                        }
            self.insertInCategoryTable(scheduled_downloads_dict)

    # insert new category in category_db_table
    def insertInCategoryTable(self, dict):
        # lock data base
        self.lockCursor()

        self.persepolis_db_cursor.execute("""INSERT INTO category_db_table VALUES(
                                                                            :category,
                                                                            :start_time_enable,
                                                                            :start_time,
                                                                            :end_time_enable,
                                                                            :end_time,
                                                                            :reverse,
                                                                            :limit_enable,
                                                                            :limit_value,
                                                                            :after_download,
                                                                            :gid_list
                                                                            )""", dict)
        self.persepolis_db_connection.commit()

        # job is done! open the lock
        self.lock = False

    # insert in to download_db_table in persepolis.db

    def insertInDownloadTable(self, list):
        # lock data base
        self.lockCursor()

        for dict in list:
            self.persepolis_db_cursor.execute("""INSERT INTO download_db_table VALUES(
                                                                            :file_name,
                                                                            :status,
                                                                            :size,
                                                                            :downloaded_size,
                                                                            :percent,
                                                                            :connections,
                                                                            :rate,
                                                                            :estimate_time_left,
                                                                            :gid,
                                                                            :link,
                                                                            :first_try_date,
                                                                            :last_try_date,
                                                                            :category
                                                                            )""", dict)

        # commit changes
        self.persepolis_db_connection.commit()

        # job is done! open the lock
        self.lock = False

        if len(list) != 0:
            # item must be inserted to gid_list of 'All Downloads' and gid_list of category
            # find download category and gid
            category = dict['category']

            # get category_dict from data base
            category_dict = self.searchCategoryInCategoryTable(category)

            # get all_downloads_dict from data base
            all_downloads_dict = self.searchCategoryInCategoryTable('All Downloads')

            # get gid_list
            category_gid_list = category_dict['gid_list']

            all_downloads_gid_list = all_downloads_dict['gid_list']

            for dict in list:
                gid = dict['gid']

                # add gid of item to gid_list
                category_gid_list.append(gid)
                all_downloads_gid_list.append(gid)

            # update category_db_table
            self.updateCategoryTable([all_downloads_dict])
            self.updateCategoryTable([category_dict])

    # insert in addlink table in persepolis.db

    def insertInAddLinkTable(self, list):
        # lock data base
        self.lockCursor()

        for dict in list:
            # first column and after download column is NULL
            self.persepolis_db_cursor.execute("""INSERT INTO addlink_db_table VALUES(NULL,
                                                                                :gid,
                                                                                :out,
                                                                                :start_time,
                                                                                :end_time,
                                                                                :link,
                                                                                :ip,
                                                                                :port,
                                                                                :proxy_user,
                                                                                :proxy_passwd,
                                                                                :download_user,
                                                                                :download_passwd,
                                                                                :connections,
                                                                                :limit_value,
                                                                                :download_path,
                                                                                :referer,
                                                                                :load_cookies,
                                                                                :user_agent,
                                                                                :header,
                                                                                NULL
                                                                                )""", dict)
        self.persepolis_db_connection.commit()

        # job is done! open the lock
        self.lock = False

    def insertInVideoFinderTable(self, list):
        # lock data base
        self.lockCursor()

        for dictionary in list:
            # first column is NULL
            self.persepolis_db_cursor.execute("""INSERT INTO video_finder_db_table VALUES(NULL,
                                                                                :video_gid,
                                                                                :audio_gid,
                                                                                :video_completed,
                                                                                :audio_completed,
                                                                                :muxing_status,
                                                                                :checking,
                                                                                :download_path
                                                                                )""", dictionary)
        self.persepolis_db_connection.commit()

        # job is done! open the lock
        self.lock = False

    def searchGidInVideoFinderTable(self, gid):
        # lock data base
        self.lockCursor()

        self.persepolis_db_cursor.execute(
            """SELECT * FROM video_finder_db_table WHERE audio_gid = '{}' OR video_gid = '{}'""".format(str(gid), str(gid)))
        result_list = self.persepolis_db_cursor.fetchall()

        # job is done
        self.lock = False

        if result_list:
            tuple = result_list[0]
        else:
            return None

        dictionary = {'video_gid': tuple[1],
                      'audio_gid': tuple[2],
                      'video_completed': tuple[3],
                      'audio_completed': tuple[4],
                      'muxing_status': tuple[5],
                      'checking': tuple[6],
                      'download_path': tuple[7]}

        # return the results
        return dictionary

    # return download information in download_db_table with special gid.
    def searchGidInDownloadTable(self, gid):
        # lock data base
        self.lockCursor()

        self.persepolis_db_cursor.execute("""SELECT * FROM download_db_table WHERE gid = '{}'""".format(str(gid)))
        list = self.persepolis_db_cursor.fetchall()

        # job is done! open the lock
        self.lock = False

        if list:
            tuple = list[0]
        else:
            return None

        dict = {'file_name': tuple[0],
                'status': tuple[1],
                'size': tuple[2],
                'downloaded_size': tuple[3],
                'percent': tuple[4],
                'connections': tuple[5],
                'rate': tuple[6],
                'estimate_time_left': tuple[7],
                'gid': tuple[8],
                'link': tuple[9],
                'first_try_date': tuple[10],
                'last_try_date': tuple[11],
                'category': tuple[12]
                }

        # return results
        return dict

    # return all items in download_db_table
    # '*' for category, cause that method returns all items.
    def returnItemsInDownloadTable(self, category=None):
        # lock data base
        self.lockCursor()

        if category:
            self.persepolis_db_cursor.execute(
                """SELECT * FROM download_db_table WHERE category = '{}'""".format(category))
        else:
            self.persepolis_db_cursor.execute("""SELECT * FROM download_db_table""")

        rows = self.persepolis_db_cursor.fetchall()

        # job is done! open the lock
        self.lock = False

        downloads_dict = {}
        for tuple in rows:
            # change format of tuple to dictionary
            dict = {'file_name': tuple[0],
                    'status': tuple[1],
                    'size': tuple[2],
                    'downloaded_size': tuple[3],
                    'percent': tuple[4],
                    'connections': tuple[5],
                    'rate': tuple[6],
                    'estimate_time_left': tuple[7],
                    'gid': tuple[8],
                    'link': tuple[9],
                    'first_try_date': tuple[10],
                    'last_try_date': tuple[11],
                    'category': tuple[12]
                    }

            # add dict to the downloads_dict
            # gid is key and dict is value
            downloads_dict[tuple[8]] = dict

        return downloads_dict

    # this method checks existence of a link in addlink_db_table

    def searchLinkInAddLinkTable(self, link):
        # lock data base
        self.lockCursor()

        self.persepolis_db_cursor.execute("""SELECT * FROM addlink_db_table WHERE link = (?)""", (link,))
        list = self.persepolis_db_cursor.fetchall()

        # job is done! open the lock
        self.lock = False

        if list:
            return True
        else:
            return False

    # return download information in addlink_db_table with special gid.

    def searchGidInAddLinkTable(self, gid):
        # lock data base
        self.lockCursor()

        self.persepolis_db_cursor.execute("""SELECT * FROM addlink_db_table WHERE gid = '{}'""".format(str(gid)))
        list = self.persepolis_db_cursor.fetchall()

        # job is done! open the lock
        self.lock = False

        if list:
            tuple = list[0]
        else:
            return None

        dict = {'gid': tuple[1],
                'out': tuple[2],
                'start_time': tuple[3],
                'end_time': tuple[4],
                'link': tuple[5],
                'ip': tuple[6],
                'port': tuple[7],
                'proxy_user': tuple[8],
                'proxy_passwd': tuple[9],
                'download_user': tuple[10],
                'download_passwd': tuple[11],
                'connections': tuple[12],
                'limit_value': tuple[13],
                'download_path': tuple[14],
                'referer': tuple[15],
                'load_cookies': tuple[16],
                'user_agent': tuple[17],
                'header': tuple[18],
                'after_download': tuple[19]
                }

        return dict

    # return items in addlink_db_table
    # '*' for category, cause that method returns all items.

    def returnItemsInAddLinkTable(self, category=None):
        # lock data base
        self.lockCursor()

        if category:
            self.persepolis_db_cursor.execute(
                """SELECT * FROM addlink_db_table WHERE category = '{}'""".format(category))
        else:
            self.persepolis_db_cursor.execute("""SELECT * FROM addlink_db_table""")

        rows = self.persepolis_db_cursor.fetchall()

        # job is done! open the lock
        self.lock = False

        addlink_dict = {}
        for tuple in rows:
            # change format of tuple to dictionary
            dict = {'gid': tuple[1],
                    'out': tuple[2],
                    'start_time': tuple[3],
                    'end_time': tuple[4],
                    'link': tuple[5],
                    'ip': tuple[6],
                    'port': tuple[7],
                    'proxy_user': tuple[8],
                    'proxy_passwd': tuple[9],
                    'download_user': tuple[10],
                    'download_passwd': tuple[11],
                    'connections': tuple[12],
                    'limit_value': tuple[13],
                    'download_path': tuple[13],
                    'referer': tuple[14],
                    'load_cookies': tuple[15],
                    'user_agent': tuple[16],
                    'header': tuple[17],
                    'after_download': tuple[18]
                    }

            # add dict to the addlink_dict
            # gid as key and dict as value
            addlink_dict[tuple[1]] = dict

        return addlink_dict


# this method updates download_db_table

    def updateDownloadTable(self, list):
        # lock data base
        self.lockCursor()

        keys_list = ['file_name',
                     'status',
                     'size',
                     'downloaded_size',
                     'percent',
                     'connections',
                     'rate',
                     'estimate_time_left',
                     'gid',
                     'link',
                     'first_try_date',
                     'last_try_date',
                     'category'
                     ]

        for dict in list:
            for key in keys_list:
                # if a key is missed in dict,
                # then add this key to the dict and assign None value for the key.
                if key not in dict.keys():
                    dict[key] = None

            # update data base if value for the keys is not None
            self.persepolis_db_cursor.execute("""UPDATE download_db_table SET   file_name = coalesce(:file_name, file_name),
                                                                                    status = coalesce(:status, status),
                                                                                    size = coalesce(:size, size),
                                                                                    downloaded_size = coalesce(:downloaded_size, downloaded_size),
                                                                                    percent = coalesce(:percent, percent),
                                                                                    connections = coalesce(:connections, connections),
                                                                                    rate = coalesce(:rate, rate),
                                                                                    estimate_time_left = coalesce(:estimate_time_left, estimate_time_left),
                                                                                    link = coalesce(:link, link),
                                                                                    first_try_date = coalesce(:first_try_date, first_try_date),
                                                                                    last_try_date = coalesce(:last_try_date, last_try_date),
                                                                                    category = coalesce(:category, category)
                                                                                    WHERE gid = :gid""", dict)

        # commit the changes
        self.persepolis_db_connection.commit()

        # job is done! open the lock
        self.lock = False


# this method updates category_db_table

    def updateCategoryTable(self, list):
        # lock data base
        self.lockCursor()

        keys_list = ['category',
                     'start_time_enable',
                     'start_time',
                     'end_time_enable',
                     'end_time',
                     'reverse',
                     'limit_enable',
                     'limit_value',
                     'after_download',
                     'gid_list']

        for dict in list:

            # format of gid_list is list and must be converted to string for sqlite3
            if 'gid_list' in dict.keys():
                dict['gid_list'] = str(dict['gid_list'])

            for key in keys_list:
                # if a key is missed in dict,
                # then add this key to the dict and assign None value for the key.
                if key not in dict.keys():
                    dict[key] = None

            # update data base if value for the keys is not None
            self.persepolis_db_cursor.execute("""UPDATE category_db_table SET   start_time_enable = coalesce(:start_time_enable, start_time_enable),
                                                                                    start_time = coalesce(:start_time, start_time),
                                                                                    end_time_enable = coalesce(:end_time_enable, end_time_enable),
                                                                                    end_time = coalesce(:end_time, end_time),
                                                                                    reverse = coalesce(:reverse, reverse),
                                                                                    limit_enable = coalesce(:limit_enable, limit_enable),
                                                                                    limit_value = coalesce(:limit_value, limit_value),
                                                                                    after_download = coalesce(:after_download, after_download),
                                                                                    gid_list = coalesce(:gid_list, gid_list)
                                                                                    WHERE category = :category""", dict)

        # commit changes
        self.persepolis_db_connection.commit()

        # job is done! open the lock
        self.lock = False


# this method updates addlink_db_table

    def updateAddLinkTable(self, list):
        # lock data base
        self.lockCursor()

        keys_list = ['gid',
                     'out',
                     'start_time',
                     'end_time',
                     'link',
                     'ip',
                     'port',
                     'proxy_user',
                     'proxy_passwd',
                     'download_user',
                     'download_passwd',
                     'connections',
                     'limit_value',
                     'download_path',
                     'referer',
                     'load_cookies',
                     'user_agent',
                     'header',
                     'after_download']

        for dict in list:
            for key in keys_list:
                # if a key is missed in dict,
                # then add this key to the dict and assign None value for the key.
                if key not in dict.keys():
                    dict[key] = None

            # update data base if value for the keys is not None
            self.persepolis_db_cursor.execute("""UPDATE addlink_db_table SET out = coalesce(:out, out),
                                                                                start_time = coalesce(:start_time, start_time),
                                                                                end_time = coalesce(:end_time, end_time),
                                                                                link = coalesce(:link, link),
                                                                                ip = coalesce(:ip, ip),
                                                                                port = coalesce(:port, port),
                                                                                proxy_user = coalesce(:proxy_user, proxy_user),
                                                                                proxy_passwd = coalesce(:proxy_passwd, proxy_passwd),
                                                                                download_user = coalesce(:download_user, download_user),
                                                                                download_passwd = coalesce(:download_passwd, download_passwd),
                                                                                connections = coalesce(:connections, connections),
                                                                                limit_value = coalesce(:limit_value, limit_value),
                                                                                download_path = coalesce(:download_path, download_path),
                                                                                referer = coalesce(:referer, referer),
                                                                                load_cookies = coalesce(:load_cookies, load_cookies),
                                                                                user_agent = coalesce(:user_agent, user_agent),
                                                                                header = coalesce(:header, header),
                                                                                after_download = coalesce(:after_download , after_download)
                                                                                WHERE gid = :gid""", dict)
        # commit the changes!
        self.persepolis_db_connection.commit()

        # job is done! open the lock
        self.lock = False

    def updateVideoFinderTable(self, list):

        # lock data base
        self.lockCursor()

        keys_list = ['video_gid',
                     'audio_gid',
                     'video_completed',
                     'audio_completed',
                     'muxing_status',
                     'checking']

        for dictionary in list:
            for key in keys_list:
                # if a key is missed in dict,
                # then add this key to the dict and assign None value for the key.
                if key not in dictionary.keys():
                    dictionary[key] = None

            if dictionary['video_gid']:
                # update data base if value for the keys is not None
                self.persepolis_db_cursor.execute("""UPDATE video_finder_db_table SET video_completed = coalesce(:video_completed, video_completed),
                                                                                audio_completed = coalesce(:audio_completed, audio_completed),
                                                                                muxing_status = coalesce(:muxing_status, muxing_status),
                                                                                checking = coalesce(:checking, checking),
                                                                                download_path = coalesce(:download_path, download_path)
                                                                                WHERE video_gid = :video_gid""", dictionary)
            elif dictionary['audio_gid']:
                # update data base if value for the keys is not None
                self.persepolis_db_cursor.execute("""UPDATE video_finder_db_table SET video_completed = coalesce(:video_completed, video_completed),
                                                                                audio_completed = coalesce(:audio_completed, audio_completed),
                                                                                muxing_status = coalesce(:muxing_status, muxing_status),
                                                                                checking = coalesce(:checking, checking),
                                                                                download_path = coalesce(:download_path, download_path)
                                                                                WHERE audio_gid = :audio_gid""", dictionary)

        # commit the changes!
        self.persepolis_db_connection.commit()

        # job is done! open the lock
        self.lock = False

    def setDefaultGidInAddlinkTable(self, gid, start_time=False, end_time=False, after_download=False):
        # lock data base
        self.lockCursor()

        # change value of start_time and end_time and after_download for special gid to NULL value
        if start_time:
            self.persepolis_db_cursor.execute("""UPDATE addlink_db_table SET start_time = NULL
                                                                        WHERE gid = '{}' """.format(gid))
        if end_time:
            self.persepolis_db_cursor.execute("""UPDATE addlink_db_table SET end_time = NULL
                                                                        WHERE gid = '{}' """.format(gid))
        if after_download:
            self.persepolis_db_cursor.execute("""UPDATE addlink_db_table SET after_download = NULL
                                                                        WHERE gid = '{}' """.format(gid))

        self.persepolis_db_connection.commit()

        # job is done! open the lock
        self.lock = False

    # return category information in category_db_table

    def searchCategoryInCategoryTable(self, category):
        # lock data base
        self.lockCursor()

        self.persepolis_db_cursor.execute(
            """SELECT * FROM category_db_table WHERE category = '{}'""".format(str(category)))
        list = self.persepolis_db_cursor.fetchall()

        # job is done! open the lock
        self.lock = False

        if list:
            tuple = list[0]
        else:
            return None

        # convert string to list
        gid_list = ast.literal_eval(tuple[9])

        # create a dictionary from results
        dict = {'category': tuple[0],
                'start_time_enable': tuple[1],
                'start_time': tuple[2],
                'end_time_enable': tuple[3],
                'end_time': tuple[4],
                'reverse': tuple[5],
                'limit_enable': tuple[6],
                'limit_value': tuple[7],
                'after_download': tuple[8],
                'gid_list': gid_list
                }

        # return dictionary
        return dict

    # return categories name
    def categoriesList(self):
        # lock data base
        self.lockCursor()

        self.persepolis_db_cursor.execute("""SELECT category FROM category_db_table ORDER BY ROWID""")
        rows = self.persepolis_db_cursor.fetchall()

        # create a list from categories name
        queues_list = []

        for tuple in rows:
            queues_list.append(tuple[0])

        # job is done! open the lock
        self.lock = False

        # return the list
        return queues_list

    def setDBTablesToDefaultValue(self):
        # lock data base
        self.lockCursor()

        # change start_time_enable , end_time_enable , reverse ,
        # limit_enable , after_download value to default value !
        self.persepolis_db_cursor.execute("""UPDATE category_db_table SET start_time_enable = 'no', end_time_enable = 'no',
                                        reverse = 'no', limit_enable = 'no', after_download = 'no'""")

        # change status of download to 'stopped' if status isn't 'complete' or 'error'
        self.persepolis_db_cursor.execute("""UPDATE download_db_table SET status = 'stopped' 
                                        WHERE status NOT IN ('complete', 'error')""")

        # change start_time and end_time and
        # after_download value to None in addlink_db_table!
        self.persepolis_db_cursor.execute("""UPDATE addlink_db_table SET start_time = NULL,
                                                                        end_time = NULL,
                                                                        after_download = NULL
                                                                                        """)

        # change checking value to no in video_finder_db_table
        self.persepolis_db_cursor.execute("""UPDATE video_finder_db_table SET checking = 'no'""")

        self.persepolis_db_connection.commit()

        # job is done! open the lock
        self.lock = False

    def findActiveDownloads(self, category=None):
        # lock data base
        self.lockCursor()

        # find download items is download_db_table with status = "downloading" or "waiting" or paused or scheduled
        if category:
            self.persepolis_db_cursor.execute("""SELECT gid FROM download_db_table WHERE (category = '{}') AND (status = 'downloading' OR status = 'waiting' 
                                            OR status = 'scheduled' OR status = 'paused')""".format(str(category)))
        else:
            self.persepolis_db_cursor.execute("""SELECT gid FROM download_db_table WHERE (status = 'downloading' OR status = 'waiting' 
                                            OR status = 'scheduled' OR status = 'paused')""")

        # create a list for returning answer
        result = self.persepolis_db_cursor.fetchall()
        gid_list = []

        for result_tuple in result:
            gid_list.append(result_tuple[0])

        # job is done! open the lock
        self.lock = False

        return gid_list

# this method returns items with 'downloading' or 'waiting' status
    def returnDownloadingItems(self):
        # lock data base
        self.lockCursor()

        # find download items is download_db_table with status = "downloading" or "waiting" or paused or scheduled
        self.persepolis_db_cursor.execute(
            """SELECT gid FROM download_db_table WHERE (status = 'downloading' OR status = 'waiting')""")

        # create a list for returning answer
        result = self.persepolis_db_cursor.fetchall()
        gid_list = []

        for result_tuple in result:
            gid_list.append(result_tuple[0])

        # job is done! open the lock
        self.lock = False

        return gid_list

# this method returns items with 'paused' status.
    def returnPausedItems(self):
        # lock data base
        self.lockCursor()

        # find download items is download_db_table with status = "downloading" or "waiting" or paused or scheduled
        self.persepolis_db_cursor.execute("""SELECT gid FROM download_db_table WHERE (status = 'paused')""")

        # create a list for returning answer
        result = self.persepolis_db_cursor.fetchall()
        gid_list = []

        for result_tuple in result:
            gid_list.append(result_tuple[0])

        # job is done! open the lock
        self.lock = False

        return gid_list

    # return all video_gids and audio_gids in video_finder_db_table
    def returnVideoFinderGids(self):
        # lock data base
        self.lockCursor()

        self.persepolis_db_cursor.execute("""SELECT video_gid, audio_gid FROM video_finder_db_table""")

        # create a list for result
        result = self.persepolis_db_cursor.fetchall()

        # job is done! open the lock
        self.lock = False

        gid_list = []
        video_gid_list = []
        audio_gid_list = []

        for result_tuple in result:
            gid_list.append(result_tuple[0])
            video_gid_list.append(result_tuple[0])

            gid_list.append(result_tuple[1])
            audio_gid_list.append(result_tuple[1])

        # job is done
        return gid_list, video_gid_list, audio_gid_list

    # This method deletes a category from category_db_table
    def deleteCategory(self, category):

        # delete gids of this category from gid_list of 'All Downloads'
        category_dict = self.searchCategoryInCategoryTable(category)
        all_downloads_dict = self.searchCategoryInCategoryTable('All Downloads')

        # get gid_list
        category_gid_list = category_dict['gid_list']
        all_downloads_gid_list = all_downloads_dict['gid_list']

        for gid in category_gid_list:
            # delete item from all_downloads_gid_list
            all_downloads_gid_list.remove(gid)

        # update category_db_table
        self.updateCategoryTable([all_downloads_dict])

        # delete category from data_base
        # lock data base
        self.lockCursor()

        self.persepolis_db_cursor.execute(
            """DELETE FROM category_db_table WHERE category = '{}'""".format(str(category)))

        # commit changes
        self.persepolis_db_connection.commit()

        # job is done! open the lock
        self.lock = False


# this method deletes all items in data_base

    def resetDataBase(self):
        # update gid_list in categories with empty gid_list
        all_downloads_dict = {'category': 'All Downloads', 'gid_list': []}
        single_downloads_dict = {'category': 'Single Downloads', 'gid_list': []}
        scheduled_downloads_dict = {'category': 'Scheduled Downloads', 'gid_list': []}

        self.updateCategoryTable([all_downloads_dict, single_downloads_dict, scheduled_downloads_dict])

        # lock data base
        self.lockCursor()

        # delete all items in category_db_table, except 'All Downloads' and 'Single Downloads'
        self.persepolis_db_cursor.execute(
            """DELETE FROM category_db_table WHERE category NOT IN ('All Downloads', 'Single Downloads', 'Scheduled Downloads')""")
        self.persepolis_db_cursor.execute("""DELETE FROM download_db_table""")
        self.persepolis_db_cursor.execute("""DELETE FROM addlink_db_table""")

        # commit
        self.persepolis_db_connection.commit()

        # release lock
        self.lock = False

# This method deletes a download item from download_db_table
    def deleteItemInDownloadTable(self, gid, category):
        # lock data base
        self.lockCursor()

        self.persepolis_db_cursor.execute("""DELETE FROM download_db_table WHERE gid = '{}'""".format(str(gid)))

        # commit changes
        self.persepolis_db_connection.commit()

        # job is done! open the lock
        self.lock = False

        # delete item from gid_list in category and All Downloads
        for category_name in category, 'All Downloads':
            category_dict = self.searchCategoryInCategoryTable(category_name)

            # get gid_list
            gid_list = category_dict['gid_list']

            # delete item
            if gid in gid_list:
                gid_list.remove(gid)

                # if gid is in video_finder_db_table, both of video_gid and audio_gid must be deleted from gid_list
                video_finder_dictionary = self.searchGidInVideoFinderTable(gid)

                if video_finder_dictionary:
                    video_gid = video_finder_dictionary['video_gid']
                    audio_gid = video_finder_dictionary['audio_gid']

                    if gid == video_gid:
                        gid_list.remove(audio_gid)
                    else:
                        gid_list.remove(video_gid)

                # update category_db_table
                self.updateCategoryTable([category_dict])


# this method replaces:
# GB >> GiB
# MB >> MiB
# KB >> KiB
# Read this link for more information:
# https://en.wikipedia.org/wiki/Orders_of_magnitude_(data)
    def correctDataBase(self):

        # lock data base
        self.lockCursor()

        for units in [['KB', 'KiB'], ['MB', 'MiB'], ['GB', 'GiB']]:
            dict = {'old_unit': units[0],
                    'new_unit': units[1]}

            self.persepolis_db_cursor.execute("""UPDATE download_db_table 
                    SET size = replace(size, :old_unit, :new_unit)""", dict)
            self.persepolis_db_cursor.execute("""UPDATE download_db_table 
                    SET rate = replace(rate, :old_unit, :new_unit)""", dict)
            self.persepolis_db_cursor.execute("""UPDATE download_db_table 
                    SET downloaded_size = replace(downloaded_size, :old_unit, :new_unit)""", dict)

        self.persepolis_db_connection.commit()

        # job is done! open the lock
        self.lock = False

    # close connections

    def closeConnections(self):
        # lock data base
        self.lockCursor()

        self.persepolis_db_cursor.close()
        self.persepolis_db_connection.close()

        # job is done! open the lock
        self.lock = False
