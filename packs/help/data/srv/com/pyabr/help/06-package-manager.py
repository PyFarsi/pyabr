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
        <title>{get_string('06-package-manager')}</title>
        <meta charset='utf-8'/>
        <style>
        {style}
        </style>
    </head>
    <body>
    <a href="abr://help.pyabr.com">
            <font color='blue' class='lists'>{get_string('back')}</font>
            <hr/>
        </a>
    </body>
</html>
''')