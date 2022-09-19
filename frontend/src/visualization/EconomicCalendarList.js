import React, { useEffect, useState } from 'react'
import './visual.css';
import 'antd/dist/antd.css';
import { Table } from 'antd';


const EconomicCalendarList = () => {

    let [economicCalendar, setEconomicCalendar] = useState([])


    let getEconomicCalendar = async () => {
      
        let response = await fetch(`/lookup/economic_calendar/`)
        let data = await response.json()
        setEconomicCalendar(data)

    }

    useEffect(() => {

        getEconomicCalendar()

    }, []);

    return (
        <div>
        <Table className='table'
            scroll={{ y: 600 }}
           
            columns = {[
                  {
                    title: 'Date',
                    dataIndex: 'date',
                    key: 'date',
                    
                  },
                  {
                    title: 'Time',
                    dataIndex: 'time',
                    key: 'time',
                  },
                  {
                    title: 'Country',
                    dataIndex: 'zone',
                    key: 'zone',
                  },
                  {
                    title: 'Event',
                    dataIndex: 'event',
                    key: 'event',
                  },
                  {
                    title: 'Importance',
                    dataIndex: 'importance',
                    key: 'importance',
                  },
                  {
                    title: 'Forecast',
                    dataIndex: 'forecast',
                    key: 'forecast',
                  },
                  {
                    title: 'Actual',
                    dataIndex: 'actual',
                    key: 'actual',
                  },
                  {
                    title: 'Previous',
                    dataIndex: 'previous',
                    key: 'previous',
                  },
            ]} 
            dataSource = {economicCalendar}

        />
        </div>
    )
  }
  

export default EconomicCalendarList;