print ("BIENVENIDO A EMPAREJANDO.COM\n")

print("Necesitamos conocer algunos datos sobre ti para encontrar tu pareja ideal")

nombre = input("Escribe tu nombre: ")
ano = int(input("¿Año de nacimiento? "))
taburete = input("¿Te gusta taburete? [Si/No] ")

edad = 2020-ano

print("Hola "+nombre+". Si no me equivoco tienes", edad,"años.")

# Versión alternativa para el IF
# if taburete in ('Si','Sí','S','s','si','sí'):
if (taburete=="Si" or taburete=="Sí" or taburete=="si" or taburete=="S" or taburete=="s"):
    print("OKEY boomer. Lo tuyo va a ser un caso difícil")
else:
    print("Bueno, al menos es un comienzo. Veremos qué se puede hacer contigo.")