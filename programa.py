import src.funciones as fun
import os
from dotenv import load_dotenv
import json
import requests
import re
import pandas as pd
resm = ""


fun.cargaDataSet()
fun.filtraPais()
fun.limpiaDataSet()

item = input(str("Introduzca el elemento a buscar: "))
year = input("Ahora introduzca el año de la búsqueda: ")

fun.extraeDatos(item,year)
fun.graficoDatos(item,year)
hombres = fun.requestINEh(year)
mujeres = fun.requestINEm(year)
fun.graficaPoblacion(mujeres,hombres)