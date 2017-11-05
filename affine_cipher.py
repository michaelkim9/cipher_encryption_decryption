# Imports
import string
from ciphers import Cipher



class Affine(Cipher):
	'''Encrypts and Decrypts a message using the Affine Cipher.
	   Each letter is enciphered with the function (ax + b) mod 26, 
	   where b is the magnitude of the shift.
	   After finding the value of (ax + b) for each character, 
	   take the remainder when dividing the result by 26.'''
	def __init__(self, alpha = None, beta = None):
		'''Initializing the cipher.
		   Obtaining alpha and beta.
		   Creates a new list to apply the alphabet based on cipher.'''

		self.alphabet = list(string.ascii_uppercase)
		accepted_alpha = [3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25]
		self.cipher_list = []

		# Request alpha key as input and verify validity
		if not alpha:
			while True:
				try:
					self.alpha = int(input('Please enter alpha key. Odd integer from 3-25, except 13 \n > '))
					if self.alpha in accepted_alpha:
						break
				except ValueError:
					print('Invalid alpha value')


		# Request beta key as input and verify validity
		if not beta:
			self.beta = int(input('Please enter beta key, any integer 1-100 \n > '))
		else:
			self.beta = beta


		# Adding indexes to cipher list
		for letter in self.alphabet:
			self.cipher_list.append(
				((self.alpha * self.alphabet.index(letter)) + self.beta) 
				% len(self.alphabet)
				)


	# Encrypt input message with the list of indexes from cipher_list
	def encrypt(self, text):
		'''Encrypts message by mathching the index of entered letter
		   to cipher_list index, then matching back to the alphabet.'''
		final_output = []

		for letter in text.upper():
			if letter in self.alphabet:
				index = self.alphabet.index(letter)
				final_output.append(self.alphabet[self.cipher_list[index]])
			else:
				final_output.append(letter)

		return ''.join(final_output)


	# Decrypt input message with the list of indexes from cipher_list
	def decrypt(self, text):
		'''Decrypts message by matching the index of entered letter
		   to cipher_list index, then matching back to the alphabet.'''
		final_output = []

		for letter in text.upper():
			if letter in self.alphabet:
				index = self.alphabet.index(letter)
				final_output.append(self.alphabet[self.cipher_list.index(index)])
			else:
				final_output.append(letter)

		return ''.join(final_output)