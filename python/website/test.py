# -*- coding:utf-8 -*- 
import urllib 
import re 
#主要任务：根据入口页面，先抓取所有链接，然后根据链接抓取对应的页面，保存成文本文件 
class CheckPage(): 
    def __init__(self,domain,num): 
        self.num=num 
        self.domain=domain#域名，暂时只限于某一个域名 
        self.urlList=[]#总的链接列表 
        self.restList=[]#待处理的链接列表 
        self.code=0#处理数量 
    def CheckA(self,url): 
        data=urllib.urlopen(url)#打开网址 
        try: 
            content=data.read()#读取页面 
        except:#进行错误处理 
            return False 
        self.code=self.code+1#处理的页面加１ 
        if(self.restList!=[]): 
            self.restList.remove(url)#把处理过的页面地址从带处理列表中删除 
        filename="D:\\pagers\\"+str(self.code).rjust(5,"0")+".txt"#自动生成文件名 
        f1=open(filename,"w")#用写方式打开文件 
        f1.write(content)#写文件内容 
        f1.close()#关闭文件 
        #用正则表达式提取链接地址 
        p=re.compile('.+?',re.I|re.S) 
        return p.findall(content)#查找所有的链接地址 
     
    def CheckURL(self,content): 
        p=re.compile('(|\'>|>)',re.I|re.S)#提取链接地址 
        m=p.search(content)#查找链接地址 
        if(m!=None): 
            tmpurl=p.search(content).group(3)#如果查找到了，就取出链接地址的组 
        else: 
            tmpurl="" 
        #检查总的列表中是否有相同 
        if(tmpurl!=""): 
            self.CheckSame(tmpurl) 
         
    def CheckSame(self,url): 
        #判断url是否有效，去除javascript和# 
        if(url=="#"):return False 
        if(url.find("mailto:")!=-1 or url.find("(")!=-1):return False#去除邮件链接 
        #排除外链，需要排除包含http://，但不包含域名的 
        if(url.find("http://")!=-1): 
            if(url.find("域名")!=-1): 
                p=re.compile("http://.*?域名",re.I)#如果带http的地址是内链，去掉http，这里需要注意，需要处理不带www的域名 
                p.sub("",url) 
            else: 
                return False#如果是外链，就不处理 
        #暂时不考虑相对路径及父路径，如果是相对路径，需要把当前的url加上，如果是父路径，需要先取得当前的url的上一级 
        #给没有http://的加上，为了下载页面 
        url="http://域名"+url 
        #去除重复的url地址 
        for n in self.urlList: 
            if (url==n): 
                return False 
        self.urlList.append(url)#如果是有效的链接地址，加到列表中 
        self.restList.append(url)
    def GetPage(self,url): 
        if(self.code<10):#限制抓取的页面数量 
            m=self.CheckA(url)#获取链接列表             
            for n in m:                 
                self.CheckURL(n)#对链接地址进行处理             
            return 1         
        else:             
            return 0
         
c=CheckPage("http://cloudaice.com/",0)
c.GetPage("http://cloudaice.com/") 
while(1==1):#无限循环，直到条件满足退出 
    if(c.urlList==[]):break 
    for l in c.restList: 
        if( c.GetPage(l)==0):break 
   
#类中添加方法函数 
    def SaveImage(self,content): 
        p=re.compile('.+?',re.I|re.S) 
        m=p.findall(content) 
        for n in m: 
            p1=re.compile('(|\'>|>)',re.I|re.S) 
            m1=p1.search(n) 
            if(m1!=None): 
                tmp=m1.group(3) 
                url="http://www.pdp.com.cn"+tmp 
                n1=tmp.split("/") 
                urllib.urlretrieve(url,"D:\\pagers\\"+n1[-1]) 
