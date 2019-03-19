
# coding: utf-8

# In[ ]:


import urllib.request
import certifi
#import ocr
import ocr_ut
import cvcrop
import blob
import get_peg
import pandas as pd

#certifi.where()
#'/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/certifi/cacert.pem'

pemfile = '/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/certifi/cacert.pem'

# Function definition is here
def printme( str ):
   "This prints a passed string into this function"
   print (str)
   return;

def get_url( name ):
   # Download the file from `url` and save it locally under `file_name`:
   #url='https://www.nasdaq.com//charts/BABA_peg.jpeg'
   url='https://finance.yahoo.com/quote/' + name + '/key-statistics'
   return url;

path = 'stock.txt'
days_file = open(path,'r')
#print (days_file.read())
stock_list = []
#print (days_file.readline())
while True:
    li = days_file.readline()
    if len(li) > 2:      
        #li.replace("\n","")
        li = li[:-1]
        stock_list.append(li)   
    #print(line)
    if not li: 
        break


        # close the file after reading the lines.
days_file.close()
#print(stock_list)
print('my stock count is :')
print(len(stock_list))

#printme('test')
#pow2 = []
file = open("mystock.txt","w")
file_name = "mystock.txt"

data_list = []

for x in range(len(stock_list)):
    code = stock_list[x]
    full_url = get_url(stock_list[x])
    peg = 0.0
    try:
        text = get_peg.get_peg_from_url(full_url)
        peg = float(text.replace(" ", "")) * 1.00
    except:
        print ("error message!")
    s2 = "{:.2f}".format( peg ) # new
    data_list.append([code,float(peg)])
    file.write(code + '\t\t' + s2 +'\n') 

df = pd.DataFrame(data_list,columns=['Code','PEG'])
final_df = df.sort_values(by='PEG')
print(final_df)
final_df.to_csv('peg.csv', sep='\t', encoding='utf-8')

file.close() 
