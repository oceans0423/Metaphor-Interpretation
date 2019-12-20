# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 16:53:02 2019

@author: pcy
"""

import xlrd  #导入xlrd模块

import jieba
import jieba.analyse
                                                        

class ExcelData():
    def __init__(self,data_path,sheetname):
        self.data_path = 'G:\\poetry metaphor meaning estimate\\training corpus.xlsx'  # excle表格路径，需传入绝对路径
        self.sheetname = "moon"                                 # excle表格内sheet名
        self.data = xlrd.open_workbook(self.data_path)             # 打开excel表格
        self.table = self.data.sheet_by_name(self.sheetname)       # 切换到相应sheet
        self.keys = self.table.row_values(0)                       # 第一行作为key值
        self.rowNum = self.table.nrows                             # 获取表格行数
        self.colNum = self.table.ncols                             # 获取表格列数
        print(self.rowNum)
        print(self.colNum)

    def readExcel(self):
        if self.rowNum<2:
            print("excle内数据行数小于2")
        else:
            L = []                                                 #列表L存放取出的数据
            for i in range(1,self.rowNum):                         #从第二行（数据行）开始取数据
                sheet_data = {}                                    #定义一个字典用来存放对应数据
                                      
                sheet_data[self.keys[4]] = self.table.row_values(i)[4]    #把第i行第j列的值取出赋给第j列的键值，构成字典
                L.append(sheet_data)                               #一行值取完之后（一个字典），追加到L列表中
            print(type(L))
            return L

if __name__ == '__main__':
    data_path = "G:poetry metaphor meaning estimate\\training corpus.xlsx"                                     #文件的绝对路径
    sheetname = "moon"
    get_data = ExcelData(data_path,sheetname)                       #定义get_data对象
    data = get_data.readExcel()
    f = open('translation.txt','w+',encoding='utf8')
    #print(data[0])
    output_str = ""
    for i in range(len(data)):
        output_str += data[i]['translation'] +'\n'
    f.write(output_str)
    print(data)
    
def stopwordslist(stopwords_filepath):  
    stopwords = [line.strip() for line in open(stopwords_filepath, 'r', encoding='utf-8').readlines()]
    stopwords.append('\u3000')
    stopwords.append('\n')
    stopwords.append(' ')
    return stopwords  
 

def segment(userdict_filepath = open("userdict2.txt"), stopwords_filepath = "stopwords.txt"):
    f = open('translation seg.txt','w+',encoding='utf8')
    jieba.load_userdict(userdict_filepath)
    stopwords = stopwordslist("stopwords.txt") # 这里加载停用词的路径
    for line in open('translation.txt',encoding='utf8'):
        seg_list = jieba.cut(line)
        seg_list_without_stopwords = []
        for word in seg_list:
            if word not in stopwords:
                if word !='\t':
                    seg_list_without_stopwords.append(word)
        for word in seg_list_without_stopwords:
            f.write(word)
        f.write('\n')
        
test = segment('userdict2.txt','stopwords.txt')
print(test)
f = open('translation seg without stopwords.txt','w+',encoding='utf8')    
for line in open('translation seg.txt',encoding='utf8'):
    seg = jieba.cut(line)
    f.write(' '.join(seg)+'\n')    

        