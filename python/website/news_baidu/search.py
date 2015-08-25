# coding:utf-8
import sys
import time
import urllib2
from bs4 import BeautifulSoup  # from BeautifulSoup  import BeautifulSoup 旧的版本，
import os

rn = '20'
max_page = 10;
# 函数1，根据关键字获取查询网页
def baidu_search(key_words, pagenum):
    pn = str(rn * pagenum)
    url = 'http://news.baidu.com/ns?word=' + key_words + '&pn=' + pn + '&cl=2&ct=1&tn=news&rn=' + rn + '&ie=utf-8&bt=0&et=0'
    # 'http://news.baidu.com/ns?word=%E5%B0%8F%E7%BE%8E%E5%88%B0%E5%AE%B6&pn=20&cl=2&ct=1&tn=news&rn=20&ie=utf-8&bt=0&et=0'
    html = urllib2.urlopen(url).read()
    return html


# 函数2，处理一个要搜索的关键字


def deal_key(key_words):
    if os.path.exists('data') == False:
        os.mkdir('data')
    filename = 'data/' + key_words + '.txt'
    fp = open(filename, 'wb')  # 打开方式用‘w'时，下边的写要str转换，而对于网页要编码转换，遇到有些不规范的空格还出错
    if fp:
        pass
    else:
        print('文件打失败：' + filename)
        return
    x = 0
    while x <= max_page:
        htmlpage = baidu_search(key_words, x)
        soup = BeautifulSoup(htmlpage)
        for item in soup.findAll("div", {"class": "result"}):  # 这个格式应该参考百度网页布局
            a_click = item.find('a')
            if a_click:
                fp.write(a_click.get_text().encode('utf-8'))  #标题
            fp.write("\t")
            # fp.write(b'#')
            # if a_click:
            #     fp.write(a_click.get("href").encode('utf-8'))  #链接
            # fp.write(b'#')
            c_author = item.find('p', {'class': 'c-author'}).get_text()  #作者
            fp.write(c_author.encode('utf-8'))
            # fp.write(b'#')
            fp.write("\n")

            # c_abstract = item.find("div", {"class": "c-abstract"})
            # if c_abstract:
            #     strtmp = c_abstract.get_text()
            #     fp.write(strtmp.encode('utf-8'))  #描述
            # fp.write(b'#')
        x = x + 1
        fp.write(b'\n')
    fp.close()


# 函数3，读取搜索文件内容，依次取出要搜索的关键字
def search_file():
    fp = open('searchfile.txt')
    i = 0
    keyword = fp.readline()
    while keyword:
        i = i + 1
        if i == 5:
            print('sleep...')
            time.sleep(15)
            print('end...')
            i = 0
        nPos = keyword.find('\n')
        if nPos > -1:
            keyword = keyword[:-1]  #keyword.replace('\n','')
        deal_key(keyword)
        keyword = fp.readline()

#脚本入口
print('Start:')
search_file()
print('End！')
