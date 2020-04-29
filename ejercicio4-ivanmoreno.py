# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 18:57:21 2020

@author: ivann
"""

from datetime import date

print ("BIENVENIDO A EMPAREJANDO.COM\n")

print("Necesitamos conocer algunos datos sobre ti para encontrar tu pareja ideal")

nombre = input("Escribe tu nombre: ")
ano = int(input("¿Año de nacimiento? "))
taburete = input("¿Te gusta taburete? [Si/No] ")

ano_actual=date.today().year
edad = ano_actual-ano

print("Hola "+nombre+". Si no me equivoco tienes", edad,"años.")

if taburete in ('Si','Sí','S','s','si','sí'):
    tabu = True
else:
    tabu = False

if (tabu):
    print("OKEY boomer. Lo tuyo va a ser un caso difícil")
else:
    print("Bueno, al menos es un comienzo. Veremos qué se puede hacer contigo.")
    
    
usuario=[nombre,edad,tabu]

for dato in usuario:
    print(dato)
