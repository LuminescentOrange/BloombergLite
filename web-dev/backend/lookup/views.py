from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import *
from .serializers import *
from .alphaVantageApi import *
from .polygonApi import *
from .investpyApi import *
from lookup import serializers

# Create your views here.

@api_view(['GET'])
def getRoutes(request):
    routes = [
        {
            'Endpoint': '/lookup/quarterly_real_gdp/',
            'method': 'GET',
        },
        {
            'Endpoint': '/lookup/annual_real_gdp/',
            'method': 'GET',
        },
        {
            'Endpoint': '/lookup/real_gdp_per_capita/',
            'method': 'GET',
        },
        {
            'Endpoint': '/lookup/daily_3month_treasury_yield/',
            'method': 'GET',
        },
        {
            'Endpoint': '/lookup/weekly_3month_treasury_yield/',
            'method': 'GET',
        },
        {
            'Endpoint': '/lookup/monthly_3month_treasury_yield/',
            'method': 'GET',
        },
        {
            'Endpoint': '/lookup/daily_2year_treasury_yield/',
            'method': 'GET',
        },
        {
            'Endpoint': '/lookup/weekly_2year_treasury_yield/',
            'method': 'GET',
        },
        {
            'Endpoint': '/lookup/monthly_2year_treasury_yield/',
            'method': 'GET',
        },
        {
            'Endpoint': '/lookup/daily_5year_treasury_yield/',
            'method': 'GET',
        },
        {
            'Endpoint': '/lookup/weekly_5year_treasury_yield/',
            'method': 'GET',
        },
        {
            'Endpoint': '/lookup/monthly_5year_treasury_yield/',
            'method': 'GET',
        },
        {
            'Endpoint': '/lookup/daily_7year_treasury_yield/',
            'method': 'GET',
        },
        {
            'Endpoint': '/lookup/weekly_7year_treasury_yield/',
            'method': 'GET',
        },
        {
            'Endpoint': '/lookup/monthly_7year_treasury_yield/',
            'method': 'GET',
        },
        {
            'Endpoint': '/lookup/daily_10year_treasury_yield/',
            'method': 'GET',
        },
        {
            'Endpoint': '/lookup/weekly_10year_treasury_yield/',
            'method': 'GET',
        },
        {
            'Endpoint': '/lookup/monthly_10year_treasury_yield/',
            'method': 'GET',
        },
        {
            'Endpoint': '/lookup/daily_30year_treasury_yield/',
            'method': 'GET',
        },
        {
            'Endpoint': '/lookup/weekly_30year_treasury_yield/',
            'method': 'GET',
        },
        {
            'Endpoint': '/lookup/monthly_30year_treasury_yield/',
            'method': 'GET',
        },
        {
            'Endpoint': '/lookup/daily_federal_funds_rate/',
            'method': 'GET',
        },
        {
            'Endpoint': '/lookup/weekly_federal_funds_rate/',
            'method': 'GET',
        },
        {
            'Endpoint': '/lookup/monthly_federal_funds_rate/',
            'method': 'GET',
        },
        {
            'Endpoint': '/lookup/monthly_cpi/',
            'method': 'GET',
        },
        {
            'Endpoint': '/lookup/semiannual_cpi/',
            'method': 'GET',
        },
        {
            'Endpoint': '/lookup/inflation/',
            'method': 'GET',
        },
        {
            'Endpoint': '/lookup/inflation_expectation/',
            'method': 'GET',
        },
        {
            'Endpoint': '/lookup/consumer_sentiment/',
            'method': 'GET',
        },
        {
            'Endpoint': '/lookup/retail_sales/',
            'method': 'GET',
        },
        {
            'Endpoint': '/lookup/durables/',
            'method': 'GET',
        },
        {
            'Endpoint': '/lookup/unemployment/',
            'method': 'GET',
        },
        {
            'Endpoint': '/lookup/nonfarm_payroll/',
            'method': 'GET',
        },
        {
            'Endpoint': '/lookup/annual_income_statement/:symbol/',
            'method': 'GET',
        },
        {
            'Endpoint': '/lookup/quarterly_income_statement/:symbol/',
            'method': 'GET',
        },
        {
            'Endpoint': '/lookup/annual_balance_sheet/:symbol/',
            'method': 'GET',
        },
        {
            'Endpoint': '/lookup/quarterly_balance_sheet/:symbol/',
            'method': 'GET',
        },
        {
            'Endpoint': '/lookup/annual_cash_flow/:symbol/',
            'method': 'GET',
        },
        {
            'Endpoint': '/lookup/quarterly_cash_flow/:symbol/',
            'method': 'GET',
        },
        {
            'Endpoint': '/lookup/earning/:symbol/',
            'method': 'GET',
        },
        {
            'Endpoint': '/lookup/overview/:symbol/',
            'method': 'GET',
        },
        {
            'Endpoint': '/lookup/earning_calendar/',
            'method': 'GET',
        },
        {
            'Endpoint': '/lookup/earning_calendar/:symbol/',
            'method': 'GET',
        },
        {
            'Endpoint': '/lookup/news/:symbol/',
            'method': 'GET',
        },
        {
            'Endpoint': '/lookup/options_contracts/:symbol/',
            'method': 'GET',
        },
        {
            'Endpoint': '/lookup/single_option_contract/:symbol/:optionID/',
            'method': 'GET',
        },
        {
            'Endpoint': '/lookup/economic_calendar/',
            'method': 'GET',
        },
    ]
    return Response(routes)

@api_view(['GET'])
def getQuarterlyRealGdp(request):
    if Quarterly_Real_GDP.objects.count() == 0:
        data = updateRealGdpFromAPI('quarterly')
        for i in data["data"]:
            record = Quarterly_Real_GDP(date=i["date"], value=i["value"])
            record.save()
    quarterly_real_gdp = Quarterly_Real_GDP.objects.all()
    serializer = Quarterly_Real_GDP_Serializer(quarterly_real_gdp, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getAnnualRealGdp(request):
    if Annual_Real_GDP.objects.count() == 0:
        data = updateRealGdpFromAPI('annual')
        for i in data["data"]:
            record = Annual_Real_GDP(date=i["date"], value=i["value"])
            record.save()
    annual_real_gdp = Annual_Real_GDP.objects.all()
    serializer = Annual_Real_GDP_Serializer(annual_real_gdp, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getRealGdpPerCapita(request):
    if Real_GDP_Per_Capita.objects.count() == 0:
        data = updateRealGdpPerCapitaFromAPI()
        for i in data["data"]:
            record = Real_GDP_Per_Capita(date=i["date"], value=i["value"])
            record.save()
    real_gdp_per_capita = Real_GDP_Per_Capita.objects.all()
    serializer = Real_GDP_Per_Capita_Serializer(real_gdp_per_capita, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getDaily3monthTreasuryYield(request):
    if Daily_3month_Treasury_Yield.objects.count() == 0:
        data = updateTreasuryYieldFromAPI('daily', '3month')
        for i in data["data"]:
            record = Daily_3month_Treasury_Yield(date=i["date"], value=i["value"])
            record.save()
    daily_3month_treasury_yield = Daily_3month_Treasury_Yield.objects.all()
    serializer = Daily_3month_Treasury_Yield_Serializer(daily_3month_treasury_yield, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getWeekly3monthTreasuryYield(request):
    if Weekly_3month_Treasury_Yield.objects.count() == 0:
        data = updateTreasuryYieldFromAPI('weekly', '3month')
        for i in data["data"]:
            record = Weekly_3month_Treasury_Yield(date=i["date"], value=i["value"])
            record.save()
    weekly_3month_treasury_yield = Weekly_3month_Treasury_Yield.objects.all()
    serializer = Weekly_3month_Treasury_Yield_Serializer(weekly_3month_treasury_yield, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getMonthly3monthTreasuryYield(request):
    if Monthly_3month_Treasury_Yield.objects.count() == 0:
        data = updateTreasuryYieldFromAPI('monthly', '3month')
        for i in data["data"]:
            record = Monthly_3month_Treasury_Yield(date=i["date"], value=i["value"])
            record.save()
    monthly_3month_treasury_yield = Monthly_3month_Treasury_Yield.objects.all()
    serializer = Monthly_3month_Treasury_Yield_Serializer(monthly_3month_treasury_yield, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getDaily2yearTreasuryYield(request):
    if Daily_2year_Treasury_Yield.objects.count() == 0:
        data = updateTreasuryYieldFromAPI('daily', '2year')
        for i in data["data"]:
            record = Daily_2year_Treasury_Yield(date=i["date"], value=i["value"])
            record.save()
    daily_2year_treasury_yield = Daily_2year_Treasury_Yield.objects.all()
    serializer = Daily_2year_Treasury_Yield_Serializer(daily_2year_treasury_yield, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getWeekly2yearTreasuryYield(request):
    if Weekly_2year_Treasury_Yield.objects.count() == 0:
        data = updateTreasuryYieldFromAPI('weekly', '2year')
        for i in data["data"]:
            record = Weekly_2year_Treasury_Yield(date=i["date"], value=i["value"])
            record.save()
    weekly_2year_treasury_yield = Weekly_2year_Treasury_Yield.objects.all()
    serializer = Weekly_2year_Treasury_Yield_Serializer(weekly_2year_treasury_yield, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getMonthly2yearTreasuryYield(request):
    if Monthly_2year_Treasury_Yield.objects.count() == 0:
        data = updateTreasuryYieldFromAPI('monthly', '2year')
        for i in data["data"]:
            record = Monthly_2year_Treasury_Yield(date=i["date"], value=i["value"])
            record.save()
    monthly_2year_treasury_yield = Monthly_2year_Treasury_Yield.objects.all()
    serializer = Monthly_2year_Treasury_Yield_Serializer(monthly_2year_treasury_yield, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getDaily5yearTreasuryYield(request):
    if Daily_5year_Treasury_Yield.objects.count() == 0:
        data = updateTreasuryYieldFromAPI('daily', '5year')
        for i in data["data"]:
            record = Daily_5year_Treasury_Yield(date=i["date"], value=i["value"])
            record.save()
    daily_5year_treasury_yield = Daily_5year_Treasury_Yield.objects.all()
    serializer = Daily_5year_Treasury_Yield_Serializer(daily_5year_treasury_yield, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getWeekly5yearTreasuryYield(request):
    if Weekly_5year_Treasury_Yield.objects.count() == 0:
        data = updateTreasuryYieldFromAPI('weekly', '5year')
        for i in data["data"]:
            record = Weekly_5year_Treasury_Yield(date=i["date"], value=i["value"])
            record.save()
    weekly_5year_treasury_yield = Weekly_5year_Treasury_Yield.objects.all()
    serializer = Weekly_5year_Treasury_Yield_Serializer(weekly_5year_treasury_yield, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getMonthly5yearTreasuryYield(request):
    if Monthly_5year_Treasury_Yield.objects.count() == 0:
        data = updateTreasuryYieldFromAPI('monthly', '5year')
        for i in data["data"]:
            record = Monthly_5year_Treasury_Yield(date=i["date"], value=i["value"])
            record.save()
    monthly_5year_treasury_yield = Monthly_5year_Treasury_Yield.objects.all()
    serializer = Monthly_5year_Treasury_Yield_Serializer(monthly_5year_treasury_yield, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getDaily7yearTreasuryYield(request):
    if Daily_7year_Treasury_Yield.objects.count() == 0:
        data = updateTreasuryYieldFromAPI('daily', '7year')
        for i in data["data"]:
            record = Daily_7year_Treasury_Yield(date=i["date"], value=i["value"])
            record.save()
    daily_7year_treasury_yield = Daily_7year_Treasury_Yield.objects.all()
    serializer = Daily_7year_Treasury_Yield_Serializer(daily_7year_treasury_yield, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getWeekly7yearTreasuryYield(request):
    if Weekly_7year_Treasury_Yield.objects.count() == 0:
        data = updateTreasuryYieldFromAPI('weekly', '7year')
        for i in data["data"]:
            record = Weekly_7year_Treasury_Yield(date=i["date"], value=i["value"])
            record.save()
    weekly_7year_treasury_yield = Weekly_7year_Treasury_Yield.objects.all()
    serializer = Weekly_7year_Treasury_Yield_Serializer(weekly_7year_treasury_yield, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getMonthly7yearTreasuryYield(request):
    if Monthly_7year_Treasury_Yield.objects.count() == 0:
        data = updateTreasuryYieldFromAPI('monthly', '7year')
        for i in data["data"]:
            record = Monthly_7year_Treasury_Yield(date=i["date"], value=i["value"])
            record.save()
    monthly_7year_treasury_yield = Monthly_7year_Treasury_Yield.objects.all()
    serializer = Monthly_7year_Treasury_Yield_Serializer(monthly_7year_treasury_yield, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getDaily10yearTreasuryYield(request):
    if Daily_10year_Treasury_Yield.objects.count() == 0:
        data = updateTreasuryYieldFromAPI('daily', '10year')
        for i in data["data"]:
            record = Daily_10year_Treasury_Yield(date=i["date"], value=i["value"])
            record.save()
    daily_10year_treasury_yield = Daily_10year_Treasury_Yield.objects.all()
    serializer = Daily_10year_Treasury_Yield_Serializer(daily_10year_treasury_yield, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getWeekly10yearTreasuryYield(request):
    if Weekly_10year_Treasury_Yield.objects.count() == 0:
        data = updateTreasuryYieldFromAPI('weekly', '10year')
        for i in data["data"]:
            record = Weekly_10year_Treasury_Yield(date=i["date"], value=i["value"])
            record.save()
    weekly_10year_treasury_yield = Weekly_10year_Treasury_Yield.objects.all()
    serializer = Weekly_10year_Treasury_Yield_Serializer(weekly_10year_treasury_yield, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getMonthly10yearTreasuryYield(request):
    if Monthly_10year_Treasury_Yield.objects.count() == 0:
        data = updateTreasuryYieldFromAPI('monthly', '10year')
        for i in data["data"]:
            record = Monthly_10year_Treasury_Yield(date=i["date"], value=i["value"])
            record.save()
    monthly_10year_treasury_yield = Monthly_10year_Treasury_Yield.objects.all()
    serializer = Monthly_10year_Treasury_Yield_Serializer(monthly_10year_treasury_yield, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getDaily30yearTreasuryYield(request):
    if Daily_30year_Treasury_Yield.objects.count() == 0:
        data = updateTreasuryYieldFromAPI('daily', '30year')
        for i in data["data"]:
            record = Daily_30year_Treasury_Yield(date=i["date"], value=i["value"])
            record.save()
    daily_30year_treasury_yield = Daily_30year_Treasury_Yield.objects.all()
    serializer = Daily_30year_Treasury_Yield_Serializer(daily_30year_treasury_yield, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getWeekly30yearTreasuryYield(request):
    if Weekly_30year_Treasury_Yield.objects.count() == 0:
        data = updateTreasuryYieldFromAPI('weekly', '30year')
        for i in data["data"]:
            record = Weekly_30year_Treasury_Yield(date=i["date"], value=i["value"])
            record.save()
    weekly_30year_treasury_yield = Weekly_30year_Treasury_Yield.objects.all()
    serializer = Weekly_30year_Treasury_Yield_Serializer(weekly_30year_treasury_yield, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getMonthly30yearTreasuryYield(request):
    if Monthly_30year_Treasury_Yield.objects.count() == 0:
        data = updateTreasuryYieldFromAPI('monthly', '30year')
        for i in data["data"]:
            record = Monthly_30year_Treasury_Yield(date=i["date"], value=i["value"])
            record.save()
    monthly_30year_treasury_yield = Monthly_30year_Treasury_Yield.objects.all()
    serializer = Monthly_30year_Treasury_Yield_Serializer(monthly_30year_treasury_yield, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getDailyFederalFundsRate(request):
    if Daily_Federal_Funds_Rate.objects.count() == 0:
        data = updateFederalFundsRate('daily')
        for i in data["data"]:
            record = Daily_Federal_Funds_Rate(date=i["date"], value=i["value"])
            record.save()
    daily_federal_funds_rate = Daily_Federal_Funds_Rate.objects.all()
    serializer = Daily_Federal_Funds_Rate_Serializer(daily_federal_funds_rate, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getWeeklyFederalFundsRate(request):
    if Weekly_Federal_Funds_Rate.objects.count() == 0:
        data = updateFederalFundsRate('weekly')
        for i in data["data"]:
            record = Weekly_Federal_Funds_Rate(date=i["date"], value=i["value"])
            record.save()
    weekly_federal_funds_rate = Weekly_Federal_Funds_Rate.objects.all()
    serializer = Weekly_Federal_Funds_Rate_Serializer(weekly_federal_funds_rate, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getMonthlyFederalFundsRate(request):
    if Monthly_Federal_Funds_Rate.objects.count() == 0:
        data = updateFederalFundsRate('monthly')
        for i in data["data"]:
            record = Monthly_Federal_Funds_Rate(date=i["date"], value=i["value"])
            record.save()
    monthly_federal_funds_rate = Monthly_Federal_Funds_Rate.objects.all()
    serializer = Monthly_Federal_Funds_Rate_Serializer(monthly_federal_funds_rate, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getMonthlyCpi(request):
    if Monthly_Cpi.objects.count() == 0:
        data = updateCpiFromAPI("monthly")
        for i in data["data"]:
            record = Monthly_Cpi(date=i["date"], value=i["value"])
            record.save()
    monthly_cpi = Monthly_Cpi.objects.all()
    serializer = Monthly_Cpi_Serializer(monthly_cpi, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getSemiannualCpi(request):
    if Semiannual_Cpi.objects.count() == 0:
        data = updateCpiFromAPI("semiannual")
        for i in data["data"]:
            record = Semiannual_Cpi(date=i["date"], value=i["value"])
            record.save()
    semiannual_cpi = Semiannual_Cpi.objects.all()
    serializer = Semiannual_Cpi_Serializer(semiannual_cpi, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getInflation(request):
    if Inflation.objects.count() == 0:
        data = updateInflationFromAPI()
        for i in data["data"]:
            record = Inflation(date=i["date"], value=i["value"])
            record.save()
    inflation = Inflation.objects.all()
    serializer = Inflation_Serializer(inflation, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getInflationExpectation(request):
    if Inflation_Expectation.objects.count() == 0:
        data = updateInflationExpectationFromAPI()
        for i in data["data"]:
            record = Inflation_Expectation(date=i["date"], value=i["value"])
            record.save()
    inflation_expectation = Inflation_Expectation.objects.all()
    serializer = Inflation_Expectation_Serializer(inflation_expectation, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getConsumerSentiment(request):
    if Consumer_Sentiment.objects.count() == 0:
        data = updateConsumerSentimentFromAPI()
        for i in data["data"]:
            record = Consumer_Sentiment(date=i["date"], value=i["value"])
            record.save()
    consumer_sentiment = Consumer_Sentiment.objects.all()
    serializer = Consumer_Sentiment_Serializer(consumer_sentiment, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getRetailSales(request):
    if Retail_Sales.objects.count() == 0:
        data = updateRetailSalesFromAPI()
        for i in data["data"]:
            record = Retail_Sales(date=i["date"], value=i["value"])
            record.save()
    retail_sales = Retail_Sales.objects.all()
    serializer = Retail_Sales_Serializer(retail_sales, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getDurables(request):
    if Durables.objects.count() == 0:
        data = updateDurablesFromAPI()
        for i in data["data"]:
            record = Durables(date=i["date"], value=i["value"])
            record.save()
    durables = Durables.objects.all()
    serializer = Durables_Serializer(durables, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getUnemployment(request):
    if Unemployment.objects.count() == 0:
        data = updateUnemploymentFromAPI()
        for i in data["data"]:
            record = Unemployment(date=i["date"], value=i["value"])
            record.save()
    unemployment = Unemployment.objects.all()
    serializer = Unemployment_Serializer(unemployment, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getNonfarmPayroll(request):
    if Nonfarm_Payroll.objects.count() == 0:
        data = updateNonfarmPayrollFromAPI()
        for i in data["data"]:
            record = Nonfarm_Payroll(date=i["date"], value=i["value"])
            record.save()
    nonfarm_payroll = Nonfarm_Payroll.objects.all()
    serializer = Nonfarm_Payroll_Serializer(nonfarm_payroll, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getAnnualIncomeStatement(request, pk):
    annual_income_statement = Annual_Income_Statement.objects.filter(symbol=pk)
    if annual_income_statement.count() == 0:
        data = updateIncomeStatementFromAPI(pk)
        for i in data["annualReports"]:
            record = Annual_Income_Statement(
                symbol = pk,
                fiscalDateEnding = i["fiscalDateEnding"],
                reportedCurrency = i["reportedCurrency"],
                grossProfit = i["grossProfit"],
                totalRevenue = i["totalRevenue"],
                costOfRevenue = i["costOfRevenue"],
                costofGoodsAndServicesSold = i["costofGoodsAndServicesSold"],
                operatingIncome = i["operatingIncome"],
                sellingGeneralAndAdministrative = i["sellingGeneralAndAdministrative"],
                researchAndDevelopment = i["researchAndDevelopment"],
                operatingExpenses = i["operatingExpenses"],
                investmentIncomeNet = i["investmentIncomeNet"],
                netInterestIncome = i["netInterestIncome"],
                interestIncome = i["interestIncome"],
                interestExpense = i["interestExpense"],
                nonInterestIncome = i["nonInterestIncome"],
                otherNonOperatingIncome = i["otherNonOperatingIncome"],
                depreciation = i["depreciation"],
                depreciationAndAmortization = i["depreciationAndAmortization"],
                incomeBeforeTax = i["incomeBeforeTax"],
                incomeTaxExpense = i["incomeTaxExpense"],
                interestAndDebtExpense = i["interestAndDebtExpense"],
                netIncomeFromContinuingOperations = i["netIncomeFromContinuingOperations"],
                comprehensiveIncomeNetOfTax = i["comprehensiveIncomeNetOfTax"],
                ebit = i["ebit"],
                ebitda = i["ebitda"],
                netIncome = i["netIncome"]
            )
            record.save()
        annual_income_statement = Annual_Income_Statement.objects.filter(symbol=pk)
    serializer = Annual_Income_Statement_Serializer(annual_income_statement, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getQuarterlyIncomeStatement(request, pk):
    quarterly_income_statement = Quarterly_Income_Statement.objects.filter(symbol=pk)
    if quarterly_income_statement.count() == 0:
        data = updateIncomeStatementFromAPI(pk)
        for i in data["quarterlyReports"]:
            record = Quarterly_Income_Statement(
                symbol = pk,
                fiscalDateEnding = i["fiscalDateEnding"],
                reportedCurrency = i["reportedCurrency"],
                grossProfit = i["grossProfit"],
                totalRevenue = i["totalRevenue"],
                costOfRevenue = i["costOfRevenue"],
                costofGoodsAndServicesSold = i["costofGoodsAndServicesSold"],
                operatingIncome = i["operatingIncome"],
                sellingGeneralAndAdministrative = i["sellingGeneralAndAdministrative"],
                researchAndDevelopment = i["researchAndDevelopment"],
                operatingExpenses = i["operatingExpenses"],
                investmentIncomeNet = i["investmentIncomeNet"],
                netInterestIncome = i["netInterestIncome"],
                interestIncome = i["interestIncome"],
                interestExpense = i["interestExpense"],
                nonInterestIncome = i["nonInterestIncome"],
                otherNonOperatingIncome = i["otherNonOperatingIncome"],
                depreciation = i["depreciation"],
                depreciationAndAmortization = i["depreciationAndAmortization"],
                incomeBeforeTax = i["incomeBeforeTax"],
                incomeTaxExpense = i["incomeTaxExpense"],
                interestAndDebtExpense = i["interestAndDebtExpense"],
                netIncomeFromContinuingOperations = i["netIncomeFromContinuingOperations"],
                comprehensiveIncomeNetOfTax = i["comprehensiveIncomeNetOfTax"],
                ebit = i["ebit"],
                ebitda = i["ebitda"],
                netIncome = i["netIncome"]
            )
            record.save()
        quarterly_income_statement = Quarterly_Income_Statement.objects.filter(symbol=pk)
    serializer = Quarterly_Income_Statement_Serializer(quarterly_income_statement, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getAnnualBalanceSheet(request, pk):
    annual_balance_sheet = Annual_Balance_Sheet.objects.filter(symbol=pk)
    if annual_balance_sheet.count() == 0:
        data = updateBalanceSheetFromAPI(pk)
        for i in data["annualReports"]:
            record = Annual_Balance_Sheet(
                symbol = pk,
                fiscalDateEnding = i["fiscalDateEnding"],
                reportedCurrency = i["reportedCurrency"],
                totalAssets = i["totalAssets"],
                totalCurrentAssets = i["totalCurrentAssets"],
                cashAndCashEquivalentsAtCarryingValue = i["cashAndCashEquivalentsAtCarryingValue"],
                cashAndShortTermInvestments = i["cashAndShortTermInvestments"],
                inventory = i["inventory"],
                currentNetReceivables = i["currentNetReceivables"],
                totalNonCurrentAssets = i["totalNonCurrentAssets"],
                propertyPlantEquipment = i["propertyPlantEquipment"],
                accumulatedDepreciationAmortizationPPE = i["accumulatedDepreciationAmortizationPPE"],
                intangibleAssets = i["intangibleAssets"],
                intangibleAssetsExcludingGoodwill = i["intangibleAssetsExcludingGoodwill"],
                goodwill = i["goodwill"],
                investments = i["investments"],
                longTermInvestments = i["longTermInvestments"],
                shortTermInvestments = i["shortTermInvestments"],
                otherCurrentAssets = i["otherCurrentAssets"],
                otherNonCurrrentAssets = i["otherNonCurrrentAssets"],
                totalLiabilities = i["totalLiabilities"],
                totalCurrentLiabilities = i["totalCurrentLiabilities"],
                currentAccountsPayable = i["currentAccountsPayable"],
                deferredRevenue = i["deferredRevenue"],
                currentDebt = i["currentDebt"],
                shortTermDebt = i["shortTermDebt"],
                totalNonCurrentLiabilities = i["totalNonCurrentLiabilities"],
                capitalLeaseObligations = i["capitalLeaseObligations"],
                longTermDebt = i["longTermDebt"],
                currentLongTermDebt = i["currentLongTermDebt"],
                longTermDebtNoncurrent = i["longTermDebtNoncurrent"],
                shortLongTermDebtTotal = i["shortLongTermDebtTotal"],
                otherCurrentLiabilities = i["otherCurrentLiabilities"],
                otherNonCurrentLiabilities = i["otherNonCurrentLiabilities"],
                totalShareholderEquity = i["totalShareholderEquity"],
                treasuryStock = i["treasuryStock"],
                retainedEarnings = i["retainedEarnings"],
                commonStock = i["commonStock"],
                commonStockSharesOutstanding = ["commonStockSharesOutstanding"]
            )
            record.save()
        annual_balance_sheet = Annual_Balance_Sheet.objects.filter(symbol=pk)
    serializer = Annual_Balance_Sheet_Serializer(annual_balance_sheet, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getQuarterlyBalanceSheet(request, pk):
    quarterly_balance_sheet = Quarterly_Balance_Sheet.objects.filter(symbol=pk)
    if quarterly_balance_sheet.count() == 0:
        data = updateBalanceSheetFromAPI(pk)
        for i in data["quarterlyReports"]:
            record = Quarterly_Balance_Sheet(
                symbol = pk,
                fiscalDateEnding = i["fiscalDateEnding"],
                reportedCurrency = i["reportedCurrency"],
                totalAssets = i["totalAssets"],
                totalCurrentAssets = i["totalCurrentAssets"],
                cashAndCashEquivalentsAtCarryingValue = i["cashAndCashEquivalentsAtCarryingValue"],
                cashAndShortTermInvestments = i["cashAndShortTermInvestments"],
                inventory = i["inventory"],
                currentNetReceivables = i["currentNetReceivables"],
                totalNonCurrentAssets = i["totalNonCurrentAssets"],
                propertyPlantEquipment = i["propertyPlantEquipment"],
                accumulatedDepreciationAmortizationPPE = i["accumulatedDepreciationAmortizationPPE"],
                intangibleAssets = i["intangibleAssets"],
                intangibleAssetsExcludingGoodwill = i["intangibleAssetsExcludingGoodwill"],
                goodwill = i["goodwill"],
                investments = i["investments"],
                longTermInvestments = i["longTermInvestments"],
                shortTermInvestments = i["shortTermInvestments"],
                otherCurrentAssets = i["otherCurrentAssets"],
                otherNonCurrrentAssets = i["otherNonCurrrentAssets"],
                totalLiabilities = i["totalLiabilities"],
                totalCurrentLiabilities = i["totalCurrentLiabilities"],
                currentAccountsPayable = i["currentAccountsPayable"],
                deferredRevenue = i["deferredRevenue"],
                currentDebt = i["currentDebt"],
                shortTermDebt = i["shortTermDebt"],
                totalNonCurrentLiabilities = i["totalNonCurrentLiabilities"],
                capitalLeaseObligations = i["capitalLeaseObligations"],
                longTermDebt = i["longTermDebt"],
                currentLongTermDebt = i["currentLongTermDebt"],
                longTermDebtNoncurrent = i["longTermDebtNoncurrent"],
                shortLongTermDebtTotal = i["shortLongTermDebtTotal"],
                otherCurrentLiabilities = i["otherCurrentLiabilities"],
                otherNonCurrentLiabilities = i["otherNonCurrentLiabilities"],
                totalShareholderEquity = i["totalShareholderEquity"],
                treasuryStock = i["treasuryStock"],
                retainedEarnings = i["retainedEarnings"],
                commonStock = i["commonStock"],
                commonStockSharesOutstanding = ["commonStockSharesOutstanding"]
            )
            record.save()
        quarterly_balance_sheet = Quarterly_Balance_Sheet.objects.filter(symbol=pk)
    serializer = Quarterly_Balance_Sheet_Serializer(quarterly_balance_sheet, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getAnnualCashFlow(request, pk):
    annual_cash_flow = Annual_Cash_Flow.objects.filter(symbol=pk)
    if annual_cash_flow.count() == 0:
        data = updateCashFlowFromAPI(pk)
        for i in data["annualReports"]:
            record = Annual_Cash_Flow(
                symbol = pk,
                fiscalDateEnding = i["fiscalDateEnding"],
                reportedCurrency = i["reportedCurrency"],
                operatingCashflow = i["operatingCashflow"],
                paymentsForOperatingActivities = i["paymentsForOperatingActivities"],
                proceedsFromOperatingActivities = i["proceedsFromOperatingActivities"],
                changeInOperatingLiabilities = i["changeInOperatingLiabilities"],
                changeInOperatingAssets = i["changeInOperatingAssets"],
                depreciationDepletionAndAmortization = i["depreciationDepletionAndAmortization"],
                capitalExpenditures = i["capitalExpenditures"],
                changeInReceivables = i["changeInReceivables"],
                changeInInventory = i["changeInInventory"],
                profitLoss = i["profitLoss"],
                cashflowFromInvestment = i["cashflowFromInvestment"],
                cashflowFromFinancing = i["cashflowFromFinancing"],
                proceedsFromRepaymentsOfShortTermDebt = i["proceedsFromRepaymentsOfShortTermDebt"],
                paymentsForRepurchaseOfCommonStock = i["paymentsForRepurchaseOfCommonStock"],
                paymentsForRepurchaseOfEquity = i["paymentsForRepurchaseOfEquity"],
                paymentsForRepurchaseOfPreferredStock = i["paymentsForRepurchaseOfPreferredStock"],
                dividendPayout = i["dividendPayout"],
                dividendPayoutCommonStock = i["dividendPayoutCommonStock"],
                dividendPayoutPreferredStock = i["dividendPayoutPreferredStock"],
                proceedsFromIssuanceOfCommonStock = i["proceedsFromIssuanceOfCommonStock"],
                proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet = i["proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet"],
                proceedsFromIssuanceOfPreferredStock = i["proceedsFromIssuanceOfPreferredStock"],
                proceedsFromRepurchaseOfEquity = i["proceedsFromRepurchaseOfEquity"],
                proceedsFromSaleOfTreasuryStock = i["proceedsFromSaleOfTreasuryStock"],
                changeInCashAndCashEquivalents = i["changeInCashAndCashEquivalents"],
                changeInExchangeRate = i["changeInExchangeRate"],
                netIncome = i["netIncome"]
            )
            record.save()
        annual_cash_flow = Annual_Cash_Flow.objects.filter(symbol=pk)
    serializer = Annual_Cash_Flow_Serializer(annual_cash_flow, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getQuarterlyCashFlow(request, pk):
    quarterly_cash_flow = Quarterly_Cash_Flow.objects.filter(symbol=pk)
    if quarterly_cash_flow.count() == 0:
        data = updateCashFlowFromAPI(pk)
        for i in data["quarterlyReports"]:
            record = Quarterly_Cash_Flow(
                symbol = pk,
                fiscalDateEnding = i["fiscalDateEnding"],
                reportedCurrency = i["reportedCurrency"],
                operatingCashflow = i["operatingCashflow"],
                paymentsForOperatingActivities = i["paymentsForOperatingActivities"],
                proceedsFromOperatingActivities = i["proceedsFromOperatingActivities"],
                changeInOperatingLiabilities = i["changeInOperatingLiabilities"],
                changeInOperatingAssets = i["changeInOperatingAssets"],
                depreciationDepletionAndAmortization = i["depreciationDepletionAndAmortization"],
                capitalExpenditures = i["capitalExpenditures"],
                changeInReceivables = i["changeInReceivables"],
                changeInInventory = i["changeInInventory"],
                profitLoss = i["profitLoss"],
                cashflowFromInvestment = i["cashflowFromInvestment"],
                cashflowFromFinancing = i["cashflowFromFinancing"],
                proceedsFromRepaymentsOfShortTermDebt = i["proceedsFromRepaymentsOfShortTermDebt"],
                paymentsForRepurchaseOfCommonStock = i["paymentsForRepurchaseOfCommonStock"],
                paymentsForRepurchaseOfEquity = i["paymentsForRepurchaseOfEquity"],
                paymentsForRepurchaseOfPreferredStock = i["paymentsForRepurchaseOfPreferredStock"],
                dividendPayout = i["dividendPayout"],
                dividendPayoutCommonStock = i["dividendPayoutCommonStock"],
                dividendPayoutPreferredStock = i["dividendPayoutPreferredStock"],
                proceedsFromIssuanceOfCommonStock = i["proceedsFromIssuanceOfCommonStock"],
                proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet = i["proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet"],
                proceedsFromIssuanceOfPreferredStock = i["proceedsFromIssuanceOfPreferredStock"],
                proceedsFromRepurchaseOfEquity = i["proceedsFromRepurchaseOfEquity"],
                proceedsFromSaleOfTreasuryStock = i["proceedsFromSaleOfTreasuryStock"],
                changeInCashAndCashEquivalents = i["changeInCashAndCashEquivalents"],
                changeInExchangeRate = i["changeInExchangeRate"],
                netIncome = i["netIncome"]
            )
            record.save()
        quarterly_cash_flow = Quarterly_Cash_Flow.objects.filter(symbol=pk)
    serializer = Quarterly_Cash_Flow_Serializer(quarterly_cash_flow, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getEarning(request, pk):
    earning = Earning.objects.filter(symbol=pk)
    if (earning.count() == 0):
        data = updateEarningFromAPI(pk)
        for i in data["quarterlyEarnings"]:
            symbol = pk
            fiscalDateEnding = i["fiscalDateEnding"]
            reportedEPS = i["reportedEPS"]
            surprise = i["surprise"]
            surprisePercentage = i["surprisePercentage"]
            record = Earning(symbol=symbol, fiscalDateEnding=fiscalDateEnding, reportedEPS=reportedEPS, surprise=surprise, surprisePercentage=surprisePercentage)
            record.save()
        earning = Earning.objects.filter(symbol=pk)
    serializer = Earning_Serializer(earning, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getOverview(request, pk):
    if (Overview.objects.filter(symbol=pk).count() == 0):
        data = updateOverviewFromAPI(pk)
        record = Overview(
            symbol = data['Symbol'],
            assetType = data['AssetType'],
            name = data['Name'],
            description = data['Description'],
            CIK = data['CIK'],
            exchange = data['Exchange'],
            currency = data['Currency'],
            country = data['Country'],
            sector = data['Sector'],
            industry = data['Industry'],
            address = data['Address'],
            fiscalYearEnd = data['FiscalYearEnd'],
            latestQuarter = data['LatestQuarter'],
            marketCapitalization = data['MarketCapitalization'],
            EBITDA = data['EBITDA'],
            PERatio = data['PERatio'],
            PEGRatio = data['PEGRatio'],
            bookValue = data['BookValue'],
            dividendPerShare = data['DividendPerShare'],
            dividendYield = data['DividendYield'],
            EPS = data['EPS'],
            revenuePerShareTTM = data['RevenuePerShareTTM'],
            profitMargin = data['ProfitMargin'],
            operatingMarginTTM = data['OperatingMarginTTM'],
            returnOnAssetsTTM = data['ReturnOnAssetsTTM'],
            returnOnEquityTTM = data['ReturnOnEquityTTM'],
            revenueTTM = data['RevenueTTM'],
            grossProfitTTM = data['GrossProfitTTM'],
            dilutedEPSTTM = data['DilutedEPSTTM'],
            quarterlyEarningsGrowthYOY = data['QuarterlyEarningsGrowthYOY'],
            quarterlyRevenueGrowthYOY = data['QuarterlyRevenueGrowthYOY'],
            analystTargetPrice = data['AnalystTargetPrice'],
            trailingPE = data['TrailingPE'],
            forwardPE = data['ForwardPE'],
            priceToSalesRatioTTM = data['PriceToSalesRatioTTM'],
            priceToBookRatio = data['PriceToBookRatio'],
            EVToRevenue = data['EVToRevenue'],
            EVToEBITDA = data['EVToEBITDA'],
            beta = data['Beta'],
            _52WeekHigh = data['52WeekHigh'],
            _52WeekLow = data['52WeekLow'],
            _50DayMovingAverage = data['50DayMovingAverage'],
            _200DayMovingAverage = data['200DayMovingAverage'],
            sharesOutstanding = data['SharesOutstanding'],
            dividendDate = data['DividendDate'],
            exDividendDate = data['ExDividendDate'],
        )
        record.save()
    overview = Overview.objects.filter(symbol=pk)
    serializer = Overview_Serializer(overview, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getEarningCalendar(request):
    if (Earning_Calendar.objects.all().count() == 0):
        data = updateEarningCalendarFromAPI()
        for i in data:
            record = Earning_Calendar(
                symbol = i[0],
                name = i[1],
                reportDate = i[2],
                fiscalDateEnding = i[3],
                estimate = i[4],
                currency = i[5]
            )
            record.save()
    earning_calendar = Earning_Calendar.objects.all().order_by('reportDate')
    serializer = Earning_Calendar_Serializer(earning_calendar, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getIndividualEarningCalendar(request, pk):
    if (Earning_Calendar.objects.all().count() == 0):
        data = updateEarningCalendarFromAPI()
        for i in data:
            record = Earning_Calendar(
                symbol = i[0],
                name = i[1],
                reportDate = i[2],
                fiscalDateEnding = i[3],
                estimate = i[4],
                currency = i[5]
            )
            record.save()
    earning_calendar = Earning_Calendar.objects.filter(symbol=pk)
    serializer = Earning_Calendar_Serializer(earning_calendar, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getIndividualNews(request, pk):
    news = getNewsFromPolygonAPI(symbol=pk)
    return Response(news)

@api_view(['GET'])
def getOptionsContracts(request, pk):
    optionsContracts = getOptionsContractsFromPolygonAPI(symbol=pk)
    return Response(optionsContracts)

@api_view(['GET'])
def getSingleOptionContract(request, pk1, pk2):
    optionContract = getSingleOptionContractFromPolygonAPI(symbol=pk1, optionID=pk2)
    return Response(optionContract)

@api_view(['GET'])
def getEconomicCalendar(request):
    economicCalendar = getEconomicCalendarFromInvestpyAPI()
    return Response(economicCalendar)