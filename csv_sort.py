
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
    data_list_0_5 = []
    data_list_0_5_1 = []
    data_list_1_2 = []
    data_list_2 = []
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
        peg = float(ss[2])
        if peg > 0.001:
            data_list.append([ss[1],peg])
            if peg <= 0.5:
                data_list_0_5.append([ss[1],peg])
            elif peg <= 1:
                data_list_0_5_1.append([ss[1],peg])   
            elif peg <= 2:
                data_list_1_2.append([ss[1],peg])  
            else:
                data_list_2.append([ss[1],peg])    
    df = pd.DataFrame(data_list,columns=['Code','PEG'])
    df_0_5 = pd.DataFrame(data_list_0_5,columns=['Code','PEG'])
    df_0_5_1 = pd.DataFrame(data_list_0_5_1,columns=['Code','PEG'])
    df_1_2 = pd.DataFrame(data_list_1_2,columns=['Code','PEG'])
    df_2 = pd.DataFrame(data_list_2,columns=['Code','PEG'])
    final_df = df.sort_values(by='PEG')
    final_df_0_5 = df_0_5.sort_values(by='PEG')
    final_df_0_5_1 = df_0_5_1.sort_values(by='PEG')
    final_df_1_2 = df_1_2.sort_values(by='PEG')
    final_df_2 = df_2.sort_values(by='PEG')
    print(final_df)
    final_df.to_csv('1_peg_' + filename + '.csv', sep='\t', encoding='utf-8')
    final_df_0_5.to_csv('1_peg_' + filename + '_0_5.csv', sep='\t', encoding='utf-8')
    final_df_0_5_1.to_csv('1_peg_' + filename + '_0_5-1.csv', sep='\t', encoding='utf-8')
    final_df_1_2.to_csv('1_peg_' + filename + '_1-2.csv', sep='\t', encoding='utf-8')
    final_df_2.to_csv('1_peg_' + filename + '_2.csv', sep='\t', encoding='utf-8')
    return;

csv_file = 'out.csv'
csv_sort(csv_file)


