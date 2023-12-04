#!/usr/bin/env python
# coding: utf-8

# In[2]:


#skipping to step 8 of visualization 
#fix 6
import pandas as pd
dictsub = {}
for i in range(1, 5):
    name1 = "chr" + str(i) + "withsub.tsv"
    sub = pd.read_csv(name1, sep='\t', index_col = 0)
    dictsub[i] = len(sub[sub["isSub"] == True])
for i in range(6, 23):
    name1 = "chr" + str(i) + "withsub.tsv"
    sub = pd.read_csv(name1, sep='\t', index_col = 0)
    dictsub[i] = len(sub[sub["isSub"] == True])    


# In[ ]:





# In[108]:


name1 = "chr" + str(3) + "withsub.tsv"
sub = pd.read_csv(name1, sep='\t', index_col = 0)
dictsub[3] = len(sub[sub["isSub"] == True])
#sub[:10]
#dictsub
name1 = "chr" + str(4) + "withsub.tsv"
sub = pd.read_csv(name1, sep='\t', index_col = 0)
dictsub[4] = len(sub[sub["isSub"] == True])


# In[33]:


name = "chr" + str(18) + "withsub.tsv"
chromS = pd.read_csv(name, sep='\t', index_col = 0)
chromS[chromS["isSub"] == True]


# In[148]:


from collections import OrderedDict
x = OrderedDict(sorted(dictsub.items()))
dictsub = dict(x)


# In[3]:


#int_docs_info = {int() : v for k, v in docss_info.items()}
dictsub


# In[40]:


import pandas as pd
name = "step3fixed.tsv"
pract = pd.read_csv(name, sep = "\t")
#print(pract[:10])
#pract = list(pract["EnsemblID"])
#diseases = list(diseases["Ensembl Gene ID"])
diseases = pd.read_csv("vipsall.csv")
#name = "chr" + str(z) +"step4.tsv"
#name= "unsorted-chr1.phyloP100way.wigFix.bed"
#pract = pd.read_csv(name, sep = "\t")
pract1 = list(pract["EnsemblID"])
diseases = list(diseases["Ensembl Gene ID"])
dictcount = {}
for i in pract["Chr"].unique():
    dictcount[str(i)] = 0

for i in diseases:
    if i in pract1:
        ID= pract[pract["EnsemblID"] == i]
        chrome = list(ID["Chr"])
        chrome = chrome[0]
        dictcount[chrome] = dictcount[chrome] + 1


# In[41]:


dictcount.values()


# In[32]:


listchr = ['chr15', 'chr21', 'chr18', 'chr20', 'chr9', 'chr13', 'chr22', 'chr8', 'chrX', 'chr4','chr7',
       'chr3', 'chr14', 'chr17', 'chr12', 'chr2',
       'chr10', 'chr6', 'chr5', 'chr19', 'chr16',
       'chr11', 'chr1', 'chrY']


# In[58]:


dictsub= {"chr1":174,
"chr2":107,
"chr3":118,
"chr4":62,
"chr5":94,
"chr6":79,
"chr7":70,
"chr8":68,
"chr9":79,
"chr10":59,
"chr11":116,
"chr12":121,
"chr13":30,
"chr14":66,
"chr15":53,
"chr16":68,
"chr17":113,
"chr18":21,
"chr19":134,
"chr20":52,
"chr21":19,
"chr22":44,
"chrX":64,
"chrY":1}


# In[64]:


import matplotlib.pyplot as plt
#print(plt.__version__)
def addlabels(x,y):
    for i in range(len(x)):
        plt.text(i, y[i]+3 , y[i], ha = 'center')


names = list(dictsub.keys())
values = list(dictsub.values())
for x in range(len(names)):
    names[x] = str(names[x])
    
plt.bar(range(len(dictsub)), values, tick_label= names, label = values)
#fig = plt.figure()
plt.title('VIP Distribution by Chromesome')
plt.xlabel('Chromesome')
plt.ylabel('# of VIP genes')
addlabels(names, values)
#fig.set_figwidth(10)
#plt.show()
#fig.savefig('sub_chr7_chr22.png')
figure = plt.gcf() # get current figure
figure.set_size_inches(25, 7)

# when saving, specify the DPI
plt.savefig('VIP_allchr.png', dpi = 100)


# In[157]:


#phylo P scores and subsitiutions which are positve which are negative 
dictsub


# In[6]:


dictpostive ={}
for i in range(1, 5):
    name1 = "chr" + str(i) + "withsub.tsv"
    sub = pd.read_csv(name1, sep='\t', index_col = 0)
    sub = sub[sub["isSub"] == True]
    sub = sub[sub["PhyloP"] > 0]
    dictpostive["chr" + str(i)] = len(sub)
for i in range(6, 23):
    name1 = "chr" + str(i) + "withsub.tsv"
    sub = pd.read_csv(name1, sep='\t', index_col = 0)
    sub = sub[sub["isSub"] == True]
    sub = sub[sub["PhyloP"] > 0]
    dictpostive["chr" + str(i)] = len(sub)    


# In[168]:



    


# In[7]:


dictpostive


# In[8]:


dictneg ={}
for i in range(1,5):
    name1 = "chr" + str(i) + "withsub.tsv"
    sub = pd.read_csv(name1, sep='\t', index_col = 0)
    sub = sub[sub["isSub"] == True]
    sub = sub[sub["PhyloP"] < 0]
    dictneg["chr" + str(i)] = len(sub)


# In[9]:


for i in range(6,23):
    name1 = "chr" + str(i) + "withsub.tsv"
    sub = pd.read_csv(name1, sep='\t', index_col = 0)
    sub = sub[sub["isSub"] == True]
    sub = sub[sub["PhyloP"] < 0]
    dictneg["chr" + str(i)] = len(sub)


# In[10]:


dictneg


# In[13]:


#print(plt.__version__)
#import matlab
def addlabelspos(x,y):
    for i in range(len(x)):
        plt.text(i, valuesneg[i] + valuespos[i]/2 , y[i], ha = 'center')
def addlabelsneg(x,y):
    for i in range(len(x)):
        plt.text(i, y[i]/2 , y[i], ha = 'center')


names = list(dictneg.keys())
names1 = list(dictpostive.keys())
valuespos = list(dictpostive.values())
valuesneg = list(dictneg.values())

fig, ax = plt.subplots()

ax.bar(names, valuesneg, label='Negative', color = '#F08080' )
ax.bar(names1, valuespos, bottom= valuesneg, label='Postitive', color = '#00C957' )

plt.title('Number of Subsitutions on Human Branch by Chromesome')
plt.xlabel('Chromesome')
plt.ylabel('# of Subsitutions')
addlabelspos(names, valuespos)
addlabelsneg(names,valuesneg)
ax.legend()
#fig.set_figwidth(10)
#plt.show()
#fig.savefig('sub_chr7_chr22.png')
figure = plt.gcf() # get current figure
figure.set_size_inches(15, 15)
plt.show()
# when saving, specify the DPI
plt.savefig('subPhyloP_chr1_chr23.png', dpi = 100)


# In[13]:


#chromesome 4, disease phylop scores distribution
import pandas as pd
import matplotlib.pyplot as plt
name1 = "chrYwithdisease.tsv"
sub = pd.read_csv(name1, sep='\t', index_col = 0)

#sub = sub[sub["isSub"] == True]
sub = sub[sub["isDisease"] == True]
#sub = sub[sub["PhyloP"] < 0]
#dictneg["chr" + str(i)] = len(sub)
#sub
#len(sub)
sub.hist(column = "PhyloP", bins = 100)
plt.title("Chromesome Y distribution of PhyloP scores")
plt.xlabel("PhyloP scores")
plt.ylabel("# of sites")


# In[ ]:


#phylo total VIP
import pandas as pd
import numpy as n
import matplotlib.pyplot as plt
name1 = "chr13withdisease.tsv"
sub = pd.read_csv(name1, sep='\t', index_col = 0)
sub = sub[sub["isDisease"] == True]
# Random gaussian data.
Ntotal = len(sub)
data = sub["PhyloP"]

# This is  the colormap I'd like to use.
cm = plt.cm.get_cmap('RdYlBu_r')

# Get the histogramp
Y,X = n.histogram(data, 30)
x_span = X.max()-X.min()
C = [cm(((x-X.min())/x_span)) for x in X]

plt.bar(X[:-1],Y,color=C,width=X[1]-X[0])
plt.title("Chromesome Y distribution of PhyloP scores in VIPS")
plt.xlabel("PhyloP scores")
plt.ylabel("# of sites")
plt.show()
#plt.savefig("ChrY_Disease_Histogram_PhyloP.png")


# In[20]:


#phylo total non-vips
import pandas as pd
import numpy as n
import matplotlib.pyplot as plt
name1 = "chrYwithdisease.tsv"
sub = pd.read_csv(name1, sep='\t', index_col = 0)
sub = sub[n.isfinite(sub['isDisease'] == False)]
# Random gaussian data.
Ntotal = len(sub)
print(sub.isnull().sum())
data = sub[n.isfinite(sub['PhyloP'])]
data = data["PhyloP"]
# This is  the colormap I'd like to use.
cm = plt.cm.get_cmap('RdYlBu_r')

# Get the histogramp
Y,X = n.histogram(data, 300)
x_span = X.max()-X.min()
C = [cm(((x-X.min())/x_span)) for x in X]

plt.bar(X[:-1],Y,color=C,width=X[1]-X[0])
plt.title("Chromesome Y distribution of PhyloP scores in Non-VIPS")
plt.xlabel("PhyloP scores")
plt.ylabel("# of sites")
plt.show()
plt.savefig("ChrY_NonVIPs_Histogram_PhyloP.png")


# In[82]:


#box plot of phyloP distribution 
# Import libraries
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

name1 = "chrYwithdisease.tsv"
sub = pd.read_csv(name1, sep='\t', index_col = 0)
sub = sub[np.isfinite(sub['isDisease'] == False)]
# Random gaussian data.
Ntotal = len(sub)
#print(sub.isnull().sum())
data_1 = sub[np.isfinite(sub['PhyloP'])]
data_1 = data_1["PhyloP"]
# Creating dataset
name1 = "chrYwithdisease.tsv"
sub = pd.read_csv(name1, sep='\t', index_col = 0)
sub = sub[sub["isDisease"] == True]
# Random gaussian data.
Ntotal = len(sub)
data_2 = sub["PhyloP"]

data = [data_1, data_2]
print(len(data_1), len(data_2))
fig = plt.figure(figsize =(10, 7))
ax1 = fig.add_subplot(111)
#ax2 = fig.add_subplot(111) 
# Creating axes instance
bp = ax1.boxplot(data, patch_artist = True,
                notch ='True', vert = 0)
#two= ax2.boxplot(data_2, patch_artist = True,
               # notch ='True', vert = 0)


colors = ['#F08080', '#00C957']
 
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)
 

# color and linewidth of
# whiskers
for whisker in bp['whiskers']:
    whisker.set(color ='#8B008B',
                linewidth = 1.5,
                linestyle =":")
 
# changing color and linewidth of
# caps
for cap in bp['caps']:
    cap.set(color ='#8B008B',linewidth = 2)
 
# changing color and linewidth of
# medians
for median in bp['medians']:
    median.set(color ='red',linewidth = 3)
 
# changing style of fliers
for flier in bp['fliers']:
    flier.set(marker ='D', color ='#e7298a',alpha = 0.5)
     
# x-axis labels
#ax.set_yticklabels(['Non-VIPs', 'VIPS'])
plt.yticks(range(3), ["",'Non-VIPs', 'VIPS'], color='black')
plt.xlabel("PhyloP Scores")
#ax.yaxis.set_ticks(data_1) 
#ax.yaxis.set_ticklabels(["Non-VIPs", "VIPS"])
#ax.yticks([1, 2], ['Non-VIPs', 'VIPS'])
# Adding title
plt.title("Y Chromesome PhyloP scores distibution in Non-VIPs and VIPS")
 
# Removing top axes and right axes
# ticks
ax.get_xaxis().tick_bottom()
ax.get_yaxis().tick_left()
     
# show plot
plt.show()
plt.savefig("ChrY_NonVIPs_VIP_boxplot.png")


# In[5]:


#box plot of phyloP distribution 
# Import libraries
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

name1 = "step13withdisease.tsv"
sub = pd.read_csv(name1, sep='\t', index_col = 0)
sub = sub[np.isfinite(sub['isDisease'] == False)]
# Random gaussian data.
Ntotal = len(sub)
#print(sub.isnull().sum())
data_1 = sub[np.isfinite(sub['PhyloP'])]
data_1 = data_1["PhyloP"]
# Creating dataset
name1 = "chrYwithdisease.tsv"
sub = pd.read_csv(name1, sep='\t', index_col = 0)
sub = sub[sub["isDisease"] == True]
# Random gaussian data.
Ntotal = len(sub)
data_2 = sub["PhyloP"]

data = [data_1, data_2]
print(len(data_1), len(data_2))
fig = plt.figure(figsize =(10, 7))
ax = fig.add_subplot(111)
#ax2 = fig.add_subplot(111) 
# Creating axes instance
bp = ax.boxplot(data, patch_artist = True,
                notch ='True', vert = 0)
#two= ax2.boxplot(data_2, patch_artist = True,
               # notch ='True', vert = 0)


colors = ['#F08080', '#00C957']
 
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)
 

# color and linewidth of
# whiskers
for whisker in bp['whiskers']:
    whisker.set(color ='#8B008B',
                linewidth = 1.5,
                linestyle =":")
 
# changing color and linewidth of
# caps
for cap in bp['caps']:
    cap.set(color ='#8B008B',linewidth = 2)
 
# changing color and linewidth of
# medians
for median in bp['medians']:
    median.set(color ='red',linewidth = 3)
 
# changing style of fliers
for flier in bp['fliers']:
    flier.set(marker ='D', color ='#e7298a',alpha = 0.5)
     
# x-axis labels
#ax.set_yticklabels(['Non-VIPs', 'VIPS'])
plt.yticks(range(3), ["",'Non-VIPs', 'VIPS'], color='black')
plt.xlabel("PhyloP Scores")
#ax.yaxis.set_ticks(data_1) 
#ax.yaxis.set_ticklabels(["Non-VIPs", "VIPS"])
#ax.yticks([1, 2], ['Non-VIPs', 'VIPS'])
# Adding title
plt.title("Chromesome 13 PhyloP scores distibution in Non-VIPs and VIPS")
 
# Removing top axes and right axes
# ticks
ax.get_xaxis().tick_bottom()
ax.get_yaxis().tick_left()
     
# show plot
plt.show()
plt.savefig("Chr13_NonVIPs_VIP_boxplot.png")


# In[6]:


#Non-VIP with Sub
#phylo total non-vips
import pandas as pd
import numpy as n
import matplotlib.pyplot as plt
name1 = "step13withdisease.tsv"
sub = pd.read_csv(name1, sep='\t', index_col = 0)
sub = sub[n.isfinite(sub['isDisease'] == False)]
sub= sub[sub["isSub"] == True]
# Random gaussian data.
Ntotal = len(sub)
print(sub.isnull().sum())
data = sub[n.isfinite(sub['PhyloP'])]
data = data["PhyloP"]
# This is  the colormap I'd like to use.
cm = plt.cm.get_cmap('RdYlBu_r')

# Get the histogramp
Y,X = n.histogram(data, 30)
x_span = X.max()-X.min()
C = [cm(((x-X.min())/x_span)) for x in X]

plt.bar(X[:-1],Y,color=C,width=X[1]-X[0])
plt.title("Chromesome 13 distribution of PhyloP scores in Subsitutions of Non-VIPS")
plt.xlabel("PhyloP scores")
plt.ylabel("# of sites")
plt.show()
plt.savefig("Chr13_NonVIPs_SUB_Histogram_PhyloP.png")


# In[8]:


#phylo total VIP + Sub

import numpy as n
import matplotlib.pyplot as plt
import pandas as pd
name1 = "step13withdisease.tsv"
sub = pd.read_csv(name1, sep='\t', index_col = 0)
sub = sub[sub["isDisease"] == True]
sub = sub[sub["isSub"] ==True]
# Random gaussian data.
Ntotal = len(sub)
data = sub["PhyloP"]

# This is  the colormap I'd like to use.
cm = plt.cm.get_cmap('RdYlBu_r')

# Get the histogramp
Y,X = n.histogram(data, 30)
x_span = X.max()-X.min()
C = [cm(((x-X.min())/x_span)) for x in X]

plt.bar(X[:-1],Y,color=C,width=X[1]-X[0])
plt.title("Chromesome 13 distribution of PhyloP scores in VIPS")
plt.xlabel("PhyloP scores")
plt.ylabel("# of sites")
#plt.show()
plt.savefig("Chr13_VIP+Sub_Histogram_PhyloP.png")


# In[26]:


name1 = "step5split.tsv"
step5 = pd.read_csv(name1, sep='\t', index_col = 0)
step5["Chr"].unique()


# In[35]:


listchr = list(step5["Chr"].unique())
dictchr = {}
for i in listchr:
    dictchr[i] = len(step5[step5["Chr"] == i])
dictchr.pop("9")
dictchr.pop("MT")


# In[38]:


import matplotlib.pyplot as plt
#print(plt.__version__)
def addlabels(x,y):
    for i in range(len(x)):
        plt.text(i, y[i]+3 , y[i], ha = 'center')


names = list(dictchr.keys())
values = list(dictchr.values())
for x in range(len(names)):
    names[x] = "chr" + str(names[x])
    
plt.bar(range(len(dictchr)), values, tick_label= names, label = values)
#fig = plt.figure()
plt.title('Subsitution Distribution by Chromesome')
plt.xlabel('Chromesome')
plt.ylabel('# of Substiutions')
addlabels(names, values)
#fig.set_figwidth(10)
#plt.show()
#fig.savefig('sub_chr7_chr22.png')
figure = plt.gcf() # get current figure
figure.set_size_inches(25, 7)
plt.show()
# when saving, specify the DPI
plt.savefig('SUBS_allchr.png', dpi = 100)


# In[39]:


import pandas as pd
from collections import OrderedDict

step55 = pd.read_csv("sub_disease_allchrome.tsv", sep='\t', index_col = 0)
step55 = step55[step55["isDisease"] == True]
listchr = list(step55["Chr"].unique())
print(listchr)
#listchr = list(step55["Chr"].unique())
dictchr = {}
for i in range(1,23):
    dictchr[str(i)] = len(step55[step55["Chr"] == str(i)])
#dictchr.pop("9")
#dictchr.pop("MT")
dictchr["X"] = len(step55[step55["Chr"] == "X"])
dictchr["Y"] = len(step55[step55["Chr"] == "Y"])
#val_list = list(dictchr.values())
#sorted(words.iteritems(), key=lambda x: int(x[1])
#sorted(dictchr.items())
#sorted(int(dictchr.items()), key=lambda x: int(val_list.index(x[1])))
dictchrdisease = dictchr

step55 = pd.read_csv("sub_disease_allchrome.tsv", sep='\t', index_col = 0)
step55 = step55[step55["isDisease"] == False]
listchr = list(step55["Chr"].unique())
print(listchr)
#listchr = list(step55["Chr"].unique())
dictchr = {}
for i in range(1,23):
    dictchr[str(i)] = len(step55[step55["Chr"] == str(i)])
#dictchr.pop("9")
#dictchr.pop("MT")
dictchr["X"] = len(step55[step55["Chr"] == "X"])
dictchr["Y"] = len(step55[step55["Chr"] == "Y"])
dictchromeall = dictchr


# In[40]:


print(dictchrdisease)
print(dictchromeall)


# In[47]:


import matplotlib.pyplot as plt
#print(plt.__version__)
def addlabels(x,y):
    for i in range(len(x)):
        plt.text(i, y[i]+3 , y[i], ha = 'center')


names = list(dictchromeall.keys())
values = list(dictchromeall.values())
for x in range(len(names)):
    names[x] = "chr" + str(names[x])
names1 = list(dictchrdisease.keys())
values1 = list(dictchrdisease.values())
for x in range(len(names1)):
    names1[x] = "chr" + str(names1[x])
    
plt.bar(range(len(dictchromeall)), values, tick_label= names, label = values, color = '#F08080')
plt.bar(range(len(dictchrdisease)), values1, tick_label= names1, label = values1, color = '#00C957')
#fig = plt.figure()
plt.title('Non-VIP and VIP Subsitution Distribution by Chromesome')
plt.xlabel('Chromesome')
plt.ylabel('# of Substiutions')
addlabels(names, values)
addlabels(names1, values1)
#plt.legend(["Non-VIP", "VIP"], loc=0, frameon=legend_drawn_flag)
#fig.set_figwidth(10)
#plt.show()
#fig.savefig('sub_chr7_chr22.png')
figure = plt.gcf() # get current figure
figure.set_size_inches(25, 7)
plt.show()
# when saving, specify the DPI
plt.savefig('SUB_VIP_NON-VIPS_allchr.png', dpi = 100)


# In[ ]:


plt.hist(data, color = "skyblue", lw=0)
bins = numpy.linspace(-10, 10, 100)
import matplotlib.pyplot as plt
#print(plt.__version__)
def addlabels(x,y):
    for i in range(len(x)):
        plt.text(i, y[i]+3 , y[i], ha = 'center')


names = list(dictchr.keys())
values = list(dictchr.values())
for x in range(len(names)):
    names[x] = "chr" + str(names[x])
    
plt.bar(range(len(dictchr)), values, tick_label= names, label = values, color = blue)
#fig = plt.figure()
#plt.title('VIP Subsitution Distribution by Chromesome')
#plt.xlabel('Chromesome')
#plt.ylabel('# of Substiutions')
#addlabels(names, values)
#fig.set_figwidth(10)
#plt.show()
#fig.savefig('sub_chr7_chr22.png')
figure = plt.gcf() # get current figure
figure.set_size_inches(25, 7)
plt.show()
#pyplot.hist(x, bins, alpha=0.5, label='x', color = "blue")
#pyplot.hist(y, bins, alpha=0.5, label='y', color = "red")

