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

max_page = 300000
#key_word_list = ['大众点评', '百度糯米', '美团']
#key_word_list = ['百度糯米', '美团']
#key_word_list = ['优恪']
base_num = 100000
base_url = 'http://bcy.net/u/'
default_pic = 'http://img1.doubanio.com/icon/user_normal.jpg'
# 函数1 获取网页内容
def douban_search(user_id_plus):
    print 'come on --------------------------------------------------------'+str(user_id_plus)
    key_word = base_num + user_id_plus
    url = base_url + str(key_word)
    request = urllib2.Request(url)
    request.add_header('User-Agent', 'Mozilla/5.0')
    html = urllib2.urlopen(request).read()
    return html


# 函数2，处理一个要搜索的关键字


def deal_key():
    # if os.path.exists('data') == False:
    #     os.mkdir('data')
    filename = '/Volumes/storage/weiyun_sync/bcy_net/data3'
    fp = open(filename, 'wb')  # 打开方式用‘w'时，下边的写要str转换，而对于网页要编码转换，遇到有些不规范的空格还出错
    if fp:
        pass
    else:
        print('文件打失败：' + filename)
        return

    x = 0
    user = {}
    while x <= max_page:
        htmlpage = douban_search(x)
        x = x + 1
        user_temp = analysisPage(htmlpage, fp)
        if (user_temp):
            user[x] = user_temp
            fp.write(user_temp['pic'])
            fp.write('\t');
            fp.write(user_temp['name'])
            fp.write(b'\n')
#        time.sleep(1)
    fp.close()

def analysisPage(htmlpage, fp):
    user_info = {}
    soup = BeautifulSoup(htmlpage)
    for user_info_ori in soup.findAll("a", {"class":"_avatar--user"}):
        user_info_name = user_info_ori.get("alt", '').encode('utf-8')
        user_info_pic = user_info_ori.find("img")["src"]
        user_info = {'pic':user_info_pic, 'name':user_info_name}
    return user_info
    '''
    for item in soup.findAll("div", {"class": "result"}):  # 这个格式应该参考百度网页布局
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
            htmlpage = douban_search('', '', base_url+c_url)
            analysisPage(htmlpage, fp)
            fp.write(">>>")
            fp.write("\n")

        # c_abstract = item.find("div", {"class": "c-abstract"})
        # if c_abstract:
        # strtmp = c_abstract.get_text()
        # fp.write(strtmp.encode('utf-8'))  #描述
        # fp.write(b'#')
    '''


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


# 脚本入口
print('Start:')
deal_key()
print('End！')
