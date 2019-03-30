
# coding: utf-8

# In[ ]:


import urllib.request
import time
import blob
import get_average
import csv_splitter
import pandas as pd
import os
import glob
from multiprocessing import Pool
import datetime

#!/usr/bin/python

import sys, getopt


def get_url( name ):
   # Download the file from `url` and save it locally under `file_name`:
   #url='https://finance.yahoo.com/quote/AAPL/analysis'
   url='https://finance.yahoo.com/quote/' + name + '/analysis'
   return url;

def get_peg_from_csv( filename ):
    csv_filename = filename
    print('filename is '+ filename)
    df1 = pd.read_csv(csv_filename)
    data_list = []
    #print(df1)

    for i in range(df1.shape[0]):
        process = "{:.2f}".format( 100.0 * i / df1.shape[0] )
        print(df1.iloc[i,0] + '\t' + process + '%[ i / total = ' + str(i) + ' / ' + str(df1.shape[0]) + ']')
      
        print(df1.iloc[i,0])
        var = df1.iloc[i,0].split("\t")
        print(var)   
       
        code = var[1]
        peg =  var[2]
        print(code,peg)
       # if code != 'BABA':
            #time.sleep( 10 )
        #    continue
        
        full_url = get_url(code)
        current = 0.0
        mean = 0.0
        try:
           
            arr = get_average.get_average_from_url(full_url)
           
            #print('arr=')
            #print(arr)
            current = arr[0]
            mean = arr[1]
            print('current=',current)
            print('mean=',mean)
        except:
            #print ("error message!")
            pass
  

        #time.sleep( 2 )
        #s2 = "{:.2f}".format( current ) # new
        increase = 0
        if current > 0.001:
           increase = 100.0*(mean-current)/current
           increase = "{:.1f}".format( increase ) # new
        data_list.append([code,peg,current,mean,increase])
            #file.write(code + '\t\t' + s2 +'\n') 

    df2 = pd.DataFrame(data_list,columns=['Code','PEG','Current','Mean','Increase'])
    final_df = df2.sort_values(by='Increase')
    #print(final_df)
    name = filename[filename.rfind('/')+1: len(filename)]
    print('name=',name)
    csv_file = './data/ave/ave_' + name
    if os.path.exists(csv_file):
       os.remove(csv_file)
    final_df.to_csv(csv_file, sep='\t', encoding='utf-8')

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
   start = datetime.datetime.now()
   get_peg_from_csv(inputfile)
   end = datetime.datetime.now()
   print ('get_peg_from_csv cost(s)=',(end-start).seconds)

if __name__ == "__main__":
   main(sys.argv[1:])




