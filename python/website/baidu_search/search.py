'''
环境：
   1，python-3.3.2，环境编码格式utf-8
   2，beautifulsoup4-4.1.0
说明：
   1，将要搜索的关键词放在个脚本文件同级目录下searchfile.txt中，一个关键词一行
   2，搜索结果会位于同级目录下data文件夹中，一个关键词一个文件
脚本：
'''
#coding:utf-8
import sys
import time
import urllib.request
from bs4  import BeautifulSoup                              #from BeautifulSoup  import BeautifulSoup 旧的版本，
import os
mymap=['0','1','2','3','4','5','6','7']
#函数1，根据关键字获取查询网页
def baidu_search(key_words,pagenum):             
        url='http://www.baidu.com/s?wd='+key_words+'&pn='+mymap[pagenum]
    html=urllib.request.urlopen(url).read()
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
    x=0
    while x<=7:
                htmlpage=baidu_search(key_words,x)
        soup=BeautifulSoup(htmlpage)
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
        x=x+1
        fp.write(b'\n')
    fp.close()
#函数3，读取搜索文件内容，依次取出要搜索的关键字
def search_file():          
        fp=open('searchfile.txt')
    i=0
    keyword=fp.readline()
    while keyword:
                i=i+1
        if i==5:
                        print('sleep...')
            time.sleep(15)
            print('end...')
            i=0
        nPos=keyword.find('\n')
        if nPos>-1:
                        keyword=keyword[:-1]#keyword.replace('\n','')
        deal_key(keyword)
        keyword=fp.readline()
#脚本入口
print('Start:')
search_file()
print('End！')
