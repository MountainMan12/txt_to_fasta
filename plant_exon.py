#!/usr/bin/env python
#AUTHOR: Pawan Verma
#Contact: pawan12394@gmail.com
import pandas as pd

df = pd.read_csv('exons_plants.csv', header = 0)
fh = open('exons_seq.fasta','w') #Write to a .fasta file

cols = list(df.columns)
del cols[0] #First element not required 
#Generating a fasta file using columns 2-15 as header info
for i in range(0, len(df.index)):
    header = list(df.iloc[df.index[i],1:len(df.columns)]) 
    #All header elements are seprated by '_' 
    fh.write('>'+''.join(str(x)+'='+str(y)+',' for x,y in zip(cols,header))+'\n')
    #Write FASTA sequence
    fh.write(str(df.iloc[df.index[i], 0])+'\n')

fh.close()




