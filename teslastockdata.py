import yfinance as yf
import pandas as pd

tsla = yf.download('TSLA', period = '19d', interval='1d')

tsla.to_csv('tsladata.csv', encoding='utf-8', index=False)
