#!/usr/bin/env python
# coding: utf-8

# In[40]:

#this step took tsv files of all protein coding genes and the ranges and put phylop (1 base evolutionary change) 
#for each base in the gene range, i did this for each chromesome in list chr due to limits of computing power

#Step4
#This will alogrithimically go through and put phylop scores for ranges of protein codin genes
import pandas as pd
#Step 3 is protein coding genes ~18000
step3 = pd.read_csv("step3fixed.tsv",sep='\t')
#The next thing is finding the phyloP
column_names=["chr","start",'end', "id", "phyloP"]
#nrows= 10000
name = "unsorted-chr4.phyloP100way.wigFix.bed"
#name = "hg19total.wig.bed"
single = pd.read_csv(name, sep='\t', comment='t', header=None,  names = column_names, usecols = [0,1,4])


# In[19]:


# In[13]:





# In[23]:


single["chr"].unique()



# In[41]:


listchr = ['chr15', 'chr21', 'chr18', 'chr20', 'chr9', 'chr13', 'chr22', 'chr8', 'chrX', 'chr4','chr7',
       'chr3', 'chr14', 'chr17', 'chr12', 'chr2',
       'chr10', 'chr6', 'chr5', 'chr19', 'chr16',
       'chr11', 'chr1', 'chrY']
#listchr[0]


# In[71]:


#chrn = chromesomefind(21)
#chrn.iloc[0][8].split(",")
print(single.iloc[0][2])
#single[single["start"] == 64063756].iloc[0][2]
#print(single[single["start"] == 10862621].iloc[0][4])


# In[42]:


def findStartEnd(step3start, step3end):
    startindex = single[single["start"] == step3start].index[0]
    endindex = single[single["end"] == step3end].index[0]
    #single.iloc[:,1].where(step3start)
    return startindex, endindex


# In[43]:


def  DictCodon(filterstep3):
    #go through and create dictonary for start paired ends
    dictCodon = {}
    liststarts = filterstep3[7].split(",")
    listends = filterstep3[8].split(",")
    if len(liststarts) != len(listends):
        if len(liststarts) > len(listends):
            liststarts.pop()
        else:
            listends.pop()
    for i in range(len(liststarts)):
        dictCodon[liststarts[i]] = listends[i]
    return dictCodon


# In[44]:


def findPhyloP(start,stop, filterstep3, step4df):
    for p in range(int(start),int(stop)+1):
        try:
            phylop = single[single["start"] == p].iloc[0][2]
            step4df = step4df.append({'Chr' : filterstep3[2] , 'Pos': p ,'PhyloP': phylop, "Strand": filterstep3[3], 'EnsemblID' : filterstep3[1]}, ignore_index = True)
        
        except IndexError:
            step4df = step4df.append({'Chr' : filterstep3[2] , 'Pos': p ,'PhyloP': 'NA', "Strand": filterstep3[3], 'EnsemblID' : filterstep3[1]}, ignore_index = True)
    return step4df



# In[ ]:


#output: create df that has all phylop for all chromesome21 scores
#find phylop = start
#for i in range(start,stop):
#print phylop
#move to after range
step4df = pd.DataFrame(columns = [ "Chr",'Pos','PhyloP', 'Strand','EnsemblID'])

for z in listchr:
    z = "chr4"
    chrn = step3[step3["Chr"]== z]
    for i in range(len(chrn)):
        filterstep3 = chrn.iloc[i,]
        #create a function that makes the stars and ends paired into dictonaries 
        dictcodons = DictCodon(filterstep3)
        #take each pair and create a function that returns all phyloP scores for them 
        for key in dictcodons:
            #find all phyloP scores and positions
            step4df = findPhyloP(key, dictcodons[key], filterstep3, step4df)
        #step4df = findallPhyloP(filterstep3[5], filterstep3[6], filterstep3, step4df)
        #print(step4df)
        #create function that goes through from start to end and looks and stores each codon value
        #break
    step4df.to_csv("chr4step4.tsv", sep="\t")
    break
#step4df.to_csv("chr16step4.tsv", sep="\t")
#the break above allowed me to do it by chromesome due to computing contstraints


# In[38]:





# In[67]:



# In[32]:


step4df.to_csv("chr4step4.tsv", sep="\t")


# In[35]:


step4df["EnsemblID"].isnull().sum()


# In[7]:


len(step4df)


# In[86]:


step4df = pd.DataFrame(columns = [ "Chr",'Pos','PhyloP', 'Strand','EnsemblID'])

for z in listchr:
    z = "chr4"
    chrn = step3[step3["Chr"]== z]
    for i in range(len(chrn)):
        print(type(chrn))
        filterstep3 = chrn.iloc[i,]
    
        #create a function that makes the stars and ends paired into dictonaries 
        dictcodons = DictCodon(filterstep3)
        #print(len(dictcodons))
        #take each pair and create a function that returns all phyloP scores for them 
        for key in dictcodons:
            #find all phyloP scores and positions
            step4df = findPhyloP(key, dictcodons[key], filterstep3, step4df)
        #step4df = findallPhyloP(filterstep3[5], filterstep3[6], filterstep3, step4df)
        #print(step4df)
        #create function that goes through from start to end and looks and stores each codon value
        break
    break
#step4df.to_csv("chr16step4.tsv", sep="\t")


# In[39]:


Y = pd.read_csv("chr4step4.tsv",sep='\t')
Y


# In[ ]:




