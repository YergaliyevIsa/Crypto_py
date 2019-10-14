import string
import sys


#type(filenames) == list or tuple

def counter(filenames):
	a = list(string.ascii_letters)
	a.extend([chr(i) for i in range(ord('а'), ord('а') + 32)])
	a.extend([chr(i) for i in range(ord('А'), ord('А') + 32)])
	frequency = dict.fromkeys(a, 0)
	for file in filenames:
		with open(file, 'r', encoding = 'utf-8') as f:
			for line in f:
				for letter in line:
					if letter in frequency:
						frequency[letter] += 1
	return frequency

filenames = []
for line in sys.stdin:
	filenames.append(line.rstrip())
for key, val in counter(filenames).items():
	print(key, val)

		
