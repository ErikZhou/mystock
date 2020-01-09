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

URL = 'https://www.nasdaq.com/market-activity/stocks/qcom/price-earnings-peg-ratios'

COLUMNS = ['code', 'rate']

def get_webpage(code, filename):
    print(filename)
    soup = bs4.BeautifulSoup(open(filename, encoding='utf-8'), "html.parser")
    # print(soup.prettify())
    # page = soup.findAll('div')
    # print(page)
    # table = soup.find("div")  # Find the "table" tag in the page
    # print(table)
    rows = soup.find_all("tr")  # Find all the "tr" tags in the table
    cy_data = []
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
            return (code, peg)


def get_one_year_peg(code):
    peg = ''
    filename = code + '.html'
    file = pathlib.Path(filename)
    if file.exists():
        print("File exist")
    else:
        print("File not exist")
        url = 'https://www.nasdaq.com/market-activity/stocks/' + code + '/price-earnings-peg-ratios'
        save_url_to_file(url, filename)

    ret = get_webpage(code, filename)
    print(ret)
    peg = str(ret[1])
    return peg

def save_url_to_file(url, filename):
    driver = webdriver.Firefox(executable_path='/usr/local/bin/geckodriver')
    get_html = filename  # "test.html"
    # 打开文件，准备写入
    f = open(get_html, 'wb')
    # url = 'http://www.baidu.com'  # 这里填你要保存的网页的网址
    driver.get(url)
    time.sleep(4)  # 保证浏览器响应成功后再进行下一步操作
    # 写入文件
    f.write(driver.page_source.encode("utf-8", "ignore"))  # 忽略非法字符
    print('写入成功')
    # 关闭文件
    f.close()
    return


def main(argv):
    code = ''
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
            code = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
    print('code is "', code)
    #print('Output file is "', outputfile)

    peg = get_one_year_peg(code)
    print('code=', code, ' peg=', peg)


if __name__ == "__main__":
    main(sys.argv[1:])
