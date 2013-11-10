#!/usr/bin/python
#Filename:crawler.py

"""
import urllib2
from bs4 import BeautifulSoup
htmlSource = urllib.urlopen("http://http://blog.csdn.net/sding").read(200000)
soup = BeautifulSoup.BeautifulSoup(htmlSource)
for item in soup.fetch('a'):
    print item['href']


"""
import urllib2
import re
from bs4 import BeautifulSoup

url = 'http://www.xiami.com/artist/top/id/1234'
url = 'http://www.webguo.com/'
#url = 'http://www.immomo.com/'
content = urllib2.urlopen(url).read()
content = re.findall('<a.*?href=.*?<\/a>', content, re.I)
soup = BeautifulSoup(content)
#url_list = soup.findAll(name='a', href=re.compile('^https?://'))
#re.findall('<a.*?href=.*?<\/a>',ss,re.I)


#print content
print type(url_list)
print url_list
#print "\n"

for item in url_list:
    res = item.re.compile('^https?://cn')
    print res
    print "\n"
#print url_list

