#!/usr/local/bin/python
# coding: utf-8
import smtplib
import time
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
import xlrd
import sys
msg = MIMEMultipart()
reload(sys) 
sys.setdefaultencoding('utf-8')
import re
#构造附件1
#att1 = MIMEText(open('hello.py', 'rb').read(), 'base64', 'gb2312')
#att1["Content-Type"] = 'application/octet-stream'
#att1["Content-Disposition"] = 'attachment; filename="卫生巾1.14.xls"'#这里的filename可以任意写，写什么名字，邮件中显示什么名字
#msg.attach(att1)
#构造附件2
#att2 = MIMEText(open('/home/a2bgeek/develop/python/mail.py', 'rb').read(), 'base64', 'gb2312')
#att2["Content-Type"] = 'application/octet-stream'
#att2["Content-Disposition"] = 'attachment; filename="123.txt"'
#msg.attach(att2)
#加邮件头
#strTo = ['glovenone@163.com', 'ly1125bing@163.com']

fname = "ly/resend.xlsx"
bk = xlrd.open_workbook(fname)
shxrange = range(bk.nsheets)
try:
    sh = bk.sheet_by_name("Sheet1")
except:
    print "no sheet in %s named Sheet1" % fname
#获取行数
nrows = sh.nrows
#获取列数
ncols = sh.ncols
print "nrows %d, ncols %d" % (nrows,ncols)
#获取第一行第一列数据 
cell_value = sh.cell_value(1,1)

row_list = []
strToList = []
UserList = []
errorEmail = []
#获取各行数据
for i in range(1,nrows):
    row_data = sh.row_values(i)
    strToList.append(row_data[1])
    UserList.append(row_data[0])

emailFrom = 'fengxiangbiao@okoer.com'
emailPwd = 'okoer098'
#strToList = ['glovenone@163.com', 'ly1125bing@163.com']
timeNow = time.strftime("%Y%m%d--%H%M%S",time.localtime())
error_file_name = 'error_email'+str(timeNow)
error_file = open(error_file_name, 'w')
for i in range(len(strToList)):
#    content = '这是一封测试邮件的内容，请忽略'
    content_0 = open('ly/content.txt')
    content_1 = content_0.read()
#    content_1.replace('test1234test',UserList[i])
    strinfo = re.compile('test1234test')
    content = strinfo.sub(UserList[i],content_1)
    
    msg = MIMEText(content, 'html', 'utf-8')
    msg['from'] = emailFrom
    msg['subject'] = '优恪网卫生巾众筹检测“安全姨妈卫士荣誉证书”'
    strTo = strToList[i]
    msg['to'] = strTo
    #发送邮件
    try:
        server = smtplib.SMTP_SSL()
        server.connect('smtp.exmail.qq.com', 465)
        server.login(emailFrom,emailPwd)
        server.sendmail(msg['from'], strTo ,msg.as_string())
        server.quit()
        print '发送成功'
        print i
        time.sleep(1)
    except Exception, e:
        print str(e)
        print '出错了!'
        print strTo
        error_file.write(strTo+"\n")
error_file.close()

