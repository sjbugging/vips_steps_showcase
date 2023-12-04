#!/usr/bin/env python
# coding: utf-8

# In[1]:


#step 6 sub indormation 
import pandas as pd
sub = pd.read_csv("step5split.tsv", sep='\t', dtype = str, index_col = 0)


# In[90]:


sub20 = sub[sub["Chr"] == "8"]
sub20
listsub = list(sub20["Loc"])
listsub[:10]

listsub = [int(i) for i in listsub]
#listsub


# In[4]:


sub[sub["Chr"] == "13"]


# In[15]:


name= "chr13step4.tsv"
ch = pd.read_csv(name, sep='\t', index_col = 0)
sub20 = sub[sub["Chr"] == "13"]
listsub = list(sub20["Loc"])
#listsub = [int(i) for i in listsub]
    #print(ch[:10])
    #listsub = list(sub20["Loc"])
    #print(listsub)
    #print(type(listsub[0]))
    #print(sub20["Loc"])
    #print(type(ch.iloc[0][1]) )
jointsub = []
for z in range(len(ch)):
    if ch.iloc[z][1] in listsub:
        jointsub.append(ch.iloc[z][1])
        
print(jointsub)
ch['isSub'] = False
    #print(len(jointsub))
for x in jointsub:
    row = ch.index[ch["Pos"]== x]
    ch.loc[ch["Pos"]== x, 'isSub' ]= True
        
ch[ch['isSub'] == True]
#name1 = "chr13withsub.tsv"
#ch.to_csv(name1, sep="\t")


# In[28]:


import pandas as pd
name= "chr13step4.tsv"
ch = pd.read_csv(name, sep='\t', index_col = 0)
#print(ch[:10])
sub = pd.read_csv("step5split.tsv", sep='\t', dtype = str, index_col = 0)
sub20 = sub[sub["Chr"] == "13"]
sub20 = sub20.drop_duplicates(subset=["Location" ], keep='first')


# In[49]:


#print(sub20[:10])
type(list(sub20["Loc"])[0])
#print(ch[ch["Pos"] == 100635113 ])


# In[ ]:


listsub = list(sub20["Loc"])
listsub = pd.to_numeric(listsub, downcast='integer')
listchr = list(ch["Pos"])

ch['isSub'] = False

#print(len(jointsub))

    
    
for i in listsub:
    if i in listchr :
        indexc = ch.index[ch['Pos'] == i]
        #rows = ch[ch["Pos"] == i]
        ch.loc[indexc, 'isSub' ]= True
        #print(type(rows))
        #print(rows)
        #break
        
        #for index, row in rows.iterrows():


# In[56]:


#ch[ch["isSub"] == True]
ch.to_csv("chr13withsub", sep="\t")


# In[ ]:




