#!/usr/bin/env python
#coding=utf-8
import urllib2, re, sys, chardet
from bs4 import BeautifulSoup, SoupStrainer


#import html5lib
#from html5lib import sanitizer
##from html5lib import treebuilders
reload(sys)
sys.setdefaultencoding('utf-8')

url = 'http://segmentfault.com/q/1010000000185278'
html = urllib2.urlopen(url).read()
#!/usr/bin/env python

encoding = chardet.detect(html)['encoding']
html = html.decode(encoding, 'ignore').encode('utf-8', 'ignore')
soup = BeautifulSoup(html)

#url_list = soup.findAll(name='a', href=re.compile('^(http|https|ftp)://'))

key_word = '编码'
url_list = soup.findAll(name='a', text=re.compile(u""+key_word))
for link in url_list:
    #print(link.get('href'))
    print(link)
    #print link

#url_list = soup.findAll(name='a',href=re.compile('^(http|https|ftp)://'))
#url_list = soup.a['href']
#print url_list
#for each_url in url_list:
#    str_url = str(each_url).split('"')
#    print str_url[1]
