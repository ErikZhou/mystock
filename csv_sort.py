# coding: utf-8

# In[ ]:
import pandas as pd
import os
import glob
import re
from multiprocessing import Pool


# Function definition is here
def printme(str):
    "This prints a passed string into this function"
    print(str)
    return


def df_to_csv(data_list, filename, rate):
    df = pd.DataFrame(data_list, columns=['Code', 'PEG'])
    final_df = df.sort_values(by='PEG')
    final_df.to_csv('1_peg_' + filename + '_' + str(rate) + '.csv', sep='\t', encoding='utf-8')
    return


def csv_sort(filename):
    csv_file_name = filename
    df = pd.read_csv(csv_file_name)
    # print(df)
    print('=======')
    print(df.shape)
    data_list = []
    data_list_0_5 = []
    data_list_0_5_1 = []
    data_list_1_2 = []
    data_list_2 = []
    data_list_777 = []
    data_list_888 = []
    data_list_999 = []
    for i in range(df.shape[0]):
        # print(df.iloc[i,0])
        # process = "{:.2f}".format( 100.0 * i / df.shape[0] )
        # print(process)
        # print('i / total = ' + str(i) + ' / ' + str(df.shape[0]))
        line = df.iloc[i, 0]
        ss = re.findall(r'\S+', line)
        # print(ss)
        # peg = 0.0
        # s2 = "{:.2f}".format( peg ) # new
        peg = float(ss[2])
        if peg > 0.001:
            data_list.append([ss[1], peg])
            if peg <= 0.5:
                data_list_0_5.append([ss[1], peg])
            elif peg <= 1:
                data_list_0_5_1.append([ss[1], peg])
            elif peg <= 2:
                data_list_1_2.append([ss[1], peg])
            elif peg == 777:
                data_list_777.append([ss[1], peg])
            elif peg == 888:
                data_list_888.append([ss[1], peg])
            elif peg == 999:
                data_list_999.append([ss[1], peg])
            else:
                data_list_2.append([ss[1], peg])
    df_to_csv(data_list, filename, 'all')
    df_to_csv(data_list_0_5, filename, 0.5)
    df_to_csv(data_list_0_5_1, filename, '0.5-1')
    df_to_csv(data_list_1_2, filename, '1-2')
    df_to_csv(data_list_2, filename, '2')
    df_to_csv(data_list_777, filename, 777)
    df_to_csv(data_list_888, filename, 888)
    df_to_csv(data_list_999, filename, 999)
    return


csv_file = 'out.csv'
csv_sort(csv_file)
