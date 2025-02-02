# -*- coding: utf-8 -*-
"""Preprocessing_Train_Task_1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xvKrq2EICiEBeSfzfstUQ40FlbdpsHVk
"""

import pandas as pd
import pickle
import nltk
import gensim
from gensim.parsing.preprocessing import remove_stopwords
nltk.download('punkt')
import json

labels = {0:"Acute_Threat_Fear",1:"Loss",2:"Arousal",3:"Circadian_Rhythms",4:"Frustrative_Nonreward",5:"Potential_Threat_Anxiety",6:"Sleep_Wakefulness",7:"Sustained_Threat"}

data1 = pd.read_excel(labels[0]+".xlsx")
data2 = pd.read_excel(labels[1]+".xlsx")
data3 = pd.read_excel(labels[2]+".xlsx")
data4 = pd.read_excel(labels[3]+".xlsx")
data5 = pd.read_excel(labels[4]+".xlsx")
data6 = pd.read_excel(labels[5]+".xlsx")
data7 = pd.read_excel(labels[6]+".xlsx")
data8 = pd.read_excel(labels[7]+".xlsx")

data1["Label"] = 0
data2["Label"] = 1
data3["Label"] = 2
data4["Label"] = 3
data5["Label"] = 4
data6["Label"] = 5
data7["Label"] = 6
data8["Label"] = 7

data = pd.concat([data1,data2,data3,data4,data5,data6,data7,data8],ignore_index=True)

for i in range(data.shape[0]):
    for j in range(1,3):
        
        data.iloc[i,j] = data.iloc[i,j].lower()

for i in range(data.shape[0]):
  for j in range(1,3):
    a = nltk.tokenize.sent_tokenize(data.iloc[i,j])
    y = ""
    for x in a:
        y = y+" "+remove_stopwords(x)
    data.iloc[i,j] = y

vocab = {}
l = 1
m = 1
for i in range(data.shape[0]):
    for j in range(1,3):
        a = nltk.tokenize.word_tokenize(data.iloc[i,j])
        for k in a:
            
            if vocab.get(k)==None:
                vocab[k] = l
                l = l+1

jon = json.dumps(vocab)
f = open("vocab.json","w")
f.write(jon)
f.close()

with open("vocab.json") as f:
  vocab = json.load(f)

dat = {}
l2 = []
l1 = []
no = 0
nop = 0
for i in range(data.shape[0]):
    for j in range(1,3):
        a = nltk.tokenize.word_tokenize(data.iloc[i,j])
        for k in a:
            print(k)
            if vocab.get(k)!=None:
                l1.append(vocab.get(k))
                nop = nop+1
            else:
                no = no+1
    
    
    #l2.append(data.iloc[i,5])
    l2.append(data.iloc[i,3])
    l2.append(l1.copy())
    dat[i] = l2.copy()
    l2.clear()
    l1.clear()

f = open("Train_Data.pkl","wb")
pickle.dump(dat,f)
f.close()

vocab

l3 = []
l2 = []
l1 = []
for i in range(data.shape[0]):
    for j in range(1,3):
        a = nltk.tokenize.sent_tokenize(data.iloc[i,j])
        for k in a:
            b = nltk.tokenize.word_tokenize(k)
            l1.append(0)
            for l in b:
                print(l)
                l1.append(vocab.get(l))
            print(l1)
            l2.append(l1.copy())
            l1.clear()
    l3.append(l2.copy())
    l2.clear()

l3

with open('x.pkl', 'wb') as f:
    pickle.dump(l3,f)

l

len(vocab)

