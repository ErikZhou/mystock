
# coding: utf-8

# In[ ]:


import urllib.request
import time
import blob
import get_peg
import csv_splitter
import pandas as pd
import os
import glob
from multiprocessing import Pool
#!/usr/bin/python

import sys, getopt


def get_url( name ):
   # Download the file from `url` and save it locally under `file_name`:
   #url='https://www.nasdaq.com//charts/BABA_peg.jpeg'
   url='https://finance.yahoo.com/quote/' + name + '/key-statistics'
   return url;

def get_peg_from_csv( filename ):
    csv_filename = filename
    print('filename is '+ filename)
    df1 = pd.read_csv(csv_filename)
    data_list = []

    for i in range(df1.shape[0]):
        #print(df.iloc[i,0])
        process = "{:.2f}".format( 100.0 * i / df1.shape[0] )
        print(df1.iloc[i,0] + '\t' + process + '%[ i / total = ' + str(i) + ' / ' + str(df1.shape[0]) + ']')
    #if i > 10:
     #   break

        code = df1.iloc[i,0]
       # if code != 'BABA':
            #time.sleep( 10 )
        #    continue
        
        full_url = get_url(code)
        peg = 0.0
        try:
            text = get_peg.get_peg_from_url(full_url)
            peg = float(text.replace(" ", "")) * 1.00
        except:
            #print ("error message!")
            peg = 0.0

        #time.sleep( 2 )
        s2 = "{:.2f}".format( peg ) # new
        #if peg > 0.001:
        data_list.append([code,float(peg)])
            #file.write(code + '\t\t' + s2 +'\n') 

    df2 = pd.DataFrame(data_list,columns=['Code','PEG'])
    final_df = df2.sort_values(by='PEG')
    #print(final_df)
    final_df.to_csv('peg_' + filename + '.csv', sep='\t', encoding='utf-8')

    return;

def main(argv):
   inputfile = ''
   outputfile = ''
   try:
      opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
   except getopt.GetoptError:
      print ('test.py -i <inputfile> -o <outputfile>')
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print ('test.py -i <inputfile> -o <outputfile>')
         sys.exit()
      elif opt in ("-i", "--ifile"):
         inputfile = arg
      elif opt in ("-o", "--ofile"):
         outputfile = arg
   print ('Input file is "', inputfile)
   print ('Output file is "', outputfile)
   get_peg_from_csv(inputfile)

if __name__ == "__main__":
   main(sys.argv[1:])



