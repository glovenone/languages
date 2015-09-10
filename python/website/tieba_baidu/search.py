# coding:utf-8
import sys
import time
import urllib2
from bs4 import BeautifulSoup  # from BeautifulSoup  import BeautifulSoup 旧的版本，
import os
import datetime  # 导入日期时间模块
import time
reload(sys)
sys.setdefaultencoding('utf-8')

rn = '20'
max_page = 15
key_word_list = ['大众点评', '百度糯米', '美团']
#key_word_list = ['百度糯米', '美团']
base_url = 'http://tieba.baidu.com'
# 函数1，根据关键字获取查询网页
def baidu_search(key_words, pagenum, url=''):
    print 'come on --------------------------------------------------------'+str(pagenum)
    if( url=='' ):
        pn_num = int(rn) * int(pagenum)
        pn = str(pn_num)
        url = 'http://tieba.baidu.com/f/search/res?isnew=1&kw=&qw=' + key_words + '&pn=' + pn + '&un=&only_thread=0&sm=1&sd=&ed=&rn=' + rn
    html = urllib2.urlopen(url).read()
    return html


# 函数2，处理一个要搜索的关键字
def deal_key(key_words):
    # if os.path.exists('data') == False:
    #     os.mkdir('data')
    today = datetime.date.today()
    time_num = time.strftime("%H%M%S")
    time_str = str(time_num)
    name_str = str(today) + str(time_num)
    filename = '/Volumes/storage/weiyun_sync/baidu_tieba/data/' + key_words + name_str + '.txt'
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
#        time.sleep(1)
    fp.close()

def analysisPage(htmlpage, fp):
    count=0
    soup = BeautifulSoup(htmlpage)
    for item in soup.findAll("div", {"class": "s_post"}):  # 这个格式应该参考百度网页布局
        p_title = item.find('span', {'class':'p_title'})
        title = ''
        if p_title and count > 0:
            title_get = p_title.get_text()
            title = title_get.encode('utf-8')
            # fp.write(title.replace(' ', ''))  # 标题
            # fp.write("--")
            #  print title

        p_content = item.find('div', {'class':'p_content'})
        content = ''
        if p_content:
            content_get = p_content.get_text()
            content = content_get.encode('utf-8')

        p_forum = item.find('a', {'class':'p_forum'})
        forum = ''
        if p_forum:
            forum_get = p_forum.get_text()
            forum = forum_get.encode('utf-8')

        p_username_all = item.findAll('a')
        username = ''

        if(len(p_username_all)>=3):
            username = p_username_all[2].get_text()

        p_date = item.find('font', {'class':'p_date'})
        date = ''
        if p_date:
            date_get = p_date.get_text()
            date = date_get.encode('utf-8')

        print title
        fp.write(title)
        fp.write("\t")
        fp.write(content)
        fp.write("\t")
        fp.write(forum)
        fp.write("\t")
        fp.write(username)
        fp.write("\t")
        fp.write(date)
        fp.write("\t")
        fp.write("\n")

        count = count + 1

        # fp.write(b'#')
        # if a_click:
        # fp.write(a_click.get("href").encode('utf-8'))  #链接
        # fp.write(b'#')
        # c_author = item.find('p', {'class': 'c-author'}).get_text()  # 作者
        # print c_author
        # fp.write(c_author.encode('utf-8'))
        # fp.write(b'#')
        # fp.write("\n")
# 标题，内容摘要，贴吧名称，作者名称，发文日期

        # c_abstract = item.find("div", {"class": "c-abstract"})
        # if c_abstract:
        # strtmp = c_abstract.get_text()
        # fp.write(strtmp.encode('utf-8'))  #描述
        # fp.write(b'#')


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
#        time.sleep(20)

# 脚本入口
print('Start:')
search_file()
print('End！')
