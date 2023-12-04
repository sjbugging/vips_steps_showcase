#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Step 2, basically collapse the multiple reads to find the longest contig of the VIPs exons

import pandas as pd

genes = pd.read_csv("EnsemblGenes.tsv",sep='\t') #nrows = 10,000
#genes= genes.reset_index()

print( genes.iloc[0,1])


# In[2]:


#genes["chrom"].unique()
len(genes)
genes[204939:]


# In[3]:


IDS = genes["name2"].unique()

len(IDS)
      #  columnstarts = genes.loc[row, genes['name2'] == 'ENSG00000157191']


# In[7]:


def PosPrepDict(df):
    #print(len(df))
    res= {}
    for i in range(len(df)):
        #print(df)
        columnstarts = df.iloc[i ,2].split(",")
        columnstarts = columnstarts[:-1]
        columnends = df.iloc[i, 3].split(",")
        columnends = columnends[:-1]
        #print(columnstarts)
        res1 = {columnstarts[i]: columnends[i] for i in range(len(columnstarts))}
        #print(res1)
        for key in res1:#basically update only if key isnt already found if found compare keys!
            if key in res: #700 810, 700 820
                if res1[key]> res[key]:
                    res.update(res1)
            else:
                res.update(res1)
        #res = res1(list(filter(None, ({key : val for key, val in res1.items() if val}))))
    #print(res)
    return res

    #making each own dictonary and combining -combined dictonary out


# In[8]:


def PosFindStEnd(thisdict):
    import collections
    thisdict2 = collections.OrderedDict(sorted(thisdict.items()))
    listk = list(thisdict2.keys())

    listv = list(thisdict2.values())

    start = []
    end = []
    for i in listk:
                #print(i, thisdict2[i])
                #if the key is the smallest key of the key list (usually the first one)
                if i == min(listk):
                    start.append(i)
                #if the value of the key is the largest value of value list   
                if thisdict2[i] == max(listv) :
                    if len(listk) == 1:
                        start.append(i)
                    end.append(thisdict2[i])
                    return(start,end)
                elif listk[listk.index(i)+1] > thisdict2[i]: #if the next key in the sorted keys > current key value
                    #if the value of the key is already there and its not the first key honestly this is redudant but needed?
                    if listv[listk.index(i)] in end and i != min(listk):
                        if listk[listk.index(i)-1] < listk[listk.index(i)]:
                            start.append(i)
                            end.append(thisdict2[i])
                    else:
                        end.append(thisdict2[i])
                        start.append(listk[listk.index(i)+1])
                    
    return(start,end)
    


# In[9]:


#genes.nunique()["name2"]
IDS = genes["name2"].unique()
#print(len(IDS))
#print(IDS)
step25df = pd.DataFrame(columns = ['EnsemblID', "Chr",'Strand', 'Codons', "totalStart", "totalEnd",'exonStarts', 'exonEnds'])
for i in range(len(IDS)):
    #i = 60233
    #print(i)
    #step25df = pd.DataFrame(columns = ['EnsemblID', 'Strand', 'Codons', 'exonStarts', 'exonEnds'])
    filterIDS = genes.loc[genes['name2'] == IDS[i], ['strand', 'chrom','exonStarts', 'exonEnds','name2']]
    filterIDS.columns = ['strand','chrom','exonStarts', 'exonEnds','name2']
    
    #print(filterIDS)
    codict = PosPrepDict(filterIDS)
    #print(codict)
    findict = PosFindStEnd(codict)
    start = findict[0]
    end = findict[1]
    #print(start)
    #print(min(start))
    #print(end)
    #genes.iloc[i,2]
    codons = len(start)
    step25df = step25df.append({'EnsemblID' : IDS[i] , "Chr": filterIDS.iloc[0,1] ,'Strand' : filterIDS.iloc[0,0] ,'Codons': codons, "totalStart" : min(start), "totalEnd": max(end), 'exonStarts' : ",".join(start), 'exonEnds': ",".join(end)},
        ignore_index = True)
    #break
    #making each own dictonary and combining -combined dictonary out
    #sorting dictonary- sort dictory and subsequent list outcomes
    #Finding start and end outcomes 
    #store in data frame start end and ensembl ID
    
step25df


# In[10]:


#step25df
step25df.to_csv("step25finalfixed.tsv", sep="\t")
#expecting yes, with the first 2,hi again, buye with '8384365', hi with 2, bye with 8384389, hi 7 times? 


# In[2]:




# In[ ]:


#testing

thisdict = {
  700: 710,
  800: 849,
  849: 875,
  850: 900,
}

import collections
thisdict2 = collections.OrderedDict(sorted(thisdict.items()))

first_round = True
start = []
end = []
for key in thisdict2.keys():
    if first_round:
        first = key
        last = thisdict2[key]
        first_round = False
    else:
        if key <= last:
            last = thisdict2[key]
        else:
            start.append(first)
            end.append(last)
            first = key
            last = thisdict2[key]
start.append(first)
end.append(last)


# In[12]:





# In[13]:





# In[ ]:




