#!/usr/bin/env python

import argparse
from subprocess import check_output
import src.funciones as fun
from src.generapdf import creaPDF2
import os
import json
import requests
import pandas as pd

def parse():
    parser = argparse.ArgumentParser(description='Introduces un producto y un año y analizo su producción en España y la población en ese momento')
    parser.add_argument('-i',dest='item',help="Introduce el producto que quieres analizar")
    parser.add_argument('-y',dest='year',default=1975, help="Año que quieres analizar")
    args = parser.parse_args()
    return args

def main():
    args = parse()
    item = args.item
    year = args.year
    print (args)
    fun.cargaDataSet()
    fun.filtraPais()
    fun.limpiaDataSet()
    fun.extraeDatos(item,year)
    hombres = fun.requestINEh(year)
    mujeres = fun.requestINEm(year)
    fun.extraeBonus(item,year)
    pobltot = fun.requestINEtot(year)
    fun.graficoDatos(item,year)
    fun.graficaPoblacion(mujeres,hombres)
    fun.graficaPoblacionBonus(pobltot)
    fun.graficoBonus(item,year)
    creaPDF2()

if __name__ == "__main__":
        main()