import time
import datetime
import requests
import json
import os

bitcoinApiURL = 'https://api.coindesk.com/v1/bpi/currentprice.json'
newsURL = 'https://newsapi.org/v2/everything?q=bitcoin&apiKey='
newsApiKey = '767208745b3048a5b85af0e32c0e5bc1'
bitcoinTimeStep = 5 # minutes
bitCoinPriceFileBase = '~/Downloads/BitcoinPrice/'
newsFolderBase = '~/Downloads/NewsFolder/'

def getCurrentTimeStamp():
    return datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')

def getYearMonthDay():
    timestamp = getCurrentTimeStamp()
    return getCurrentTimeStamp().split(' ')[0].split('-')

def getCurrentFolder():
    yearMonth = '-'.join(getYearMonthDay()[:-1])
    return yearMonth + '/'

def getCurrentBitCoinPriceFile():
    day = getYearMonthDay()[-1]
    return bitCoinPriceFileBase + getCurrentFolder() + day + '.txt'

def getBitcoinPrice():
    response = requests.get(bitcoinApiURL)
    jObj = json.loads(response.text)
    return jObj['bpi']['USD']['rate_float']

def getCurrentNews():
    url = newsURL + newsApiKey
    response = requests.get(bitcoinApiURL)
    return json.loads(response.text)

def writePriceToFile(price, gotNews):
    ''' params:
    gotNews - Boolean: Says if news collection was triggered
    price - float or string: USD price of bitcoin'''
    filename = getCurrentBitCoinPriceFile()
    if not os.path.exists(filename):
        with open(filename, 'w'):
            pass
    with open(filename, 'a') as f:
        currentTimeStamp = getCurrentTimeStamp()
        f.write(','.join([str(currentTimeStamp), str(price), str(gotNews)]))

def getPastPrice(timeToGoBack, currentPrice):
    filename = getCurrentBitCoinPriceFile()
    year, month, day = map(int, getYearMonthDay())
    if

while True:
    try:
        currentPrice = getBitcoinPrice()
