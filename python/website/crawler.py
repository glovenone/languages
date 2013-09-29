#!/usr/bin/python
#Filename:crawler.py
import urllib
import BeautifulSoup

url = "http://www.python.org/index.html"
urls = []
htmlSource = urllib.urlopen(url).read(200000)
host = urllib.request(htmlSource)

soup = BeautifulSoup.BeautifulSoup(htmlSource)
for item in soup.fetch('a'):
#    print item['href']
    urls.append(item['href'])
'''
print htmlSource;
'''
