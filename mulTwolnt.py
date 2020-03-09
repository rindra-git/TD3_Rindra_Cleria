#!/usr/bin/env python

import sys


def mul(a,b):
	return a * b



if __name__ == "__main__":


	if len(sys.argv) > 3 :
    		print("Saisissez que deux arguments")

	elif (len(sys.argv) == 3):
		a = int(sys.argv[1])
		b = int(sys.argv[2])
		print (mul(a,b))

	else:
		print("Peu d'argument")
		print("Entrer la valeur manquante")
		a = int(sys.argv[1])
		b = int(input())
		print(mul(a,b))


