# -*- coding: utf-8 -*-
"""Project_demo_code

HIGH SECURE SYSTEM

CRYPTOGRAPHY SYSTEM USING VIGENERE CIPHER AND POLYBIUS CIPHER

By- SHIVAM VATSHAYAN
"""

# Python code to implement 
# Vigenere Cipher 

# This function generates the 
# key in a cyclic manner until 
# it's length isn't equal to 
# the length of original text 
def generateKey(string, key): 
	key = list(key) 
	if len(string) == len(key): 
		return(key) 
	else: 
		for i in range(len(string) -
					len(key)): 
			key.append(key[i % len(key)]) 
	return("" . join(key))

"""Hi there, 

wait wait !

This is Just Demo

Full Project is longer as it envolve many process like encrytion and decryption

Mail me now at vatshayan007@gmail.com to get this full project code with project report and PPT now.

Mail me now at vatshayan007@gmail.com
"""

