import bs4          # The most important library for us, see the note below
import requests     # Requests will allow us to access the website via HTTP requests
import pandas as pd # A standard tabular data manipulation library
from bs4 import BeautifulSoup
import sys 

#https://finance.yahoo.com/quote/AAPL/analysis
URL = 'https://finance.yahoo.com/quote/AAPL/analysis'

def get_webpage(url):
    response = requests.get(url)  #  Get the url
    return bs4.BeautifulSoup(response.text, 'html.parser') #  Turn the url response into a BeautifulSoup object

def get_web(url):
    #print(url)
    soup = get_webpage(url)
    #print(soup.prettify())
    #soup = get_webpage(url)
    #divs = soup.find_all('div') # Find the "table" tag in the page
    #print(divs)
    #print(soup)
    strsoup = str(soup)
    index = strsoup.find("targetMeanPrice" )
    MeanPrice=''
    CurrentPrice=''
    if( index > 0):
        len1 = len('targetMeanPrice":{"raw":')
        MeanPrice = strsoup[index + len1:(index + len1 +40)]
        MeanPrice = MeanPrice[0 : MeanPrice.find(',')]
        print(MeanPrice)

    index = strsoup.find('regularMarketPrice')
    if( index > 0):
        len1 = len('regularMarketPrice":{"raw":')
        CurrentPrice = strsoup[index + len1:(index + len1 +40)]
        CurrentPrice = CurrentPrice[0 : CurrentPrice.find(',')]
        print(CurrentPrice)
    
    print('======')
    cols = [0.0,0.0]
    cols[0] = float(CurrentPrice)
    cols[1] = float(MeanPrice)
    print(cols)
    return cols
    
#if __name__ == "__main__":
def get_average_from_url(url):
    #print('begin')
    print(url)
    #get_rate(URL)
    cols = get_web(url)
    #page = get_webpage(url)
    #print('get_average_from_url end')
    return cols
    
    #print(data.head())
    #print(data)
