# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 19:29:44 2020

@author: ivann
"""

abecedario = 'abcdefghijklmnñopqrstuvwxyz'

print("MI CIFRADO CÉSAR")
texto = input("Escribe el texto a cifrar:")
clave = int(input("Escribe la clave de cifrado (un número del 1 al 27):"))


texto_cifrado=""

for letra in texto:
    nueva_posicion = abecedario.find (letra) + clave
    letra_cifrada = int(nueva_posicion) % len(abecedario)
    texto_cifrado = texto_cifrado + str(abecedario [letra_cifrada])
print("\nEl mensaje cifrado es:",texto_cifrado)


texto_descifrado=""

for letra in texto_cifrado:
    nueva_posicion = abecedario.find (letra) - clave
    letra_cifrada = int(nueva_posicion) % len(abecedario)
    texto_descifrado = texto_descifrado + str(abecedario[letra_cifrada])

print("\nEl mensaje descifrado es:",texto_descifrado)


