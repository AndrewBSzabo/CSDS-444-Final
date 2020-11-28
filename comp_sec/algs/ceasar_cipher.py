alphabet_start = 32
alphabet_end = 126
alphabet_size = alphabet_end - alphabet_start + 1

def CaesarEncrypt(plaintext,numrotate):
    cipher = ''

    for c in plaintext:
        cipher += chr(((ord(c) + numrotate - alphabet_start) % alphabet_size) + alphabet_start)

    return cipher

def CaesarDecrypt(ciphertext, numrotate):    
    plaintext = ''

    for c in ciphertext:
        plaintext += chr(((ord(c) - numrotate - alphabet_start) % alphabet_size) + alphabet_start)
        
    return plaintext


