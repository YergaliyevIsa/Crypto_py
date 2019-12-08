import os.path as osp
import random
import argparse

def genkey(out):
	key = [i for i in range(256)]
	random.shuffle(key)
	print(key)
	key = bytes(key)
	print(key)
	with open(out, 'wb') as f:
		f.write(key)

def get_key(path_to_key):
	with open(path_to_key, 'rb') as f:
		key = f.read()
	return list(map(int, key))
#key - список из чисеk
def encrypt(inp, path_to_key, out):
	key = get_key(path_to_key)
	print(key)
	with open(inp, 'rb') as f:
		x = f.read()
	x = list(map(int , x))
	x = bytes([key[i] for i in x])
	print(x)
	with open(out, 'wb') as f:
		f.write(x)
		
def decrypt(inp, path_to_key, out):
	key = get_key(path_to_key)
	print(key)
	key = {key[i] : i for i in range(256)}
	with open(inp, 'rb') as f:
		x = f.read()
	x = list(map(int , x))	
	x = bytes([key[i] for i in x])
#	print(x)
	with open(out, 'wb') as f:
		f.write(x)


def _break(inp, ciphertext, out):
	with open(inp, 'rb') as f:
		opentext = f.read()
	opentext = list(map(int, opentext))
	freq_table = [[0, i] for i in range(256) , [0, j] for j in range(256)] 
	for byte in opentext:
		freq_table[0][byte][0] += 1
	with open(ciphertext, 'rb') as f:
		cipher = f.read()
	cipher = list(map(int, cipher))
	for byte in cipher:
		freq_table[1][byte][0] += 1
	freq_table[0].sort(key = lambda val: val[0])
	freq_table[1].sort(key = lambda val: val[0])
	key = [(freq_table[0][index][1], freq_table[1][index][1]) for index in range(256)]
	key.sort(key = lambda val: val[0])
	print(key)
	key = bytes(key)
	with open(out, 'wb') as f:
		f.write(key)


"""
python3 genkey  {-o | --out} path_to_key
python3 encrypt {-k | --key} path_to_key {-i, --input} path_to_input  {-o | --out} path_to_output
python3 decrypt {-k | --key} path_to_key {-i, --input} path_to_input  {-o | --out} path_to_output
python3 break  {-i | --input} path_to_text {-c | --cipher}  path_to_ciphertext {-o | --out} path_to_out
"""
parser = argparse.ArgumentParser(description = 'Parametrs of cipher')
parser.add_argument("mode", choices = ['genkey', 'encrypt', 'decrypt', 'break'])
parser.add_argument('-o', '--out', default = 'output')
parser.add_argument('-k', '--key', default = 'seckey')
parser.add_argument('-i', '--input', default = 'input')
parser.add_argument('-c', '--cipher', default = 'cipher')
args = parser.parse_args()
if args.mode == 'genkey':
	genkey(osp.normpath(args.out))
elif args.mode == 'encrypt':
	encrypt(args.input, osp.normpath(args.key), osp.normpath(args.out))
elif args.mode == 'decrypt':
	decrypt(osp.normpath(args.input), osp.normpath(args.key), osp.normpath(args.out))
elif args.mode == 'break':
	_break(osp.normpath(args.input), osp.normpath(args.cipher), osp.normpath(args.out))