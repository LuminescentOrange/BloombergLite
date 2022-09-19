import React, { useEffect, useState } from 'react'
import { useParams } from 'react-router-dom'
import ReactECharts from 'echarts-for-react';
import * as echarts from 'echarts';
import './visual.css';
import 'antd/dist/antd.css';
import CustomSearch from '../components/CustomSearch';
import { Table, Tag, Space } from 'antd';


const CashFlow = () => {

    
    let [earning, setEarning] = useState([])
    let [earning1, setEarning1] = useState([])
  

  
    let getEarning = async (symbol) => {
      let response = await fetch(`/lookup/annual_cash_flow/${symbol.toUpperCase()}`)
      
      let data = await response.json()
      setEarning(data)
    }
    let getEarning1 = async (symbol) => {
      let response1 = await fetch(`/lookup/quarterly_cash_flow/${symbol}`)
      
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
                    title: 'Operating Cashflow',
                    key: 'operatingCashflow',
                    dataIndex: 'operatingCashflow',
                
                  },
                  {
                    title: 'Payments For Operating Activities',
                    key: 'paymentsForOperatingActivities',
                    dataIndex:'paymentsForOperatingActivities'
                
                  },
                  {
                    title: 'Proceeds From Operating Activities',
                    dataIndex: 'proceedsFromOperatingActivities',
                    key: 'proceedsFromOperatingActivities',
                  },
                  {
                    title: 'Change In Operating Liabilities',
                    dataIndex: 'changeInOperatingLiabilities',
                    key: 'changeInOperatingLiabilities',
                  },
                  {
                    title: 'Change In Operating Assets',
                    dataIndex: 'changeInOperatingAssets',
                    key: 'changeInOperatingAssets',
                    
                  },
                  {
                    title: 'Depreciation Depletion And Amortization',
                    key: 'depreciationDepletionAndAmortization',
                    dataIndex: 'depreciationDepletionAndAmortization',
                
                  },
                  {
                    title: 'Capital Expenditures',
                    key: 'capitalExpenditures',
                    dataIndex:'capitalExpenditures'
                
                  },
                  {
                    title: 'Change In Receivables',
                    dataIndex: 'changeInReceivables',
                    key: 'changeInReceivables',
                    
                  },
                  {
                    title: 'change In Inventory',
                    dataIndex: 'changeInInventory',
                    key: 'changeInInventory',
                    
                  },
                  {
                    title: 'Profit Loss',
                    dataIndex: 'profitLoss',
                    key: 'profitLoss',
                  },
                  {
                    title: 'Cashflow From Investment',
                    dataIndex: 'cashflowFromInvestment',
                    key: 'cashflowFromInvestment',
                  },
                  {
                    title: 'Cashflow From Financing',
                    key: 'cashflowFromFinancing',
                    dataIndex: 'cashflowFromFinancing',
                
                  },
                  {
                    title: 'Proceeds From Repayments Of Short Term Debt',
                    key: 'proceedsFromRepaymentsOfShortTermDebt',
                    dataIndex:'proceedsFromRepaymentsOfShortTermDebt'
                
                  },
                  {
                    title: 'Payments For Repurchase Of CommonStock',
                    dataIndex: 'paymentsForRepurchaseOfCommonStock',
                    key: 'paymentsForRepurchaseOfCommonStock',
                  },
                  {
                    title: 'Payments For Repurchase Of Equity',
                    dataIndex: 'paymentsForRepurchaseOfEquity',
                    key: 'paymentsForRepurchaseOfEquity',
                  },
                  {
                    title: 'Payments For Repurchase Of Preferred Stock',
                    key: 'paymentsForRepurchaseOfPreferredStock',
                    dataIndex: 'paymentsForRepurchaseOfPreferredStock',
                
                  },
                  {
                    title: 'Dividend Payout',
                    key: 'dividendPayout',
                    dataIndex: 'dividendPayout',
                
                  },
                  {
                    title: 'Dividend Payout Common Stock',
                    key: 'dividendPayoutCommonStock',
                    dataIndex:'dividendPayoutCommonStock'
                
                  },                  
                  {
                    title: 'Dividend Payout Preferred Stock',
                    dataIndex: 'dividendPayoutPreferredStock',
                    key: 'dividendPayoutPreferredStock',
                    
                  },
                  {
                    title: 'Proceeds From Issuance Of CommonStock',
                    dataIndex: 'proceedsFromIssuanceOfCommonStock',
                    key: 'proceedsFromIssuanceOfCommonStock',
                  },
                  {
                    title: 'Proceeds From Issuance Of Long Term Debt And Capital Securities Net',
                    dataIndex: 'proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet',
                    key: 'proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet',
                  },
                  {
                    title: 'Proceeds From Issuance Of Preferred Stock',
                    key: 'proceedsFromIssuanceOfPreferredStock',
                    dataIndex: 'proceedsFromIssuanceOfPreferredStock',
                
                  },
                  {
                    title: 'Proceeds From Repurchase Of Equity',
                    key: 'proceedsFromRepurchaseOfEquity',
                    dataIndex:'proceedsFromRepurchaseOfEquity'
                
                  },
                  {
                    title: 'Proceeds From Sale Of Treasury Stock',
                    key: 'proceedsFromSaleOfTreasuryStock',
                    dataIndex:'proceedsFromSaleOfTreasuryStock'
                
                  },
                  {
                    title: 'Change In Cash And Cash Equivalents',
                    dataIndex: 'changeInCashAndCashEquivalents',
                    key: 'changeInCashAndCashEquivalents',
                  },
                  {
                    title: 'Change In Exchange Rate',
                    dataIndex: 'changeInExchangeRate',
                    key: 'changeInExchangeRate',
                  },
                  {
                    title: 'Net Income',
                    key: 'netIncome',
                    dataIndex:'netIncome'
                
                  },
                
            ]} 
            dataSource = {
                earning
            }
            title={() => 'Annual Cash Flow'}
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
                    title: 'Operating Cashflow',
                    key: 'operatingCashflow',
                    dataIndex: 'operatingCashflow',
                
                  },
                  {
                    title: 'Payments For Operating Activities',
                    key: 'paymentsForOperatingActivities',
                    dataIndex:'paymentsForOperatingActivities'
                
                  },
                  {
                    title: 'Proceeds From Operating Activities',
                    dataIndex: 'proceedsFromOperatingActivities',
                    key: 'proceedsFromOperatingActivities',
                  },
                  {
                    title: 'Change In Operating Liabilities',
                    dataIndex: 'changeInOperatingLiabilities',
                    key: 'changeInOperatingLiabilities',
                  },
                  {
                    title: 'Change In Operating Assets',
                    dataIndex: 'changeInOperatingAssets',
                    key: 'changeInOperatingAssets',
                    
                  },
                  {
                    title: 'Depreciation Depletion And Amortization',
                    key: 'depreciationDepletionAndAmortization',
                    dataIndex: 'depreciationDepletionAndAmortization',
                
                  },
                  {
                    title: 'Capital Expenditures',
                    key: 'capitalExpenditures',
                    dataIndex:'capitalExpenditures'
                
                  },
                  {
                    title: 'Change In Receivables',
                    dataIndex: 'changeInReceivables',
                    key: 'changeInReceivables',
                    
                  },
                  {
                    title: 'change In Inventory',
                    dataIndex: 'changeInInventory',
                    key: 'changeInInventory',
                    
                  },
                  {
                    title: 'Profit Loss',
                    dataIndex: 'profitLoss',
                    key: 'profitLoss',
                  },
                  {
                    title: 'Cashflow From Investment',
                    dataIndex: 'cashflowFromInvestment',
                    key: 'cashflowFromInvestment',
                  },
                  {
                    title: 'Cashflow From Financing',
                    key: 'cashflowFromFinancing',
                    dataIndex: 'cashflowFromFinancing',
                
                  },
                  {
                    title: 'Proceeds From Repayments Of Short Term Debt',
                    key: 'proceedsFromRepaymentsOfShortTermDebt',
                    dataIndex:'proceedsFromRepaymentsOfShortTermDebt'
                
                  },
                  {
                    title: 'Payments For Repurchase Of CommonStock',
                    dataIndex: 'paymentsForRepurchaseOfCommonStock',
                    key: 'paymentsForRepurchaseOfCommonStock',
                  },
                  {
                    title: 'Payments For Repurchase Of Equity',
                    dataIndex: 'paymentsForRepurchaseOfEquity',
                    key: 'paymentsForRepurchaseOfEquity',
                  },
                  {
                    title: 'Payments For Repurchase Of Preferred Stock',
                    key: 'paymentsForRepurchaseOfPreferredStock',
                    dataIndex: 'paymentsForRepurchaseOfPreferredStock',
                
                  },
                  {
                    title: 'Dividend Payout',
                    key: 'dividendPayout',
                    dataIndex: 'dividendPayout',
                
                  },
                  {
                    title: 'Dividend Payout Common Stock',
                    key: 'dividendPayoutCommonStock',
                    dataIndex:'dividendPayoutCommonStock'
                
                  },                  
                  {
                    title: 'Dividend Payout Preferred Stock',
                    dataIndex: 'dividendPayoutPreferredStock',
                    key: 'dividendPayoutPreferredStock',
                    
                  },
                  {
                    title: 'Proceeds From Issuance Of CommonStock',
                    dataIndex: 'proceedsFromIssuanceOfCommonStock',
                    key: 'proceedsFromIssuanceOfCommonStock',
                  },
                  {
                    title: 'Proceeds From Issuance Of Long Term Debt And Capital Securities Net',
                    dataIndex: 'proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet',
                    key: 'proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet',
                  },
                  {
                    title: 'Proceeds From Issuance Of Preferred Stock',
                    key: 'proceedsFromIssuanceOfPreferredStock',
                    dataIndex: 'proceedsFromIssuanceOfPreferredStock',
                
                  },
                  {
                    title: 'Proceeds From Repurchase Of Equity',
                    key: 'proceedsFromRepurchaseOfEquity',
                    dataIndex:'proceedsFromRepurchaseOfEquity'
                
                  },
                  {
                    title: 'Proceeds From Sale Of Treasury Stock',
                    key: 'proceedsFromSaleOfTreasuryStock',
                    dataIndex:'proceedsFromSaleOfTreasuryStock'
                
                  },
                  {
                    title: 'Change In Cash And Cash Equivalents',
                    dataIndex: 'changeInCashAndCashEquivalents',
                    key: 'changeInCashAndCashEquivalents',
                  },
                  {
                    title: 'Change In Exchange Rate',
                    dataIndex: 'changeInExchangeRate',
                    key: 'changeInExchangeRate',
                  },
                  {
                    title: 'Net Income',
                    key: 'netIncome',
                    dataIndex:'netIncome'
                
                  },
                ]} 
            dataSource = {
                earning1
            }
            title={() => 'Quarterly Cash Flow'}
            scroll={{ x: 3700, y: 500 }}
        />

        </div>

    )
  }
  

    export default CashFlow;