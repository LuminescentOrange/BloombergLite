import React, { useEffect, useState } from 'react'
import './visual.css';
import 'antd/dist/antd.css';
import { Table, Tag, Space } from 'antd';
import useSearch from '../components/CustomSearch';
import CustomSearch from '../components/CustomSearch';


const News = () => {

    let [news, setNews] = useState([])


    let getNews = async (symbol) => {
      
        let response = await fetch(`/lookup/news/${symbol.toUpperCase()}/`)
        let data = await response.json()
        setNews(data.results)

          
    }

    return (
        <div><CustomSearch doSearch={getNews}/>
        
        <Table className='table'
            scroll={{ y: 600 }}
           
            columns = {[
                  {
                    title: 'Title',
                    dataIndex: 'title',
                    key: 'title',
                    
                  },
                  {
                    title: 'Article_URL',
                    dataIndex: 'article_url',
                    key: 'article_url',
                    render: (value) => {
                        return (
                          <a
                            onClick={(event) => event.stopPropagation()}
                            href={value}
                            target="_blank"
                          >{value}</a>
                        );
                    }
                  },
                  {
                    title: 'Publisher',
                    dataIndex: ['publisher', 'name'],
                    key: 'publisher',
                  },
                  {
                    title: 'Related_Tickers',
                    dataIndex: 'tickers',
                    key: 'tickers',
                  },
                  {
                    title: 'Published_UTC',
                    dataIndex: 'published_utc',
                    key: 'published_utc',
                  },
            ]} 
            dataSource = {news}

        />
        </div>
    )
  }
  

export default News;