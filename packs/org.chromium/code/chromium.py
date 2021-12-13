import subprocess,os,sys
from pyabr.core import *

# set bookmarks
f = open('/usr/share/chromium/initial_bookmarks.html','w')
f.write('''<!DOCTYPE NETSCAPE-Bookmark-file-1>
<META HTTP-EQUIV="Content-Type" CONTENT="text/html; charset=UTF-8">
<TITLE>Bookmarks</TITLE>
<H1>Bookmarks</H1>
<DL><p>
    <DT><H3 PERSONAL_TOOLBAR_FOLDER="true">Bookmarks Bar</H3>
    <DL><p>
        <DT><A HREF="https://pyabr.ir" ICON="data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiIHN0YW5kYWxvbmU9Im5vIj8+CjxzdmcKICAgdmlld0JveD0iMCAwIDIyIDIyIgogICB2ZXJzaW9uPSIxLjEiCiAgIGlkPSJzdmc2IgogICBzb2RpcG9kaTpkb2NuYW1lPSJicmVlemUtY2xvdWQuc3ZnIgogICBpbmtzY2FwZTp2ZXJzaW9uPSIxLjEgKGNlNjY2M2IzYjcsIDIwMjEtMDUtMjUpIgogICB4bWxuczppbmtzY2FwZT0iaHR0cDovL3d3dy5pbmtzY2FwZS5vcmcvbmFtZXNwYWNlcy9pbmtzY2FwZSIKICAgeG1sbnM6c29kaXBvZGk9Imh0dHA6Ly9zb2RpcG9kaS5zb3VyY2Vmb3JnZS5uZXQvRFREL3NvZGlwb2RpLTAuZHRkIgogICB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciCiAgIHhtbG5zOnN2Zz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPgogIDxzb2RpcG9kaTpuYW1lZHZpZXcKICAgICBpZD0ibmFtZWR2aWV3OCIKICAgICBwYWdlY29sb3I9IiNmZmZmZmYiCiAgICAgYm9yZGVyY29sb3I9IiM2NjY2NjYiCiAgICAgYm9yZGVyb3BhY2l0eT0iMS4wIgogICAgIGlua3NjYXBlOnBhZ2VzaGFkb3c9IjIiCiAgICAgaW5rc2NhcGU6cGFnZW9wYWNpdHk9IjAuMCIKICAgICBpbmtzY2FwZTpwYWdlY2hlY2tlcmJvYXJkPSIwIgogICAgIHNob3dncmlkPSJmYWxzZSIKICAgICBpbmtzY2FwZTp6b29tPSIzMy4wNDU0NTUiCiAgICAgaW5rc2NhcGU6Y3g9IjEwLjk4NDg2OSIKICAgICBpbmtzY2FwZTpjeT0iMTAuOTg0ODY5IgogICAgIGlua3NjYXBlOndpbmRvdy13aWR0aD0iMTgzMiIKICAgICBpbmtzY2FwZTp3aW5kb3ctaGVpZ2h0PSIxMDI1IgogICAgIGlua3NjYXBlOndpbmRvdy14PSIwIgogICAgIGlua3NjYXBlOndpbmRvdy15PSIwIgogICAgIGlua3NjYXBlOndpbmRvdy1tYXhpbWl6ZWQ9IjEiCiAgICAgaW5rc2NhcGU6Y3VycmVudC1sYXllcj0ic3ZnNiIgLz4KICA8ZGVmcwogICAgIGlkPSJkZWZzMzA1MSI+CiAgICA8c3R5bGUKICAgICAgIHR5cGU9InRleHQvY3NzIgogICAgICAgaWQ9ImN1cnJlbnQtY29sb3Itc2NoZW1lIj4KICAgICAgLkNvbG9yU2NoZW1lLVRleHQgewogICAgICAgIGNvbG9yOiMyMzI2Mjk7CiAgICAgIH0KICAgICAgPC9zdHlsZT4KICA8L2RlZnM+CiAgPHBhdGgKICAgICBzdHlsZT0iZmlsbDojM2RhZWU5O2ZpbGwtb3BhY2l0eToxO3N0cm9rZTpub25lIgogICAgIGQ9Ik0gMTEgNCBBIDYgNiAwIDAgMCA1IDEwIEEgNiA2IDAgMCAwIDUuMDAzOTA2MiAxMC4xMjg5MDYgQSA0IDQgMCAwIDAgMiAxNCBBIDQgNCAwIDAgMCA2IDE4IEwgMTUgMTggQSA1IDUgMCAwIDAgMjAgMTMgQSA1IDUgMCAwIDAgMTYuNzU3ODEyIDguMzI0MjE4OCBBIDYgNiAwIDAgMCAxMSA0IHogTSAxMSA1IEEgNSA1IDAgMCAxIDE1LjkxOTkyMiA5LjExMTMyODEgQSA0LjAwMDAwMTkgNC4wMDAwMDE5IDAgMCAxIDE5IDEzIEEgNC4wMDAwMDE5IDQuMDAwMDAxOSAwIDAgMSAxNSAxNyBMIDYgMTcgQSAyLjk5OTk5NzkgMi45OTk5OTc5IDAgMCAxIDMgMTQgQSAyLjk5OTk5NzkgMi45OTk5OTc5IDAgMCAxIDYgMTEgQSAyLjk5OTk5NzkgMi45OTk5OTc5IDAgMCAxIDYuMTA3NDIxOSAxMS4wMDU4NTkgQSA1IDUgMCAwIDEgNiAxMCBBIDUgNSAwIDAgMSAxMSA1IHogIgogICAgIGNsYXNzPSJDb2xvclNjaGVtZS1UZXh0IgogICAgIGlkPSJwYXRoNCIgLz4KPC9zdmc+Cg==">Pyabr.ir</A>
        <DT><A HREF="https://pyabr.ir/blog" ICON="data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiIHN0YW5kYWxvbmU9Im5vIj8+CjxzdmcKICAgdmlld0JveD0iMCAwIDIyIDIyIgogICB2ZXJzaW9uPSIxLjEiCiAgIGlkPSJzdmc2IgogICBzb2RpcG9kaTpkb2NuYW1lPSJicmVlemUtY2xvdWQuc3ZnIgogICBpbmtzY2FwZTp2ZXJzaW9uPSIxLjEgKGNlNjY2M2IzYjcsIDIwMjEtMDUtMjUpIgogICB4bWxuczppbmtzY2FwZT0iaHR0cDovL3d3dy5pbmtzY2FwZS5vcmcvbmFtZXNwYWNlcy9pbmtzY2FwZSIKICAgeG1sbnM6c29kaXBvZGk9Imh0dHA6Ly9zb2RpcG9kaS5zb3VyY2Vmb3JnZS5uZXQvRFREL3NvZGlwb2RpLTAuZHRkIgogICB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciCiAgIHhtbG5zOnN2Zz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPgogIDxzb2RpcG9kaTpuYW1lZHZpZXcKICAgICBpZD0ibmFtZWR2aWV3OCIKICAgICBwYWdlY29sb3I9IiNmZmZmZmYiCiAgICAgYm9yZGVyY29sb3I9IiM2NjY2NjYiCiAgICAgYm9yZGVyb3BhY2l0eT0iMS4wIgogICAgIGlua3NjYXBlOnBhZ2VzaGFkb3c9IjIiCiAgICAgaW5rc2NhcGU6cGFnZW9wYWNpdHk9IjAuMCIKICAgICBpbmtzY2FwZTpwYWdlY2hlY2tlcmJvYXJkPSIwIgogICAgIHNob3dncmlkPSJmYWxzZSIKICAgICBpbmtzY2FwZTp6b29tPSIzMy4wNDU0NTUiCiAgICAgaW5rc2NhcGU6Y3g9IjEwLjk4NDg2OSIKICAgICBpbmtzY2FwZTpjeT0iMTAuOTg0ODY5IgogICAgIGlua3NjYXBlOndpbmRvdy13aWR0aD0iMTgzMiIKICAgICBpbmtzY2FwZTp3aW5kb3ctaGVpZ2h0PSIxMDI1IgogICAgIGlua3NjYXBlOndpbmRvdy14PSIwIgogICAgIGlua3NjYXBlOndpbmRvdy15PSIwIgogICAgIGlua3NjYXBlOndpbmRvdy1tYXhpbWl6ZWQ9IjEiCiAgICAgaW5rc2NhcGU6Y3VycmVudC1sYXllcj0ic3ZnNiIgLz4KICA8ZGVmcwogICAgIGlkPSJkZWZzMzA1MSI+CiAgICA8c3R5bGUKICAgICAgIHR5cGU9InRleHQvY3NzIgogICAgICAgaWQ9ImN1cnJlbnQtY29sb3Itc2NoZW1lIj4KICAgICAgLkNvbG9yU2NoZW1lLVRleHQgewogICAgICAgIGNvbG9yOiMyMzI2Mjk7CiAgICAgIH0KICAgICAgPC9zdHlsZT4KICA8L2RlZnM+CiAgPHBhdGgKICAgICBzdHlsZT0iZmlsbDojM2RhZWU5O2ZpbGwtb3BhY2l0eToxO3N0cm9rZTpub25lIgogICAgIGQ9Ik0gMTEgNCBBIDYgNiAwIDAgMCA1IDEwIEEgNiA2IDAgMCAwIDUuMDAzOTA2MiAxMC4xMjg5MDYgQSA0IDQgMCAwIDAgMiAxNCBBIDQgNCAwIDAgMCA2IDE4IEwgMTUgMTggQSA1IDUgMCAwIDAgMjAgMTMgQSA1IDUgMCAwIDAgMTYuNzU3ODEyIDguMzI0MjE4OCBBIDYgNiAwIDAgMCAxMSA0IHogTSAxMSA1IEEgNSA1IDAgMCAxIDE1LjkxOTkyMiA5LjExMTMyODEgQSA0LjAwMDAwMTkgNC4wMDAwMDE5IDAgMCAxIDE5IDEzIEEgNC4wMDAwMDE5IDQuMDAwMDAxOSAwIDAgMSAxNSAxNyBMIDYgMTcgQSAyLjk5OTk5NzkgMi45OTk5OTc5IDAgMCAxIDMgMTQgQSAyLjk5OTk5NzkgMi45OTk5OTc5IDAgMCAxIDYgMTEgQSAyLjk5OTk5NzkgMi45OTk5OTc5IDAgMCAxIDYuMTA3NDIxOSAxMS4wMDU4NTkgQSA1IDUgMCAwIDEgNiAxMCBBIDUgNSAwIDAgMSAxMSA1IHogIgogICAgIGNsYXNzPSJDb2xvclNjaGVtZS1UZXh0IgogICAgIGlkPSJwYXRoNCIgLz4KPC9zdmc+Cg==">Blog & Tutorials</A>
        <DT><A HREF="https://www.goftino.com/c/eBF5N8" ICON="data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiIHN0YW5kYWxvbmU9Im5vIj8+CjxzdmcKICAgdmlld0JveD0iMCAwIDIyIDIyIgogICB2ZXJzaW9uPSIxLjEiCiAgIGlkPSJzdmc2IgogICBzb2RpcG9kaTpkb2NuYW1lPSJicmVlemUtY2xvdWQuc3ZnIgogICBpbmtzY2FwZTp2ZXJzaW9uPSIxLjEgKGNlNjY2M2IzYjcsIDIwMjEtMDUtMjUpIgogICB4bWxuczppbmtzY2FwZT0iaHR0cDovL3d3dy5pbmtzY2FwZS5vcmcvbmFtZXNwYWNlcy9pbmtzY2FwZSIKICAgeG1sbnM6c29kaXBvZGk9Imh0dHA6Ly9zb2RpcG9kaS5zb3VyY2Vmb3JnZS5uZXQvRFREL3NvZGlwb2RpLTAuZHRkIgogICB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciCiAgIHhtbG5zOnN2Zz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPgogIDxzb2RpcG9kaTpuYW1lZHZpZXcKICAgICBpZD0ibmFtZWR2aWV3OCIKICAgICBwYWdlY29sb3I9IiNmZmZmZmYiCiAgICAgYm9yZGVyY29sb3I9IiM2NjY2NjYiCiAgICAgYm9yZGVyb3BhY2l0eT0iMS4wIgogICAgIGlua3NjYXBlOnBhZ2VzaGFkb3c9IjIiCiAgICAgaW5rc2NhcGU6cGFnZW9wYWNpdHk9IjAuMCIKICAgICBpbmtzY2FwZTpwYWdlY2hlY2tlcmJvYXJkPSIwIgogICAgIHNob3dncmlkPSJmYWxzZSIKICAgICBpbmtzY2FwZTp6b29tPSIzMy4wNDU0NTUiCiAgICAgaW5rc2NhcGU6Y3g9IjEwLjk4NDg2OSIKICAgICBpbmtzY2FwZTpjeT0iMTAuOTg0ODY5IgogICAgIGlua3NjYXBlOndpbmRvdy13aWR0aD0iMTgzMiIKICAgICBpbmtzY2FwZTp3aW5kb3ctaGVpZ2h0PSIxMDI1IgogICAgIGlua3NjYXBlOndpbmRvdy14PSIwIgogICAgIGlua3NjYXBlOndpbmRvdy15PSIwIgogICAgIGlua3NjYXBlOndpbmRvdy1tYXhpbWl6ZWQ9IjEiCiAgICAgaW5rc2NhcGU6Y3VycmVudC1sYXllcj0ic3ZnNiIgLz4KICA8ZGVmcwogICAgIGlkPSJkZWZzMzA1MSI+CiAgICA8c3R5bGUKICAgICAgIHR5cGU9InRleHQvY3NzIgogICAgICAgaWQ9ImN1cnJlbnQtY29sb3Itc2NoZW1lIj4KICAgICAgLkNvbG9yU2NoZW1lLVRleHQgewogICAgICAgIGNvbG9yOiMyMzI2Mjk7CiAgICAgIH0KICAgICAgPC9zdHlsZT4KICA8L2RlZnM+CiAgPHBhdGgKICAgICBzdHlsZT0iZmlsbDojM2RhZWU5O2ZpbGwtb3BhY2l0eToxO3N0cm9rZTpub25lIgogICAgIGQ9Ik0gMTEgNCBBIDYgNiAwIDAgMCA1IDEwIEEgNiA2IDAgMCAwIDUuMDAzOTA2MiAxMC4xMjg5MDYgQSA0IDQgMCAwIDAgMiAxNCBBIDQgNCAwIDAgMCA2IDE4IEwgMTUgMTggQSA1IDUgMCAwIDAgMjAgMTMgQSA1IDUgMCAwIDAgMTYuNzU3ODEyIDguMzI0MjE4OCBBIDYgNiAwIDAgMCAxMSA0IHogTSAxMSA1IEEgNSA1IDAgMCAxIDE1LjkxOTkyMiA5LjExMTMyODEgQSA0LjAwMDAwMTkgNC4wMDAwMDE5IDAgMCAxIDE5IDEzIEEgNC4wMDAwMDE5IDQuMDAwMDAxOSAwIDAgMSAxNSAxNyBMIDYgMTcgQSAyLjk5OTk5NzkgMi45OTk5OTc5IDAgMCAxIDMgMTQgQSAyLjk5OTk5NzkgMi45OTk5OTc5IDAgMCAxIDYgMTEgQSAyLjk5OTk5NzkgMi45OTk5OTc5IDAgMCAxIDYuMTA3NDIxOSAxMS4wMDU4NTkgQSA1IDUgMCAwIDEgNiAxMCBBIDUgNSAwIDAgMSAxMSA1IHogIgogICAgIGNsYXNzPSJDb2xvclNjaGVtZS1UZXh0IgogICAgIGlkPSJwYXRoNCIgLz4KPC9zdmc+Cg==">Online Support</A>
    </DL><p>
</DL><p>
''')
f.close()

f = open('/etc/chromium/master_preferences','w')
f.write ('''{
  "distribution": {
     "import_bookmarks": false,
     "import_bookmarks_from_file": "/usr/share/chromium/initial_bookmarks.html",
     "make_chrome_default": false,
     "make_chrome_default_for_user": false,
     "verbose_logging": true,
     "skip_first_run_ui": true,
     "create_all_shortcuts": true,
     "suppress_first_run_default_browser_prompt": true
  },
  "browser": {
     "show_home_button": true,
     "has_seen_welcome_page" : true,
     "check_default_browser" : false
  },
  "profile": {
     "default_content_setting_values": {
        "payment_handler": 2
     }
  },
  "bookmark_bar": {
     "show_on_all_tabs": true
  },
  "net": {
     "network_prediction_options": 2
  },
  "search": {
     "suggest_enabled": false
  },
  "signin": {
     "allowed": false,
     "allowed_on_next_startup": false
  },
  "autofill": {
     "profile_enabled": false,
     "credit_card_enabled": false
  },
  "payments": {
     "can_make_payment_enabled": false
  },
  "safebrowsing": {
     "enabled": false
  },
  "dns_prefetching": {
     "enabled": false
  },
  "alternate_error_pages": {
     "enabled": false
  },
  "credentials_enable_service": false,
  "credentials_enable_autosignin": false,
  "default_apps": "noinstall",
  "hide_web_store_icon": true,
  "homepage_is_newtabpage": true,
  "homepage": "https://pyabr.ir"
}
''')
f.close()

# Set home folder

if files.readall('/proc/info/su')=='root':
    user = f'/stor/root'
else:
    user = f'/stor/desk/{files.readall("/proc/info/su")}'

subprocess.call(['rm','-rf',f'{user}/.config/chromium'])
    
os.environ['HOME'] = user
# Running Chromium

if sys.argv[1:]==[] or sys.argv[1:]==['']:
    subprocess.call(['chromium','--no-sandbox'])
else:
    subprocess.call(['chromium','--no-sandbox',f'--app={sys.argv[1]}'])