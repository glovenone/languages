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

max_page = 7088 #最大页数
base_url = 'http://www.xxsy.net/search' #网页的基础路径

# 函数1，根据关键字获取查询网页
def do_search(pagenum):
    print 'come on --------------------------------------------------------'+str(pagenum)  #打印出来看记录

    url = base_url+'?s_wd=&sort=9&pn='+str(pagenum)  #拼接url
    html = urllib2.urlopen(url).read()       #爬取页面所有元素
    return html

# 处理分页
def deal_key():
    if os.path.exists('data') == False:       #判断文件夹是否存在
         os.mkdir('data')           #不存在则自动创建文件夹
    filename = "data/xxsy"+time.strftime("%Y-%m-%d-%H:%M:%S",time.localtime())  #文件名后缀添加时间，防止重复
    fp = open(filename, 'wb')  # 打开方式用‘w'时，下边的写要str转换，而对于网页要编码转换，遇到有些不规范的空格还出错

    page = 1  #开始爬取的页数
    while page <= max_page:  #循环爬取
        htmlpage = do_search(page)  #执行页面爬取
        page = page + 1   #爬取后准备下一页
        print '********************page:'+str(page)+'******************';  #打印查看
        analysisPage(htmlpage, fp)  #解析页面内容
        fp.write(b'\n')  #写入文件结尾
#        time.sleep(1)
    fp.close()

# 分析某一页
def analysisPage(htmlpage, fp):
    soup = BeautifulSoup(htmlpage)   #使用美丽的汤解析文件内容
    count=1 #计数用
    for item in soup.find("div",{"class":"result-list"}).findAll("li"):
        print '********************count:'+str(count)+'******************';
        info = item.find("div",{"class":"info"})
        title_link = info.find('h4') # book total info
        title = title_link.a.text
        print '--------------title-------------------';
        print title


        subtitle_info = info.find("span",{"class":"subtitle"}).findAll("a")
        author_name= subtitle_info[0].text
        book_type = subtitle_info[1].text
        tags_info = info.find("span",{"class":"subtitle"}).findAll("a",{"class":"tags"})
        tags = ''
        for tag_item in tags_info:
            tags = tags+"/"+tag_item.text


        '''
        try: #发现这里会报错，添加错误处理
            tag = subtitle_info[2].text
        except IndexError:
            tag = ''
        '''

        detail = info.find("p",{"class":"detail"}).text

        number = info.find("p",{"class":"number"}).findAll("span")
        number_click = number[0].text
        number_vote = number[1].text
        number_subscribe= number[2].text
        number_upgrade= number[3].text
        number_words= number[4].text


        #写入文件
        fp.write(title)
        fp.write("\t")
        fp.write(author_name)
        fp.write("\t")
        fp.write(book_type)
        fp.write("\t")
        fp.write(tags)
        fp.write("\t")
        fp.write(detail)
        fp.write("\t")
        fp.write(number_click)
        fp.write("\t")
        fp.write(number_vote)
        fp.write("\t")
        fp.write(number_subscribe)
        fp.write("\t")
        fp.write(number_upgrade)
        fp.write("\t")
        fp.write(number_words)
        fp.write("\t")
        fp.write("\n")

        count = count + 1


# 脚本入口
print('Start:')
deal_key()
print('End！')
