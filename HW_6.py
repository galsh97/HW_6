#!/usr/bin/env python
# coding: utf-8

# In[101]:


import pandas as pd
import json , requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('LP_destinations.csv',encoding='latin-1')


# In[116]:


df['num_of_words']  = df['Description'].str.split().str.len()


# In[117]:


No_punct_description = [] 
r ="\,.:-;…,"
for line in df['Description']:
    for char in r:
        line = line.replace(char,"")
    No_punct_description.append(line)
df['No_punct_description'] = No_punct_description


# In[118]:



listrest = []
listmue =[]
listbea= []
for index,row in df.iterrows():
    str_count1 = row['Description'].count('restaurant')
    str_count2 = row['Description'].count('museum')
    str_count3 = row['Description'].count('beache')+row['Description'].count('ocean')+row['Description'].count('sea')
    listrest.append(str_count1)
    listmue.append(str_count2)
    listbea.append(str_count3)
df['has_restaurants']=listrest
df['has_museums'] =listmue
df['has_beaches']=listbea


# In[119]:


avg = df['num_of_words'].mean()


# In[122]:



maxindex = df.iloc[df['num_of_words'].idxmax()]


# In[123]:


df.hist('num_of_words')


# In[124]:



plt.scatter(df['has_beaches'], df['has_restaurants'])
plt.xlabel("num of beaches")
plt.ylabel("num of resturants")


# In[126]:


plt.scatter(df['has_museums'], df['has_beaches'])
plt.xlabel("num of museums")
plt.ylabel("num of _beaches")

