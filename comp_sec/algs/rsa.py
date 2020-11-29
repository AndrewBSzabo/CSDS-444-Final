p = 503
q = 521
n = p * q
nt = 261040
e = 3
d = 174027

def getConsts():
    return p, q, n, nt, e, d

def encrypt(message):
    encrypted_message = ""

    for m in message:
        # c = m ** e % n
        encrypted_message += str((ord(m) ** e) % n) + " "

    return encrypted_message

def decrypt(message):
    values = message.split()
    for i in range(len(values)):
        # m = c ** d % n
        values[i] = chr((int(values[i]) ** d) % n)
    decrypted_message = "".join(values)

    return decrypted_message
