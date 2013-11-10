#!/usr/bin/env python
import urllib2
from bs4 import BeautifulSoup,SoupStrainer
import re
import sys
#import html5lib
#from html5lib import sanitizer
##from html5lib import treebuilders
reload(sys)
sys.setdefaultencoding( "utf-8" )
page = urllib2.urlopen("http://www.qq.com")
soup = BeautifulSoup(page)
soup.originalEncoding
soup.prettify

url_list = soup.findAll(name='a',href=re.compile('^http://'))
for each_url in url_list:
    str_url = str(each_url).split('"')
    print str_url[1]