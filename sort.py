
# coding: utf-8

# In[ ]:
import pandas as pd
import os
import sys, getopt
import glob
import re
import time
import datetime


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
    print('shape=',df.shape)
    data_list = []

    for i in range(df.shape[0]):
        line= df.iloc[i,0]
        print('line =', line)
        str_arr = re.split(r'\s+',line)
        Code = str_arr[1]
        print(Code)
        PEG = str_arr[2]
        Current = float(str_arr[3])
        Mean = str_arr[4]
        Increase = float(str_arr[5])
        
        #process = "{:.2f}".format( 100.0 * i / df.shape[0] )
        #print(process)
        #print('i / total = ' + str(i) + ' / ' + str(df.shape[0]))
        
        #ss = re.findall(r'\S+', line)
        #print(ss)
        #peg = 0.0
        #s2 = "{:.2f}".format( peg ) # new
        if Current > 10 and Current < 300 and Increase > 40.0: 
            data_list.append([Code,PEG,Current,Mean,Increase])
            
             
    df = pd.DataFrame(data_list,columns=['Code','PEG','Current','Mean','Increase'])

    final_df = df.sort_values(by='Increase',ascending=False)
    print('shape=',df.shape)
    #print(final_df)
    name = filename[filename.rfind('/')+1: len(filename)]
    print('name=',name)
    csv_file = './data/ave/ave_sort' + name
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
   csv_sort(inputfile)
   end = datetime.datetime.now()
   print ('csv_sort cost(s)=',(end-start).seconds)

if __name__ == "__main__":
   main(sys.argv[1:])


