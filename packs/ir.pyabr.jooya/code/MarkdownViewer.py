import subprocess
import sys, markdown
from pyabr.core import *
from pyabr.quick import *

application = QtGui.QGuiApplication([])

class MainApp(MainApp):
    def __init__(self):
        super(MainApp, self).__init__()
        self.load (res.get('@layout/MarkdownViewer'))
        self.setProperty('title',res.getname('MarkdownViewer'))
        app.launchedlogo(self.property('title'), res.etc('MarkdownViewer', 'logo'))

        self.webView = self.findChild('webView')

        style='''<!DOCTYPE HTML>
<html>
<head>
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
<style>
@font-face {
	font-family: 'IRANSansX';
	src: url('/usr/share/fonts/truetype/IRANSansX-Regular.ttf') format('truetype');
} 
body {
    font-family: "IRANSansX" !important;
}
</style>
</head>
<body>
<!-- JavaScript Bundle with Popper -->
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>'''

        # sys argv commands
        if not sys.argv[1:]==[]:
            html = markdown.markdown(files.readall(sys.argv[1]))
            html = style+html+"</body></html>"
            files.write('/tmp/MarkdownViewer-render.html',html)
            self.webView.setProperty("url","file:///stor/tmp/MarkdownViewer-render.html")

application.setWindowIcon (QIcon(res.get(res.etc('MarkdownViewer','logo'))))
w = MainApp()
application.exec()