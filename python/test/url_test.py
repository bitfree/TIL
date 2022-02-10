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

import socket
from datetime import datetime
from tabnanny import check
import urllib.request
from urllib.error import URLError, HTTPError
import sched,time
import winsound


# url_list.txt must be located in current folder

# global timeout using socket
timeout = 5
socket.setdefaulttimeout(timeout)

s = sched.scheduler(time.time, time.sleep)

interval = 60*5
delay=1

def check_url_list():
    print(datetime.now())
    
    f = open('url_list.txt','r')
    # create a password manager
    password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()
       
    for top_level_url in list(f):
        target_url = top_level_url.replace("\n",'')
        # print(target_url)

        # Add the username and password.
        # If we knew the realm, we could use it instead of None.
        password_mgr.add_password(None, target_url, 'userid', 'userp')
        headers = { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36" }
        handler = urllib.request.HTTPBasicAuthHandler(password_mgr)
        # create "opener" (OpenerDirector instance)
        opener = urllib.request.build_opener(handler)

        # use the opener to fetch a URL
        # opener.open(a_url)

        proxy_handler = urllib.request.ProxyHandler({})   # 자동 감지 프락시를 비활성화하려면 빈 딕셔너리를 전달하십시오.
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
            print(target_url + " has something problem: "  + str(e))
            winsound.Beep(440,2000)
            winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
            winsound.PlaySound("beep.wav", winsound.SND_FILENAME)

            # print(e)
            if e == ValueError:
                pass 
            elif e == TimeoutError:
                pass
    
    f.close()
    s.enter(interval,1, check_url_list)
    
s.enter(delay,1, check_url_list)
s.run()
