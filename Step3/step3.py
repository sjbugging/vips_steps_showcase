#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#this file is to implement step3
#i have the 20,000 genes now just first combine the ensembl id data to 
#have the strand-exon ends columns in protein coding genes 
#then need to step 4 and that will be to alogithimcally go through
#and find just the phylop scores for the ranges of protein coding genes 
#12/30 going back and doing VIP


# In[5]:


#import step1final.tsv
import pandas as pd

#step1 = pd.read_csv("step1final.tsv",sep='\t')
step1 = pd.read_csv("vipsall.csv")
step25 = pd.read_csv("step25finalfixed.tsv", sep = '\t')
print(len(step1))
len(step25)


# In[13]:


chr22 = step25[step25["Chr"] == "chr22"]
len(chr22)


# In[ ]:


s = pd.Series(list())


# In[14]:


len(step25)


# In[15]:


step1.iloc[0,1]


# In[62]:


#ensemblID, chr, strand, codons, totalStart, totalEnd, exonStarts, exonEnds, Associated Gene Name
step25[:10]


# In[8]:


#count = 0
step3df = pd.DataFrame(columns = ['EnsemblID', "Chr",'Strand', 'Codons', "totalStart", "totalEnd",'exonStarts', 'exonEnds', "Associated Gene Name"])
for i in range(len(step1)):   
    #find step1 in step 25 and add the columns 
    if step1.iloc[i][0] in step25['EnsemblID'].unique():
        index25 = step25.index[step25['EnsemblID'] == step1.iloc[i][0]]
        index25 = list(index25)[0]
        step3df = step3df.append({'EnsemblID' : step1.iloc[i,0] , "Chr": step25.iloc[index25,2] ,'Strand' : step25.iloc[index25,3] ,'Codons': step25.iloc[index25,4], "totalStart" : step25.iloc[index25,5], "totalEnd": step25.iloc[index25,6], 'exonStarts' : step25.iloc[index25,7], 'exonEnds': step25.iloc[index25,8]}, ignore_index = True)
        


# In[9]:


len(step3df)



# In[10]:


step3df["Chr"].unique()
#how many step 1 are in step 25


# In[11]:


step3df.to_csv("step3diseases.tsv", sep="\t")


# In[13]:


step3reg = pd.read_csv("step3fixed.tsv", sep = "\t")


# In[14]:


len(step3reg)


# In[ ]:




