* Some API keys that require advanced subscriptions were expired, which will affect normal use of some functionalities.
* Regarding the API key substitution, please see the final documentation.

## Title
A web application to visualize historical lookup and streaming data in financial market.

## Team:
Jundong (Ted) Chen - Leader: tedjdbusiness@gmail.com
Qiyuan Cheng: qiyuanc3@illinois.edu
Sparshdeep Singh: ss85@illinois.edu
Fang (Kevin) Li: fangli3@illinois.edu

## Project Description

This document is the final report of a semester long project for "IE498 - High Frequency Trading" under [Professor David Lariviere](https://davidl.web.illinois.edu/).

The web application utilizes [`Django Rest API Framework`](https://www.django-rest-framework.org/) and [`Cors Header`](https://github.com/adamchainz/django-cors-headers) to connect the [`React`](https://reactjs.org/) frontend and the [`Django`](https://www.djangoproject.com/) backend. Upon frontend, we use [`antd`](https://ant.design/docs/react/introduce) library for UI implementation and we use Django default [`Sqlite`](https://www.sqlite.org/index.html) database to store historical lookup data from external API in backend.

There are three major external API in this application: [`Alpha Vantage`](https://www.alphavantage.co/documentation/) (Historical Lookup Data), [`Polygon`](https://polygon.io/docs/options/getting-started) (Streaming Options Quote and Trade Data), and [`Investpy`](https://investpy.readthedocs.io/_info/introduction.html) (Economic Calendar Data). Users will be able to visualize and interact with both historical lookup data and streaming options data in frontend.

**The historical lookup data includes:**

Macro Economic Data:
- Economic Calendar
- Real GDP Quarterly/Annual
- Real GDP per Capita
- Daily/Weekly/Monthly Treasury Yield 3M/2Y/5Y/7Y/10Y/30Y
- Daily/Weekly/Monthly Federal Funds Rate
- Monthly/Semiannual CPI
- Inflation
- Inflation Expectation
- Consumer Sentiment
- Retail Sales
- Durables
- Unemployment
- Nonfarm Payroll

Company Fundamental Data:
- Quarterly/Annual Income Statement
- Quarterly/Annual Balance Sheet
- Quarterly/Annual Cash Flow
- Earning History
- Company Overview
- Related News
- Earning Calendar
- Options Chain

**The streaming data includes:**

Options Data:
- Options Quote
- Options Trade
