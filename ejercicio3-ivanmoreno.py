# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 18:56:00 2020

@author: ivann
"""

print ("BIENVENIDO A EMPAREJANDO.COM\n")

print("Necesitamos conocer algunos datos sobre ti para encontrar tu pareja ideal")

nombre = input("Escribe tu nombre: ")
ano = int(input("¿Año de nacimiento? "))
taburete = input("¿Te gusta taburete? [Si/No] ")

edad = 2020-ano

print("Hola "+nombre+". Si no me equivoco tienes", edad,"años.")

if taburete in ('Si','Sí','S','s','si','sí'):
    print("OKEY boomer. Lo tuyo va a ser un caso difícil")
else:
    print("Bueno, al menos es un comienzo. Veremos qué se puede hacer contigo.")
    


for contador in range(1,edad):
    print("Que no cumple",contador)

print("¡ Que sí cumple",edad,"!")