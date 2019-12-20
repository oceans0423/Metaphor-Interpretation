# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 11:09:37 2019

@author: pcy
"""


import pandas as pd                                            
import collections


if __name__ == '__main__':
    data_path = "G:\\poetry metaphor meaning estimate\\training corpus11.xlsx"                                     #文件的绝对路径
    #f = open('userdict2.txt','w+',encoding='utf8')
    

    df = pd.read_excel(data_path)
    filter_df = df[df['sentiment']=='negative']['feature words in poem']
    
    output_str1 = ""
    for item in filter_df.iteritems():
        output_str1 += item[1]+' '
        #f.write(item[1]+'\n')
        
    print(output_str1)
    
    filter_df1 = df[df['sentiment']=='positive']['feature words in poem']
    
    output_str2 = ""
    for item in filter_df1.iteritems():
        if str(item[1]) != 'nan':
            output_str2 += (item[1] + ' ')
            #f.write(item[1]+'\n')
        
        
    print(output_str2)
    #print(len(output_str1.split()))
    #print(len(output_str2.split()))
    
    f = open('userdict2.txt','w+',encoding='utf8')
    
    
    Nn = len(output_str1.split())
    Np = len(output_str2.split())
    Mn = collections.Counter(output_str1.split())
    Mp = collections.Counter(output_str2.split())
    
    
    for i in output_str1.split():
        if i !=' ':
            #print('word %s occurs %d tims'%(i,Mn[i]))
            q=Mn[i]/Nn
            #print('words %s frequency in label Negative is'%(i),q)
        #print(Mn[i])
        
   

    
  