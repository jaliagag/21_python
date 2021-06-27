"""Escribir un programa que imprima todos m�ltiplos de un n�mero �n� entero entre 1 y 9 que ingresa el usuario hasta el 30. Si el n�mero se encuentra fuera del rango anterior imprimir el mensaje �El n�mero debe ser un valor entero entre 1 y 9�."""

numero = int(input('ingrese un número: '))

if numero < 1 or numero > 9:
  print('El número debe ser un valor entero entre 1 y 9')
else:
  for x in range(1,31):
    multiplo = (numero*x)
    if multiplo <= 30:
      print(multiplo)
