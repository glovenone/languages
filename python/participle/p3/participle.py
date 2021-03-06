#!/usr/bin/python
#-*- encoding:utf-8 -*-
import jieba                                                    #导入jieba模块
import sys

def splitSentence(inputFile, outputFile):
    fin = open(inputFile, 'r')                                  #以读的方式打开文件
    fout = open(outputFile, 'w')                                #以写得方式打开文件
    reload(sys)
    sys.setdefaultencoding('utf-8') 
    outDict = {}
    outStr = ''
    for eachLine in fin:
        line = eachLine.strip().decode('utf-8', 'ignore')       #去除每行首尾可能出现的空格，并转为Unicode进行处理
        wordList = list(jieba.cut(line))                        #用结巴分词，对每行内容进行分词
        for word in wordList:
            if word in outDict:
                outDict[word] += 1
            else:
                outDict[word] = 1
        print outDict
        for d,x in outDict.items():
            outStr += d
            outStr += "\t\t\t"
            outStr += str(x)
            outStr += "\n "

#            outStr += ' '
#        fout.write(outStr.strip().encode('utf-8') + '\n')       #将分词好的结果写入到输出文件
    fout.write(outStr)       #将分词好的结果写入到输出文件
    fin.close()
    fout.close()

splitSentence('../text', 'myOutput.txt')
