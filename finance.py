import yfinance as yf  
import pandas as pd    
import numpy as np     
import matplotlib.pyplot as plt  

# Define parametros
ticker = "AAPL"  # Apple stock
start_date = "2010-01-01"
end_date = "2020-01-01"

data = yf.download(ticker, start=start_date, end=end_date)

print(data.head())

short_window = 50  # Short-term SMA
long_window = 200  # Long-term SMA

data['SMA50'] = data['Close'].rolling(window=short_window).mean()
data['SMA200'] = data['Close'].rolling(window=long_window).mean()


data['Signal'] = 0  
data.loc[data['SMA50'] > data['SMA200'], 'Signal'] = 1  #Compra
data.loc[data['SMA50'] < data['SMA200'], 'Signal'] = -1  #Vende

#Cria position para evitar bias
data['Position'] = data['Signal'].shift(1)

#Calcula o percentual de alteracao de preco
data['Daily Return'] = data['Close'].pct_change()

#Calcula retorno baseado na estrategia
data['Strategy Return'] = data['Position'] * data['Daily Return']

#Calcula retorno cumulativo
data['Cumulative Market Return'] = (1 + data['Daily Return']).cumprod()
data['Cumulative Strategy Return'] = (1 + data['Strategy Return']).cumprod()

plt.figure(figsize=(14, 7))
plt.plot(data['Close'], label='Close Price', alpha=0.5)
plt.plot(data['SMA50'], label='SMA50', alpha=0.75)
plt.plot(data['SMA200'], label='SMA200', alpha=0.75)
plt.title(f"{ticker} Price and Moving Averages")
plt.legend()
plt.show()

plt.figure(figsize=(14, 7))
plt.plot(data['Cumulative Market Return'], label='Market Return', alpha=0.75)
plt.plot(data['Cumulative Strategy Return'], label='Strategy Return', alpha=0.75)
plt.title("Cumulative Returns")
plt.legend()
plt.show()

total_strategy_return = data['Cumulative Strategy Return'].iloc[-1] - 1
total_market_return = data['Cumulative Market Return'].iloc[-1] - 1

print(f"Total Strategy Return: {total_strategy_return:.2%}")
print(f"Total Market Return: {total_market_return:.2%}")
