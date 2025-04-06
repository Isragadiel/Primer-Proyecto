#Ejercicio 1 

edad = int(input("Por favor, introduce tu edad: "))

if edad >= 18:
   print("Es mayor de edad")

#Ejercicio 2 

nota = float(input("Por favor, introduce tu nota: "))

if nota >= 6:
   print("Aprobado")
else:
   print("Desaprobado")

#Ejercicio 3

numero = int(input("Por favor, introduce un número par: "))

if numero % 2 == 0:
   print("Ha ingresado un número par")
else:
   print("Por favor, ingrese un número par")

#Ejercicio 4

edad = int(input("Por favor, introduce tu edad: "))

if edad < 12:
   print("Niño/a")
elif edad >= 12 and edad < 18:
   print("Adolescente")
elif edad >= 18 and edad < 30:
   print("Adulto/a joven")
else:
   print("Adulto/a")

#Ejercicio 5

contraseña = input("Por favor, introduce tu contraseña (entre 8 y 14 caracteres): ")

if len(contraseña) >= 8 and len(contraseña) <= 14:
   print("Ha ingresado una contraseña correcta")
else:
   print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

#Ejercicio 6

import random
from statistics import mode, median, mean

numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

moda_num = mode(numeros_aleatorios)
mediana_num = median(numeros_aleatorios)
media_num = mean(numeros_aleatorios)

print(f"Moda: {moda_num}")
print(f"Mediana: {mediana_num}")
print(f"Media: {media_num}")

if media_num > mediana_num:
     print("Sesgo positivo")
elif media_num < mediana_num:
     print("Sesgo negativo")
else:
     print("No hay sesgo")

#Ejercicio 7

frase = input("Por favor, introduce una frase o palabra: ")

vocales = "aeiouAEIOU"

if frase and frase[-1] in vocales:
   frase += "!"
   print(frase)
else:
   print(frase)    

#Ejercicio 8

nombre = input("Por favor, introduce tu nombre: ")
opcion = input("Elige una opción:\n1. Mayúsculas\n2. Minúsculas\n3. Primera letra mayúscula\n")

if opcion == "1":
   print(nombre.upper())
elif opcion == "2":
   print(nombre.lower())
elif opcion == "3":
   print(nombre.capitalize())
else:
   print("Opción inválida")

#Ejercicio 9
magnitud = float(input("Por favor, introduce la magnitud del terremoto: "))

if magnitud < 3:
  print("Muy leve (imperceptible)")
elif magnitud >= 3 and magnitud < 4:
  print("Leve (ligeramente perceptible)")
elif magnitud >= 4 and magnitud < 5:
  print("Moderado (sentido por personas, pero generalmente no causa daños)")
elif magnitud >= 5 and magnitud < 6:
  print("Fuerte (puede causar daños en estructuras débiles)")
elif magnitud >= 6 and magnitud < 7:
  print("Muy Fuerte (puede causar daños significativos)")
else:
  print("Extremo (puede causar graves daños a gran escala)")

#Ejercicio 10

hemisferio = input("¿En qué hemisferio te encuentras? (N/S): ").upper()
mes = int(input("¿Qué mes del año es (1-12)? "))
dia = int(input("¿Qué día es (1-31)? "))

if hemisferio == "N":
  if mes == 12 and dia >= 21 or mes == 1 or mes == 2 or mes == 3 and dia <= 20:
    print("Invierno")
  elif mes == 3 and dia >= 21 or mes == 4 or mes == 5 or mes == 6 and dia <= 20:
    print("Primavera")
  elif mes == 6 and dia >= 21 or mes == 7 or mes == 8 or mes == 9 and dia <= 20:
    print("Verano")
  else:
    print("Otoño")
elif hemisferio == "S":
  if mes == 12 and dia >= 21 or mes == 1 or mes == 2 or mes == 3 and dia <= 20:
    print("Verano")
  elif mes == 3 and dia >= 21 or mes == 4 or mes == 5 or mes == 6 and dia <= 20:
    print("Otoño")
  elif mes == 6 and dia >= 21 or mes == 7 or mes == 8 or mes == 9 and dia <= 20:
    print("Invierno")
  else:
    print("Primavera")
else:
  print("Hemisferio inválido")
