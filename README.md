![Foto_de_Frutas](https://github.com/agalvezcorell/Project.2-pipelines-project/blob/master/output/portada3.jpg)

# ¿Quién se come lo que cultivamos?

## Análisis de producción de alimentos en España por años

En este proyecto utilizo el dataset [Who eats the food we grow?](https://www.kaggle.com/dorbicycle/world-foodfeed-production)
La Organización de las Naciones Unidas para la Agricultura y la Alimentación proporciona acceso gratuito a los datos de la agricultura y la alimentación de más de 245 países y territorios, desde el año 1961 hasta la actualización más reciente (depende del conjunto de datos).
Se clasifican:
Food - se refiere a la cantidad total de alimento disponible como alimento humano durante el período de referencia.
Feed - se refiere a la cantidad de alimento disponible para alimentar al ganado y las aves de corral durante el período de referencia.

### Datasets y uso de APIs

Abriendo el programa con la terminar e introduciéndole un alimento de la lista y un año comprendido entre 1975 y 2013, el script que he realizado con Python3 realiza una consulta en tiempo real a la API del Instituto Nacional de Estadística español para aportar información a la que ya contiene el dataset.

El resultado es un archivo pdf generado que contiene gráficos que muestran:
- Las toneladas del alimento producidas para alimento humano y animal.
- La población en ese año en España y una división entre hombres y mujeres.
- La evolución de la producción de ese producto en los 10 años siguientes.
- Un gráfico de barras con el crecimiento de la población en los 10 años siguientes.
### Ejemplo de ejecución del programa
Para ejecutar el programa, es necesario llamarlo desde la terminal de la siguiente manera: python3 producto.py
Y añadirle las flags con los argumentos a buscar: -i"Item" (siendo el producto) -y"año" (siendo el año)

Ejemplo de ejecución:

```python3 producto.py -i'Cereals, Other' -y1987```

Los años válidos son entre 1975 y 2013.

### Productos aportados en el dataset que se pueden consultar:

- Barley and products
- Stimulants
- Maize Germ Oil
- Grapefruit and products
- Pigmeat
- Grapes and products (excl wine)
- Groundnut Oil
- Alcoholic Beverages
- Cereals, Other
- Aquatic Plants
- Vegetables
- Meat, Other
- Milk - Excluding Butter
- Freshwater Fish
- Peas
- Butter, Ghee
- Crustaceans
- Beverages, Alcoholic
- Cottonseed Oil
- Apples and products
- Vegetable Oils
- Cream
- Sweet potatoes
- Rye and products
- Spices, Other
- Pelagic Fish
- Roots, Other
- Cocoa Beans and products
- Palm Oil
- Fish, Seafood
- Coconut Oil
- Oilcrops
- Meat
- Fish, Body Oil
- Soyabean Oil
- Plantains
- Bananas
- Lemons, Limes and products
- Oranges, Mandarines
- Sugar (Raw Equivalent)
- Coffee and products
- Sweeteners, Other
- Marine Fish, Other
- Soyabeans
- Honey
- Sunflowerseed Oil
- Pulses
- Cottonseed
- Sesameseed Oil
- Starchy Roots
- Vegetables, Other
- Mutton & Goat Meat
- Cassava and products
- Oilcrops, Other
- Cereals - Excluding Beer
- Animal fats
- Aquatic Animals, Others
- Sesame seed
- Sunflower seed
- Offals
- Wheat and products
- Bovine Meat
- Fats, Animals, Raw
- Tomatoes and products
- Olives (including preserved)
- Pineapples and products
- Beans
- Coconuts - Incl Copra
- Demersal Fish
- Cephalopods
- Spices
- Fruits - Excluding Wine
- Millet and products
- Onions
- Offals, Edible
- Aquatic Products, Other
- Maize and products
- Cloves
- Rape and Mustard Oil
- Sorghum and products
- Tea (including mate)
- Fruits, Other
- Dates
- Citrus, Other
- Treenuts
- Pepper
- Yams
- Olive Oil
- Pimento
- Oats
- Rice (Milled Equivalent)
- Groundnuts (Shelled Eq)
- Pulses, Other and products
- Oilcrops Oil, Other
- Fish, Liver Oil
- Potatoes and products
- Nuts and products
- Poultry Meat
- Beer
- Molluscs, Other
- Eggs
- Palmkernel Oil
- Beverages, Fermented
- Wine
- Rape and Mustardseed
- Sugar & Sweeteners