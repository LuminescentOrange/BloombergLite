import investpy
from datetime import date
import json

def getEconomicCalendarFromInvestpyAPI():
    r = investpy.economic_calendar(countries=['united states'], from_date=date.today().strftime("%d/%m/%Y"), to_date='31/12/2022')
    js = r.to_json(orient='records')
    data = json.loads(js)
    return data