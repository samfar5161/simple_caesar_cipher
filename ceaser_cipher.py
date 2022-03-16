# -*- coding: utf-8 -*-
"""
Created on Tue Mar 1 21:17:49 2022

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

    # utility function for dealing with uppercase characters during the 
    # encryption/decryption process. Creates an index of where uppercase 
    # letters are in the text. It's conveluted but it works.
    def get_uppercase_character_index(text):
        index = []
        for l in text:
            if(l.isupper() == True):
                index.append(1)
            else:
                index.append(0)       
        return index
    
    # utility function for dealing with uppercase characters during the 
    # encryption/decryption process. Applies the index created above to the 
    # output text. Conveluted but works.
    def apply_uppercase_index(text, index):
        new_text = ''
        if(len(text) != len(index)):
            return 'Invalid Paramters'
            
        
        for i in range(len(index)):
            if index[i] == 1:
                new_text += text[i].upper()
            elif index[i] == 0: 
                new_text += text[i]    
        return new_text        
            
    def encrypt_text(text, cipher_key):
        upper_idx = caesar_cipher.get_uppercase_character_index(text)
        encrypted_text = ''
        text = text.lower()
        for x in text:
            for i in cipher_key:
                if(x == i[0]):
                    encrypted_text = encrypted_text + i[1]
            if (x == ' '):
                encrypted_text = encrypted_text + x                   
        
        encrypted_text = caesar_cipher.apply_uppercase_index(encrypted_text, upper_idx)
        return encrypted_text
            
    def decrypt_text(text, cipher_key):
        upper_idx = caesar_cipher.get_uppercase_character_index(text)
        decrypted_text = ''
        text = text.lower()
        for x in text:
            for i in cipher_key:
                if(x == i[1]):
                    decrypted_text = decrypted_text + i[0]
            if (x == ' '):
                decrypted_text = decrypted_text + x                    
        
        decrypted_text = caesar_cipher.apply_uppercase_index(decrypted_text, upper_idx)
        return decrypted_text
           
    def bruteforce_decrypt_text(text): 
        output_decryption = []
        for d in range(26):
            cipher_key = caesar_cipher.generate_cipher_key(d)
            output_decryption.append(caesar_cipher.decrypt_text(text, cipher_key))            
        return output_decryption
