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


# 函数2，处理搜索
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

# 脚本入口
print('Start:')
deal_key()
print('End！')
