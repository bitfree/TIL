# -*- coding: UTF-8 -*-
'''
this script open gerrit url and show result
Tested with python 3.10
'''


## TODO:
## log : execute log
## mail or send text log to someone 

'''
Ref Here: 
https://docs.python.org/ko/3/library/urllib.request.html
urllib.request — URL을 열기 위한 확장 가능한 라이브러리
소스 코드: Lib/urllib/request.py
urllib.request 모듈은 복잡한 세계에서 URL(대부분 HTTP)을 여는 데 도움이 되는 함수와 클래스를 정의합니다 — 기본(basic)과 다이제스트 인증, 리디렉션, 쿠키 등.
더 보기
더 고수준 HTTP 클라이언트 인터페이스로 Requests 패키지를 권장합니다. (https://requests.readthedocs.io/en/master/)
'''


from datetime import datetime
import urllib.request
from urllib.error import URLError, HTTPError

# url_list.txt


f = open('url_list.txt','r')

# create a password manager
password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()

for top_level_url in list(f):
    target_url = top_level_url.replace("\n",'')
    # print(target_url)

    # Add the username and password.
    # If we knew the realm, we could use it instead of None.
    password_mgr.add_password(None, target_url, 'user', 'user_pass')

    headers = { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36" }

    handler = urllib.request.HTTPBasicAuthHandler(password_mgr)

    # create "opener" (OpenerDirector instance)
    opener = urllib.request.build_opener(handler)

    # use the opener to fetch a URL
    # opener.open(a_url)

    proxy_handler = urllib.request.ProxyHandler({})
    opener = urllib.request.build_opener(handler,proxy_handler)

    urllib.request.install_opener(opener)
    
    try: 
        res = opener.open(target_url)
        # print(type(res))
        the_page =  res.read()
        # print(type(the_page))
        # print(the_page)
    except urllib.error.URLError as e:
        # datetime.ctime(datetime)
        print(datetime.now())
        print(target_url)
        print(e)
        if e == ValueError:
            pass 

    
    

f.close()
