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

max_page = 24837#最大页数
base_url = 'http://search.17k.com/search.xhtml'

# 函数1，根据关键字获取查询网页
def do_search(pagenum):
    print 'come on --------------------------------------------------------'+str(pagenum)

    url = base_url+'?_versions=5&page='+str(pagenum)
    html = urllib2.urlopen(url).read()
    print url
    return html

# 处理分页
def deal_key():
    if os.path.exists('data') == False:
        os.mkdir('data')
    filename = "data/17k"+time.strftime("%Y-%m-%d-%H:%M:%S",time.localtime())
    fp = open(filename, 'wb')  # 打开方式用‘w'时，下边的写要str转换，而对于网页要编码转换，遇到有些不规范的空格还出错

    page = 15383
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
    count = 1 #计数用
    for item in soup.find("div",{"class":"search-list"}).findAll("div",{"class":"textlist"}):
        print '********************count:'+str(count)+'******************';
        title_link = item.find("div",{"class":"textmiddle"}).find("dt") # book total info
        title = title_link.a.text
        print '--------------title-------------------';
        print title

        author_info = item.find("li",{"class":"bq"}) #author total info
        author_info_a_list = author_info.findAll("a") #author name , type

        author_name = author_info_a_list[0].text
        print '--------------author_name-------------------';
        print author_name
        author_type= author_info_a_list[1].text
        print '--------------author_type-------------------';
        print author_type

        word_count = author_info.find("code").text;
        print '--------------word_count-------------------';
        print word_count

        tag_info = item.find("li",{"class":"bq10"}).find("a")
        if tag_info is None:
            continue
        tag = tag_info.text
        print '--------------tag-------------------';
        print tag

        #brief= item.findAll("li")[2].text
        #print '--------------desc-------------------';
        #print brief

        content_update = item.findAll("li")[3].find("code").text
        print '--------------content_update-------------------';
        print content_update

        #写入文件
        fp.write(title)
        fp.write("\t")
        fp.write(author_name)
        fp.write("\t")
        fp.write(author_type)
        fp.write("\t")
        fp.write(word_count)
        fp.write("\t")
        fp.write(tag)
        fp.write("\t")
#        fp.write(brief)
#        fp.write("\t")
        fp.write(content_update)
        fp.write("\t")
        fp.write("\n")

        count = count + 1


# 脚本入口
print('Start:')
deal_key()
print('End！')
