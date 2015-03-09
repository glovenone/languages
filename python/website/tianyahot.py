#!/usr/bin/python
#Filename:crawler.py

import urllib
#from BeautifulSoup import BeautifulSoup
from bs4 import BeautifulSoup
from datetime import * 
import time

url = 'http://bbs.tianya.cn/list.jsp?item=funinfo&grade=3&order=1' #yulebagua
url2 = 'http://bbs.tianya.cn/list.jsp?item=free&grade=3&order=1' #tianyazatan
htmlSource = urllib.urlopen(url);
soup_ori = BeautifulSoup(htmlSource)
soup = str(soup_ori).replace('<a href="/','<a href="http://bbs.tianya.cn/')

htmlSource2 = urllib.urlopen(url2);
soup2_ori = BeautifulSoup(htmlSource2)
soup2 = str(soup2_ori).replace('<a href="/','<a href="http://bbs.tianya.cn/')

timeNow = time.strftime("%Y-%m-%d--%H-%M-%S",time.localtime())

path = '/Volumes/storage/weiyun_sync/tianyahot'
f1 = path+'/tianyabagua'+str(timeNow)+'.html'
f2 = path+'/tianyazatan'+str(timeNow)+'.html'

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

