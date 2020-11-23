p = 503
q = 521
n = p * q
nt = 130520
e = 3
d = 43507

def encrypt(message):
    values = message.split()
    for i in range(len(values)):
        # c = m ** e % n
        values[i] = str((int(values[i]) ** e) % n)
    encrypted_message = " ".join(values)

    return encrypted_message

def decrypt(message):
    values = message.split()
    for i in range(len(values)):
        # m = c ** d % n
        values[i] = str((int(values[i]) ** d) % n)
    decrypted_message = " ".join(values)

    return decrypted_message
