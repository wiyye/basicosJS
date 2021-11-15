import requests
link ="https://restcountries.com/v3.1/name/"
pais = "spain"
respuesta = requests.get(link+pais)
respuestaJson = respuesta.json()

## print(respuestaJson)
print(respuestaJson[0]['name']['common']
)

