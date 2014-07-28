#!/usr/bin/python
#Filename:crawler.py

import urllib
#import BeautifulSoup
from bs4 import BeautifulSoup
url = 'http://top.qidian.com/'
htmlSource = urllib.urlopen(url);
soup = BeautifulSoup(htmlSource)
print soup

id_div_2_1 = soup.find(id='div_2_1')

print id_div_2_1
#for item in soup.fetch('a'):
#    print item['href']

