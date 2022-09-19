import React, { useEffect, useState } from 'react'
import { useParams } from 'react-router-dom'
import ReactECharts from 'echarts-for-react';
import * as echarts from 'echarts';


const FederalFundsRate = () => {

  const { symbol } = useParams()
  let [earning, setEarning] = useState([])
  let [earning1, setEarning1] = useState([])
  let [earning2, setEarning2] = useState([])

  useEffect(() => {
    getEarning()
    getEarning1()
    getEarning2()
    
  }, [])



  let getEarning = async () => {
    let response = await fetch(`/lookup/daily_federal_funds_rate/`)
    let data = await response.json()
    setEarning(data)
  }

  let getEarning1 = async () => {
    let response1 = await fetch(`/lookup/weekly_federal_funds_rate/`)
    let data1 = await response1.json()
    setEarning1(data1)
  }

  let getEarning2 = async () => {
    let response2 = await fetch(`/lookup/monthly_federal_funds_rate/`)
    let data2 = await response2.json()
    setEarning2(data2)
  }


  return (
    // <div>
    //   {earning.map((earningVal, index) => (
    //     <div key={index}>
    //         <h3>{earningVal.symbol} - {earningVal.fiscalDateEnding}</h3>
    //         <h5>ReportedEPS: {earningVal.reportedEPS}</h5>
    //         <h5>Surprise: {earningVal.surprise}</h5>
    //         <h5>SurprisePercentage: {earningVal.surprisePercentage}</h5>
    //     </div>
    //   ))}
    // </div>
    <><ReactECharts 
        // echarts={echarts}
      option={{
      tooltip: {
          trigger: 'axis',
          position: function (pt) {
            return [pt[0], '10%'];
          }
      },
      title: {
          left: 'center',
          text: 'Daily Federal Funds Rate'
      },
      // toolbox: {
      //   feature: {
      //     dataZoom: {
      //       yAxisIndex: 'none'
      //     },
      //     restore: {},
      //     saveAsImage: {}
      //   }
      // },    
      xAxis: {
          type: 'category',
          data: earning.map(item=>item.date),
          inverse:true
      },
      yAxis: {
          type: 'value'
      },
      dataZoom: [
        {
          type: 'inside',
          start: 0,
          end: 100
        },
        {
          start: 0,
          end: 100
        }
      ],


      series: [
          {
          data: earning.map(item=>item.value),
          name: 'Federal Funds Rate',
          type: 'line',
          symbol: 'none',
          sampling: 'lttb',
          itemStyle: {
            color: 'rgb(255, 70, 131)'
          },
          areaStyle: {
            color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
              {
                offset: 0,
                color: 'rgb(255, 158, 68)'
              },
              {
                offset: 1,
                color: 'rgb(255, 70, 131)'
              }
            ])
          },
          }
      ]
      }}
        // notMerge={true}
        // lazyUpdate={true}
        // theme={"theme_name"}
        // onChartReady={this.onChartReadyCallback}
        // onEvents={EventsDict}

    />

    <ReactECharts 
        // echarts={echarts}
      option={{
      tooltip: {
          trigger: 'axis',
          position: function (pt) {
            return [pt[0], '10%'];
          }
      },

      title: {
          left: 'center',
          text: 'Weekly Federal Funds Rate'
      },  
      
      xAxis: {
          type: 'category',
          axisLabel: {formatter :'{value}' },
          data: earning1.map(item=>item.date),
          inverse:true
      },
      yAxis: {
          type: 'value'
      },

      dataZoom: [
        {
          type: 'inside',
          start: 0,
          end: 100
        },
        {
          start: 0,
          end: 100
        }
      ],

      series: [
          {
          data: earning1.map(item=>item.value),
          name: 'Federal Funds Rate',
          type: 'line',
          symbol: 'none',
          sampling: 'lttb',
          itemStyle: {
            color: 'rgb(255, 70, 131)'
          },
          areaStyle: {
            color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
              {
                offset: 0,
                color: 'rgb(255, 158, 68)'
              },
              {
                offset: 1,
                color: 'rgb(255, 70, 131)'
              }
            ])
          },
          }
      ]
      }}
        // notMerge={true}
        // lazyUpdate={true}
     // theme={"theme_name"}
        // onChartReady={this.onChartReadyCallback}
        // onEvents={EventsDict}

    />
    <ReactECharts 
        // echarts={echarts}
      option={{
      tooltip: {
          trigger: 'axis',
          position: function (pt) {
            return [pt[0], '10%'];
          }
      },

      title: {
          left: 'center',
          text: 'Monthly Federal Funds Rate'
      },  
      
      xAxis: {
          type: 'category',
          axisLabel: {formatter :'{value}' },
          data: earning2.map(item=>item.date),
          inverse:true
      },
      yAxis: {
          type: 'value'
      },

      dataZoom: [
        {
          type: 'inside',
          start: 0,
          end: 100
        },
        {
          start: 0,
          end: 100
        }
      ],

      series: [
          {
          data: earning2.map(item=>item.value),
          name: 'Federal Funds Rate',
          type: 'line',
          symbol: 'none',
          sampling: 'lttb',
          itemStyle: {
            color: 'rgb(255, 70, 131)'
          },
          areaStyle: {
            color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
              {
                offset: 0,
                color: 'rgb(255, 158, 68)'
              },
              {
                offset: 1,
                color: 'rgb(255, 70, 131)'
              }
            ])
          },
          }
      ]
      }}
        // notMerge={true}
        // lazyUpdate={true}
     // theme={"theme_name"}
        // onChartReady={this.onChartReadyCallback}
        // onEvents={EventsDict}

    />
    </>
    
    
  )
    }

    export default FederalFundsRate;