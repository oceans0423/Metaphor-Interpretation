# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 10:45:30 2019

@author: pcy
"""

import pandas as pd                                            
import collections
import jieba
import jieba.analyse





data_path = "G:\\poetry metaphor meaning estimate\\training corpus11.xlsx"



def label(i):
    df = pd.read_excel(data_path)
    filter_df = df[df['Metaphorical meaning']==i]['feature words in poem']
    output_str = ""
    for item in filter_df.iteritems():
        output_str += item[1]+' '
        
        
    #print(len(output_str.split()))
    
    
    return(output_str)
    
    
    
def count_feature_words(i,j): #i是标签 j是单词
    
    featureW = label(i)
    #print(featureW)
    N = len(featureW.split())
    M = collections.Counter(featureW.split())
    
    #print('word %s occurs %d tims'%(j,M[j]))
    q=M[j]/N
    #print('words %s frequency in label %s is'%(j,i),q)
    return(q)
    

def test_in_poem():
    
   # poem_path = "G:\\poetry metaphor meaning estimate\\test 50 corpus.xlsx"
    
   #df = pd.read_excel(poem_path)
    #verse=df.ix[:,['Poem','Verse']].values#读所有poem以及对应诗句
    #print(type(verse))
    #print(verse)
    #sentence = ""
    #for i in range(len(verse)):
        
     #   sentence += verse[i][1]+'\n'
    #print(sentence)
    #seg_sentence = ""
    #jieba.load_userdict('userdict.txt')
    #jieba.set_dictionary(r'C:\Users\pcy\Anaconda3\lib\site-packages\jieba\mydict.txt')
    #f = open('test 50 poem.txt','w+',encoding='utf8')
   
   
    #seg_line = jieba.cut(sentence)
    #print(' '.join(seg_line))
    
    #seg_sentence = ' '.join(seg_line)
   # print(seg_sentence)
    #f.write(seg_sentence)
    f = open('test poem.txt','r+',encoding='utf8')
    featrueW=""
    for line in f.readlines():
        test_poem =[]
        featrue_word = []
        for i in line.split():
            #print(i)
            
            test_poem.append(i)
        #print(test_poem)
        
        
        fword = "" #定义字符串来存放特征词
        for word in open('userdict.txt','r+', encoding='utf8'):
            fword += word+'\n'
            
        fword = ' '.join(set(fword.split()))
        #print(len(fword.split()))
        for word in fword.split():
            featrue_word.append(word)
        #print(featrue_word)
        set_list1 = set(test_poem)
        set_list2 = set(featrue_word)
        featrue_in_test = set_list1&set_list2
        
        
        listtransfor = [str(i) for i in featrue_in_test ]
        
        #featrue_in_test = repr(featrue_in_test)
        featrueW += ' '.join(listtransfor)+'\n'
   # print(featrueW)
    
  
        
   
    return(featrueW)
        
       

    
def calculate():
    Fw = test_in_poem()
    
    #Fw.replace('{','')
    print(Fw)
    strlable = "Frustration,leaving,Lonely,missing,Nostalgia,Sadness,bold-and-unconstrained,Piacevole,Praise,ambition"
   
            
    for line in Fw.splitlines():
        #print(line)
        fq=0.0
        label = ""
        for i in strlable.split(','):
            Q = 0.0
            #print(i)
            for w in line.split():
                #print(w)
                Q += count_feature_words(i,w)
            #print(Q)
                
            if Q >= fq:
                fq = Q
                label=i
                   
        print('label %s frequency is highest:%.8f'%(label,fq))
                
    
    
    
def Title():
     Fw = test_in_poem()
     for i in range(len(Fw)):
            poem_path = "G:\\poetry metaphor meaning estimate\\test corpus.xlsx"
            df = pd.read_excel(poem_path)
            verse=df.ix[:,['Poem','Verse']].values
            
            print(verse[i][0])
            
     
    
                    
                
#strlable = "Frustration,leaving,Lonely,missing,Nostalgia,Sadness,bold-and-unconstrained,Piacevole,Praise,ambition"
#featureWords = ""               
#for i in strlable.split(','):
 #   featureWords += label(i)
#print(len(featureWords.split()))    
#i = 'ambition'
#featureWords = label(i)
    
#frequency_of_featurewords = count_feature_words(i,'万里')
    
#print(featureWords)
    
#test =  test_in_poem()   
test = calculate()   
        
   
