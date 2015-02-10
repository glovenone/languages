#coding=utf-8
#Author: http://blog.csdn.net/boksic
import sys,re

reload(sys) 
sys.setdefaultencoding('utf-8')
txt = open('../text','r').read()
wfile=open('result.txt','w')


r = re.compile('[\x80-\xff]+')
m = r.findall(txt)
dict={}
z1 = re.compile('[\x80-\xff]{2}')
z2 = re.compile('[\x80-\xff]{4}')
z3 = re.compile('[\x80-\xff]{6}')
z4 = re.compile('[\x80-\xff]{8}')
for i in m:
    x = i.encode('gb18030')
    i = z1.findall(x)
    #i+= z2.findall(x)
    #i+= z2.findall(x[2:])
    #i+= z3.findall(x)
    #i+= z3.findall(x[2:])
    #i+= z3.findall(x[4:])
    #i+= z4.findall(x)
    #i+= z4.findall(x[2:])
    #i+= z4.findall(x[4:])
    #i+= z4.findall(x[6:])
    for j in i:
        
        if (j in dict):
            dict[j]+=1
        else:
            dict[j]=1
            
            
dict=sorted(dict.items(), key=lambda d:d[1])
for a,b in dict:
    if b>0:
        wfile.write(a+','+str(b)+'\n')
    
    

