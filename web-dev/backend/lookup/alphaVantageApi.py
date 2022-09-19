import requests
import csv

apikey = 'V8N87BFJBZOF06KM'

def updateRealGdpFromAPI(interval):
    url = f'https://www.alphavantage.co/query?function=REAL_GDP&interval={interval}&apikey={apikey}'
    r = requests.get(url)
    data = r.json()
    return data

def updateRealGdpPerCapitaFromAPI():
    url = 'https://www.alphavantage.co/query?function=REAL_GDP_PER_CAPITA&apikey={apikey}'
    r = requests.get(url)
    data = r.json()
    return data

def updateTreasuryYieldFromAPI(interval, maturity):
    url = f'https://www.alphavantage.co/query?function=TREASURY_YIELD&interval={interval}&maturity={maturity}&apikey={apikey}'
    r = requests.get(url)
    data = r.json()
    return data

def updateFederalFundsRate(interval):
    url = f'https://www.alphavantage.co/query?function=FEDERAL_FUNDS_RATE&interval={interval}&apikey={apikey}'
    r = requests.get(url)
    data = r.json()
    return data

def updateCpiFromAPI(interval):
    url = f'https://www.alphavantage.co/query?function=CPI&interval={interval}&apikey={apikey}'
    r = requests.get(url)
    data = r.json()
    return data

def updateInflationFromAPI():
    url = 'https://www.alphavantage.co/query?function=INFLATION&apikey={apikey}'
    r = requests.get(url)
    data = r.json()
    return data

def updateInflationExpectationFromAPI():
    url = 'https://www.alphavantage.co/query?function=INFLATION_EXPECTATION&apikey={apikey}'
    r = requests.get(url)
    data = r.json()
    return data

def updateConsumerSentimentFromAPI():
    url = 'https://www.alphavantage.co/query?function=CONSUMER_SENTIMENT&apikey={apikey}'
    r = requests.get(url)
    data = r.json()
    return data

def updateRetailSalesFromAPI():
    url = 'https://www.alphavantage.co/query?function=RETAIL_SALES&apikey={apikey}'
    r = requests.get(url)
    data = r.json()
    return data

def updateDurablesFromAPI():
    url = 'https://www.alphavantage.co/query?function=DURABLES&apikey={apikey}'
    r = requests.get(url)
    data = r.json()
    return data

def updateUnemploymentFromAPI():
    url = 'https://www.alphavantage.co/query?function=UNEMPLOYMENT&apikey={apikey}'
    r = requests.get(url)
    data = r.json()
    return data

def updateNonfarmPayrollFromAPI():
    url = 'https://www.alphavantage.co/query?function=NONFARM_PAYROLL&apikey={apikey}'
    r = requests.get(url)
    data = r.json()
    return data

def updateIncomeStatementFromAPI(symbol):
    url = f'https://www.alphavantage.co/query?function=INCOME_STATEMENT&symbol={symbol}&apikey={apikey}'
    r = requests.get(url)
    data = r.json()
    return data

def updateBalanceSheetFromAPI(symbol):
    url = f'https://www.alphavantage.co/query?function=BALANCE_SHEET&symbol={symbol}&apikey={apikey}'
    r = requests.get(url)
    data = r.json()
    return data

def updateCashFlowFromAPI(symbol):
    url = f'https://www.alphavantage.co/query?function=CASH_FLOW&symbol={symbol}&apikey={apikey}'
    r = requests.get(url)
    data = r.json()
    return data

def updateEarningFromAPI(symbol):
    url = f'https://www.alphavantage.co/query?function=EARNINGS&symbol={symbol}&apikey={apikey}'
    r = requests.get(url)
    data = r.json()
    return data

def updateOverviewFromAPI(symbol):
    url = f'https://www.alphavantage.co/query?function=OVERVIEW&symbol={symbol}&apikey={apikey}'
    r = requests.get(url)
    data = r.json()
    return data

def updateEarningCalendarFromAPI():
    CSV_URL = 'https://www.alphavantage.co/query?function=EARNINGS_CALENDAR&horizon=12month&apikey={apikey}'

    with requests.Session() as s:
        download = s.get(CSV_URL)
        decoded_content = download.content.decode('utf-8')
        cr = csv.reader(decoded_content.splitlines(), delimiter=',')
        my_list = list(cr)
        my_list.pop(0)
        return my_list