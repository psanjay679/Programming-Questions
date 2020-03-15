#!/usr/bin/python
import re

filename = "data.txt"

f = open(filename, "r").read()
x = re.findall(r'mov\s+DWORD PTR \[rbp\-0x8\]\,0x(.*)?', f)
x = list()
y = list()

for line in f:
	if "mov    DWORD PTR [rbp-0x8]":
		print(line.split(','))
		x.append(line.split(',')[1])
	if 'xor' in line:
		print(line.split(','))
		y.append(line.split(',')[1])

ans = list()

for a, b in zip(x, y):
	ans.append(chr(int(a, 0x10) ^ int(b, 0x10)))

print(''.join(ans))