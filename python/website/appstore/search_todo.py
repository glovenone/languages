# coding:utf-8
import sys
import time
import urllib2
#from bs4 import BeautifulSoup   
from BeautifulSoup  import BeautifulSoup #旧的版本，
import os
import datetime  # 导入日期时间模块
import time
#reload(sys)
#sys.setdefaultencoding('utf-8')

rn = '20'
max_page = 15
base_url = 'http://ranking.yxhi.com/cn/'
# 函数1，根据关键字获取查询网页
def go_search(app_type):
    url = base_url + '?type=' + app_type
    print url
    html = urllib2.urlopen(url).read()
    return html


# 函数2，处理一个要搜索的关键字
def deal_type(app_type):
    today = datetime.date.today()
    today_str = str(today)
    filename = '/Users/glove/Documents/appstore/' + app_type + '_' + today_str + '.txt'
    fp = open(filename, 'wb')  # 打开方式用‘w'时，下边的写要str转换，而对于网页要编码转换，遇到有些不规范的空格还出错
    if fp:
        pass
    else:
        print('文件打失败：' + filename)
        return
    htmlpage = go_search(app_type)
    analysisPage(htmlpage, fp)
#   fp.write(b'\n')
    fp.close()

def analysisPage(htmlpage, fp):
    soup = BeautifulSoup(htmlpage)
    print soup
    for item in soup.findAll("div", {"class": "result"}):  # 这个格式应该参考百度网页布局
        '''
        a_click = item.find('a')

        if a_click:
            title_get = a_click.get_text()
            title = title_get.encode('utf-8')
            fp.write(title.replace(' ', ''))  # 标题
            print title
            fp.write("--")

        # fp.write(b'#')
        # if a_click:
        # fp.write(a_click.get("href").encode('utf-8'))  #链接
        # fp.write(b'#')
        c_author = item.find('p', {'class': 'c-author'}).get_text()  # 作者
        print c_author
        fp.write(c_author.encode('utf-8'))
        fp.write(b'#')
        fp.write("\n")

        c_more_link = item.find('a', {'class': 'c-more_link'});
        if(c_more_link):
            fp.write("<<<<")
            fp.write("\n")
            c_url  = c_more_link.get('href') # url
            htmlpage = baidu_search('', '', base_url+c_url)
            analysisPage(htmlpage, fp)
            fp.write(">>>")
            fp.write("\n")

        # c_abstract = item.find("div", {"class": "c-abstract"})
        # if c_abstract:
        # strtmp = c_abstract.get_text()
        # fp.write(strtmp.encode('utf-8'))  #描述
        # fp.write(b'#')
        '''

def main():
    type_list = ['free', 'grossing', 'paid']
    for app_type in type_list:
        deal_type(app_type)
# 脚本入口
print('Start:')
main()
print('End！')
