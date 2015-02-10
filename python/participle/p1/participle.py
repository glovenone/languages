# -*- coding: utf-8-*-
import urllib2
import re
import sys
import os


#os.system(cmd)os.system('ls')


doc_no = 1
def start_fun():
        reload(sys)
        sys.setdefaultencoding('utf-8')
        print sys.getdefaultencoding()


def testfun():
        str_test = "http://hao123.com\" class is >china</b>"
        searchstr= re.findall(r'http://(.*?)\"',str_test)
        print searchstr[0]
def split_word(webpage_chinese_file,webpage_chinese_word_file):
        #调用命令行对中文文档进行分词处理
        #os.system('cd splitword && ictclas_demo_c.exe ../'+ webpage_chinese_file + ' ../'+webpage_chinese_word_file )
        os.system(webpage_chinese_file + ' ../'+webpage_chinese_word_file )
def doc_word_count_deal(webpage_chinese_word_file,webpage_all_word_count_docno):
        global doc_no
        word_dicts = dict()


        #1、读取中文分词内容到缓存中
        word_file = open(webpage_chinese_word_file,"r")
        word_buf = word_file.read()
        word_file.close()


        #2、将分词以空格分隔并按/过滤提取分词中文内容和词性，不是名词或者长度小于2的不进行记录
        word_sets =  word_buf.split(' ')
        for i in word_sets:
                print i
                if i == "" :
                    continue
                j = i.index('/')
                #print 'j='+str(j)
                k = i[j+1:j+2]
                i = i[0:j]
                
                
                #print i
                #word_dicts[i]如果不存在KEY则会报KeyError错误
                if len(i) <= 2 or (k != None and k != 'n'):
                        #print 'k='+k
                        continue
                if word_dicts.get(i) == None :
                        word_dicts[i] = 1
                else:
                        word_dicts[i] = word_dicts[i] + 1
        #sorted(word_dicts.viewvalues())
        #list ->word_dicts = [ v for v in sorted(word_dicts.values())]


        #3、将过滤后的中文分词按照出现次数进行排序，将排序好的数据存储到相应的文件中                       
        word_count = open(webpage_all_word_count_docno,'w')
        word_dicts_list = sorted([(v, k) for k, v in word_dicts.items()], reverse=True)
        for i in word_dicts_list:
                print i[1],i[0]
                word_count.write(str(doc_no)+" "+i[1]+" "+str(i[0])+"\n")
        word_count.close()
        doc_no = doc_no + 1
                        
        """
        for i in word_dicts.viewkeys():
                print i,word_dicts[i]
        """        
def get_webpage_china(url_addr,webpage_src_file,webpage_chinese_file):
        #reload( sys )
        #sys.setdefaultencoding('utf-8')
        print sys.getdefaultencoding()
        #1、获取URL地址网页内容，默认为ascii,utf-8编码
        url = url_addr
        content = urllib2.urlopen(url).read()


        #2、打开文件将网页内容写入文件        
        file = open(webpage_src_file,'w')
        file.write(content)
        file.close


        #str=f.read()
        #fp.write(str.encode("utf-8"))
        
        #3、正则匹配获取网页中alert中所对应的内容
        """
        pattern1 = re.findall(r'alert\"(.∗)\"',content)
        for i in pattern1:
                print i
                print 'hello world!\n'


        sub1 = re.sub(r'alert\"(.∗)\"','Hello World!',content)
        """


        #chinaeseStr = re.match(ur".*[\u4e00-\u9fa5]+",content)
        #a="<p class=\"w490\"> 百度知道</p> "
        #(?<=>)[^a-zA-Z0-9_]+(?=<) 正则 ?<=只匹配最前面不进入分组，?=匹配最后不进入分组
        #4、获取网页中文内容
        chinaeseStr= re.findall(ur"[\u4e00-\u9fa5]+",content.decode('utf-8'))
        #5、将中文内容写入文件
        file_chinese = open(webpage_chinese_file,'w')
        for i in chinaeseStr:
                #print i
                file_chinese.write(i.encode('utf-8'))
        file_chinese.close()                
        
def main():
#        url_addr = 'http://192.168.1.170:8000/jsoa/CheckUser.jspx'
        url_addr = 'http://blog.sina.com.cn/s/blog_8bdd25f80101c7te.html'
        webpage_src_file = 'webpage_src_file.txt'
        webpage_chinese_file = 'webpage_chinese_file.txt'
        webpage_chinese_word_file = 'webpage_chinese_word_file.txt'
        webpage_all_word_count_docno = 'webpage_all_word_count_docno.txt'


        get_webpage_china(url_addr,webpage_src_file,webpage_chinese_file)
        split_word(webpage_chinese_file,webpage_chinese_word_file)
        doc_word_count_deal(webpage_chinese_word_file,webpage_all_word_count_docno)


main()    
