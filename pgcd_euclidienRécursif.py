#!/usr/bin/python3
# coding: utf-8


def pgcd_recursif(a, b):
  if (a > b):
      a = a % b
  else:
      b = b % a
  if (a == 0):
      return b
  if (b == 0):
      return a
  return pgcd_recursif(a, b)


a = int(input(“Entrez le premier nombre : “))
b = int(input(“Entrez le second nombre :”))
print (“Leur pgcd est :”, pgcd_recursif(a, b))
