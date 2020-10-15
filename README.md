"""
mystock
999 exception
888 None no such page
887 with $ e.g AMH$D, AMH$E
777 N/A

https://www.barchart.com/stocks/indices/sp/sp100?page=all&viewName=main
https://finance.yahoo.com/quote/aapl/key-statistics
https://www.nasdaq.com/market-activity/stocks/qcom/price-earnings-peg-ratios
"""

## run
./run.sh

## steps

1. python mystock.py
get all code from 
and split into files with 200 for each

2. python pool.py 
using process poll to get peg for each code

3. python csv_merge.py 
merge csv result into one file

4. python csv_sort.py 

## test 
python peg.py -i data/test.csv
python get_peg_one_year.py -i data/test.csv 
