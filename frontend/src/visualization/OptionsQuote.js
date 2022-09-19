import { message } from 'antd';
import React, { useEffect, useRef, useState } from 'react';
import CustomSearch from '../components/CustomSearch';
import { Table} from 'antd';

var W3CWebSocket = require('websocket').w3cwebsocket

const OptionsQuote = () => {

  //  const [dataJson, setDataJson] = useState([])
    const [dataJsonQ, setDataJsonQ] = useState([])
    const [dataJsonT, setDataJsonT] = useState([])
    // let dataJson = {};
    const api_key = "3UyFGzf0pj6LALE6eLtomJF4wB0PtvNj";
    const ws = useRef(null)
    //const ws = new W3CWebSocket("wss://socket.polygon.io/options");

    /*
    if (Array.isArray(quoteTickers) && quoteTickers.length) {
      quoteTickers = quoteTickers.map(i => 'Q.' + i);
      tradeTickers = tradeTickers.map(i => 'Q.' + i);
    }
    const combinedTickers = quoteTickers.concat(tradeTickers)
    console.log(combinedTickers)
    */

    useEffect(() => {
      if (sessionStorage.getItem('selectedContracts') !== null) {
        var quoteTickers = (sessionStorage.getItem('selectedContracts')).split(',')
        quoteTickers = quoteTickers.map(i => 'Q.' + i);
        var tradeTickers = (sessionStorage.getItem('selectedContracts')).split(',')
        tradeTickers = tradeTickers.map(i => 'T.' + i);
        const combinedTickers = (quoteTickers.concat(tradeTickers)).toString()
        console.log(combinedTickers)

        ws.current = new W3CWebSocket("wss://socket.polygon.io/options");

        ws.current.onopen = function() {
          console.log('WebSocket Client Connected')
          var auth_data = {
              "action": "auth",
              "params": api_key
          }

          ws.current.send(JSON.stringify(auth_data))
          
          var channel_data = {
            "action": "subscribe",
            "params": combinedTickers
            //"params": combinedTickers
          }

          ws.current.send(JSON.stringify(channel_data))
        }

        ws.current.onmessage = function(message) {
          console.log(message)   
          let dataFromServer = JSON.parse(message.data)

          if (dataFromServer[0].ev === 'Q') {
            setDataJsonQ((pre)=>[...dataFromServer, ...pre])
          }

          if (dataFromServer[0].ev === 'T') {
            setDataJsonT((pre)=>[...dataFromServer, ...pre])
          }
        } //accept
        
        ws.current.onclose = function() {
            console.log('WebSocket Client Closed')
        }
        
        return () => ws.current.close()
      }
        
    }, [])
   
 
  
    return (
        <div>
            < Table
            columns = {[
                  {
                    title: 'Event Type',
                    dataIndex: 'ev',
                    key: 'ev',
                    fixed: 'left',
                  },
                  {
                    title: 'Symbol',
                    dataIndex: 'sym',
                    key: 'sym',
                    fixed: 'left',
                  },
                  {
                    title: 'Bid Exchange ID',
                    dataIndex: 'bx',
                    key: 'bx',
                    fixed: 'left',
                  },
                  {
                    title: 'Bid Price',
                    dataIndex: 'bp',
                    key: 'bp',
                  },
                  {
                    title: 'Bid Size',
                    key: 'bs',
                    dataIndex: 'bs',
                
                  },
                  {
                    title: 'Ask Exchange ID',
                    key: 'ax',
                    dataIndex:'ax'
                
                  },
                  {
                    title: 'Ask Price',
                    dataIndex: 'ap',
                    key: 'ap',
                  },
                  {
                    title: 'Ask Size',
                    dataIndex: 'as',
                    key: 'as',
                  },

                  {
                    title: 'Timestamp',
                    key: 't',
                    dataIndex:'t'
                
                  },


                ]} 
            dataSource = {
                //message.data
                dataJsonQ
                //dataJson

            }
            title={() => 'Quote'}
            
        />

        < Table
            columns = {[
                  {
                    title: 'Event Type',
                    dataIndex: 'ev',
                    key: 'ev',
                    fixed: 'left',
                  },
                  {
                    title: 'Symbol',
                    dataIndex: 'sym',
                    key: 'sym',
                    fixed: 'left',
                  },
                  {
                    title: 'Exchange ID',
                    dataIndex: 'x',
                    key: 'x',
                    fixed: 'left',
                  },
                  {
                    title: 'Trade ID',
                    dataIndex: 'i',
                    key: 'i',
                    fixed: 'left',
                  },
                  {
                    title: 'Price',
                    dataIndex: 'p',
                    key: 'p',
                  },

                  {
                    title: 'Size',
                    key: 's',
                    dataIndex: 's',
                
                  },
                  {
                    title: 'Trade Condition',
                    key: 'c',
                    dataIndex:'c'
                
                  },

                  {
                    title: 'Timestamp',
                    key: 't',
                    dataIndex:'t'
                
                  },

                  
                  {
                    title: 'Sequence',
                    dataIndex: 'q',
                    key: 'q',
                  },

                ]} 
            dataSource = {
                //message.data
                dataJsonT

            }
            title={() => 'Trade'}
            
        />
            
        </div>
    )
}

export default OptionsQuote
