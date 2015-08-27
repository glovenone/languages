# coding:utf-8
import sys
import time
import urllib2
from bs4 import BeautifulSoup  # from BeautifulSoup  import BeautifulSoup 旧的版本，
import os
import datetime  # 导入日期时间模块
import time
#reload(sys)
#sys.setdefaultencoding('utf-8')

rn = '20'
max_page = 15
key_word_list = ['大众点评', '百度糯米', '美团']
#key_word_list = ['微云'] #测试用
base_url = 'http://news.baidu.com'
# 函数1，根据关键字获取查询网页
def baidu_search(key_words, pagenum, url=''):
    print('sleep 5 start');
    sleep(5)
    print('sleep 5 end');
    if( url=='' ):
        pn_num = int(rn) * int(pagenum)
        pn = str(pn_num)
        url = 'http://news.baidu.com/ns?word=' + key_words + '&pn=' + pn + '&cl=2&ct=1&tn=news&rn=' + rn + '&ie=utf-8&bt=0&et=0'
    # 'http://news.baidu.com/ns?word=%E5%B0%8F%E7%BE%8E%E5%88%B0%E5%AE%B6&pn=20&cl=2&ct=1&tn=news&rn=20&ie=utf-8&bt=0&et=0'
    html = urllib2.urlopen(url).read()
    return html


# 函数2，处理一个要搜索的关键字


def deal_key(key_words):
    # if os.path.exists('data') == False:
    #     os.mkdir('data')
    today = datetime.date.today()
    today_str = str(today)
    time_num = time.strftime("%H%M%S")
    time_str = str(time_num)
    filename = '/Volumes/storage/weiyun_sync/baidu_news/data/' + key_words + today_str + '-' + time_str + '.txt'
    fp = open(filename, 'wb')  # 打开方式用‘w'时，下边的写要str转换，而对于网页要编码转换，遇到有些不规范的空格还出错
    if fp:
        pass
    else:
        print('文件打失败：' + filename)
        return
    x = 0
    while x <= max_page:
        htmlpage = baidu_search(key_words, x)
        x = x + 1
        analysisPage(htmlpage, fp)
        fp.write(b'\n')
    fp.close()

def analysisPage(htmlpage, fp):
    soup = BeautifulSoup(htmlpage)
    for item in soup.findAll("div", {"class": "result"}):  # 这个格式应该参考百度网页布局
        a_click = item.find('a')

        if a_click:
            title_get = a_click.get_text()
            title = title_get.encode('utf-8')
            fp.write(title.replace(' ', ''))  # 标题
            fp.write("--")

        # fp.write(b'#')
        # if a_click:
        # fp.write(a_click.get("href").encode('utf-8'))  #链接
        # fp.write(b'#')
        c_author = item.find('p', {'class': 'c-author'}).get_text()  # 作者
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


# 函数3，读取搜索文件内容，依次取出要搜索的关键字
# def search_file():
#     fp = open('./searchfile.txt')
#     i = 0
#     keyword = fp.readline()
#     while keyword:
#         i = i + 1
#         if i == 5:
#             print('sleep...')
#             time.sleep(15)
#             print('end...')
#             i = 0
#         nPos = keyword.find('\n')
#         if nPos > -1:
#             keyword = keyword[:-1]  # keyword.replace('\n','')
#         deal_key(keyword)
#         keyword = fp.readline()

# 3.读数组
def search_file():
    i = 0
    for keyword in key_word_list:
        i = i + 1
        if i == 5:
            print('sleep...')
            time.sleep(15)
            print('end...')
            i = 0
        deal_key(keyword)

# 脚本入口
print('Start:')
search_file()
print('End！')
