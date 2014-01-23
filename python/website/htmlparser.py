#获取页面中链接的名称
from HTMLParser import HTMLParser
import urllib
import sys
class parselinks(HTMLParser):
    def __init__(self):
        self.data=[]
        self.href=0
        self.linkname=''
        self.urls = []
        HTMLParser.__init__(self)
    def handle_starttag(self,tag,attrs):
        if tag =='a':
            for name,value in attrs:
                if name == 'href':
                    self.href=1
    def handle_data(self,data):
        if self.href:
            self.linkname+=data
    def handle_endtag(self,tag):
        if tag=='a':
            self.linkname=''.join(self.linkname.split())
            self.linkname=self.linkname.strip()
            if  self.linkname:
                self.data.append(self.linkname)
            self.linkname=''
            self.href=0
    def getresult(self):
        for value in self.data:
            self.urls.append(value)
#            print value
        print self.urls
if __name__=="__main__":
    IParser = parselinks()
    IParser.feed(urllib.urlopen("http://www.python.org/index.html").read())
#    IParser.feed(urllib.urlopen("http://cloudaice.com/").read())
    IParser.getresult()
    IParser.close()
