#!/usr/bin/python
#Filename:crawler.py

import urllib
import BeautifulSoup
htmlSource = urllib.urlopen("http://http://blog.csdn.net/sding").read(200000)
soup = BeautifulSoup.BeautifulSoup(htmlSource)
for item in soup.fetch('a'):
    print item['href']
