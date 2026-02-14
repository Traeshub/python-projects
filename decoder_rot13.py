# Decoding ROT13 ciphers|There is no built-in functions for ciphers (ROT1 & 13), string translation is used
#confirm it's this cipher by 3 letter words within the encoding -> gur(the) and nag(and)



cipher_text = input("Enter the RTO13 cipher text \n")
alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabet_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

rot13_alphabet = alphabet[13:] + alphabet[:13]
rot13_alphabet_upper = alphabet_upper[13:] + alphabet_upper[:13]
translator = str.maketrans(rot13_alphabet + rot13_alphabet_upper, alphabet + alphabet_upper) 
plain_text = cipher_text.translate(translator)

print("Decoded text:", plain_text)