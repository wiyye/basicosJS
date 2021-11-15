import requests
from bs4 import BeautifulSoup
import pandas as pd

pagina= "https://docs.google.com/spreadsheets/d/e/2PACX-1vTzYZsrp-s-_JIPbIhoxtMKFEw-dMOwb54Ome36o2r40kRR7ZhtSmYXs8uVpHfVs9mTJVqsmPGks14f/pubhtml"

respuesta=requests.get(pagina)
respuestaTexto=respuesta.text
#print(respuestaTexto)
sopa=BeautifulSoup(respuestaTexto, 'lxml')
print(sopa)
filas=sopa.findAll('tr')
print('----------------------')
print(filas)
nombres=[]
edades=[]
pesosKg=[]
estaturasMts=[]
totalFilas=len(filas)
nombre=''
edad=0
pesoKg=0.0
estaturaMts=0.0

for i in range(totalFilas):
    laFila=filas[i]
    celdas=laFila.findAll('td')
    if len(celdas)==4:
        nombre=celdas[0].text
        edad=celdas[1].text
        pesoKg=celdas[2].text
        estaturaMts=celdas[3].text
        #print(celdas)
        print(nombre+','+edad+','+pesoKg+','+estaturaMts)
        if nombre !='Nombre':
            nombres.append(nombre)
            edades.append(edad)
            pesosKg.append(pesoKg)
            estaturasMts.append(estaturaMts)
    
    
    print('*****************************')

print(nombres)
print(edades)
print(pesosKg)
print(estaturasMts)

D={'Nombre': nombres, 'Edad':edades, 
'PesoKg':pesosKg, 'EstaturaMts':estaturasMts}

tabla=pd.DataFrame(D)
print(tabla)
tabla.to_csv('personitas.csv')