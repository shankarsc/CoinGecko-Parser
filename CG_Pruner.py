from pycoingecko import CoinGeckoAPI
import pandas as pd
cg = CoinGeckoAPI()

def get_price(ticker, denom_currency, days):
    """
    Splits the dataset returned from CoinGecko into Date and Price columns
    Define the ticker, denominated currency, and number of days of data required
    """
    dataset = pd.DataFrame(cg.get_coin_market_chart_by_id(ticker, denom_currency, days))
    dataset = pd.DataFrame(dataset['prices'].to_list(), columns=['Date', 'Price'])
    dataset['Date'] = pd.to_datetime(dataset['Date'], unit='ms')
    dataset = dataset.set_index('Date')

    return dataset

def get_volume(ticker, denom_currency, days):
    """
    Splits the dataset returned from CoinGecko into Date and Volume columns
    Define the ticker, denominated currency, and number of days of data required
    """
    dataset = pd.DataFrame(cg.get_coin_market_chart_by_id(ticker, denom_currency, days))
    dataset = pd.DataFrame(dataset['total_volumes'].to_list(), columns=['Date', 'Volume'])
    dataset['Date'] = pd.to_datetime(dataset['Date'], unit='ms')
    dataset = dataset.set_index('Date')

    return dataset

def get_market_cap(ticker, denom_currency, days):
    """
    Splits the dataset returned from CoinGecko into Date and Volume columns
    Define the ticker, denominated currency, and number of days of data required
    """
    dataset = pd.DataFrame(cg.get_coin_market_chart_by_id(ticker, denom_currency, days))
    dataset = pd.DataFrame(dataset['market_caps'].to_list(), columns=['Date', 'Market Cap'])
    dataset['Date'] = pd.to_datetime(dataset['Date'], unit='ms')
    dataset = dataset.set_index('Date')

    return dataset

def get_daily_change(data):
    """
    Returns the daily change for the selected column
    """
    return (data.shift(-1) - data).dropna()

def get_prct_change(data):
    """
    Obtain the daily percentage change for the price data 
    """
    return ((data.shift(-1)-data)/data).dropna()