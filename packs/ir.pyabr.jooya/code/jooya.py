import sys

from pyabr.core import *
from pyabr.quick import *

application = QtGui.QGuiApplication([])

class MainApp(MainApp):
    def loop(self):
        if not files.isfile('.jooya_history'): files.create('.jooya_history')
        if not files.isfile('.jooya_history_icons'): files.create('.jooya_history_icons')
        if not files.isfile('.jooya_history_titles'): files.create('.jooya_history_titles')

        if not (self.webView.property('url').toString() in control.read_list('.jooya_history') and self.webView.property('title') in control.read_list('.jooya_history_titles')):
            files.append('.jooya_history',f"{self.webView.property('url').toString()}\n")
            files.append('.jooya_history_titles', f"{self.webView.property('title')}\n")
            files.append('.jooya_history_icons', f"{self.webView.property('icon').toString()}\n")
            self.setProperty('title',f"Jooya - {self.webView.property('title')}")
            app.launchedlogo(self.property('title'), res.etc('jooya', 'logo'))
            self.txtURL.setProperty('text', self.webView.property('url').toString())

            self.addJooyaHistoryModel()
            self.addJooyaSearchEngineModel()

        if not self.sesel.property('text')=='':
            files.write ('/etc/jooya/searchengine',self.sesel.property('text'))

            self.webengine = files.readall('/etc/jooya/searchengine')
            self.webengineurl = control.read_record('url',f'/etc/jooya/engines/{self.webengine}')
            self.webenginequrl = control.read_record('qurl', f'/etc/jooya/engines/{self.webengine}')
            self.webenginename = control.read_record('name', f'/etc/jooya/engines/{self.webengine}')
            self.webenginekey = control.read_record('key', f'/etc/jooya/engines/{self.webengine}')
            self.webView.setProperty('url',self.webengineurl)

        self.sesel.setProperty('text','')

        QTimer.singleShot(1000,self.loop)

    def search_(self):
        if self.txtURL.property('text').startswith('https://') or self.txtURL.property('text').startswith('http://'):
            self.webView.setProperty('url',self.txtURL.property('text'))
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

    def __init__(self):
        super(MainApp, self).__init__()
        self.load (res.get('@layout/jooya'))
        app.launchedlogo(self.property('title'), res.etc('jooya', 'logo'))

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

        self.act_new_window = self.findChild('act_new_window')
        self.act_new_window.triggered.connect (self.act_new_window_)
        self.act_exit = self.findChild('act_exit')
        self.act_exit.triggered.connect (sys.exit)
        self.act_fullscreen = self.findChild('act_fullscreen')
        self.act_fullscreen.triggered.connect (self.act_fullscreen_)

        self.popup_addsearchengine = self.findChild('popup_addsearchengine')

        self.btnSeAdd = self.findChild('btnSeAdd')
        self.btnSeAdd.clicked.connect (self.seAdd_)
        self.seID = self.findChild('seID')
        self.seName = self.findChild('seName')
        self.seUrl = self.findChild('seUrl')
        self.seQUrl = self.findChild('seQUrl')
        self.seKey = self.findChild('seKey')

        # sys argv commands
        if not sys.argv[1:]==[]:
            self.webView.setProperty("url",QUrl(sys.argv[1]))

        self.loop()

application.setWindowIcon (QIcon(res.get(res.etc('jooya','logo'))))
w = MainApp()
application.exec()