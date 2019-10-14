def Caesar_encrypt(plaintext, key):
	ans = ''
	for letter in plaintext:
		if 'a' <= letter <= 'z':
			ans += chr((ord(letter) - ord('a') + key) % 26 + ord('a'))
		elif 'A' <= letter <= 'Z':
			ans += chr((ord(letter) - ord('A') + key) % 26 + ord('A'))
		else:
			ans += letter
	return ans

def Caesar_decrypt(cipher, key):
	ans = ''
	for letter in cipher:
		if 'a' <= letter <= 'z':
			ans += chr(ord(letter) - key) if ord(letter) - key >= ord('a') else chr(ord(letter) - key + ord('a')) 
		elif 'A' <= letter <= 'Z':
			ans += chr(ord(letter) - key) if ord(letter) - key >= ord('A') else chr(ord(letter) - key + ord('A'))
		else:
			ans += letter
	return ans

text = input()
k = int(input())
print(Caesar_encrypt(text, k))
print(Caesar_decrypt(Caesar_encrypt(text, k), k))