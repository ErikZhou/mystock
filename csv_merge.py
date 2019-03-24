
# coding: utf-8

# In[ ]:

import get_peg
import csv_splitter
import pandas as pd
import os
import glob
from multiprocessing import Pool

def f(x):
    return x*x

p = Pool(5)
print(p.map(f, [1, 2, 3]))

# Function definition is here
def printme( str ):
   "This prints a passed string into this function"
   print (str)
   return;

path = './'
extension = 'csv'
os.chdir(path)
result = [i for i in glob.glob('peg_output*.{}'.format(extension))]
#for x in result:
#    print(x)
    #get_peg_from_csv(x)

print('=======')

csv_file = 'out.csv'
if os.path.exists(csv_file):
    # path exists
    os.remove(csv_file)
fout=open(csv_file,"a")
# first file:
for line in open("peg_output_1.csv.csv"):
    fout.write(line)
# now the rest:    
for x in result:
    print(x)
    if(x == 'peg_output_1.csv.csv'):
        continue

    f = open(x)
    next(f) # skip the header
    for line in f:
         fout.write(line)
    f.close() # not really needed
fout.close()



