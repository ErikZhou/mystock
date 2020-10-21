import bs4          # The most important library for us, see the note below
import requests     # Requests will allow us to access the website via HTTP requests
import pandas as pd # A standard tabular data manipulation library

URL = 'https://finance.yahoo.com/quote/fang/key-statistics'
URL = 'https://finance.yahoo.com/quote/aapl/key-statistics'

def get_webpage(url):
    response = requests.get(url)  #  Get the url
    return bs4.BeautifulSoup(response.text, 'html.parser') #  Turn the url response into a BeautifulSoup object

COLUMNS = ['cy-pair', 'rate']

def scrape(webpage):
    table = webpage.find("table") # Find the "table" tag in the page
    rows = table.find_all("tr")  # Find all the "tr" tags in the table
    cy_data = [] 
    for row in rows:
        #print(row)
        cells = row.find_all("td") #  Find all the "td" tags in each row 
        if(str(cells).find("PEG Ratio (5 yr expected)" ) > 0):
            #print(cells)
            #print('\n')
            return str(cells)
        #cells = cells[0:1] # Select the correct columns (1 & 2 as python is 0-indexed)
        #cy_data.append([cell.text for cell in cells]) # For each "td" tag, get the text inside it
    return

def get_rate(url):
    page = requests.get(url).text
    soup = bs4.BeautifulSoup(page, 'lxml')
    ratio = soup.findAll('td', attrs={'class': 'Fz(s) Fw(500) Ta(end)'})
    print (ratio[0].findNextSiblings())
    for row in ratio:
        print(row)


def get_data(data, start_key, end_key, length):
    start = data.find(start_key)
    data1 = data[start+ len(start_key) : start + len(start_key)+ length]
    data2 = ''
    if end_key == '':
        data2 = data1
    else: 
        end = data1.find(end_key)
        data2 = data1[:end]
    #print(data2)
    return data2


#if __name__ == "__main__":
def get_peg_from_url(url):
    #print('begin')
    #get_rate(URL)
    page = get_webpage(url)
    data = scrape(page)
    if( data == None):
        return '888' # meanings not found the page

    #print(data)
    #print('\n')
    start_key = 'Ta(c) Pstart(10px) Miw(60px) Miw(80px)--pnclg Bgc($lv1BgColor)'
    end_key = '</td>'
    data1 = get_data(data, start_key, end_key, 100)

    start_key = '>'
    end_key = ''
    data2 = get_data(data1, start_key, end_key, 100)
    #print(data1)
    rate = data2
    if(rate.rfind('N/A') > 0):
        return '777' # meanings N/A
    print(rate)
    return rate
    
    #print(data.head())
    #print(data)
#unit test
#get_peg_from_url(URL)

