import pandas as pd
import yfinance as yf
import plotly.express as px
import plotly.graph_objects as go
import time

tsla = yf.download('TSLA', period = '18d', interval='1d')
musktweets = pd.read_json('tweets_from_elon.json')

print(musktweets['created_at'].value_counts())

fig = go.Figure()
fig.add_trace(go.Scatter(y=tsla['Close'], mode = 'lines'))

fig.update_layout(title = 'TSLA Data', yaxis_title = 'Close price', xaxis_title = 'Days')

fig.show()