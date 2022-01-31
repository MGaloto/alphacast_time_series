
import math
import pandas_datareader as web
import numpy as np
import pandas as np
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')


#S&P 500, nasdaq composite, IBEX 35, DAX, Nikkei ,Dow Jones, IBOVESPA, IPC MEXICO, HANG SENG INDEX 

indices = ['^GSPC', '^IXIC', '^IBEX', '^GDAXI', '^N225', '^DJI', '^BVSP', '^MXX','^HSI']

df = web.DataReader(indices, data_source='yahoo',
                    start='2007-01-01',
                    end='2022-01-31')['Close']


df.columns = ['S&P_500', 'Nasdaq', 'IBEX_35', 'DAX', 'Nikkei' ,'Dow_Jones', 'BOVESPA', 'IPC_Mexico', 'HANG_SENG_INDEX']




#%%

# El metodo de ffill, front filling, significa relleno frontal, le asigna al valor faltante el valor del periodo posterior, muy util para series temporales. El otro metodo es el bfill donde usamos el periodo previo.

df= df.fillna(method='ffill')

df= df.fillna(method='bfill')


#%%