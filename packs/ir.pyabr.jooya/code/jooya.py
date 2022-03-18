import subprocess
import sys, markdown
from pyabr.core import *
from pyabr.quick import *

application = QtGui.QGuiApplication([])

class MainApp(MainApp):
    def loop(self):
        if not (self.webView.property('url').toString() in control.read_list(f'{self.username}/.jooya_history') and self.webView.property('title') in control.read_list(f'{self.username}/.jooya_history_titles')):
            files.append(f'{self.username}/.jooya_history',f"{self.webView.property('url').toString()}\n")
            files.append(f'{self.username}/.jooya_history_titles', f"{self.webView.property('title')}\n")
            files.append(f'{self.username}/.jooya_history_icons', f"{self.webView.property('icon').toString()}\n")
            self.setProperty('title',f"Jooya - {self.webView.property('title')}")
            app.launchedlogo(self.property('title'), res.etc('jooya', 'logo'))
            self.txtURL.setProperty('text', self.webView.property('url').toString())

            self.addJooyaHistoryModel()
            self.addJooyaSearchEngineModel()
            self.addJooyaBookmarkModel()

        if not self.sesel.property('text')=='':
            files.write ('/etc/jooya/searchengine',self.sesel.property('text'))

            self.webengine = files.readall('/etc/jooya/searchengine')
            self.webengineurl = control.read_record('url',f'/etc/jooya/engines/{self.webengine}')
            self.webenginequrl = control.read_record('qurl', f'/etc/jooya/engines/{self.webengine}')
            self.webenginename = control.read_record('name', f'/etc/jooya/engines/{self.webengine}')
            self.webenginekey = control.read_record('key', f'/etc/jooya/engines/{self.webengine}')
            self.webView.setProperty('url',self.webengineurl)

        if self.txtURL.property('text').startswith('stor:///') and files.isfile(self.txtURL.property('text').replace('stor:///','/')):
            if self.txtURL.property('text').endswith('.html') or self.txtURL.property('text').endswith('.htm') or self.txtURL.property('text').endswith('.xhtml') or self.txtURL.property('text').endswith('.xml'):
                self.webView.setProperty('url',self.txtURL.property('text').replace('stor:///','file:///stor/'))
            elif self.txtURL.property('text').endswith('.md'):
                files.write('/tmp/jooya-render.html',markdown.markdown(files.readall(self.txtURL.property('text').replace('stor:///','/'))))
                self.webView.setProperty('url', 'file:///stor/tmp/jooya-render.html')

        self.sesel.setProperty('text','')

        QTimer.singleShot(1000,self.loop)

    def search_(self):
        if self.txtURL.property('text').startswith('https://') or self.txtURL.property('text').startswith('http://'):
            self.webView.setProperty('url',self.txtURL.property('text'))
        elif self.txtURL.property('text').startswith('stor:///') and files.isfile(self.txtURL.property('text').replace('stor:///','/')):
            if self.txtURL.property('text').endswith('.html') or self.txtURL.property('text').endswith('.htm') or self.txtURL.property('text').endswith('.xhtml') or self.txtURL.property('text').endswith('.xml'):
                self.webView.setProperty('url',self.txtURL.property('text').replace('stor:///','file:///stor/'))
            elif self.txtURL.property('text').endswith('.md'):
                files.write('/tmp/jooya-render.html',markdown.markdown(files.readall(self.txtURL.property('text').replace('stor:///','/'))))
                self.webView.setProperty('url', 'file:///stor/tmp/jooya-render.html')
        else:
            self.webView.setProperty('url',self.webenginequrl.replace("{0}",self.txtURL.property('text')))

    def act_new_window_(self):
        app.start('jooya','')

    FullScreen = False

    def act_fullscreen_(self):
        if self.FullScreen:
            self.setProperty('visibility','Windowed')
            self.act_fullscreen.setProperty('text','Full screen')
            self.FullScreen = False
        else:
            self.setProperty('visibility','FullScreen')
            self.act_fullscreen.setProperty('text', 'Exit full screen')
            self.FullScreen = True

    def seAdd_(self):
        self.popup_addsearchengine.close()
        engine = self.seID.property('text')
        name = self.seName.property('text')
        url = self.seUrl.property('text')
        qurl = self.seQUrl.property('text')
        key = self.seKey.property('text')

        files.create (f'/etc/jooya/engines/{engine}')

        control.write_record ('name',name,f'/etc/jooya/engines/{engine}')
        control.write_record ('url',url,f'/etc/jooya/engines/{engine}')
        control.write_record ('qurl',qurl,f'/etc/jooya/engines/{engine}')
        control.write_record ('key',key,f'/etc/jooya/engines/{engine}')

        files.write ('/etc/jooya/searchengine',engine)

        self.webengineurl = url
        self.webenginequrl = qurl
        self.webenginename = name
        self.webenginekey = key
        self.webView.setProperty('url',url)

    def addbookmark_(self):
        self.addJooyaBookmarkModel()

        if not self.webView.property('url').toString() in control.read_list(f'{self.username}/.jooya_bookmarks'):
            files.append(f'{self.username}/.jooya_bookmarks',f"{self.webView.property('url').toString()}\n")
            files.append(f'{self.username}/.jooya_bookmarks_titles',f"{self.webView.property('title')}\n")
            files.append(f'{self.username}/.jooya_bookmarks_icons',f"{self.webView.property('icon').toString()}\n")

    def __init__(self):
        super(MainApp, self).__init__()
        self.load (res.get('@layout/jooya'))
        self.setProperty('title',res.getname('jooya'))
        app.launchedlogo(self.property('title'), res.etc('jooya', 'logo'))

        if files.readall('/proc/info/su') == 'root':
            self.username = f'/root'
        else:
            self.username = f'/desk/{files.readall("/proc/info/su")}'

        if not files.isfile(f'{self.username}/.jooya_history'): files.create(f'{self.username}/.jooya_history')
        if not files.isfile(f'{self.username}/.jooya_history_icons'): files.create(f'{self.username}/.jooya_history_icons')
        if not files.isfile(f'{self.username}/.jooya_history_titles'): files.create(f'{self.username}/.jooya_history_titles')
        if not files.isfile(f'{self.username}/.jooya_bookmarks'): files.create(f'{self.username}/.jooya_bookmarks')
        if not files.isfile(f'{self.username}/.jooya_bookmarks_icons'): files.create(f'{self.username}/.jooya_bookmarks_icons')
        if not files.isfile(f'{self.username}/.jooya_bookmarks_titles'): files.create(f'{self.username}/.jooya_bookmarks_titles')

        # set default web engine search #
        self.webengine = files.readall('/etc/jooya/searchengine')
        self.webengineurl = control.read_record('url',f'/etc/jooya/engines/{self.webengine}')
        self.webenginequrl = control.read_record('qurl', f'/etc/jooya/engines/{self.webengine}')
        self.webenginename = control.read_record('name', f'/etc/jooya/engines/{self.webengine}')
        self.webenginekey = control.read_record('key', f'/etc/jooya/engines/{self.webengine}')

        self.sesel = self.findChild('sesel')

        self.webView = self.findChild('webView')
        self.webView.setProperty('url',self.webengineurl)

        self.back = self.findChild('back')
        self.next = self.findChild('next')
        self.refresh = self.findChild('refresh')
        self.search = self.findChild('search')
        self.search.clicked.connect (self.search_)
        self.txtURL = self.findChild('txtURL')
        self.txtURL.setProperty('placeholderText',res.get('@string/search'))

        self.act_new_window = self.findChild('act_new_window')
        self.act_new_window.setProperty('text',res.get('@string/newwindow'))
        self.act_new_window.triggered.connect (self.act_new_window_)
        self.act_exit = self.findChild('act_exit')
        self.act_exit.setProperty('text',res.get('@string/exit'))
        self.act_exit.triggered.connect (sys.exit)
        self.act_fullscreen = self.findChild('act_fullscreen')
        self.act_fullscreen.setProperty('text',res.get('@string/fullscreen'))
        self.act_fullscreen.triggered.connect (self.act_fullscreen_)
        self.act_searchengines = self.findChild('act_searchengines')
        self.act_searchengines.setProperty('text',res.get('@string/searchengines'))
        self.act_addsearchengine = self.findChild('act_addsearchengine')
        self.act_addsearchengine.setProperty('text',res.get('@string/addsearchengine'))
        self.act_history = self.findChild('act_history')
        self.act_history.setProperty('text',res.get('@string/history'))
        self.act_bookmarks = self.findChild('act_bookmarks')
        self.act_bookmarks.setProperty('text',res.get('@string/bookmarks'))
        self.men_controls = self.findChild('men_controls')
        self.men_controls.setProperty('title',res.get('@string/controls'))
        self.men_view = self.findChild('men_view')
        self.men_view.setProperty('title',res.get('@string/view'))
        self.popup_addsearchengine = self.findChild('popup_addsearchengine')
        self.popup_addsearchengine.setProperty('title',res.get('@string/addsearchengine'))
        self.popup_history = self.findChild('popup_history')
        self.popup_history.setProperty('title',res.get('@string/history'))
        self.popup_searchengines = self.findChild('popup_searchengine')
        self.popup_searchengines.setProperty('title',res.get('@string/searchengines'))
        self.popup_bookmarks = self.findChild('popup_bookmarks')
        self.popup_bookmarks.setProperty('title',res.get('@string/bookmarks'))

        self.btnSeAdd = self.findChild('btnSeAdd')
        self.btnSeAdd.setProperty('text',res.get('@string/seadd'))
        self.btnSeAdd.clicked.connect (self.seAdd_)
        self.seID = self.findChild('seID')
        self.seID.setProperty('text',res.get('@string/seid'))
        self.seName = self.findChild('seName')
        self.seName.setProperty('text',res.get('@string/sename'))
        self.seUrl = self.findChild('seUrl')
        self.seUrl.setProperty('text',res.get('@string/seurl'))
        self.seQUrl = self.findChild('seQUrl')
        self.seQUrl.setProperty('text',res.get('@string/sequrl'))
        self.seKey = self.findChild('seKey')
        self.seKey.setProperty('text',res.get('@string/sekey'))

        self.addbookmark = self.findChild('addbookmark')
        self.addbookmark.clicked.connect (self.addbookmark_)

        # sys argv commands
        if not sys.argv[1:]==[]:
            self.webView.setProperty("url",QUrl(sys.argv[1]))

        self.loop()

application.setWindowIcon (QIcon(res.get(res.etc('jooya','logo'))))
w = MainApp()
application.exec()