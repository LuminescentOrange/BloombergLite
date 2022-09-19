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

const EarningsCalendar = () => {

    // const { symbol } = useParams()
    let [earningList, setEarningList] = useState([])
    let [earning, setEarning] = useState([])

    // useEffect(() => {
    //   getEarning()

    // }, [])

    let getEarningList = async () => {
      let rs = await fetch(`/lookup/earning_calendar/`)
      let dt = await rs.json()
      setEarningList(dt)
    }


    let getEarning = async (symbol) => {
      
        let response = await fetch(`/lookup/earning_calendar/${symbol.toUpperCase()}/`)
        //let response = await fetch(`/lookup/earning/AAPL`)
        let data = await response.json()
        setEarning(data)
        console.log(earning)

    }


    useEffect(() => {
      getEarningList()
      
    }, [])

  //console.log("here" + earning);
    return (
        <div>
            <CustomSearch doSearch={getEarning}/>

            < Table className='table'
            scroll={{ y: 300 }}
           
            columns = {[
                  {
                    title: 'Symbol',
                    dataIndex: 'symbol',
                    key: 'symbol',
                    
                  },
                  {
                    title: 'Name',
                    dataIndex: 'name',
                    key: 'name',
                  },
                  {
                    title: 'Currency',
                    key: 'currency',
                    dataIndex:'currency'
                
                  },
                  {
                    title: 'Report Date',
                    dataIndex: 'reportDate',
                    key: 'reportDate',
                  },
                  {
                    title: 'Fiscal Date Ending',
                    key: 'fiscalDateEnding',
                    dataIndex: 'fiscalDateEnding',
                
                  },
                  {
                    title: 'Estimate',
                    key: 'estimate',
                    dataIndex:'estimate'
                
                  },
            ]} 
            dataSource = {
                earning
            }
           
        />
        < Table 
            scroll={{ y: 600 }}
           
            columns = {[
                  {
                    title: 'Symbol',
                    dataIndex: 'symbol',
                    key: 'symbol',
                    
                  },
                  {
                    title: 'Name',
                    dataIndex: 'name',
                    key: 'name',
                  },
                  {
                    title: 'Currency',
                    key: 'currency',
                    dataIndex:'currency'
                
                  },
                  {
                    title: 'Report Date',
                    dataIndex: 'reportDate',
                    key: 'reportDate',
                  },
                  {
                    title: 'Fiscal Date Ending',
                    key: 'fiscalDateEnding',
                    dataIndex: 'fiscalDateEnding',
                
                  },
                  {
                    title: 'Estimate',
                    key: 'estimate',
                    dataIndex:'estimate'
                
                  },
                  
            ]} 
            dataSource = {
                earningList
            }
            title={() => 'Earning Calendar'}
           
        />
        {/* </ColumnGroup> */}
            

        </div>

    )
  }
  

    export default EarningsCalendar;