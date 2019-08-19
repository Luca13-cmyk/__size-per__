#!/usr/bin/python3

import sys, os

try:
	tipo = str(sys.argv[1])
	target = str(sys.argv[2])
	if tipo == '-k':
		scan = list(os.scandir())
		arr = [arq for arq in scan if arq.name == target]
		index = scan.index(arr[0])
		size = list(scan[index].stat())[6]
		print(f"{size / 1000} Kilobytes")
except IndexError:
	print("")

