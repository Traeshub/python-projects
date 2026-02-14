# Decoding XOR obfuscation

cipher_text = input("Enter the XOR cipher text: ")
key = input("Enter the XOR key: ")                      # XOR uses the same key for both encryption and decryption, so the user needs to provide the key
cipher_bytes = cipher_text.encode()                     # converts the user's input string into a bytes. XOR operations work on bytes (numbers 0-255), not directly on characters

key_bytes = key.encode()                                # This converts the key string into a bytes object, the key needs to be in byte form so we can perform XOR
result_bytes = bytearray()                              # This creates an empty bytearray, use this to build our decoded result byte by byte
for i in range(len(cipher_bytes)):
        key_byte = key_bytes[i % len(key_bytes)]
        result_byte = cipher_bytes[i] ^ key_byte
        result_bytes.append(result_byte)

plain_text = result_bytes.decode()
print("Decoded text:", plain_text)