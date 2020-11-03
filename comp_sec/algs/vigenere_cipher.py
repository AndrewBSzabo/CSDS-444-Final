# variables indicating range of accepted alphabet (ascii characters from 32-126)
alphabet_start = 32
alphabet_end = 126
alphabet_size = alphabet_end - alphabet_start + 1

# returns the encripted message
def encrypt(message, key):
    encrypted_message = ""

    long_key = key_repeated(message, key)
    
    # for each message character and long key character pair...
    for m, k in zip(message, long_key):
        if ord(m) in range(alphabet_start,alphabet_end + 1):
            # append the character that corresponds to the message character row and key character column
            encrypted_message += chr((((ord(m) - alphabet_start) + (ord(k) - alphabet_start)) % alphabet_size) + alphabet_start)
        else:
            return f'{m}, in the message, is not in the range of supported characters (ascii characters 32-126)'

    return encrypted_message

# returns the decrypted message
def decrypt(cipher, key):
    decrypted_message = ""

    long_key = key_repeated(cipher, key)

    # for each cipher character and long key character pair...
    for c, k in zip(cipher, long_key):
        if ord(c) in range(alphabet_start, alphabet_end + 1):
            decrypted_message += chr(((ord(c) - ord(k)) % alphabet_size) + alphabet_start)
        else:
            return f'{c}, in the cipher text, is not in the range of supported characters (ascii characters 32-126)'
    
    return decrypted_message

# returns a string of repeated keys that is as long as the message
def key_repeated(message, key):
    repeated_key = ""
    for i in range(len(message)):
        if ord(key[i % len(key)]) in range(alphabet_start,alphabet_end + 1):
            repeated_key += key[i % len(key)]
        else:
            return f'{key[i % len(key)]}, in key, is not in the range of supported characters (ascii characters 32-126)'

    return repeated_key

if __name__ == "__main__":
    message = "test message!~"
    
    # for i in range(alphabet_size):
    #      message += chr(i)
    key = "key!% "

    # for i in range(alphabet_size):
    #     key += chr(alphabet_size - i - 1)

    k = encrypt(message,key)
    print(k)
    print()

    d = decrypt(k,key)

    print(d)