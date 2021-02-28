from libabr import Control, Files

files = Files()
control = Control()
locale = control.read_record("locale","/etc/gui")

def get_string (name):
    return control.read_record(name,f'/srv/com/pyabr/help/data/{locale}.locale')

if locale=='fa' or locale=='ar':
    alignment = 'rtl'
else:
    alignment = 'ltr'

style = '''
.lists {
    font-size: 120%;
}
'''

print(f'''
<html dir='{alignment}'>
    <head>
        <title>{get_string('title')}</title>
        <meta charset='utf-8'/>
        <style>
        {style}
        </style>
    </head>
    <body>
        <p>{get_string("welcome")}</p>
        <ul>
            <a href="abr://help.pyabr.com/01-now">
            <font color='blue' class='lists'>{get_string('01-now')}</font>
            </a>
            <hr/>
            <a href="abr://help.pyabr.com/02-install">
            <font color='#123456'  class='lists'>{get_string('02-install')}</font>
            </a>
            <hr/>
            <a href="abr://help.pyabr.com/03-desktop">
            <font color='blue'  class='lists'>{get_string('03-desktop')}</font>
            </a>
            <hr/>
            <a href="abr://help.pyabr.com/04-cli">
            <font color='#123456'  class='lists'>{get_string('04-cli')}</font>
            </a>
            <hr/>
            <a href="abr://help.pyabr.com/05-kernel-ports">
            <font color='blue'  class='lists'>{get_string('05-kernel-ports')}</font>
            </a>
            <hr/>
            <a href="abr://help.pyabr.com/06-package-manager">
            <font color='#123456'  class='lists'>{get_string('06-package-manager')}</font>
            </a>
            <hr/>
            <a href="abr://help.pyabr.com/07-programing">
            <font color='blue'  class='lists'>{get_string('07-programing')}</font>
            </a>
            <hr/>
            <a href="abr://help.pyabr.com/08-license">
            <font color='#123456' class='lists'>{get_string('08-license')}</font>
            </a>
        </ul>
    </body>
</html>
''')