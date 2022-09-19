import requests

api_key = "3UyFGzf0pj6LALE6eLtomJF4wB0PtvNj"

def getNewsFromPolygonAPI(symbol):
    url = f'https://api.polygon.io/v2/reference/news?ticker={symbol}&order=desc&limit=25&apiKey={api_key}'
    r = requests.get(url)
    data = r.json()
    return data

def getOptionsContractsFromPolygonAPI(symbol):
    url = f'https://api.polygon.io/v3/reference/options/contracts?underlying_ticker={symbol}&expired=false&order=asc&limit=1000&apiKey={api_key}'
    r = requests.get(url)
    data = r.json()
    return data

def getSingleOptionContractFromPolygonAPI(symbol, optionID):
    url = f'https://api.polygon.io/v3/snapshot/options/{symbol}/{optionID}?apiKey={api_key}'
    r = requests.get(url)
    data = r.json()
    return data
