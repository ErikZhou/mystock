import bs4          # The most important library for us, see the note below
import requests     # Requests will allow us to access the website via HTTP requests
import pandas as pd # A standard tabular data manipulation library
import sys

URL = 'https://money.cnn.com/quote/forecast/forecast.html?symb=SBUX'
URL = 'https://money.cnn.com/quote/forecast/forecast.html?symb=AAPL'
url_pre = 'https://money.cnn.com/quote/forecast/forecast.html?symb='

def get_webpage(url):
    response = requests.get(url)  #  Get the url
    return bs4.BeautifulSoup(response.text, 'html.parser') #  Turn the url response into a BeautifulSoup object

COLUMNS = ['cy-pair', 'rate']


def find_data(mydivs, startkey, endkey):
    start = mydivs.find(startkey)
    span = '%</span>'
    end = mydivs.find(endkey)
    price = '-100'
    print('start=',start)
    #print('end =',end)
    if(start  > 0):
        price = mydivs[start + len(startkey) : end - len(span) - 1]
        print(price)
    return price
    

def scrape(webpage):
    table = webpage.find("div") # Find the "table" tag in the page
    #print(table)
    mydivs = webpage.findAll("div", {"class": "wsod_twoCol"})
    #print(mydivs)
    startkey = 'class="posData">'
    endkey = 'increase from the last price'
    price = '-100'
    price = find_data(str(mydivs), startkey, endkey) 
    if(price == '-100'):
        startkey = 'class="negData">'
        endkey = 'decrease from the last price'
        price = find_data(str(mydivs), startkey, endkey) 
    return price


def get_price_from_url(url):
    page = get_webpage(url)
    #print(page)
    data = scrape(page)
#    if( data == None):
        #return '888' # meanings not found the page

    #rate = data[-20:]
    #print(rate)
    #rate = rate[0:len(rate)-6]
    #print(rate)
    #if(rate.rfind('N/A') > 0):
    #    return '777' # meanings N/A
    print('price return',data)
    return data


def main():
    print("This is the name of the program:", sys.argv[0]) 
    print("Number of elements including the name of the program:", len(sys.argv)) 
    print("Number of elements excluding the name of the program:", (len(sys.argv)-1)) 
    print("Argument List:", str(sys.argv))
    code = sys.argv[1]
    print('code is',code)
    url = url_pre + code
    price = get_price_from_url(url)
    print('=============')
    print('code','\t price')
    print(code,'\t', price)
#test
#get_price_from_url(URL)

if __name__ == "__main__":
    main()
