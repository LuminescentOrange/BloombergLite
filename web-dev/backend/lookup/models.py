from operator import mod
from django.db import models

# Create your models here.

class Quarterly_Real_GDP(models.Model):
    date = models.TextField()
    value = models.TextField()

    def __str__(self):
        return self.date

class Annual_Real_GDP(models.Model):
    date = models.TextField()
    value = models.TextField()

    def __str__(self):
        return self.date

class Real_GDP_Per_Capita(models.Model):
    date = models.TextField()
    value = models.TextField()

    def __str__(self):
        return self.date

class Daily_3month_Treasury_Yield(models.Model):
    date = models.TextField()
    value = models.TextField()

    def __str__(self):
        return self.date

class Weekly_3month_Treasury_Yield(models.Model):
    date = models.TextField()
    value = models.TextField()

    def __str__(self):
        return self.date

class Monthly_3month_Treasury_Yield(models.Model):
    date = models.TextField()
    value = models.TextField()

    def __str__(self):
        return self.date

class Daily_2year_Treasury_Yield(models.Model):
    date = models.TextField()
    value = models.TextField()

    def __str__(self):
        return self.date

class Weekly_2year_Treasury_Yield(models.Model):
    date = models.TextField()
    value = models.TextField()

    def __str__(self):
        return self.date

class Monthly_2year_Treasury_Yield(models.Model):
    date = models.TextField()
    value = models.TextField()

    def __str__(self):
        return self.date

class Daily_5year_Treasury_Yield(models.Model):
    date = models.TextField()
    value = models.TextField()

    def __str__(self):
        return self.date

class Weekly_5year_Treasury_Yield(models.Model):
    date = models.TextField()
    value = models.TextField()

    def __str__(self):
        return self.date

class Monthly_5year_Treasury_Yield(models.Model):
    date = models.TextField()
    value = models.TextField()

    def __str__(self):
        return self.date

class Daily_7year_Treasury_Yield(models.Model):
    date = models.TextField()
    value = models.TextField()

    def __str__(self):
        return self.date

class Weekly_7year_Treasury_Yield(models.Model):
    date = models.TextField()
    value = models.TextField()

    def __str__(self):
        return self.date

class Monthly_7year_Treasury_Yield(models.Model):
    date = models.TextField()
    value = models.TextField()

    def __str__(self):
        return self.date

class Daily_10year_Treasury_Yield(models.Model):
    date = models.TextField()
    value = models.TextField()

    def __str__(self):
        return self.date

class Weekly_10year_Treasury_Yield(models.Model):
    date = models.TextField()
    value = models.TextField()

    def __str__(self):
        return self.date

class Monthly_10year_Treasury_Yield(models.Model):
    date = models.TextField()
    value = models.TextField()

    def __str__(self):
        return self.date

class Daily_30year_Treasury_Yield(models.Model):
    date = models.TextField()
    value = models.TextField()

    def __str__(self):
        return self.date

class Weekly_30year_Treasury_Yield(models.Model):
    date = models.TextField()
    value = models.TextField()

    def __str__(self):
        return self.date

class Monthly_30year_Treasury_Yield(models.Model):
    date = models.TextField()
    value = models.TextField()

    def __str__(self):
        return self.date

class Daily_Federal_Funds_Rate(models.Model):
    date = models.TextField()
    value = models.TextField()

    def __str__(self):
        return self.date

class Weekly_Federal_Funds_Rate(models.Model):
    date = models.TextField()
    value = models.TextField()

    def __str__(self):
        return self.date

class Monthly_Federal_Funds_Rate(models.Model):
    date = models.TextField()
    value = models.TextField()

    def __str__(self):
        return self.date

class Monthly_Cpi(models.Model):
    date = models.TextField()
    value = models.TextField()

    def __str__(self):
        return self.date

class Semiannual_Cpi(models.Model):
    date = models.TextField()
    value = models.TextField()

    def __str__(self):
        return self.date

class Inflation(models.Model):
    date = models.TextField()
    value = models.TextField()

    def __str__(self):
        return self.date

class Inflation_Expectation(models.Model):
    date = models.TextField()
    value = models.TextField()

    def __str__(self):
        return self.date

class Consumer_Sentiment(models.Model):
    date = models.TextField()
    value = models.TextField()

    def __str__(self):
        return self.date

class Retail_Sales(models.Model):
    date = models.TextField()
    value = models.TextField()

    def __str__(self):
        return self.date

class Durables(models.Model):
    date = models.TextField()
    value = models.TextField()

    def __str__(self):
        return self.date

class Unemployment(models.Model):
    date = models.TextField()
    value = models.TextField()

    def __str__(self):
        return self.date

class Nonfarm_Payroll(models.Model):
    date = models.TextField()
    value = models.TextField()

    def __str__(self):
        return self.date

class Annual_Income_Statement(models.Model):
    symbol = models.TextField()
    fiscalDateEnding = models.TextField()
    reportedCurrency = models.TextField()
    grossProfit = models.TextField()
    totalRevenue = models.TextField()
    costOfRevenue = models.TextField()
    costofGoodsAndServicesSold = models.TextField()
    operatingIncome = models.TextField()
    sellingGeneralAndAdministrative = models.TextField()
    researchAndDevelopment = models.TextField()
    operatingExpenses = models.TextField()
    investmentIncomeNet = models.TextField()
    netInterestIncome = models.TextField()
    interestIncome = models.TextField()
    interestExpense = models.TextField()
    nonInterestIncome = models.TextField()
    otherNonOperatingIncome = models.TextField()
    depreciation = models.TextField()
    depreciationAndAmortization = models.TextField()
    incomeBeforeTax = models.TextField()
    incomeTaxExpense = models.TextField()
    interestAndDebtExpense = models.TextField()
    netIncomeFromContinuingOperations = models.TextField()
    comprehensiveIncomeNetOfTax = models.TextField()
    ebit = models.TextField()
    ebitda = models.TextField()
    netIncome = models.TextField()

    def __str__(self):
        return (self.symbol + self.fiscalDateEnding)

class Quarterly_Income_Statement(models.Model):
    symbol = models.TextField()
    fiscalDateEnding = models.TextField()
    reportedCurrency = models.TextField()
    grossProfit = models.TextField()
    totalRevenue = models.TextField()
    costOfRevenue = models.TextField()
    costofGoodsAndServicesSold = models.TextField()
    operatingIncome = models.TextField()
    sellingGeneralAndAdministrative = models.TextField()
    researchAndDevelopment = models.TextField()
    operatingExpenses = models.TextField()
    investmentIncomeNet = models.TextField()
    netInterestIncome = models.TextField()
    interestIncome = models.TextField()
    interestExpense = models.TextField()
    nonInterestIncome = models.TextField()
    otherNonOperatingIncome = models.TextField()
    depreciation = models.TextField()
    depreciationAndAmortization = models.TextField()
    incomeBeforeTax = models.TextField()
    incomeTaxExpense = models.TextField()
    interestAndDebtExpense = models.TextField()
    netIncomeFromContinuingOperations = models.TextField()
    comprehensiveIncomeNetOfTax = models.TextField()
    ebit = models.TextField()
    ebitda = models.TextField()
    netIncome = models.TextField()

    def __str__(self):
        return (self.symbol + self.fiscalDateEnding)

class Annual_Balance_Sheet(models.Model):
    symbol = models.TextField()
    fiscalDateEnding = models.TextField()
    reportedCurrency = models.TextField()
    totalAssets = models.TextField()
    totalCurrentAssets = models.TextField()
    cashAndCashEquivalentsAtCarryingValue = models.TextField()
    cashAndShortTermInvestments = models.TextField()
    inventory = models.TextField()
    currentNetReceivables = models.TextField()
    totalNonCurrentAssets = models.TextField()
    propertyPlantEquipment = models.TextField()
    accumulatedDepreciationAmortizationPPE = models.TextField()
    intangibleAssets = models.TextField()
    intangibleAssetsExcludingGoodwill = models.TextField()
    goodwill = models.TextField()
    investments = models.TextField()
    longTermInvestments = models.TextField()
    shortTermInvestments = models.TextField()
    otherCurrentAssets = models.TextField()
    otherNonCurrrentAssets = models.TextField()
    totalLiabilities = models.TextField()
    totalCurrentLiabilities = models.TextField()
    currentAccountsPayable = models.TextField()
    deferredRevenue = models.TextField()
    currentDebt = models.TextField()
    shortTermDebt = models.TextField()
    totalNonCurrentLiabilities = models.TextField()
    capitalLeaseObligations = models.TextField()
    longTermDebt = models.TextField()
    currentLongTermDebt = models.TextField()
    longTermDebtNoncurrent = models.TextField()
    shortLongTermDebtTotal = models.TextField()
    otherCurrentLiabilities = models.TextField()
    otherNonCurrentLiabilities = models.TextField()
    totalShareholderEquity = models.TextField()
    treasuryStock = models.TextField()
    retainedEarnings = models.TextField()
    commonStock = models.TextField()
    commonStockSharesOutstanding = models.TextField()

    def __str__(self):
        return (self.symbol + self.fiscalDateEnding)

class Quarterly_Balance_Sheet(models.Model):
    symbol = models.TextField()
    fiscalDateEnding = models.TextField()
    reportedCurrency = models.TextField()
    totalAssets = models.TextField()
    totalCurrentAssets = models.TextField()
    cashAndCashEquivalentsAtCarryingValue = models.TextField()
    cashAndShortTermInvestments = models.TextField()
    inventory = models.TextField()
    currentNetReceivables = models.TextField()
    totalNonCurrentAssets = models.TextField()
    propertyPlantEquipment = models.TextField()
    accumulatedDepreciationAmortizationPPE = models.TextField()
    intangibleAssets = models.TextField()
    intangibleAssetsExcludingGoodwill = models.TextField()
    goodwill = models.TextField()
    investments = models.TextField()
    longTermInvestments = models.TextField()
    shortTermInvestments = models.TextField()
    otherCurrentAssets = models.TextField()
    otherNonCurrrentAssets = models.TextField()
    totalLiabilities = models.TextField()
    totalCurrentLiabilities = models.TextField()
    currentAccountsPayable = models.TextField()
    deferredRevenue = models.TextField()
    currentDebt = models.TextField()
    shortTermDebt = models.TextField()
    totalNonCurrentLiabilities = models.TextField()
    capitalLeaseObligations = models.TextField()
    longTermDebt = models.TextField()
    currentLongTermDebt = models.TextField()
    longTermDebtNoncurrent = models.TextField()
    shortLongTermDebtTotal = models.TextField()
    otherCurrentLiabilities = models.TextField()
    otherNonCurrentLiabilities = models.TextField()
    totalShareholderEquity = models.TextField()
    treasuryStock = models.TextField()
    retainedEarnings = models.TextField()
    commonStock = models.TextField()
    commonStockSharesOutstanding = models.TextField()

    def __str__(self):
        return (self.symbol + self.fiscalDateEnding)

class Annual_Cash_Flow(models.Model):
    symbol = models.TextField()
    fiscalDateEnding = models.TextField()
    reportedCurrency = models.TextField()
    operatingCashflow = models.TextField()
    paymentsForOperatingActivities = models.TextField()
    proceedsFromOperatingActivities = models.TextField()
    changeInOperatingLiabilities = models.TextField()
    changeInOperatingAssets = models.TextField()
    depreciationDepletionAndAmortization = models.TextField()
    capitalExpenditures = models.TextField()
    changeInReceivables = models.TextField()
    changeInInventory = models.TextField()
    profitLoss = models.TextField()
    cashflowFromInvestment = models.TextField()
    cashflowFromFinancing = models.TextField()
    proceedsFromRepaymentsOfShortTermDebt = models.TextField()
    paymentsForRepurchaseOfCommonStock = models.TextField()
    paymentsForRepurchaseOfEquity = models.TextField()
    paymentsForRepurchaseOfPreferredStock = models.TextField()
    dividendPayout = models.TextField()
    dividendPayoutCommonStock = models.TextField()
    dividendPayoutPreferredStock = models.TextField()
    proceedsFromIssuanceOfCommonStock = models.TextField()
    proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet = models.TextField()
    proceedsFromIssuanceOfPreferredStock = models.TextField()
    proceedsFromRepurchaseOfEquity = models.TextField()
    proceedsFromSaleOfTreasuryStock = models.TextField()
    changeInCashAndCashEquivalents = models.TextField()
    changeInExchangeRate = models.TextField()
    netIncome = models.TextField()

    def __str__(self):
        return (self.symbol + self.fiscalDateEnding)

class Quarterly_Cash_Flow(models.Model):
    symbol = models.TextField()
    fiscalDateEnding = models.TextField()
    reportedCurrency = models.TextField()
    operatingCashflow = models.TextField()
    paymentsForOperatingActivities = models.TextField()
    proceedsFromOperatingActivities = models.TextField()
    changeInOperatingLiabilities = models.TextField()
    changeInOperatingAssets = models.TextField()
    depreciationDepletionAndAmortization = models.TextField()
    capitalExpenditures = models.TextField()
    changeInReceivables = models.TextField()
    changeInInventory = models.TextField()
    profitLoss = models.TextField()
    cashflowFromInvestment = models.TextField()
    cashflowFromFinancing = models.TextField()
    proceedsFromRepaymentsOfShortTermDebt = models.TextField()
    paymentsForRepurchaseOfCommonStock = models.TextField()
    paymentsForRepurchaseOfEquity = models.TextField()
    paymentsForRepurchaseOfPreferredStock = models.TextField()
    dividendPayout = models.TextField()
    dividendPayoutCommonStock = models.TextField()
    dividendPayoutPreferredStock = models.TextField()
    proceedsFromIssuanceOfCommonStock = models.TextField()
    proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet = models.TextField()
    proceedsFromIssuanceOfPreferredStock = models.TextField()
    proceedsFromRepurchaseOfEquity = models.TextField()
    proceedsFromSaleOfTreasuryStock = models.TextField()
    changeInCashAndCashEquivalents = models.TextField()
    changeInExchangeRate = models.TextField()
    netIncome = models.TextField()

    def __str__(self):
        return (self.symbol + self.fiscalDateEnding)

class Earning(models.Model):
    symbol = models.TextField()
    fiscalDateEnding = models.TextField()
    reportedEPS = models.TextField()
    surprise = models.TextField()
    surprisePercentage = models.TextField()

    def __str__(self):
        return (self.symbol + self.fiscalDateEnding)

class Overview(models.Model):
    symbol = models.TextField()
    assetType = models.TextField()
    name = models.TextField()
    description = models.TextField()
    CIK = models.TextField()
    exchange = models.TextField()
    currency = models.TextField()
    country = models.TextField()
    sector = models.TextField()
    industry = models.TextField()
    address = models.TextField()
    fiscalYearEnd = models.TextField()
    latestQuarter = models.TextField()
    marketCapitalization = models.TextField()
    EBITDA = models.TextField()
    PERatio = models.TextField()
    PEGRatio = models.TextField()
    bookValue = models.TextField()
    dividendPerShare = models.TextField()
    dividendYield = models.TextField()
    EPS = models.TextField()
    revenuePerShareTTM = models.TextField()
    profitMargin = models.TextField()
    operatingMarginTTM = models.TextField()
    returnOnAssetsTTM = models.TextField()
    returnOnEquityTTM = models.TextField()
    revenueTTM = models.TextField()
    grossProfitTTM = models.TextField()
    dilutedEPSTTM = models.TextField()
    quarterlyEarningsGrowthYOY = models.TextField()
    quarterlyRevenueGrowthYOY = models.TextField()
    analystTargetPrice = models.TextField()
    trailingPE = models.TextField()
    forwardPE = models.TextField()
    priceToSalesRatioTTM = models.TextField()
    priceToBookRatio = models.TextField()
    EVToRevenue = models.TextField()
    EVToEBITDA = models.TextField()
    beta = models.TextField()
    _52WeekHigh = models.TextField()
    _52WeekLow = models.TextField()
    _50DayMovingAverage = models.TextField()
    _200DayMovingAverage = models.TextField()
    sharesOutstanding = models.TextField()
    dividendDate = models.TextField()
    exDividendDate = models.TextField()

    def __str__(self):
        return self.symbol

class Earning_Calendar(models.Model):
    symbol = models.TextField()
    name = models.TextField()
    reportDate = models.TextField()
    fiscalDateEnding = models.TextField()
    estimate = models.TextField()
    currency = models.TextField()

    def __str__(self):
        return (self.symbol + self.reportDate)