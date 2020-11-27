import binascii
import math

k = [0] * 64
for i in range(64):
    k[i] = int(2**32*abs(math.sin(i+1)))

def leftRotate(k,bits):
    return (k%(2**32)<<bits%32)%(2**32) | (k%(2**32)>>(32-(bits%32)))
 
def F(B,C,D):
    return (B&C)|((~B)&D) 
 
def G(B,C,D):
    return (B&D) | (C&(~D)) 
 
def H(B,C,D):
    return B^C^D 
 
def I(B,C,D):
    return C^(B|(~D))
 
def md5(data):
    dataLength = (len(data)*8)%(2**64)
    pad = math.floor(((448 - (dataLength+8)%512)%512)/8)
    data = data + b'\x80' + b'\x00'*pad + dataLength.to_bytes(8,byteorder='little')
    dataLength = (len(data)*8)
    A = 0x67452301
    B = 0xefcdab89
    C = 0x98badcfe
    D = 0x10325476
    for i in range(math.floor(dataLength/512)):
        a = A
        b = B
        c = C
        d = D

        block = data[i*64:(i+1)*64]
        M = []
        size = math.floor(len(block)/16)
        
        for j in range(16):
            M.append( int.from_bytes( block[j*size:(j+1)*size],byteorder="little" ))
        
        a = b + leftRotate( (a+F(b,c,d)+M[0]+k[0]), 7)
        d = a + leftRotate( (d+F(a,b,c)+M[1]+k[1]), 12)
        c = d + leftRotate( (c+F(d,a,b)+M[2]+k[2]), 17)
        b = c + leftRotate( (b+F(c,d,a)+M[3]+k[3]), 22)
        a = b + leftRotate( (a+F(b,c,d)+M[4]+k[4]), 7)
        d = a + leftRotate( (d+F(a,b,c)+M[5]+k[5]), 12)
        c = d + leftRotate( (c+F(d,a,b)+M[6]+k[6]), 17)
        b = c + leftRotate( (b+F(c,d,a)+M[7]+k[7]), 22)
        a = b + leftRotate( (a+F(b,c,d)+M[8]+k[8]), 7)
        d = a + leftRotate( (d+F(a,b,c)+M[9]+k[9]), 12)
        c = d + leftRotate( (c+F(d,a,b)+M[10]+k[10]), 17)
        b = c + leftRotate( (b+F(c,d,a)+M[11]+k[11]), 22)
        a = b + leftRotate( (a+F(b,c,d)+M[12]+k[12]), 7)
        d = a + leftRotate( (d+F(a,b,c)+M[13]+k[13]), 12)
        c = d + leftRotate( (c+F(d,a,b)+M[14]+k[14]), 17)
        b = c + leftRotate( (b+F(c,d,a)+M[15]+k[15]), 22)
        a = b + leftRotate( (a+G(b,c,d)+M[1]+k[16]), 5)
        d = a + leftRotate( (d+G(a,b,c)+M[6]+k[17]), 9)
        c = d + leftRotate( (c+G(d,a,b)+M[11]+k[18]), 14)
        b = c + leftRotate( (b+G(c,d,a)+M[0]+k[19]), 20)
        a = b + leftRotate( (a+G(b,c,d)+M[5]+k[20]), 5)
        d = a + leftRotate( (d+G(a,b,c)+M[10]+k[21]), 9)
        c = d + leftRotate( (c+G(d,a,b)+M[15]+k[22]), 14)
        b = c + leftRotate( (b+G(c,d,a)+M[4]+k[23]), 20)
        a = b + leftRotate( (a+G(b,c,d)+M[9]+k[24]), 5)
        d = a + leftRotate( (d+G(a,b,c)+M[14]+k[25]), 9)
        c = d + leftRotate( (c+G(d,a,b)+M[3]+k[26]), 14)
        b = c + leftRotate( (b+G(c,d,a)+M[8]+k[27]), 20)
        a = b + leftRotate( (a+G(b,c,d)+M[13]+k[28]), 5)
        d = a + leftRotate( (d+G(a,b,c)+M[2]+k[29]), 9)
        c = d + leftRotate( (c+G(d,a,b)+M[7]+k[30]), 14)
        b = c + leftRotate( (b+G(c,d,a)+M[12]+k[31]), 20)
        a = b + leftRotate( (a+H(b,c,d)+M[5]+k[32]), 4)
        d = a + leftRotate( (d+H(a,b,c)+M[8]+k[33]), 11)
        c = d + leftRotate( (c+H(d,a,b)+M[11]+k[34]), 16)
        b = c + leftRotate( (b+H(c,d,a)+M[14]+k[35]), 23)
        a = b + leftRotate( (a+H(b,c,d)+M[1]+k[36]), 4)
        d = a + leftRotate( (d+H(a,b,c)+M[4]+k[37]), 11)
        c = d + leftRotate( (c+H(d,a,b)+M[7]+k[38]), 16)
        b = c + leftRotate( (b+H(c,d,a)+M[10]+k[39]), 23)
        a = b + leftRotate( (a+H(b,c,d)+M[13]+k[40]), 4)
        d = a + leftRotate( (d+H(a,b,c)+M[0]+k[41]), 11)
        c = d + leftRotate( (c+H(d,a,b)+M[3]+k[42]), 16)
        b = c + leftRotate( (b+H(c,d,a)+M[6]+k[43]), 23)
        a = b + leftRotate( (a+H(b,c,d)+M[9]+k[44]), 4)
        d = a + leftRotate( (d+H(a,b,c)+M[12]+k[45]), 11)
        c = d + leftRotate( (c+H(d,a,b)+M[15]+k[46]), 16)
        b = c + leftRotate( (b+H(c,d,a)+M[2]+k[47]), 23)
        a = b + leftRotate( (a+I(b,c,d)+M[0]+k[48]), 6)
        d = a + leftRotate( (d+I(a,b,c)+M[7]+k[49]), 10)
        c = d + leftRotate( (c+I(d,a,b)+M[14]+k[50]), 15)
        b = c + leftRotate( (b+I(c,d,a)+M[5]+k[51]), 21)
        a = b + leftRotate( (a+I(b,c,d)+M[12]+k[52]), 6)
        d = a + leftRotate( (d+I(a,b,c)+M[3]+k[53]), 10)
        c = d + leftRotate( (c+I(d,a,b)+M[10]+k[54]), 15)
        b = c + leftRotate( (b+I(c,d,a)+M[1]+k[55]), 21)
        a = b + leftRotate( (a+I(b,c,d)+M[8]+k[56]), 6)
        d = a + leftRotate( (d+I(a,b,c)+M[15]+k[57]), 10)
        c = d + leftRotate( (c+I(d,a,b)+M[6]+k[58]), 15)
        b = c + leftRotate( (b+I(c,d,a)+M[13]+k[59]), 21)
        a = b + leftRotate( (a+I(b,c,d)+M[4]+k[60]), 6)
        d = a + leftRotate( (d+I(a,b,c)+M[11]+k[61]), 10)
        c = d + leftRotate( (c+I(d,a,b)+M[2]+k[62]), 15)
        b = c + leftRotate( (b+I(c,d,a)+M[9]+k[63]), 21)
        A = (A + a)%(2**32)
        B = (B + b)%(2**32)
        C = (C + c)%(2**32)
        D = (D + d)%(2**32)
    A = "{0:08x}".format(int.from_bytes(binascii.unhexlify("{0:08x}".format(A)),byteorder='little'))
    B = "{0:08x}".format(int.from_bytes(binascii.unhexlify("{0:08x}".format(B)),byteorder='little'))
    C = "{0:08x}".format(int.from_bytes(binascii.unhexlify("{0:08x}".format(C)),byteorder='little'))
    D = "{0:08x}".format(int.from_bytes(binascii.unhexlify("{0:08x}".format(D)),byteorder='little'))
    return(A+B+C+D)

def encrypt(message):
    return md5(bytes(message, 'utf-8'))
