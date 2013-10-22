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

url = 'http://www.xiami.com/artist/top/id/1234'
url = 'http://www.webguo.com/'
content = urllib2.urlopen(url).read()
soup = BeautifulSoup(content)
#print content
print soup
"""
"""
