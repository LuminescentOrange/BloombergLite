import React, { useEffect, useState } from 'react'
import { useParams } from 'react-router-dom'
import ReactECharts from 'echarts-for-react';
import * as echarts from 'echarts';
import './visual.css';
import 'antd/dist/antd.css';
import CustomSearch from '../components/CustomSearch';
import { Table, Tag, Space } from 'antd';


const IncomeStatement = () => {

    
    let [earning, setEarning] = useState([])
    let [earning1, setEarning1] = useState([])
  

  
    let getEarning = async (symbol) => {
      let response = await fetch(`/lookup/annual_income_statement/${symbol.toUpperCase()}`)
      //let response = await fetch(`/lookup/annual_income_statement/AAPL`)
      let data = await response.json()
      setEarning(data)
    }
    let getEarning1 = async (symbol) => {
      let response1 = await fetch(`/lookup/quarterly_income_statement/${symbol}`)
      //let response1 = await fetch(`/lookup/quarterly_income_statement/AAPL`)
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
                    title: 'Gross Profit',
                    key: 'grossProfit',
                    dataIndex: 'grossProfit',
                
                  },
                  {
                    title: 'Total Revenue',
                    key: 'totalRevenue',
                    dataIndex:'totalRevenue'
                
                  },
                  {
                    title: 'Cost Of Revenue',
                    dataIndex: 'costOfRevenue',
                    key: 'costOfRevenue',
                  },
                  {
                    title: 'Cost of Goods And Services Sold',
                    dataIndex: 'costofGoodsAndServicesSold',
                    key: 'costofGoodsAndServicesSold',
                  },
                  {
                    title: 'Operating Income',
                    dataIndex: 'operatingIncome',
                    key: 'operatingIncome',
                    
                  },
                  {
                    title: 'Selling General And Administrative',
                    key: 'sellingGeneralAndAdministrative',
                    dataIndex: 'sellingGeneralAndAdministrative',
                
                  },
                  {
                    title: 'Research And Development',
                    key: 'researchAndDevelopment',
                    dataIndex:'researchAndDevelopment'
                
                  },
                  {
                    title: 'Operating Expenses',
                    dataIndex: 'operatingExpenses',
                    key: 'operatingExpenses',
                    
                  },
                  {
                    title: 'Investment IncomeNet',
                    dataIndex: 'investmentIncomeNet',
                    key: 'investmentIncomeNet',
                  },
                  {
                    title: 'Net Interest Income',
                    dataIndex: 'netInterestIncome',
                    key: 'netInterestIncome',
                  },
                  {
                    title: 'Interest Income',
                    key: 'interestIncome',
                    dataIndex: 'interestIncome',
                
                  },
                  {
                    title: 'Interest Expense',
                    key: 'interestExpense',
                    dataIndex:'interestExpense'
                
                  },
                  {
                    title: 'Non Interest Income',
                    dataIndex: 'nonInterestIncome',
                    key: 'nonInterestIncome',
                  },
                  {
                    title: 'Other Non Operating Income',
                    dataIndex: 'otherNonOperatingIncome',
                    key: 'otherNonOperatingIncome',
                  },
                  {
                    title: 'Depreciation',
                    key: 'depreciation',
                    dataIndex: 'depreciation',
                
                  },
                  {
                    title: 'Depreciation And Amortization',
                    key: 'depreciationAndAmortization',
                    dataIndex: 'depreciationAndAmortization',
                
                  },
                  {
                    title: 'Income Before Tax',
                    key: 'incomeBeforeTax',
                    dataIndex:'incomeBeforeTax'
                
                  },                  
                  {
                    title: 'Income Tax Expense',
                    dataIndex: 'incomeTaxExpense',
                    key: 'incomeTaxExpense',
                    
                  },
                  {
                    title: 'Interest And Debt Expense',
                    dataIndex: 'interestAndDebtExpense',
                    key: 'interestAndDebtExpense',
                  },
                  {
                    title: 'Net Income From Continuing Operations',
                    dataIndex: 'netIncomeFromContinuingOperations',
                    key: 'netIncomeFromContinuingOperations',
                  },
                  {
                    title: 'Comprehensive IncomeNetOfTax',
                    key: 'comprehensiveIncomeNetOfTax',
                    dataIndex: 'comprehensiveIncomeNetOfTax',
                
                  },
                  {
                    title: 'Ebit',
                    key: 'ebit',
                    dataIndex:'ebit'
                
                  },
                  {
                    title: 'Ebitda',
                    dataIndex: 'ebitda',
                    key: 'ebitda',
                  },
                  {
                    title: 'Net Income',
                    dataIndex: 'netIncome',
                    key: 'netIncome',
                  },

            ]} 
            dataSource = {
                earning
            }
            title={() => 'Annual Income Statement'}
            scroll={{ x: 3600, y: 500 }}
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
                    title: 'Gross Profit',
                    key: 'grossProfit',
                    dataIndex: 'grossProfit',
                
                  },
                  {
                    title: 'Total Revenue',
                    key: 'totalRevenue',
                    dataIndex:'totalRevenue'
                
                  },
                  {
                    title: 'Cost Of Revenue',
                    dataIndex: 'costOfRevenue',
                    key: 'costOfRevenue',
                  },
                  {
                    title: 'Cost of Goods And Services Sold',
                    dataIndex: 'costofGoodsAndServicesSold',
                    key: 'costofGoodsAndServicesSold',
                  },
                  {
                    title: 'Operating Income',
                    dataIndex: 'operatingIncome',
                    key: 'operatingIncome',
                    
                  },
                  {
                    title: 'Selling General And Administrative',
                    key: 'sellingGeneralAndAdministrative',
                    dataIndex: 'sellingGeneralAndAdministrative',
                
                  },
                  {
                    title: 'Research And Development',
                    key: 'researchAndDevelopment',
                    dataIndex:'researchAndDevelopment'
                
                  },
                  {
                    title: 'Operating Expenses',
                    dataIndex: 'operatingExpenses',
                    key: 'operatingExpenses',
                    
                  },
                  {
                    title: 'Investment IncomeNet',
                    dataIndex: 'investmentIncomeNet',
                    key: 'investmentIncomeNet',
                  },
                  {
                    title: 'Net Interest Income',
                    dataIndex: 'netInterestIncome',
                    key: 'netInterestIncome',
                  },
                  {
                    title: 'Interest Income',
                    key: 'interestIncome',
                    dataIndex: 'interestIncome',
                
                  },
                  {
                    title: 'Interest Expense',
                    key: 'interestExpense',
                    dataIndex:'interestExpense'
                
                  },
                  {
                    title: 'Non Interest Income',
                    dataIndex: 'nonInterestIncome',
                    key: 'nonInterestIncome',
                  },
                  {
                    title: 'Other Non Operating Income',
                    dataIndex: 'otherNonOperatingIncome',
                    key: 'otherNonOperatingIncome',
                  },
                  {
                    title: 'Depreciation',
                    key: 'depreciation',
                    dataIndex: 'depreciation',
                
                  },
                  {
                    title: 'Depreciation And Amortization',
                    key: 'depreciationAndAmortization',
                    dataIndex: 'depreciationAndAmortization',
                
                  },
                  {
                    title: 'Income Before Tax',
                    key: 'incomeBeforeTax',
                    dataIndex:'incomeBeforeTax'
                
                  },                  
                  {
                    title: 'Income Tax Expense',
                    dataIndex: 'incomeTaxExpense',
                    key: 'incomeTaxExpense',
                    
                  },
                  {
                    title: 'Interest And Debt Expense',
                    dataIndex: 'interestAndDebtExpense',
                    key: 'interestAndDebtExpense',
                  },
                  {
                    title: 'Net Income From Continuing Operations',
                    dataIndex: 'netIncomeFromContinuingOperations',
                    key: 'netIncomeFromContinuingOperations',
                  },
                  {
                    title: 'Comprehensive IncomeNetOfTax',
                    key: 'comprehensiveIncomeNetOfTax',
                    dataIndex: 'comprehensiveIncomeNetOfTax',
                
                  },
                  {
                    title: 'Ebit',
                    key: 'ebit',
                    dataIndex:'ebit'
                
                  },
                  {
                    title: 'Ebitda',
                    dataIndex: 'ebitda',
                    key: 'ebitda',
                  },
                  {
                    title: 'Net Income',
                    dataIndex: 'netIncome',
                    key: 'netIncome',
                  },
                ]} 
            dataSource = {
                earning1
            }
            title={() => 'Quarterly Income Statement'}
            scroll={{ x: 3600, y: 500 }}
        />

        </div>

    )
  }
  

    export default IncomeStatement;