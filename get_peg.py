import bs4          # The most important library for us, see the note below
import requests     # Requests will allow us to access the website via HTTP requests
import pandas as pd # A standard tabular data manipulation library

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

#if __name__ == "__main__":
def get_peg_from_url(url):
    #print('begin')
    #get_rate(URL)
    page = get_webpage(url)
    data = scrape(page)
    #print(data)
    #start = data.find("Fz(s) Fw(500) Ta(end)")
    #print(start)
    rate = data[-20:]
    #print(rate)
    rate = rate[0:len(rate)-6]
    #print(rate)
    index = rate.rfind('>')
    #print(index)
    #print(len(rate))
    rate = rate[index+1:len(rate)]
    print(rate)
    #print('end')
    return rate;
    
    #print(data.head())
    #print(data)
