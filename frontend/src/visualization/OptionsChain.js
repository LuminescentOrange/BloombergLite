import React, { useState, useEffect } from 'react'
import CustomSearch from '../components/CustomSearch';
import { Table, Space, List, Divider, Button } from 'antd';

const OptionsChain = () => {

    let [contracts, setContracts] = useState([])

    let [selectedContractID, setSelectedContractID] = useState([])

  
    let getContracts = async (symbol) => {
      let response = await fetch(`/lookup/options_contracts/${symbol.toUpperCase()}`)
      let data = await response.json()
      setContracts(data.results)
    }

    const selected = (record)=>{
        setSelectedContractID([...selectedContractID, record.ticker])
    }

    const removed = () => {
      setSelectedContractID([])
      sessionStorage.removeItem('selectedContracts')
    }

    const setSessionStorage = () => {
      if (selectedContractID.length) {
        sessionStorage.setItem("selectedContracts", selectedContractID)
      }
    }

    
    useEffect(() => {
      if (sessionStorage.getItem('selectedContracts') !== null) {
        var sessionTickers = (sessionStorage.getItem('selectedContracts')).split(',')
        /*
        console.log('If Array:', Array.isArray(sessionTickers))
        console.log('SessionTickers Length:', sessionTickers.length)
        console.log('SessionTickers:', sessionTickers)
        console.log('SelectedContracts:', selectedContractID)
        */
        if (Array.isArray(sessionTickers) && sessionTickers.length) {
          setSelectedContractID(sessionTickers)
        }
      }
    }, [])
    


    return (     
        <div>
            <CustomSearch doSearch={getContracts}/>  

            < Table  className='table'
        columns = {[
            {
                title: 'Underlying Ticker',
                key: 'underlying_ticker',
                dataIndex:'underlying_ticker'
            
              },
              {
                title: 'Expiration Date',
                dataIndex: 'expiration_date',
                key: 'expiration_date',
                
              },
              {
                title: 'CFI',
                dataIndex: 'cfi',
                key: 'cfi',
              },
              {
                title: 'Contract Type',
                dataIndex: 'contract_type',
                key: 'contract_type',
              },
              {
                title: 'Exercise Style',
                key: 'exercise_style',
                dataIndex: 'exercise_style',
            
              },
              {
                title: 'Primary Exchange',
                key: 'primary_exchange',
                dataIndex:'primary_exchange'
            
              },
              {
                title: 'Shares Per Contract',
                key: 'shares_per_contract',
                dataIndex:'shares_per_contract'
            
              },
              {
                title: 'Strike Price',
                key: 'strike_price',
                dataIndex:'strike_price'
            
              },
              {
                title: 'Ticker',
                key: 'ticker',
                dataIndex:'ticker'
            
              },
              {
                title: 'Action',
                key: 'action',
                render: (text, record) => (
                  <Space size="middle">

                    <a onClick={()=>{selected(record)}}>View</a>
                  </Space>
                ),
              },
              

        ]} 
        dataSource = {
            contracts
        }
        scroll={{ y: 500 }}
        // scroll={{ x: 3600, y: 500 }}
       
    /><Divider orientation="left">Ticker</Divider>
   {
        selectedContractID.map((item) => 
        <>
            
            <h3>{item}</h3>
        </>)
   }
        <Button type='text' block shape='round' onClick={removed}>Clearing Selected Contracts</Button>
        <Button type='text' block shape='round' onClick={setSessionStorage}>Watching Selected Contracts</Button>
        </div> 
      
    )
}

export default OptionsChain