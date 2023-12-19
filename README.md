# Python Playground

<p align="justify">Welcome to Python Playground! This repository is a personal journey through the fascinating world of Python, showcasing learnings, experiments, and insights into Python's documentation, the standard library, and various external libraries. Whether you're a beginner eager to explore Python's capabilities or an experienced developer looking for new tricks and tools, this repository is designed to offer something valuable for everyone.</p>

## Contents

<ul>
  <li><div align="justify"><code>YahooDataHandler</code> that allows to get data directly from Yahoo Finance website and update the latest "bar" in a live manner.</div></li>
  <li><div align="justify"><code>HistoricMySQLDataHandler</code> designed to read a MySQL database for each requested symbol from disk, and provides an interface to obtain the "latest" bar in a manner identical to a live trading interface.</div></li>
  <li><div align="justify"><code>MovingAverageCrossOverStrat</code> to carry out a basic Moving Average Crossover strategy with a short/long simple weighted moving average.</div></li>
  <li><div align="justify"><code>ETFDailyForecastStrategy</code> to carry out a forecast prediction of the price of an ETF on next day, and enter/exit trades based on that prediction.</div></li>
  <li><div align="justify"><code>OLSMRStratedy</code> to generate signals on a trading pair (should follow a mean reversion pattern to be tested), using rolling OLS method to find the best hedging ratio between 2 assets timeseries. Position signals are then generated based on exceeding z_scores, whether we are currently having positions in the market, or needing to exit.</div></li>
  
</ul>

## Getting Started

<p align="justify">These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.</p>

### Prerequisites

<p align="justify">You need <strong>Python 3.x</strong> to run the following code.  You can have multiple Python versions (2.x and 3.x) installed on the same system without problems. Python needs to be first installed then <strong>SciPy</strong> and <strong>pymysql</strong> as there are dependencies on packages.</p>

In Ubuntu, Mint and Debian you can install Python 3 like this:

    sudo apt-get install python3 python3-pip

### Prerequisites

<p align="justify">You need <strong>Python 3.x</strong> to run the following code.  You can have multiple Python versions (2.x and 3.x) installed on the same system without problems. Python needs to be first installed then <strong>SciPy</strong> and <strong>pymysql</strong> as there are dependencies on packages.</p>

In Ubuntu, Mint and Debian you can install Python 3 like this:

    sudo apt-get install python3 python3-pip
