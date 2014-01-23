#coding=utf8
#crawl.py:
#get_urls():爬取一个html页面上指定模式的url
#get_text():获取一个上的文本信息
from urllib import FancyURLopener
import sys
import re
#from BeautifulSoup import BeautifulSoup,NavigableString,Comment
from bs4 import BeautifulSoup,NavigableString,Comment
import chardet
#from pysqlite2 import dbapi2 as sqlite3


class Myerror(Exception):
     def __init__(self, value):
          self.value = value
          pass
     def __str__(self):
          return repr( "%s" % self.value )

class MyOpener(FancyURLopener):
     version = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11'

class Parser:
     def __init__(self,url):
          self.start_url = url
          try:
               # 编码检测与转换
               myopener = MyOpener()
               html = myopener.open(url).read()
               encoding = chardet.detect(html)['encoding']

               if not encoding:
                    raise Myerror("Sorry,cannot recognize encoding of the page!")
               html = html.decode(encoding,'ignore').encode('utf-8','ignore')
               self.soup = BeautifulSoup( html )
               if not self.soup.html:
                    raise Myerror("[W]Not a html:%s" % url)
          except IOError:
               raise Myerror("[W]cannot open url:%s" % url)

     def __clear(self):
        # 去除comment
        comments = self.soup.findAll(text=lambda text:isinstance(text, Comment))
        [comment.extract() for comment in comments]
          # 去除style,script
        trivals = self.soup.findAll(['script','style'])
        [trival.extract() for trival in trivals]
        # 清楚display:none或文字或font-size: 0px
        # ToDo style="font-size: 0px;
        trivals = self.soup.findAll(style=re.compile(".*((display\s*:\s*none)|(font-size\s*:\s*0)).*"))
        [trival.extract() for trival in trivals]

     # 获取包含word的url
     def get_urls( self,cw,nw ):
          urls = [ a['href'].strip().lower() for a in self.soup.findAll('a') if a.has_key('href')]
          # 过滤url，并去重
          for url in urls:
               if filter_urls(url,cw,nw) and url not in self.urls:
                    self.urls.append(url)
                    pass
               pass
          return urls

     # 返回一个网页内所有的文本
     def get_text( self ):
          self.__clear()
          doc = ''
          ns_list = self.soup.html.findAll(text=True)
          for ns in ns_list:
               ns_str = ns.string.strip()
               if ns_str and not re.match(ur"^(\s|&nbsp;)*$",ns_str):
                    doc += ' %s' % ns_str
                    pass
               pass
          return doc

     def store_urls( self,path,table,urls ):
          con = sqlite3.connect( path )
          for url in urls:
               if not url.startswith('http://'):
                    url = self.start_url[:-1]+url # 只适合http://www.chinakaoyan.com/ + /info形式的
               sql = "insert or ignore into %s (url) values('%s')" % (table,url)
               print sql
               con.execute( sql )
               pass
          con.commit()

# 过滤包含cw,但不包含nw的url
def filter_urls( url,cw,nw ):
     nws = nw.split()
     for nw in nws:
          if url.find(nw)!=-1:
               return False
          pass

     if not url.startswith('http://') and url.find('javascript')==-1 and url.find('mailto')==-1:
     #     return False
          return True
     if (cw and url.find(cw)==-1)  or url.find('mailto')!=-1 or url.find('javascript')!=-1:
          return False

     return True

def get_domain( url ):
    if url.startswith( 'http://' ):
       url = url[7:]
    elif url.startswith( 'https://' ):
       url = url[8:]
       pass

    i = url.find( '/' )
    return url[:i]

if __name__ == "__main__":
    path = "urls.db"               # url保存文件pp
    table = 'mil'#sys.argv[2].strip().lower()        # 存到sqlite中的table
    # change
    url = 'http://junshi.xilu.com/'#'http://mil.news.sina.com.cn/'#'http://mil.qianlong.com/'#http://www.militaryy.cn/html/index.html'#'http://mil.news.sohu.com/'#'http://war.news.163.com/'#'http://news.ifeng.com/mil/'
    cw = 'junshi'#sys.argv[2].strip().lower()        # 要提取的url包含的词
    nw = 'company rss bbs allyes about'                         # 过滤的词

    try:
         url = 'http://tech.sina.com.cn/'
         url = 'http://www.qq.com'
         print "1.parser page:%s" % url
         pr = Parser( url )
         print pr.get_text().encode('utf-8')
         # print "2.extract urls contain:%s, not contain:%s" % (cw,nw)
         # urls = pr.get_urls( cw,nw )
         # print "3.write %d urls to file:%s" % (len(urls),path)
         # pr.store_urls( path,table,urls )
         # print "task is done:)"
    except Myerror,e:
         print e