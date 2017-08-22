# coding:utf-8
import sys
import time
import urllib2
from BeautifulSoup  import BeautifulSoup 
import os
import datetime  # 导入日期时间模块
import time
from urllib import quote
reload(sys)
sys.setdefaultencoding('utf-8')

max_page = 14959 #最大页数
base_url = 'http://a.qidian.com/mm'

# 函数1，根据关键字获取查询网页
def do_search(pagenum):
    print 'come on --------------------------------------------------------'+str(pagenum)

    url = base_url+'?orderId=&style=1&pageSize=20&siteid=0&hiddenField=0&page='+str(pagenum)
    html = urllib2.urlopen(url).read()
    return html

# 处理分页
def deal_key():
    if os.path.exists('data') == False:
         os.mkdir('data')
    filename = "data/qidian_mm"
    fp = open(filename, 'wb')  # 打开方式用‘w'时，下边的写要str转换，而对于网页要编码转换，遇到有些不规范的空格还出错

    page = 0
    while page <= max_page:
        htmlpage = do_search(page)
        page = page + 1
        print '********************page:'+str(page)+'******************';
        analysisPage(htmlpage, fp)
        fp.write(b'\n')
#        time.sleep(1)
    fp.close()

# 分析某一页
def analysisPage(htmlpage, fp):
    soup = BeautifulSoup(htmlpage)
    count=0 #计数用
    for item in soup.find("div",{"class":"all-book-list"}).findAll("li"):
        print '********************count:'+str(count)+'******************';
        book_mid_info = item.find("div",{"class":"book-mid-info"})
        title_link = book_mid_info.find('h4') # book total info
        title = title_link.a.text
        print '--------------title-------------------';
        print title

        author_info = book_mid_info.find("p",{"class":"author"}) #author total info
        author_info_a_list = author_info.findAll("a") #author name , type

        author_name = author_info_a_list[0].text
        print '--------------author_name-------------------';
        print author_name
        author_type= author_info_a_list[1].text
        print '--------------author_type-------------------';
        print author_type
        author_status = author_info.find("span").text
        print '--------------author_status-------------------';
        print author_status

        content_update = book_mid_info.find("p",{"class":"update"}).find("span").text
        print '--------------content_update-------------------';
        print content_update

        #写入文件
        fp.write(title)
        fp.write("\t")
        fp.write(author_name)
        fp.write("\t")
        fp.write(author_type)
        fp.write("\t")
        fp.write(author_status)
        fp.write("\t")
        fp.write(content_update)
        fp.write("\t")
        fp.write("\n")

        count = count + 1


# 脚本入口
print('Start:')
deal_key()
print('End！')
