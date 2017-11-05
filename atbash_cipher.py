# Imports
import string
from ciphers import Cipher



class Atbash(Cipher):
	'''Encrypts and decrypts messages using the Atbash Cipher.
	   Formed by taking the alphabet and mapping it to its
	   reverse, so that the first letter becomes the last 
	   letter, the second letter become the second to last
	   letter, and so on.'''
	def __init__(self):
		self.alphabet = list(string.ascii_uppercase)
		self.reversed_alphabet = list(string.ascii_uppercase)[::-1]

	# Encrypts message
	def encrypt(self, text):
		'''Encrypts message bymatching index of letter to
		   encrypted alphabet index. Then matching back to the 
		   alphabet to obtain encrypted letter.'''
		final_output = []

		for letter in text.upper():
			try:
				index = self.alphabet.index(letter)
			except ValueError:
				final_output.append(letter)
			else:
				final_output.append(self.reversed_alphabet[index])
		return ''.join(final_output)


	# Decrypts message
	def decrypt(self, text):
		'''Decrypts message bymatching index of letter to
		   decrypted alphabet index. Then matching back to the 
		   alphabet to obtain decrypted letter.'''
		final_output = []

		for letter in text.upper():
			try:
				index = self.reversed_alphabet.index(letter)
			except ValueError:
				final_output.append(letter)
			else:
				final_output.append(self.alphabet[index])
		return ''.join(final_output)