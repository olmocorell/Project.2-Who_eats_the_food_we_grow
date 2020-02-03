import os
from dotenv import load_dotenv
import json
import requests
import re
import pandas as pd
import matplotlib.pyplot as plt
import datetime
lista = [17961,17962,17963,17964]
toneladas = 0


def cargaDataSet():
    global data
    data = pd.read_csv("input/FAO.csv",encoding='cp1252')
    return data

def filtraPais():
    global datasp
    datasp = data[(data["Area"]== "Spain")]
    return datasp

def limpiaDataSet():
    global datasp
    for a in lista:
        datasp = datasp.drop(a)
    datasp = datasp.drop_duplicates()

def extraeDatos(item,year):
    global toneladas
    data_filter = datasp[datasp["Item"] == f"{item}"]
    toneladas = list(data_filter[f"Y{year}"])
    return toneladas

def graficoDatos(item,year):
    data_filter = datasp[datasp["Item"] == f"{item}"]
    toneladas = list(data_filter[f"Y{year}"])
    total = sum(toneladas)
    if len(toneladas) == 1:
        toneladas = [0] + list(data_filter[f"Y{year}"])
    labels = "Feed","Food"
    colors = ['lightseagreen','hotpink']
    explode = (0.1, 0) 
    plt.pie(toneladas, labels=labels,colors=colors,explode=explode,
    autopct='%1.1f%%', shadow=True, startangle=140)
    plt.title(f"{item} {total}k t. en el año {year}")
    plt.savefig("graficodatos")
    print(f"{toneladas[0]}k tonnes Feed - {toneladas[1]}k tonnes Food")

def graficoBonus(item,year):
    
    col_food = []
    col_feed = []
    year = int(year)
    if year < 2004:
        years = list(range(year,(year+10)))
    else:
        years = list(range(year,2014))
    bonus_filter = datasp[datasp['Item']== f"{item}"]
    if (len(bonus_filter)) == 1:
        indice = bonus_filter.index[0]
        if bonus_filter.Element[indice] == 'Food':
            for ye in years:
                ton_bonus = list(bonus_filter[f"Y{ye}"])
                for ton in ton_bonus:
                    col_food.append(ton)
                    col_feed.append(0)
        elif bonus_filter.Element[indice] == 'Feed':
            for ye in years:
                ton_bonus = list(bonus_filter[f"Y{ye}"])
                for ton in ton_bonus:
                    col_food.append()
                    col_feed.append(ton)
    else:
        for ye in years:
            ton_bonus = list(bonus_filter[f"Y{ye}"])

    grafic = pd.DataFrame(col_feed, index=years, columns=["Feed"])
    grafic["Food"] = col_food
    grafic.plot.bar(color = ['lightseagreen','hotpink'])
    plt.title(f"Evolución de la producción desde {year}")
    plt.savefig("graficodatosbonus")

def requestINEh(year):
    global resh
    date = f"{year}0101:{year}1231"
    codigo = "CP300335"
    url= f'http://servicios.ine.es/wstempus/js/ES/DATOS_SERIE/{codigo}?date={date}'
    print(f"Requesting data from {url}")
    resh = requests.get(url)
    if resh.status_code != 200:
        print(resh.text)
        raise ValueError("Bad Response")
    return resh.json()

def requestINEm(year):
    global resm
    date = f"{year}0101:{year}1231"
    codigo = "CP300334"
    url= f'http://servicios.ine.es/wstempus/js/ES/DATOS_SERIE/{codigo}?date={date}'
    print(f"Requesting data from {url}")
    resm = requests.get(url)
    if resm.status_code != 200:
        print(resm.text)
        raise ValueError("Bad Response")
    return resm.json()

def requestINEtot(year):
    year = int(year)
    if year < 2004:
        date = f"{year}0101:{year+10}1231"
    else:
        date = f"{year}0101:{2013}1231"
    codigo = "CP335"
    url= f'http://servicios.ine.es/wstempus/js/ES/DATOS_SERIE/{codigo}?date={date}'
    print(f"Requesting data from {url}")
    res = requests.get(url)
    if res.status_code != 200:
        print(res.text)
        raise ValueError("Bad Response")
    return res.json()

def graficaPoblacion(homb,muj):
    global poblacionm
    global poblacionh
    for m in muj['Data']:
        fecha = datetime.date.fromtimestamp(m['Fecha'] // 1000)
        poblacionm = m['Valor']
    for h in homb['Data']:
        poblacionh = h['Valor']
    total = poblacionh + poblacionm
    fig = plt.figure(u'Gráfica de barras') # Figure
    ax = fig.add_subplot(111) # Axes
    nombres = [f"Mujeres {poblacionm}",f"Hombres {poblacionh}"]
    datos = [poblacionm,poblacionh]
    colors = ["darkmagenta", "lightsalmon"]
    xx = range(len(datos))
    ax.bar(xx, datos, width=0.8, align='center',color= colors)
    ax.set_xticks(xx)
    ax.set_xticklabels(nombres)
    plt.title(f"Total de población: {total} en {fecha}")
    plt.savefig("graficopoblacion")

def graficaPoblacionBonus(pobltot):
    poblaciones = []
    years = []
    for pers in pobltot['Data']:
        if pers['FK_Periodo'] == 27:
            poblaciones.append(pers['Valor'])
    for pers in pobltot['Data']:
        if pers['FK_Periodo'] == 27:
            years.append(pers['Anyo'])
    graficbonus = pd.DataFrame(poblaciones, index=years, columns=["Poblacion"])
    graficbonus.plot.bar(color = 'yellowgreen')
    plt.title(f"Evolución de la población")
    plt.savefig("graficopoblacionbonus")
