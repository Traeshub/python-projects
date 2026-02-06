#creating this to see if i can decode one of the JE files. THIS ONLY DECODES STRINGS

import base64
def decoder(encoded):
    base64_bytes = encoded.encode('utf-8')
    message_byte = base64.b64decode(base64_bytes)
    return message_byte.decode('utf-8')

encoded = input("Enter the Base64 encoded text to decode: \n")
decoded = decoder(encoded)
print("Decoded text:", decoded)