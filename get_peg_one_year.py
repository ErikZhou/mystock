import getopt
import sys

import bs4  # The most important library for us, see the note below
import requests  # Requests will allow us to access the website via HTTP requests
import urllib.request
import pandas as pd  # A standard tabular data manipulation library
from selenium import webdriver
import time
import os
import pathlib
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = 'https://www.nasdaq.com/market-activity/stocks/qcom/price-earnings-peg-ratios'

COLUMNS = ['code', 'rate']


def get_webpage(code, filename):
    print(filename)
    file = pathlib.Path(filename)
    if file.exists():
        print("File exist")
    else:
        print("File not exist")
        return code, 999

    soup = bs4.BeautifulSoup(open(filename, encoding='utf-8'), "html.parser")
    # print(soup.prettify())
    # page = soup.findAll('div')
    # print(page)
    rows = soup.find_all("tr")  # Find all the "tr" tags in the table
    for row in rows:
        # print(row)
        if str(row).find("Forecast 12 Month Forward PEG Ratio") > 0:
            # print(row)
            cells = row.find_all("td")  # Find all the "td" tags in each row
            print(cells)
            findstr = 'role="cell">'
            index1 = str(cells).find(findstr)
            index2 = str(cells).rfind('</td>')
            peg = str(cells)[index1 + len(findstr):index2]
            # print(cells)
            # print('\n')
            return code, peg
    return code, 999


def get_one_year_peg(code):
    peg = ''
    filename = 'appdata/' + code + '.html'
    file = pathlib.Path(filename)
    if file.exists():
        print("File exist")
    else:
        print("File not exist")
        url = 'https://www.nasdaq.com/market-activity/stocks/' + code + '/price-earnings-peg-ratios'
        save_url_to_file(url, filename)

    ret = get_webpage(code, filename)
    print('ret is ', ret)
    peg = str(ret[1])
    return peg


def save_url_to_file(url, filename):
    driver = webdriver.Firefox(executable_path='/usr/local/bin/geckodriver')
    get_html = filename  # "test.html"
    # noinspection PyBroadException
    try:
        driver.get(url)
        time.sleep(20)  # 保证浏览器响应成功后再进行下一步操作
        f = open(get_html, 'wb')
        f.write(driver.page_source.encode("utf-8", "ignore"))  # 忽略非法字符
        print('写入成功')
        f.close()
    except:
        print('except')
    finally:
        # driver.quit()
        driver.close()
    return


def get_peg_from_csv(filename, thread_index=-1):
    csv_filename = filename
    print('filename is ' + filename)
    df1 = pd.read_csv(csv_filename)
    data_list = []

    for i in range(df1.shape[0]):
        # print(df.iloc[i,0])
        process = "{:.2f}".format(100.0 * i / df1.shape[0])
        log = df1.iloc[i, 0] + '\t' + process + '%[ i / total = ' + str(i) + ' / ' + str(df1.shape[0]) + ']'
        if thread_index >= 0:
            log = 'thread_index\t' + str(thread_index) + '\t' + log
        print(log)

        code = df1.iloc[i, 0]
        peg = 0.0
        if code.find('$') >= 0:
            peg = 887.0

        text = get_one_year_peg(code)
        peg = float(text.replace(" ", "")) * 1.00
        s2 = "{:.2f}".format(peg)  # new
        # if peg > 0.001:
        data_list.append([code, float(peg)])
        # file.write(code + '\t\t' + s2 +'\n')

    df2 = pd.DataFrame(data_list, columns=['Code', 'PEG'])
    final_df = df2.sort_values(by='PEG')
    # print(final_df)
    final_df.to_csv('peg_' + filename + '.csv', sep='\t', encoding='utf-8')
    return


def main(argv):
    inputfile = ''
    outputfile = ''
    try:
        opts, args = getopt.getopt(argv, "hi:o:", ["ifile=", "ofile="])
    except getopt.GetoptError:
        print('test.py -i <inputfile> -o <outputfile>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('test.py -i <inputfile> -o <outputfile>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
    print('Input file is "', inputfile)
    print('Output file is "', outputfile)

    get_peg_from_csv(inputfile, 0)


if __name__ == "__main__":
    main(sys.argv[1:])
