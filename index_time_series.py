

# Importando librerias y ordenando el conjunto de datos



import pandas_datareader as web
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime
plt.style.use('fivethirtyeight')




indices = ['^GSPC', '^IXIC', '^IBEX', '^GDAXI', '^N225', '^DJI', '^BVSP', '^MXX','^HSI']

df = web.DataReader(indices, data_source='yahoo',
                    start='2007-01-01',
                    end='2022-01-31')['Close']

#%%


# El metodo de ffill, front filling, significa relleno frontal, le asigna al valor faltante el valor del periodo posterior, muy util para series temporales. El otro metodo es el bfill donde usamos el periodo previo.

df= df.fillna(method='ffill')

df= df.fillna(method='bfill')


#%%

# Transofmacion del data set base 100 

df = df.div(df.iloc[0]).mul(100)


 
df = df.round(decimals=2)

df['date'] =  df.index

df['date'] = df['date'].dt.date


df.columns = ['S&P_500', 'Nasdaq', 'IBEX_35', 'DAX', 'Nikkei' ,'Dow_Jones', 'BOVESPA', 'IPC_Mexico', 'HANG_SENG_INDEX', 'Date']


df.index = np.arange(0, len(df))


df['Date'] = pd.to_datetime(df.Date).dt.strftime('%Y-%m-%d')



#%%


# Api Key Alphacast

with open('C:/Users/maxig/Desktop/Carpetas/Trabajos en Python/Alphacast/New Work/Key.txt') as claves: keys = [clave for clave in claves]
print(keys)

key = keys[0]

# Iniciando Alphacast

from alphacast import Alphacast

alphacast = Alphacast(key)



#%%


alphacast.repository.read_all()


alphacast.datasets.create('Indices Bursatiles desde 2007', 1272, 'Principales indices bursatiles del mundo con base 100 en enero de 2007 hasta el 31/01/2022')


#%%

df['country'] = 'Index'

df = df[['Date', 'country', 'S&P_500', 'Nasdaq', 'IBEX_35', 'DAX', 'Nikkei' ,'Dow_Jones', 'BOVESPA', 'IPC_Mexico', 'HANG_SENG_INDEX']]

#%%

alphacast.datasets.dataset(14940).initialize_columns(dateColumnName = "Date", 
                                                            entitiesColumnNames=['country'], 
                                                            dateFormat= "%Y-%m-%d")

#%%

alphacast.datasets.dataset(14940).upload_data_from_df(df,
                                                      deleteMissingFromDB = False,
                                                      onConflictUpdateDB = False,
                                                      uploadIndex=False)

#%%

alphacast.datasets.dataset(14940).processes()


#%%

