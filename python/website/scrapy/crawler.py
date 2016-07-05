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
base_url = 'http://store.steampowered.com/'

def main():
    for i in range(1, 100000):
        page_content = craw(i)
        print page_content
        #如果不是302，则记录id
    

# 函数1 获取网页内容
def craw(num_plus):
    print 'cone on -------------------------------------------'+str(num_plus);
    key_word = base_num + num_plus 
    url = base_url + str(key_word) + '/'
    request = urllib2.Request(url)
    request.add_header('User-Agent', 'Mozilla/5.0')
    html = getUnRedirectUrl('http://steamcommunity.com/app/100000/')
    #html = getUnRedirectUrl('http://store.steampowered.com/app/310950/')
    if (html == 302):
        html = ''
    else:
        html_ori = urllib2.urlopen(request)
        html = html_ori.read()

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




#处理302的页面->不跳转
class RedirctHandler(urllib2.HTTPRedirectHandler):
  """docstring for RedirctHandler"""
#  def http_error_301(self, req, fp, code, msg, headers):
#    pass
  def http_error_302(self, req, fp, code, msg, headers):
    pass
 
def getUnRedirectUrl(url,timeout=10):
  req = urllib2.Request(url)
  debug_handler = urllib2.HTTPHandler(debuglevel = 1)
  opener = urllib2.build_opener(debug_handler, RedirctHandler)
 
  html = None
  response = None
  try:
    response = opener.open(url,timeout=timeout)
    html = response.read()
  except urllib2.URLError as e:
    if hasattr(e, 'code'):
      error_info = e.code
#    elif hasattr(e, 'reason'):
#      error_info = e.reason
  finally:
    if response:
      response.close()
  if html:
    return html
  else:
    return error_info
 

# 脚本入口
print('Start:')
main()
print('End！')

