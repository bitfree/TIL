# -*- coding: UTF-8 -*-

import urllib.request
from urllib.error import URLError, HTTPError
import json

headers = { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36" }


# create a password manager
password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()

# Add the username and password.
# If we knew the realm, we could use it instead of None.
top_level_url = "http://10.166.101.43:81/"
password_mgr.add_password(None, top_level_url, 'admin_dit', 'P@ssw0rd')
print(password_mgr)
print(top_level_url)


headers = { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36" }


handler = urllib.request.HTTPBasicAuthHandler(password_mgr)

# create "opener" (OpenerDirector instance)
opener = urllib.request.build_opener(handler)

# use the opener to fetch a URL
#opener.open(a_url)
# opener.open('http://10.166.101.43:81/#/dashboard/self',data=None) 

proxy_support = urllib.request.ProxyHandler({})
opener = urllib.request.build_opener(proxy_support)


response = opener.open(top_level_url)

the_page = response.read()

print(the_page)


# Install the opener.
# Now all calls to urllib.request.urlopen use our opener.
urllib.request.install_opener(opener)

try: 
    res= opener.open('http://10.166.101.43:81/#/dashboard/self',data=None) 
    page_2 = res.read()
    print(page_2)
except:
    pass

from plyer import notification

# pip install plyer 

notification.notify(
    title = '제목입니다.',
    message = '메시지 내용입니다.',
    app_name = "앱 이름",
    # app_icon = 'bluemen_white.ico', # 'C:\\icon_32x32.ico'
    timeout = 10,  # seconds
)