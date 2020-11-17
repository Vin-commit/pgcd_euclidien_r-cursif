#!/usr/bin/python3
# coding: utf-8


def calcul_pgcd (a, b):
  if (a > b):
    a, b = b, a
  if (b%a == 0):
    return a
  return calcul_pgcd (b%a, a)


print (“Calcul de pgcd :”)
a = int(input(“Saisissez le premier nombre : “))
b = int(input(“Saisissez le deuxième nombre : “))
print(“Pgcd ( “+str(a)+”,  “+str(b)+”) =”, calcul_pgcd(a, b))


---------------------------------------------------------------------------- Résultat -------------------------------------------------------------------------
Calcul de pgcd :
Saisissez le premier nombre : 33810
Saisissez le deuxième nombre : 4116
Pgcd (33810, 4116) = 294
