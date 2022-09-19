import React from 'react';
//import { useState } from 'react';
import { Button, Layout, message, Col, Row } from 'antd';
import Login from '../components/Login';
import Register from '../components/Register';

import { logout } from '../utils';
import { Menu } from 'antd';
import logo from '../assets/logo.png';
import './homePage.css';
import RealGDPQA from '../visualization/RealGDPQA'
import RealGDPperCapita from '../visualization/RealGDPperCapita'
import TreasuryYield3M from '../visualization/TreasuryYield3M'
import TreasuryYield2Y from '../visualization/TreasuryYield2Y'
import TreasuryYield5Y from '../visualization/TreasuryYield5Y'
import TreasuryYield7Y from '../visualization/TreasuryYield7Y'
import TreasuryYield10Y from '../visualization/TreasuryYield10Y'
import TreasuryYield30Y from '../visualization/TreasuryYield30Y'
import FederalFundsRate from '../visualization/FederalFundsRate'
import CPI from '../visualization/CPI'
import Inflation from '../visualization/Inflation'
import InflationExpectation from '../visualization/InflationExpectation'
import ConsumerSentiment from '../visualization/ConsumerSentiment'
import Durables from '../visualization/Durables'
import RetailSales from '../visualization/RetailSales'
import Unemployment from '../visualization/Unemployment'
import NonfarmPayroll from '../visualization/NonfarmPayroll'
import IncomeStatement from '../visualization/IncomeStatement'
import BalanceSheet from '../visualization/BalanceSheet'
import CashFlow from '../visualization/CashFlow'
import Earnings from '../visualization/Earnings'
import Overview from '../visualization/Overview'
import News from '../visualization/News'
import EarningsCalendar from '../visualization/EarningsCalendar'
import OptionsQuote from '../visualization/OptionsQuote';
import OptionsChain from '../visualization/OptionsChain';
import EconomicCalendarList from '../visualization/EconomicCalendarList';

const { Header, Content, Sider } = Layout;
const { SubMenu } = Menu;
//const [symbol, setSymbol] = useState([]);
 
class homePage extends React.Component {
  state = {
    loggedIn: false,
    key: "0",
  }
 
  signinOnSuccess = () => {
    this.setState({
      loggedIn: true
    })
  };
 
  signoutOnClick = () => {
    logout()
      .then(() => {
        this.setState({
          loggedIn: false
        })
        message.success(`Successfull signed out`);
      }).catch((err) => {
        message.error(err.message);
      })
  }

  
 
  render = () => (
    <Layout className='homePage-Layout'>
      <Header>
      <Row justify="space-between">
        {/* <Col>
          <Menu theme="dark" mode="horizontal" defaultSelectedKeys={['2']}>
              <Menu.Item key="1">nav 1</Menu.Item>
              <Menu.Item key="2">nav 2</Menu.Item>
              <Menu.Item key="3">nav 3</Menu.Item>
          </Menu>
        </Col> */}

         <div>
           <img src={logo} alt='logo' width="50%" />
        </div>
            
        <Col>
          {
            this.state.loggedIn ? 
            <Button shape="round" onClick={this.signoutOnClick}>
              Logout</Button> :
            (
              <>
                <Login onSuccess={this.signinOnSuccess} />
                <Register />
              </>
            )
          }
        </Col>

      </Row>
      </Header>

      <Layout >
        <Sider className="sider" width={300}  >
        

          <Menu 
          
            mode="inline"
            defaultSelectedKeys={null}
            defaultOpenKeys={['Economic Indicators']}
            theme = "dark"
            style={{ 
              marginTop: '10px',
              
            }}
            onSelect={e=>this.setState({
              key: e.key
            })}
            
            // style={{ marginTop: '10px' }}
          >
            <SubMenu key="Economic Indicators"  title="Economic Indicators">
              <Menu.Item key="EconomicCalendar" >Economic Calendar</Menu.Item>
              <Menu.Item key="RealGDPQA" >Real GDP Quarterly, Annual</Menu.Item>
              <Menu.Item key="RealGDPperCapita">Real GDP per Capita</Menu.Item>
              <SubMenu key="TreasuryYield" title="Treasury Yield">
                <Menu.Item key="TreasuryYield3M">3 Months</Menu.Item>
                <Menu.Item key="TreasuryYield2Y">2 Years</Menu.Item>
                <Menu.Item key="TreasuryYield5Y">5 Years</Menu.Item>
                <Menu.Item key="TreasuryYield7Y">7 Years</Menu.Item>
                <Menu.Item key="TreasuryYield10Y">10 Years</Menu.Item>
                <Menu.Item key="TreasuryYield30Y">30 Years</Menu.Item>
              </SubMenu>
              
              <Menu.Item key="FederalFundsRate">Federal Funds Rate</Menu.Item>
              <Menu.Item key="CPI">CPI</Menu.Item>
              <Menu.Item key="Inflation">Inflation</Menu.Item>
              <Menu.Item key="InflationExpectation">Inflation Expectation</Menu.Item>
              <Menu.Item key="ConsumerSentiment">Consumer Sentiment</Menu.Item>
              <Menu.Item key="RetailSales">Retail Sales</Menu.Item>
              <Menu.Item key="Durables">Durables</Menu.Item>
              <Menu.Item key="Unemployment">Unemployment</Menu.Item>
              <Menu.Item key="NonfarmPayroll">Nonfarm Payroll</Menu.Item>
            </SubMenu>
            <SubMenu key="sub2"  title="Fundamental Data">
              <Menu.Item key="IncomeStatement">Income Statement</Menu.Item>
              <Menu.Item key="BalanceSheet">Balance Sheet</Menu.Item>
              <Menu.Item key="CashFlow">Cash Flow</Menu.Item>
              <Menu.Item key="Earnings">Earnings</Menu.Item>
              <Menu.Item key="Overview">Company Overview</Menu.Item>
              <Menu.Item key="News">News</Menu.Item>
              <Menu.Item key="EarningsCalendar">Earnings Calendar</Menu.Item>
            </SubMenu>
            <SubMenu key="sub3" title="Streaming Options Data">
              <Menu.Item key="OptionsChain">Options Chain</Menu.Item>
              <Menu.Item key="OptionsQuote">Options Quote/Trade</Menu.Item>
            </SubMenu>

          </Menu>
        </Sider>
        <Layout style={{ padding: '24px' }}>
          <Content
            className="site-layout-background"
            style={{
              padding: 24,
              margin: 0,
              height: 800,
              overflow: 'auto'
            }}
          >
            {/* <CustomSearch/> */}
        <> {this.state.key === "EconomicCalendar" && <EconomicCalendarList /> }
           {this.state.key === "RealGDPQA" && <RealGDPQA /> }
           {this.state.key === "RealGDPperCapita" && <RealGDPperCapita /> }
           {this.state.key === "TreasuryYield3M" && <TreasuryYield3M /> }
           {this.state.key === "TreasuryYield2Y" && <TreasuryYield2Y /> }
           {this.state.key === "TreasuryYield5Y" && <TreasuryYield5Y /> }
           {this.state.key === "TreasuryYield7Y" && <TreasuryYield7Y /> }
           {this.state.key === "TreasuryYield10Y" && <TreasuryYield10Y /> }
           {this.state.key === "TreasuryYield30Y" && <TreasuryYield30Y /> }
           {this.state.key === "FederalFundsRate" && <FederalFundsRate /> }
           {this.state.key === "CPI" && <CPI /> }
           {this.state.key === "Inflation" && <Inflation /> }
           {this.state.key === "InflationExpectation" && <InflationExpectation /> }
           {this.state.key === "ConsumerSentiment" && <ConsumerSentiment /> }
           {this.state.key === "RetailSales" && <RetailSales /> }
           {this.state.key === "Durables" && <Durables /> }
           {this.state.key === "Unemployment" && <Unemployment /> }
           {this.state.key === "NonfarmPayroll" && <NonfarmPayroll /> }
           
           {this.state.key === "IncomeStatement" && <IncomeStatement /> }
           {this.state.key === "BalanceSheet" && <BalanceSheet /> }
           {this.state.key === "CashFlow" && <CashFlow /> }
           {this.state.key === "Earnings" && <Earnings /> }
           {this.state.key === "Overview" && <Overview /> }
           {this.state.key === "News" && <News /> }
           {this.state.key === "EarningsCalendar" && <EarningsCalendar /> }
           {this.state.key === "OptionsChain" && <OptionsChain /> } 
           {this.state.key === "OptionsQuote" && <OptionsQuote /> } 
           </> 
          </Content>
        </Layout>
      </Layout>
    </Layout>
  )
}
 
export default homePage;
