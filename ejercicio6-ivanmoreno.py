# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 19:29:44 2020

@author: ivann
"""

abecedario= ' abcdefghijklmnñopqrstuvwxyz '

print("Bienvenidos a mi cifrador César")

texto_claro=input("Introduce una frase para cifrarla: ")
clave=int(input("Introduce un numero para cifrar(Un número del 1 al 27):"))

texto_cifrado=""


for letra in texto_claro:
    nueva_posicion=abecedario.find(letra)+ clave
    letra_cifrada=int(nueva_posicion)%len(abecedario)
    texto_cifrado= texto_cifrado+str(abecedario[letra_cifrada])
print ("El mensaje cifrado es:" ,texto_cifrado)
print ("=====================================================")
texto_descifrado=""
for letra in texto_cifrado:
    nueva_posicion= abecedario.find(letra)-clave
    letra_cifrada= int(nueva_posicion)%len(abecedario)
    texto_descifrado= texto_descifrado+str(abecedario[letra_cifrada])
print ("El mensaje descifrado es: " ,texto_descifrado)