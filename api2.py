import requests
link ="https://api.covid19api.com/total/country/"
pais = "mexico"
respuesta = requests.get(link+pais)
respuestaJson = respuesta.json()
print(respuestaJson)