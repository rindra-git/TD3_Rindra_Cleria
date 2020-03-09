#!/usr/bin/env python

import sys

def add(a,b):
	return a + b

if __name__ == "__main__":
	if len(sys.argv)>3 :
		print ("tu veux")
	elif (len(sys.argv) == 3):
		a = int( sys.argv[1] )
		b = int( sys.argv[2] )
		print((a),"+","=",(a+b))
	elif len(sys.argv)==2:
		print("tu")
		print("veux: ")
		a = int( sys.argv[1] )
		b = int( input())
		print((a),"+",(b),(a+b))
