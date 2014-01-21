#!/usr/bin/env python
import urllib2
from bs4 import BeautifulSoup, SoupStrainer
import re
import sys
import chardet

#import html5lib
#from html5lib import sanitizer
##from html5lib import treebuilders
reload(sys)
sys.setdefaultencoding("utf-8")
url = 'http://segmentfault.com/q/1010000000185278'
page = urllib2.urlopen(url)
soup = BeautifulSoup(page)
soup.originalEncoding
soup.prettify


def getLinks(soup):
    #url_list = soup.findAll(name='a', href=re.compile('^(http|https|ftp)://'))
    url_list = soup.findAll(name='a', text=re.compile('python'))
    return url_list

    url_list = getLinks(soup)
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
