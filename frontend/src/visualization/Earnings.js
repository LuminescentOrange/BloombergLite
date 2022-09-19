import React, { useEffect, useState } from 'react'
import { useParams } from 'react-router-dom'
import ReactECharts from 'echarts-for-react';
import * as echarts from 'echarts';
import './visual.css';
import 'antd/dist/antd.css';
import { Table, Tag, Space } from 'antd';
import useSearch from '../components/CustomSearch';
import CustomSearch from '../components/CustomSearch';

const { Column, ColumnGroup } = Table;

const Earnings = () => {

    // const { symbol } = useParams()
    let [earning, setEarning] = useState([])

    // useEffect(() => {
    //   getEarning()

    // }, [])


    let getEarning = async (symbol) => {
      
        let response = await fetch(`/lookup/earning/${symbol.toUpperCase()}`)
        //let response = await fetch(`/lookup/earning/AAPL`)
        let data = await response.json()
        setEarning(data)
          
  

    }
  //console.log("here" + earning);
    return (
        <div>
            <CustomSearch doSearch={getEarning}/>
        {/* <div>
        {earning.map((earningVal, index) => (
          <div key={index}>
              <h3>{earningVal.symbol} - {earningVal.fiscalDateEnding}</h3>
              <h5>ReportedEPS: {earningVal.reportedEPS}</h5>
              <h5>Surprise: {earningVal.surprise}</h5>
              <h5>SurprisePercentage: {earningVal.surprisePercentage}</h5>
          </div>
        ))}
        </div> */}
        {/* <ColumnGroup title="Name"> */}
        
        < Table className='table'
            scroll={{ y: 600 }}
           
            columns = {[
                  {
                    title: 'Company',
                    dataIndex: 'symbol',
                    key: 'symbol',
                    
                  },
                  {
                    title: 'Fiscal Date Ending',
                    dataIndex: 'fiscalDateEnding',
                    key: 'fiscalDateEnding',
                  },
                  {
                    title: 'Reported EFS',
                    dataIndex: 'reportedEPS',
                    key: 'reportedEPS',
                  },
                  {
                    title: 'Surprise',
                    key: 'surprise',
                    dataIndex: 'surprise',
                
                  },
                  {
                    title: 'Surprise Percentage',
                    key: 'surprisePercentage',
                    dataIndex:'surprisePercentage'
                
                  },
            ]} 
            dataSource = {
                earning
            }
           
        />
        {/* </ColumnGroup> */}
            

        </div>

    )
  }
  

    export default Earnings;