#!/usr/bin/env python
import argparse
import src.funciones as fun
from src.generapdf import creaPDF2
import src.enviamail as env


def validaItem(it):
    correct_items = ['Grapes and products (excl wine)', 'Tomatoes and products', 'Marine Fish, Other', 'Olives (including preserved)', 'Fish, Body Oil', 'Sugar & Sweeteners', 'Cocoa Beans and products', 'Offals', 'Cassava and products', 'Pineapples and products', 'Pepper', 'Pigmeat', 'Eggs', 'Palmkernel Oil', 'Beans', 'Sweeteners, Other', 'Sesame seed', 'Wheat and products', 'Cream', 'Coconut Oil', 'Spices', 'Tea (including mate)', 'Poultry Meat', 'Lemons, Limes and products', 'Pelagic Fish', 'Sunflowerseed Oil', 'Aquatic Animals, Others', 'Oilcrops Oil, Other', 'Palm Oil', 'Rape and Mustard Oil', 'Peas', 'Oranges, Mandarines', 'Molluscs, Other', 'Roots, Other', 'Fruits - Excluding Wine', 'Soyabeans', 'Beer', 'Groundnuts (Shelled Eq)', 'Groundnut Oil', 'Cottonseed', 'Nuts and products', 'Cloves', 'Offals, Edible', 'Sesameseed Oil', 'Meat', 'Meat, Other', 'Freshwater Fish', 'Demersal Fish', 'Pulses', 'Animal fats', 'Maize and products', 'Oats', 'Oilcrops, Other', 'Cottonseed Oil', 'Olive Oil', 'Alcoholic Beverages', 'Aquatic Plants', 'Aquatic Products, Other', 'Barley and products', 'Spices, Other', 'Coconuts - Incl Copra', 'Dates', 'Rice (Milled Equivalent)', 'Vegetable Oils', 'Plantains', 'Milk - Excluding Butter', 'Fish, Seafood', 'Honey', 'Yams', 'Sweet potatoes', 'Wine', 'Crustaceans', 'Grapefruit and products', 'Cephalopods', 'Cereals - Excluding Beer', 'Apples and products', 'Rape and Mustardseed', 'Stimulants', 'Pimento', 'Starchy Roots', 'Treenuts', 'Mutton & Goat Meat', 'Beverages, Fermented', 'Cereals, Other', 'Pulses, Other and products', 'Oilcrops', 'Rye and products', 'Onions', 'Sorghum and products', 'Fruits, Other', 'Citrus, Other', 'Butter, Ghee', 'Potatoes and products', 'Fish, Liver Oil', 'Beverages, Alcoholic', 'Vegetables, Other', 'Maize Germ Oil', 'Bovine Meat', 'Millet and products', 'Sunflower seed', 'Soyabean Oil', 'Sugar (Raw Equivalent)', 'Coffee and products', 'Bananas', 'Vegetables', 'Fats, Animals, Raw']
    if it in correct_items:
        return it
    else:
        error = 'Inserte un producto válido, como por ejemplo'+str(correct_items)
        raise argparse.ArgumentTypeError(error)

def validaYear(ye):
    ye = int(ye)
    correct_years = list(range(1975,2013,1))
    if ye in correct_years:
        return ye
    else:
        error = 'Introduzca un año entre 1975 y 2013'
        raise argparse.ArgumentTypeError(error)

def parse():
    parser = argparse.ArgumentParser(description='Introduces un producto y un año y analizo su producción en España y la población en ese momento')
    parser.add_argument('-i',dest='item',help="Introduce el producto que quieres analizar", type=validaItem)
    parser.add_argument('-y',dest='year',default=1975, help="Año que quieres analizar", type=validaYear)
    args = parser.parse_args()
    return args

def main():
    args = parse()
    item = args.item
    year = args.year
    print (args)
    fun.cargaDataSet() #carga el dataset
    fun.filtraPais() #filtra el dataset para que sea de España
    fun.limpiaDataSet()
    fun.extraeDatos(item,year) #extrae los datos del producto y año que le pidas
    hombres = fun.requestINEh(year) #request a la api del INE población hombres
    mujeres = fun.requestINEm(year) #request a la api del INE población mujeres
    pobltot = fun.requestINEtot(year) #request población total en rango de 10 años posteriores
    fun.graficoDatos(item,year) #dibuja la gráfica food/feed producto
    fun.graficaPoblacion(mujeres,hombres) #dibuja la gráfica de población
    fun.graficaPoblacionBonus(pobltot) #dibuja la gráfica de evolución población
    fun.graficoBonus(item,year) #dibuja la gráfica de evolución del producto food/feed en 10 años
    creaPDF2() #crea un pdf y lo guarda
    env.enviaMail() #envía un e-mail con el reporte en pdf adjunto
    
if __name__ == "__main__":
        main()