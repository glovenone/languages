#!/usr/bin/python
#Filename:crawler.py
import urllib
import BeautifulSoup

url = "http://www.python.org/index.html"
urls = []
data = urllib.urlopen(url)
htmlSource = data.read()
#host = urllib.request(htmlSource)

soup = BeautifulSoup.BeautifulSoup(htmlSource)
for item in soup.fetch('a'):
#    print item['href']
    urls.append(item['href'])
#print htmlSource
print urls

print data.geturl()


'''
import urllib
google = urllib.urlopen('http://www.google.com.hk')
print 'http header:\n', google.info()
print 'http status:', google.getcode()
print 'url:', google.geturl()
#for line in google: 
#    print line,
google.close()
'''
