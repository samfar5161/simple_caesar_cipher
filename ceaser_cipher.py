# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 21:17:49 2022

@author: Ashton Farleigh

@description:
    This program was created to encrypt and decrypt common
    caesar cipher text. 
        
@issues
    Currenty, this program only works for text that is 
    all lower case. Any uppercase characters are excluded
    from encryption and decryption outputs. 
    Fix is in progress.
    
    
"""
import string

class caesar_cipher():
        
    # Starting position = 26 will generate a key that's identical to the
    # alphabet. For a +1 key, the starting position = 27. For a 
    # -3 key, the starting position = 23.    
    def generate_cipher_key(start_position):
        alphabet = string.ascii_lowercase
        alphabet_canvas = alphabet+alphabet+alphabet
        output_alphabet = []
        for l in alphabet:
            output_alphabet.append(l)
        alphabet_cipher = []
        for n in range(26):
           alphabet_cipher.append( alphabet_canvas[start_position + n] )
        for i in range(26):
            output_alphabet[i] = [output_alphabet[i], alphabet_cipher[i]]              
        return output_alphabet 

    # TODO:
    # Tweak logic so that capital letters don't get excluded         
    def encrypt_text(text, cipher_key):
        encrypted_text = ''
        text = text.lower()
        for x in text:
            for i in cipher_key:
                if(x == i[0]):
                    encrypted_text = encrypted_text + i[1]
            if (x == ' '):
                encrypted_text = encrypted_text + x                   
        return encrypted_text
    
    def decrypt_text(text, cipher_key):
        decrypted_text = ''
        for x in text:
            for i in cipher_key:
                if(x == i[1]):
                    decrypted_text = decrypted_text + i[0]
            if (x == ' '):
                decrypted_text = decrypted_text + x                    
        return decrypted_text
    
    def bruteforce_decrypt_text(text): 
        output_decryption = []
        for i in range(26):
            cipher_key = caesar_cipher.generate_cipher_key(i)
            output_decryption.append(caesar_cipher.decrypt_text(text, cipher_key))            
        return output_decryption
