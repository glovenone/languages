#!/usr/bin/python
#Filename:crawler.py

import urllib
#import BeautifulSoup
from bs4 import BeautifulSoup
from datetime import * 

url = 'http://bbs.tianya.cn/list.jsp?item=funinfo&grade=3&order=1' #yulebagua
url2 = 'http://bbs.tianya.cn/list.jsp?item=free&grade=3&order=1' #tianyazatan
htmlSource = urllib.urlopen(url);
soup = BeautifulSoup(htmlSource)

htmlSource2 = urllib.urlopen(url2);
soup2 = BeautifulSoup(htmlSource2)

f1 = '/Users/glove/data/tianya/tianyabagua'+str(date.today())+'.html'
f2 = '/Users/glove/data/tianya/tianyazatan'+str(date.today())+'.html'

f1=open(f1,'w')
print >>f1,soup
f1.close()

f2=open(f2,'w')
print >>f2,soup2
f2.close()

'''
#id_div_2_1 = soup.find(id='div_2_1')
table = soup.find('table').find_all('a')
print table
'''

