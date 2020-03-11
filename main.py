#!/usr/bin/env python



from mulTwolnt import mul

c = "Voulez-vous multiplier deux entiers?"

print(c)

d = input()

if d == "oui" :
	print("Saisissez-les,svp")
	a = int(input())
	b = int(input())
	print(mul(a,b))
elif d == "non" :

	print("okay")
