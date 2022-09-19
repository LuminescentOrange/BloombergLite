import React, { useEffect, useState } from 'react'
import { useParams } from 'react-router-dom'
import ReactECharts from 'echarts-for-react';
import * as echarts from 'echarts';
import './visual.css';
import 'antd/dist/antd.css';
import CustomSearch from '../components/CustomSearch';
import { Table, Tag, Space } from 'antd';


const BalanceSheet = () => {

    
    let [earning, setEarning] = useState([])
    let [earning1, setEarning1] = useState([])
  

  
    let getEarning = async (symbol) => {
      let response = await fetch(`/lookup/annual_balance_sheet/${symbol.toUpperCase()}`)
      
      let data = await response.json()
      setEarning(data)
    }
    let getEarning1 = async (symbol) => {
      let response1 = await fetch(`/lookup/quarterly_balance_sheet/${symbol.toUpperCase()}`)
      
      let data1 = await response1.json()
      setEarning1(data1)
    }

    return (
        <div>
            <CustomSearch doSearch={getEarning}/>

            < Table  
            columns = {[
                  {
                    title: 'Symbol',
                    dataIndex: 'symbol',
                    key: 'symbol',
                    fixed: 'left',
                    
                  },
                  {
                    title: 'Fiscal Date Ending',
                    dataIndex: 'fiscalDateEnding',
                    key: 'fiscalDateEnding',
                    fixed: 'left',
                  },
                  {
                    title: 'Reported Currency',
                    dataIndex: 'reportedCurrency',
                    key: 'reportedCurrency',
                  },
                  {
                    title: 'Total Assets',
                    key: 'totalAssets',
                    dataIndex: 'totalAssets',
                
                  },
                  {
                    title: 'Total Current Assets',
                    key: 'totalCurrentAssets',
                    dataIndex:'totalCurrentAssets'
                
                  },
                  {
                    title: 'Cash And Cash Equivalents At Carrying Value',
                    dataIndex: 'cashAndCashEquivalentsAtCarryingValue',
                    key: 'cashAndCashEquivalentsAtCarryingValue',
                  },
                  {
                    title: 'Cash And Short Term Investments',
                    dataIndex: 'cashAndShortTermInvestments',
                    key: 'cashAndShortTermInvestments',
                  },
                  {
                    title: 'Inventory',
                    dataIndex: 'inventory',
                    key: 'inventory',
                    
                  },
                  {
                    title: 'Current Net Receivables',
                    key: 'currentNetReceivables',
                    dataIndex: 'currentNetReceivables',
                
                  },
                  {
                    title: 'Total Non Current Assets',
                    key: 'totalNonCurrentAssets',
                    dataIndex:'totalNonCurrentAssets'
                
                  },
                  {
                    title: 'Property Plant Equipment',
                    dataIndex: 'propertyPlantEquipment',
                    key: 'propertyPlantEquipment',
                    
                  },
                  {
                    title: 'Accumulated Depreciation Amortization PPE',
                    dataIndex: 'accumulatedDepreciationAmortizationPPE',
                    key: 'accumulatedDepreciationAmortizationPPE',
                  },
                  {
                    title: 'Intangible Assets',
                    dataIndex: 'intangibleAssets',
                    key: 'intangibleAssets',
                  },
                  {
                    title: 'Intangible Assets Excluding Goodwill',
                    key: 'intangibleAssetsExcludingGoodwill',
                    dataIndex: 'intangibleAssetsExcludingGoodwill',
                
                  },
                  {
                    title: 'Goodwill',
                    key: 'goodwill',
                    dataIndex:'goodwill'
                
                  },
                  {
                    title: 'Investments',
                    dataIndex: 'investments',
                    key: 'investments',
                  },
                  {
                    title: 'Long Term Investments',
                    dataIndex: 'longTermInvestments',
                    key: 'longTermInvestments',
                  },
                  {
                    title: 'Short Term Investments',
                    key: 'shortTermInvestments',
                    dataIndex: 'shortTermInvestments',
                
                  },
                  {
                    title: 'Other Current Assets',
                    key: 'otherCurrentAssets',
                    dataIndex: 'otherCurrentAssets',
                
                  },
                  {
                    title: 'Other Non Currrent Assets',
                    key: 'otherNonCurrrentAssets',
                    dataIndex:'otherNonCurrrentAssets'
                
                  },                  
                  {
                    title: 'Total Liabilities',
                    dataIndex: 'totalLiabilities',
                    key: 'totalLiabilities',
                    
                  },
                  {
                    title: 'Total Current Liabilities',
                    dataIndex: 'totalCurrentLiabilities',
                    key: 'totalCurrentLiabilities',
                  },
                  {
                    title: 'Current Accounts Payable',
                    dataIndex: 'currentAccountsPayable',
                    key: 'currentAccountsPayable',
                  },
                  {
                    title: 'Deferred Revenue',
                    key: 'deferredRevenue',
                    dataIndex: 'deferredRevenue',
                
                  },
                  {
                    title: 'Current Debt',
                    key: 'currentDebt',
                    dataIndex:'currentDebt'
                
                  },
                  {
                    title: 'Short Term Debt',
                    dataIndex: 'shortTermDebt',
                    key: 'shortTermDebt',
                  },
                  {
                    title: 'Total Non Current Liabilities',
                    dataIndex: 'totalNonCurrentLiabilities',
                    key: 'totalNonCurrentLiabilities',
                  },
                  {
                    title: 'Capital Lease Obligations',
                    key: 'capitalLeaseObligations',
                    dataIndex:'capitalLeaseObligations'
                
                  },
                  {
                    title: 'Long Term Debt',
                    dataIndex: 'longTermDebt',
                    key: 'longTermDebt',
                  },
                  {
                    title: 'Current Long Term Debt',
                    dataIndex: 'currentLongTermDebt',
                    key: 'currentLongTermDebt',
                  },
                  {
                    title: 'Long Term Debt Noncurrent',
                    key: 'longTermDebtNoncurrent',
                    dataIndex:'longTermDebtNoncurrent'
                
                  },
                  {
                    title: 'Short Long Term Debt Total',
                    dataIndex: 'shortLongTermDebtTotal',
                    key: 'shortLongTermDebtTotal',
                  },
                  {
                    title: 'Other Current Liabilities',
                    dataIndex: 'otherCurrentLiabilities',
                    key: 'otherCurrentLiabilities',
                  },
                  {
                    title: 'Other Non Current Liabilities',
                    key: 'otherNonCurrentLiabilities',
                    dataIndex:'otherNonCurrentLiabilities'
                
                  },
                  {
                    title: 'Total Shareholder Equity',
                    dataIndex: 'totalShareholderEquity',
                    key: 'totalShareholderEquity',
                  },
                  {
                    title: 'Treasury Stock',
                    dataIndex: 'treasuryStock',
                    key: 'treasuryStock',
                  },
                  {
                    title: 'Retained Earnings',
                    key: 'retainedEarnings',
                    dataIndex:'retainedEarnings'
                
                  },
                  {
                    title: 'Common Stock',
                    dataIndex: 'commonStock',
                    key: 'commonStock',
                  },

            ]} 
            dataSource = {
                earning
            }
            title={() => 'Annual Balance Sheet'}
            scroll={{ x: 3700, y: 500 }}
        /><CustomSearch doSearch={getEarning1}/>
                    < Table
            columns = {[
                {
                    title: 'Symbol',
                    dataIndex: 'symbol',
                    key: 'symbol',
                    fixed: 'left',
                    
                  },
                  {
                    title: 'Fiscal Date Ending',
                    dataIndex: 'fiscalDateEnding',
                    key: 'fiscalDateEnding',
                    fixed: 'left',
                  },
                  {
                    title: 'Reported Currency',
                    dataIndex: 'reportedCurrency',
                    key: 'reportedCurrency',
                  },
                  {
                    title: 'Total Assets',
                    key: 'totalAssets',
                    dataIndex: 'totalAssets',
                
                  },
                  {
                    title: 'Total Current Assets',
                    key: 'totalCurrentAssets',
                    dataIndex:'totalCurrentAssets'
                
                  },
                  {
                    title: 'Cash And Cash Equivalents At Carrying Value',
                    dataIndex: 'cashAndCashEquivalentsAtCarryingValue',
                    key: 'cashAndCashEquivalentsAtCarryingValue',
                  },
                  {
                    title: 'Cash And Short Term Investments',
                    dataIndex: 'cashAndShortTermInvestments',
                    key: 'cashAndShortTermInvestments',
                  },
                  {
                    title: 'Inventory',
                    dataIndex: 'inventory',
                    key: 'inventory',
                    
                  },
                  {
                    title: 'Current Net Receivables',
                    key: 'currentNetReceivables',
                    dataIndex: 'currentNetReceivables',
                
                  },
                  {
                    title: 'Total Non Current Assets',
                    key: 'totalNonCurrentAssets',
                    dataIndex:'totalNonCurrentAssets'
                
                  },
                  {
                    title: 'Property Plant Equipment',
                    dataIndex: 'propertyPlantEquipment',
                    key: 'propertyPlantEquipment',
                    
                  },
                  {
                    title: 'Accumulated Depreciation Amortization PPE',
                    dataIndex: 'accumulatedDepreciationAmortizationPPE',
                    key: 'accumulatedDepreciationAmortizationPPE',
                  },
                  {
                    title: 'Intangible Assets',
                    dataIndex: 'intangibleAssets',
                    key: 'intangibleAssets',
                  },
                  {
                    title: 'Intangible Assets Excluding Goodwill',
                    key: 'intangibleAssetsExcludingGoodwill',
                    dataIndex: 'intangibleAssetsExcludingGoodwill',
                
                  },
                  {
                    title: 'Goodwill',
                    key: 'goodwill',
                    dataIndex:'goodwill'
                
                  },
                  {
                    title: 'Investments',
                    dataIndex: 'investments',
                    key: 'investments',
                  },
                  {
                    title: 'Long Term Investments',
                    dataIndex: 'longTermInvestments',
                    key: 'longTermInvestments',
                  },
                  {
                    title: 'Short Term Investments',
                    key: 'shortTermInvestments',
                    dataIndex: 'shortTermInvestments',
                
                  },
                  {
                    title: 'Other Current Assets',
                    key: 'otherCurrentAssets',
                    dataIndex: 'otherCurrentAssets',
                
                  },
                  {
                    title: 'Other Non Currrent Assets',
                    key: 'otherNonCurrrentAssets',
                    dataIndex:'otherNonCurrrentAssets'
                
                  },                  
                  {
                    title: 'Total Liabilities',
                    dataIndex: 'totalLiabilities',
                    key: 'totalLiabilities',
                    
                  },
                  {
                    title: 'Total Current Liabilities',
                    dataIndex: 'totalCurrentLiabilities',
                    key: 'totalCurrentLiabilities',
                  },
                  {
                    title: 'Current Accounts Payable',
                    dataIndex: 'currentAccountsPayable',
                    key: 'currentAccountsPayable',
                  },
                  {
                    title: 'Deferred Revenue',
                    key: 'deferredRevenue',
                    dataIndex: 'deferredRevenue',
                
                  },
                  {
                    title: 'Current Debt',
                    key: 'currentDebt',
                    dataIndex:'currentDebt'
                
                  },
                  {
                    title: 'Short Term Debt',
                    dataIndex: 'shortTermDebt',
                    key: 'shortTermDebt',
                  },
                  {
                    title: 'Total Non Current Liabilities',
                    dataIndex: 'totalNonCurrentLiabilities',
                    key: 'totalNonCurrentLiabilities',
                  },
                  {
                    title: 'Capital Lease Obligations',
                    key: 'capitalLeaseObligations',
                    dataIndex:'capitalLeaseObligations'
                
                  },
                  {
                    title: 'Long Term Debt',
                    dataIndex: 'longTermDebt',
                    key: 'longTermDebt',
                  },
                  {
                    title: 'Current Long Term Debt',
                    dataIndex: 'currentLongTermDebt',
                    key: 'currentLongTermDebt',
                  },
                  {
                    title: 'Long Term Debt Noncurrent',
                    key: 'longTermDebtNoncurrent',
                    dataIndex:'longTermDebtNoncurrent'
                
                  },
                  {
                    title: 'Short Long Term Debt Total',
                    dataIndex: 'shortLongTermDebtTotal',
                    key: 'shortLongTermDebtTotal',
                  },
                  {
                    title: 'Other Current Liabilities',
                    dataIndex: 'otherCurrentLiabilities',
                    key: 'otherCurrentLiabilities',
                  },
                  {
                    title: 'Other Non Current Liabilities',
                    key: 'otherNonCurrentLiabilities',
                    dataIndex:'otherNonCurrentLiabilities'
                
                  },
                  {
                    title: 'Total Shareholder Equity',
                    dataIndex: 'totalShareholderEquity',
                    key: 'totalShareholderEquity',
                  },
                  {
                    title: 'Treasury Stock',
                    dataIndex: 'treasuryStock',
                    key: 'treasuryStock',
                  },
                  {
                    title: 'Retained Earnings',
                    key: 'retainedEarnings',
                    dataIndex:'retainedEarnings'
                
                  },
                  {
                    title: 'Common Stock',
                    dataIndex: 'commonStock',
                    key: 'commonStock',
                  },
                ]} 
            dataSource = {
                earning1
            }
            title={() => 'Quarterly Balance Sheet'}
            scroll={{ x: 3700, y: 500 }}
        />

        </div>

    )
  }
  

    export default BalanceSheet;