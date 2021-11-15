valoresHexadecimal=['0xa076407d3f7440000', '0x140ec80fa7ee880000', 
'0x1e162c177be5cc0000', '0x281d901f4fdd100000', 
'0x3224f42723d4540000', '0x3c2c582ef7cb980000', 
'0x4633bc36cbc2dc0000', '0x503b203e9fba200000', 
'0x5a42844673b1640000', '0x6449e84e47a8a80000', '0x6e514c561b9fec0000', ]

numeroBinario='1001010011'
decimal=int(numeroBinario,2)
print(f'el numero binario {numeroBinario} a decimal es {decimal}')
binario=bin(15)
binario=binario.replace('0b','')
print(f'el numero 15 en binario es {binario}')

unHexadecimal=valoresHexadecimal[0]
decimal=int(unHexadecimal, 16)
print(f'el numero hexadecimal {unHexadecimal} en decimal es {decimal}')
otroHexadecimal='2A'
decimal=int(otroHexadecimal,16)
print(f'el numero hexadecimal {otroHexadecimal} en decimal es {decimal}')
listaDecimales=[]
decimal=0
for hexadecimal in valoresHexadecimal:
    decimal=int(hexadecimal,16)
    listaDecimales.append(decimal)
    
print(listaDecimales)   

paresValores=zip(valoresHexadecimal, listaDecimales)
paresValores=list(paresValores)
print(paresValores)


Diccionario=dict(paresValores)
print('***********************')
print(Diccionario)