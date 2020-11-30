a_p = 503
a_q = 521
a_n = a_p * a_q
a_nt = 130520
a_e = 3
a_d = 43507

b_p = 131
b_q = 191
b_n = b_p * b_q
b_nt = 24700
b_e = 7
b_d = 17643

def getConstsAlice():
    return a_p, a_q, a_n, a_nt, a_e, a_d

def getConstsBob():
    return b_p, b_q, b_n, b_nt, b_e, b_d

def encrypt(message, _e, _n):
    encrypted_message = ""
    
    for m in message:
        # c = m ** e % n
        encrypted_message += str((ord(m) ** _e) % _n) + " "

    return encrypted_message

def decrypt(message, _d, _n):
    values = message.split()
    for i in range(len(values)):
        # m = c ** d % n
        values[i] = chr((int(values[i]) ** _d) % _n)
    decrypted_message = "".join(values)

    return decrypted_message
