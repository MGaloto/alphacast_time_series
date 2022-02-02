
#--------------------------------------------------------------------------------------------------
# Se utilizara BeautifoulSoup y Selenium para hacer Scraping Web y obtener datos de la pagina:
# https://tradingeconomics.com/
# El data set final esta en: https://www.alphacast.io/datasets/8133
#--------------------------------------------------------------------------------------------------



# 1. Importar librerias

from bs4 import BeautifulSoup as BS
from selenium import webdriver
from time import sleep
import csv
from datetime import date
import pandas as pd

# 2. Ejecutar URL de Trading Economics

options = webdriver.ChromeOptions()
options.add_argument("--incognito")
driver = webdriver.Chrome('chromedriver.exe', options = options)
url = 'https://tradingeconomics.com/'
driver.get(url)


sleep(5)


# 2. Click en + para expandir la pagina.

script_boton = '''
            let boton = document.querySelector('[class="btn btn-default"]')
    if (boton){
          boton.click()
      }
    else {
        return "False"}'''

while driver.execute_script(script_boton) != "False": sleep(3)
print('No hay mas boton para extender la pagina')



# Scraping


html = driver.execute_script('return document.documentElement.outerHTML')
dom= BS(html, 'html.parser')
index_total = dom.find_all("td",{"align":"left"})


# Tabla para el CSV final

tabla = [['Date','Ranking PBI', 'country', 'GDP en Mill', 'Interes Rate', 'Inflation Rate', 'Debt/GDP', 'Population', 'GDP Pc']]


# Recorriendo la pagina

sleep(2)
ranking = 0
for country in index_total:
    pais = country.text.strip()
    gdp = country.find_next('td').text.strip()
    gdp = int(gdp) 
    interes_rate = country.find_next('td').find_next('td').find_next('td').find_next('td').text.strip().replace('%', '')
    inflation_rate = country.find_next('td').find_next('td').find_next('td').find_next('td').find_next('td').text.strip().replace('%', '')
    debt_pbi = country.find_next('td').find_next('td').find_next('td').find_next('td').find_next('td').find_next('td').find_next('td').find_next('td').text.strip().replace('%', '')
    population = country.find_next('td').find_next('td').find_next('td').find_next('td').find_next('td').find_next('td').find_next('td').find_next('td').find_next('td').find_next('td').find_next('td').text.strip()
    population = int(round(float(population) * 1000000,2))
    pib_pc = round((gdp * 1000000000) / population,2)
    ranking += 1
    Date = date.today()
    variables = [Date, ranking, pais, gdp, interes_rate, inflation_rate, debt_pbi, population, pib_pc]
    tabla.append(variables)
    print('\nRanking PBI: ', ranking,
          '\nPais: ',pais, 
          '\nPbi x Millon: ', gdp,
          '\nInteres: ',interes_rate, '%',
          '\nInflacion: ', inflation_rate, '%',
          '\nDeuda/PBI', debt_pbi, '%',
          '\nPoblacion: ', population,
          '\nPbi PC: ', pib_pc,
          '\nAño: ', Date)

    
# Guardando el CSV

with open('paises.csv', 'w', newline = '') as paises:
    salida = csv.writer(paises)
    salida.writerows(tabla)

#%%


# Abrimos el CSV con pandas


df_country = pd.read_csv('paises.csv')

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


alphacast.datasets.create('Agregados Macroeconomicos de 181 paises', 1272, 'Agregados macroeconomicos a febrero de 2022. Pbi, Tasa de Interes, Tasa de Inflacion, Deuda/PBI, Poblacion, Pbi Pc')


#%%


df = df_country[['Date','country','Ranking PBI', 'GDP en Mill', 'Interes Rate', 'Inflation Rate', 'Debt/GDP', 'Population', 'GDP Pc']]



#%%

alphacast.datasets.dataset(15173).initialize_columns(dateColumnName = "Date", 
                                                            entitiesColumnNames=['country'], 
                                                            dateFormat= "%Y-%m-%d")

#%%

alphacast.datasets.dataset(15173).upload_data_from_df(df,
                                                      deleteMissingFromDB = False,
                                                      onConflictUpdateDB = False,
                                                      uploadIndex=False)

#%%

alphacast.datasets.dataset(15173).processes()


#%%











