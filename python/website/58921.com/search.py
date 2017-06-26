# -*- coding:utf-8 -*-
import sys
import time
import requests
from BeautifulSoup  import BeautifulSoup
import os
#yearList=['2008','2009','2010','2011','2012','2013','2014','2015','2016','2017']
yearList=('2017','2016')
yearPageMap = {'2017':'7','2016':'20'}
os_char='gb18030'
#reload(sys)
#sys.setdefaultencoding('utf-8') 
#函数1，根据关键字获取查询网页
def do_search(year,pagenum):             
    url = 'http://58921.com/alltime/'+year+'/'+pagenum
    html=requests.get(url)
    return html
#函数2，处理一个要搜索的关键字
def deal_key(key_words):                     
    if os.path.exists('data')==False:
        os.mkdir('data')
    filename='data\\'+key_words+'.txt'
    fp=open(filename,'wb')                                                             #打开方式用‘w'时，下边的写要str转换，而对于网页要编码转换，遇到有些不规范的空格还出错
    if fp:
        pass
    else:
        print('文件打失败：'+filename)
        return
    x=2017
    while x>=2008:
        print year
        htmlpage=do_search(year,0)
        soup=BeautifulSoup(htmlpage)
        print soup
        for item in soup.findAll("div", {"class": "result"}):                #这个格式应该参考百度网页布局
            a_click = item.find('a')
            if a_click:
                fp.write(a_click.get_text().encode('utf-8'))                  #标题
            fp.write(b'#')
            if a_click:
                fp.write(a_click.get("href").encode('utf-8'))                 #链接
            fp.write(b'#')
            c_abstract=item.find("div", {"class": "c-abstract"})
            if c_abstract:
                strtmp=c_abstract.get_text()
                fp.write(strtmp.encode('utf-8'))                                    #描述
            fp.write(b'#')
        x=x-1
        fp.write(b'\n')
    fp.close()
#函数3，读取搜索文件内容，依次取出要搜索的关键字
def search_file():          
    for year in yearList:   
        html = do_search(year,'0')
        print html.text
#        nPos=keyword.find('\n')
 #       if nPos>-1:
  #          keyword=keyword[:-1]#keyword.replace('\n','')
   #     deal_key(keyword)
    #    keyword=fp.readline()
#脚本入口
print('Start:')
search_file()
print('End！')
