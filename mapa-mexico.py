## PASO 1: Importar librerías
import pandas as pd
import requests
import plotly.express as px

## PASO 2: Abrir archivo de datos origen utilizando la librería pandas
df = pd.read_csv('CASOS_CONFIRMADOS_COVID19_MEXICO.csv')
print(df)

## PASO 3: Importar el archivo geojson que tiene la descripción del mapa de México con el cual se realizará el cruce
## para mapear el mapa.
geojsonurl = 'https://raw.githubusercontent.com/angelnmara/geojson/master/mexicoHigh.json'
regiones_mexico_geojson=requests.get(geojsonurl).json()


## PASO 4: 
## Generar el grafico mapa que tendra como datos origen, el geojson del mapa de mécico, los datos de origen (dataframe),
## - Se correlaciona el campo estado con el campo llave del geomapa, en este caso "ENTIDAD" y "properties.name", de acuerdo 
## al contenido del geomapa
## - Se configura con el parametro color_continuous_scale  la escala de colores que se va a graficar de acuerdo a los valores
##   que contiene el campo 'CASOS POSITIVOS COVID', que nos definirá la escala 
fig = px.choropleth(
                    geojson =regiones_mexico_geojson,
                    data_frame = df,
                    locations="ENTIDAD", #Columna del dataframe 'CASOS_CONFIRMADOS_COVID19_MEXICO.csv' columna "ENTIDAD"
                    featureidkey = 'properties.name',    #identificador del gejson sobre el cual se hara la  correlacion en el MAPA
                    color = 'CASOS POSITIVOS COVID',    #columna sobre la cual se realizara la escala de color
                    title='Casos positivos COVID19 por Entidad',
                    color_continuous_scale = "Oranges" )  ## Personalizar el color de la barra

## Actualizar mapa para que solo engloge los datos del geojson
fig.update_geos( fitbounds='locations' )

## PASO 5: Personalizando el mapa
#    Adicional, se configura los parametros showcountries = False , showCoastLines = False , showland = False para omitir 
#    que se rendericen en nuestro mapa.
fig.update_geos(showcountries=False,showcoastlines=False, showland=False)

fig.show()

## PASO 6: Exportando mi gráfico hacia HTML
fig.write_html('casos_confirmados_covid19_mexico.html', auto_open=True)
## Exportando mi gráfico a imagenes (requiere librería kaleido)
fig.write_image("casos_confirmados_covid19_mexico.png")
## Exportando a imagenes vectorizadas
fig.write_image("casos_confirmados_covid19_mexico.SVG")
