<p align="center">
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/200px-Python-logo-notext.svg.png" alt="react" width="50" height="50" />
</p>




<p align="center">
<img src="https://www.alphacast.io/images/alphacast.svg" alt="react" width="300" height="150" />
</p>



Alphacast es una start-up en crecimiento que se encuentra construyendo una plataforma para facilitar el análisis económico y financiero. Think GitHub for Economists. Recopila información de cientos de fuentes de datos. Oficinas de Estadística, Bancos Centrales, Tesorería. Mercados y fuentes privadas. Ajuste estacional, suavizado, filtrado e interpolación, % PIB, conversión de divisas, precios constantes, YoY, MoM, WoW, medias móviles y mucho más.


## Web Scraping + Transform + Load Data


En este trabajo se transforman las series temporales de los principales indices bursátiles internacionales a base 100 en enero de 2007 hasta el 31/01/2022. La idea principal del trabajo es poder comparar las series de tiempo principalmente durante los dos shock que se vivieron en el periodo analizado, la crisis subprime y el Covid-19.

Una vez terminado el primer trabajo se hace Web Scraping en la pagina [TradingEconomics](https://tradingeconomics.com/) y se recopilan datos macroeconomicos de la gran mayoria de los paises del mundo.


# Librerias Utilizadas


<ui>

<li>
{matplotlib}
</li>

<li>
{pandas_datareader}
</li>

<li>
{Pandas}
</li>

<li>
{alphacast}
</li>

</ui>



# Graficos finales:


Series Temporales

![.](plots/plot1.png)

PBI Per Capita

![.](plots/plot2.png)

Deuda / PBI

![.](plots/plot3.png)

Inflacion Interanual Paises Europa

![.](plots/plot4.png)

Inflacion Interanual Paises Asia

![.](plots/plot5.png)