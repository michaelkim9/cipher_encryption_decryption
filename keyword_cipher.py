# Imports
import copy
import string
from ciphers import Cipher



class Keyword(Cipher):
	'''Encrypts and decrypts messages using the Keyword cipher.'''
	def __init__(self, keyword = None):
		'''Ask user for keyword'''
		if not keyword:
			self.input_keyword = list(input('Enter a keyword of unique letters \n> ').upper())
		else:
			self.input_keyword = keyword.upper()

		# Creating 2 lists of alphabet. One of regular alphabet. Other to modify with keyword\
		self.alphabet = list(string.ascii_uppercase)
		self.alphabet_removed = copy.copy(self.alphabet)


	# Creates the alphabet_removed list by removing letters from list and then adding keyword at beginning
	def alphabet_remove_keyword(self):
		for letter in self.input_keyword:
			if letter in self.alphabet_removed:
				self.alphabet_removed.remove(letter)
		return (self.input_keyword + self.alphabet_removed)


	# Encrypts user message
	def encrypt(self, text):
		'''Encrypts message by matching index of letter to encrypted alphabet index.'''
		final_output = []
		keyword_alphabet = self.alphabet_remove_keyword()


		for letter in text:
			if letter in self.alphabet:
				index = self.alphabet.index(letter)
				final_output.append(keyword_alphabet[index])
			else:
				final_output.append(letter)
		return ''.join(final_output)


	# Decrypts user message
	def decrypt(self, text):
		'''Decrypts message by matching index of letter to encrypted alphabet index.'''
		final_output = []
		keyword_alphabet = self.alphabet_remove_keyword()


		for letter in text:
			if letter in keyword_alphabet:
				index = keyword_alphabet.index(letter)
				final_output.append(self.alphabet[index])
			else:
				final_output.append(letter)
		return ''.join(final_output)