#!/usr/bin/python
#Filename:test.py

import os
import pycurl
import StringIO

html = StringIO.StringIO()
url = r'http://travel.sina.com.cn/sichuan-lvyou/'
c = pycurl.Curl()
c.setopt(pycurl.URL, url)
c.setopt(pycurl.SSL_VERIFYHOST, False)
c.setopt(pycurl.SSL_VERIFYPEER, False)
c.setopt(pycurl.WRITEFUNCTION, html.write)
c.setopt(pycurl.FOLLOWLOCATION, 1)
c.perform()
print c.getinfo(pycurl.HTTP_CODE), c.getinfo(pycurl.EFFECTIVE_URL)
content = html.getvalue()
print type(content)

res1 = str.find(content, 'travel.sina.com.cn')

print res1
