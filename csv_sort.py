
# coding: utf-8

# In[ ]:
import pandas as pd
import os
import glob
import re
from multiprocessing import Pool


# Function definition is here
def printme( str ):
   "This prints a passed string into this function"
   print (str)
   return;

def csv_sort( filename ):
    csv_file = filename
    df = pd.read_csv(csv_file)
    #print(df)
    print('=======')
    print(df.shape)
    data_list = []
    for i in range(df.shape[0]):
        #print(df.iloc[i,0])
        #process = "{:.2f}".format( 100.0 * i / df.shape[0] )
        #print(process)
        #print('i / total = ' + str(i) + ' / ' + str(df.shape[0]))
        line = df.iloc[i,0]
        ss = re.findall(r'\S+', line)
        #print(ss)
        #peg = 0.0
        #s2 = "{:.2f}".format( peg ) # new
        data_list.append([ss[1],float(ss[2])])
    df = pd.DataFrame(data_list,columns=['Code','PEG'])
    final_df = df.sort_values(by='PEG')
    print(final_df)
    final_df.to_csv('1_peg_' + filename + '.csv', sep='\t', encoding='utf-8')
    return;

csv_file = 'out.csv'
csv_sort(csv_file)


