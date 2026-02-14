#decoding ROT1 ciphers | There is no built-in functions for ciphers (ROT1 & 13), string translation is used

cipher_text = input("Enter the RTO1 cipher text \n")
alphabet = "abcdefghijklmnopqrstuvwxyz"                             #use this as our reference for the code knowing which letter comes next
alphabet_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

rot1_alphabet = alphabet[1:] + alphabet[:1]                         # shifts everything forward, so 'a' maps to 'b'
rot1_alphabet_upper = alphabet_upper[1:] + alphabet_upper[:1]
translator = str.maketrans(rot1_alphabet + rot1_alphabet_upper, alphabet + alphabet_upper)                 #this function maps the letters & replacements to a table 
plain_text = cipher_text.translate(translator)

print("Decoded text:", plain_text)