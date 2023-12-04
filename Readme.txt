Viral Interacting Protein Project:


Goal:
-Retrieve a measure of how conserved particular sites are within  Viral Interacting genes(phyloP scores) versus other protein coding genes, which tells us about the strength of selection 




Workflow of Steps with Project:
Step1: Get all ensembl ID for protein coding genes ENSEMBL, end start and stop by creating a program to retrieve and store the position ranges from Ensembl. Also did it for VIPs.
Output for this file: 
1. Step1final-fixed.tsv
2. Vipsall.csv *currently step 3 is set up for this


Step2: For each protein coding gene get the longest running ranges for exons. 
Files needed to run script: EnsemblGenes.tsv
Script: Step25.py
Output: Step25finalfixed.tsv


Step3: Combine step 1 & 2 so as to get all the protein coding genes ranges of exons and information 
Files needed to run script: vipsall.csv, step25finalfixed.tsv
Script: Step3.py
Output: step3fixed.tsv


Step4: Get  phyloP scores for each base in the exon ranges of Protein coding genes. Incredibly computationally costly. I completed this by separating by chromosome. 
Files needed to run script: step3fixed.tsv, the bed file of each chromosome phyloP score found here
Script: Step4.py
Output: chr(num)step4.tsv (most added)


Step5: convert substitution information file from txt to tsv compatible with program file
Output: step5split.tsv


Step6: Basically went through each base pair in the exons of the protein coding genes and added if it was substitution. This is to show conservation with phyloP
Files needed to run: step5split.tsv
Script: Step6.py
Output: chr(num)withsub.tsv , some chr(num)withdisease.tsv ( chr Y & chr 13  added)


(skipped step 7 because ended up combining with step 6)
Step8: Visualization of Protein coding gene substitutions. 
Files needed to run: all the chr(num)withsub.tsv, chr(num)withdisease.tsv, step3fixed.tsv, vipsall.tsv
Outputs: provided in script and in folder labeled (outputsstep8)


Poster Presentation! VIPposter.pdf