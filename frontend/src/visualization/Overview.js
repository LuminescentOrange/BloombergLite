import React, { useEffect, useState } from 'react'
import CustomSearch from '../components/CustomSearch';
import './visual.css';
import 'antd/dist/antd.css';
import { Descriptions} from 'antd';



const Overview = () => {

    
    let [earning, setEarning] = useState([])
  

  
    let getEarning = async (symbol) => {
      let response = await fetch(`/lookup/overview/${symbol.toUpperCase()}/`)
      //let response = await fetch(`/lookup/overview/AAPL/`)
      let data = await response.json()
      console.log(data)
      setEarning(data)
    }
  //console.log("here" + earning);

    return (
        <div >
          <CustomSearch doSearch={getEarning}/>

                {earning.map((item)=>
                  <Descriptions  bordered className='table'>

                      <Descriptions.Item label="Symbol">
                        {item.symbol}
                      </Descriptions.Item>
                      <Descriptions.Item label="Name">
                        {item.name}
                      </Descriptions.Item>
                      <Descriptions.Item label="Asset Type">
                        {item.assetType}
                      </Descriptions.Item>
                      <Descriptions.Item label="Description" span={3}>
                        {item.description}
                      </Descriptions.Item>
                      <Descriptions.Item label="CIK">
                        {item.CIK}
                      </Descriptions.Item>
                      <Descriptions.Item label="Exchange">
                        {item.exchange}
                      </Descriptions.Item>
                      <Descriptions.Item label="Currency">
                        {item.currency}
                      </Descriptions.Item>
                      <Descriptions.Item label="Country" >
                        {item.country}
                      </Descriptions.Item>
                      <Descriptions.Item label="Sector">
                        {item.sector}
                      </Descriptions.Item>
                      <Descriptions.Item label="Industry" >
                        {item.industry}
                      </Descriptions.Item>
                      <Descriptions.Item label="Address">
                        {item.address}
                      </Descriptions.Item>
                      <Descriptions.Item label="Fiscal Year End" >
                        {item.fiscalYearEnd}
                      </Descriptions.Item>
                      <Descriptions.Item label="Latest Quarter">
                        {item.latestQuarter}
                      </Descriptions.Item>
                      <Descriptions.Item label="Market Capitalization" >
                        {item.marketCapitalization}
                      </Descriptions.Item>
                      <Descriptions.Item label="EBITDA">
                        {item.EBITDA}
                      </Descriptions.Item>
                      <Descriptions.Item label="PE Ratio" >
                        {item.PERatio}
                      </Descriptions.Item>
                      <Descriptions.Item label="PEG Ratio">
                        {item.PEGRatio}
                      </Descriptions.Item>
                      <Descriptions.Item label="Book Value" >
                        {item.bookValue}
                      </Descriptions.Item>
                      <Descriptions.Item label="Dividend PerS hare">
                        {item.dividendPerShare}
                      </Descriptions.Item>
                      <Descriptions.Item label="Dividend Yield" >
                        {item.dividendYield}
                      </Descriptions.Item>
                      <Descriptions.Item label="EPS">
                        {item.EPS}
                      </Descriptions.Item>
                      <Descriptions.Item label="Revenue Per Share TTM" >
                        {item.revenuePerShareTTM}
                      </Descriptions.Item>
                      <Descriptions.Item label="Profit Margin">
                        {item.profitMargin}
                      </Descriptions.Item>
                      <Descriptions.Item label="Operating Margin TTM" >
                        {item.operatingMarginTTM}
                      </Descriptions.Item>
                      <Descriptions.Item label="Return O nAssets TTM">
                        {item.returnOnAssetsTTM}
                      </Descriptions.Item>
                      <Descriptions.Item label="Return On Equity TTM" >
                        {item.returnOnEquityTTM}
                      </Descriptions.Item>
                      <Descriptions.Item label="Revenue TTM">
                        {item.revenueTTM}
                      </Descriptions.Item>
                      <Descriptions.Item label="Gross Profit TTM" >
                        {item.grossProfitTTM}
                      </Descriptions.Item>
                      <Descriptions.Item label="Diluted EPS TTM">
                        {item.dilutedEPSTTM}
                      </Descriptions.Item>
                      <Descriptions.Item label="Quarterly Earnings Growth YOY" >
                        {item.quarterlyEarningsGrowthYOY}
                      </Descriptions.Item>
                      <Descriptions.Item label="Quarterly Revenue Growth YOY">
                        {item.quarterlyRevenueGrowthYOY}
                      </Descriptions.Item>
                      <Descriptions.Item label="Analyst Target Price" >
                        {item.analystTargetPrice}
                      </Descriptions.Item>
                      <Descriptions.Item label="Trailing PE">
                        {item.trailingPE}
                      </Descriptions.Item>
                      <Descriptions.Item label="Forward PE" >
                        {item.forwardPE}
                      </Descriptions.Item>
                      <Descriptions.Item label="Price To Sales Ratio TTM">
                        {item.priceToSalesRatioTTM}
                      </Descriptions.Item>
                      <Descriptions.Item label="Price To Book Ratio" >
                        {item.priceToBookRatio}
                      </Descriptions.Item>
                      <Descriptions.Item label="EV To Revenue">
                        {item.EVToRevenue}
                      </Descriptions.Item>
                      <Descriptions.Item label="EV To EBITDA" >
                        {item.EVToEBITDA}
                      </Descriptions.Item>
                      <Descriptions.Item label="Beta">
                        {item.beta}
                      </Descriptions.Item>
                      <Descriptions.Item label="52 Wee kHigh" >
                        {item._52WeekHigh}
                      </Descriptions.Item>
                      <Descriptions.Item label="52 Week Low">
                        {item._52WeekLow}
                      </Descriptions.Item>
                      <Descriptions.Item label="50 Day Moving Average" >
                        {item._50DayMovingAverage}
                      </Descriptions.Item>
                      <Descriptions.Item label="200 Day Moving Average">
                        {item._200DayMovingAverage}
                      </Descriptions.Item>
                      <Descriptions.Item label="Shares Outstanding" >
                        {item.sharesOutstanding}
                      </Descriptions.Item>
                      <Descriptions.Item label="Dividend Date">
                        {item.dividendDate}
                      </Descriptions.Item>
                      <Descriptions.Item label="Ex Dividend Date" >
                        {item.exDividendDate}
                      </Descriptions.Item>
                  </Descriptions>)}
        </div>

    )
  }
  

    export default Overview;