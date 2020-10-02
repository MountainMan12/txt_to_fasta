#!/usr/bin/env python
#AUTHOR: Pawan Verma
#Contact: pawan12394@gmail.com
import pandas as pd

df = pd.read_csv('exons_plants.csv', header = 0)
fh = open('exons_seq.fasta','w') #Write to a .fasta file


#Generating a fasta file using columns 2-15 as header info
for i in range(0, len(df.index)):
    header = list(df.iloc[df.index[i],1:len(df.columns)]) 
    #All header elements are seprated by '_' 
    fh.write('>'+'_'.join(str(x) for x in header)+'\n')
    #Write FASTA sequence
    fh.write(str(df.iloc[df.index[i], 0])+'\n')

fh.close()




