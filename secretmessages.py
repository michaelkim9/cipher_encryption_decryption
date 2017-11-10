import os

from caesar_cipher import Caesar
from affine_cipher import Affine
from atbash_cipher import Atbash
from keyword_cipher import Keyword


def clear_screen():
    '''Clears the command screen.'''
    os.system('cls' if os.name == 'nt' else 'clear')


def secret_messages():
    '''Asks which cipher to implement.
       Determines whether to encrypt or decrypt message.'''
    cipher_dict = {
        'CAESAR': Caesar,
        'AFFINE': Affine,
        'ATBASH': Atbash,
        'KEYWORD': Keyword
    }

    encryption_options = {
        'E': 'Encrypt',
        'D': 'Decrypt'
    }

    cipher_list = [''.join(key.title()) for key in cipher_dict]

    while True:
        clear_screen()
        # Print welcome screen
        print('Welcome. Please select one of the following ciphers:\n'
              'Enter "QUIT" to quit.\n')
        # Print cipher list
        for cipher in cipher_list:
            print('- {}'.format(cipher))
        # User chooses cipher
        cipher_input = input('\n> ').upper()
        # Check to see if this is a valid cipher
        # Break the code if user chooses to quit
        while True:
            if cipher_input == 'QUIT':
                active_cipher = None
                break
            try:
                active_cipher = cipher_dict[cipher_input]()
                break
            except KeyError:
                cipher_input = input(
                     'Not a valid cipher, please choose again.\n> '
                ).upper()

        if not active_cipher:
            break
        # User chooses encryption or decryption
        clear_screen()
        print('{} cipher selected:\n'
              'Press "E" to Encrypt or "D" to Decrypt:'.format(cipher_input))
        e_d_input = input('> ').upper()
        # Check to see if encryption or decryption input is valid
        while True:
            try:
                encrypt_choice = encryption_options[e_d_input]
                break
            except KeyError:
                e_d_input = input(
                     'Invalid. Select "E" to Encrypt and "D" to Decrypt.\n> '
                     ).upper()
                continue
        # Encrypt message
        if encrypt_choice == 'Encrypt':
            print('What is the message you would like to encrypt?')
            encrypt_message = input('> ').upper()

            print(active_cipher.encrypt(encrypt_message))
            again = input(
                '\nEncrypt or Decrypt something else? Y/n \n> ').upper()

            if again == 'Y':
                secret_messages()
            else:
                break
        # Decrypt message
        elif encrypt_choice == 'Decrypt':
            print('What is the message you would like to decrypt?')
            decrypt_message = input('> ').upper()
            print(active_cipher.decrypt(decrypt_message))
            again = input(
                '\nEncrypt or Decrypt something else? Y/n \n> ').upper()

            if again == 'Y':
                secret_messages()
            else:
                break


if __name__ == '__main__':
    '''Runs the code'''
    secret_messages()
