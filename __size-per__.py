#!/usr/bin/python3

import os, sys

scan = list(os.scandir())
size = 0


def calculo():
	global size
	arr = [arq for arq in scan if arq.name == target]
	index = scan.index(arr[0])
	size = list(scan[index].stat())[6]
	print(f"{size} Bytes")


try:
	tipo = str(sys.argv[1])
	target = str(sys.argv[2])
	if tipo == '-k':
		calculo()
		print(f"{size / 1000} Kilobytes")
	if tipo == '-m':
		calculo()
		print(f"{size / 1_000_000} Megabytes")
	if tipo == '-g':
		calculo()
		print(f"{size / 1_000_000_000} Gigabytes")
except IndexError:
	print("USE -g para Gigabytes -> python3 __size-per__.py -g [TARGET]")
	print("USE -m para Megabytes -> python3 __size-per__.py -m [TARGET]")
	print("USE -k para Kilobytes -> python3 __size-per__.py -k [TARGET]")
	print("AVISO: Somente python 3.7+.")


