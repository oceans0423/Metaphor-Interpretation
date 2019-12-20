# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 14:39:51 2019

@author: pcy
"""





N = open('negative words.txt', 'r+', encoding='utf8')
P = open('positive words.txt', 'r+', encoding='utf8')
f = open('feature words.txt', 'w+', encoding='utf8')
for i in  N.readlines():
    i = i.strip()
    #print(i)
    for line in open('translation seg without stopwords.txt','r+', encoding='utf8'):
        for word in line.split():
            #print(word)
            if i==word:
                print(i)
                f.write(' '.join(line)+i+'\n')
               
             
         
for i in  P.readlines():
    i = i.strip()
    #print(i)
    for line in open('translation seg without stopwords.txt','r+', encoding='utf8'):
        for word in line.split():
            #print(word)
            if i==word:
                print(i)
                f.write(' '.join(line)+i+'\n')
               