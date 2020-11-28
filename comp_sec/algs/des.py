import copy

init_perm_table = [x-1 for x in [58,50,42,34,26,18,10,2,60,52,44,36,28,20,12,4,62,54,46,38,30,22,14,6,64,56,48,40,32,24,16,8,57,49,41,33,25,17,9,1,59,51,43,35,27,19,11,3,61,53,45,37,29,21,13,5,63,55,47,39,31,23,15,7]]
key_shifts_per_round = [1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1]
PC1_table = [x-1 for x in [57,49,41,33,25,17,9,1,58,50,42,34,26,18,10,2,59,51,43,35,27,19,11,3,60,52,44,36,63,55,47,39,31,23,15,7,62,54,46,38,30,22,14,6,61,53,45,37,29,21,13,5,28,20,12,4]]
PC2_table = [x-1 for x in [14,17,11,24,1,5,3,28,15,6,21,10,23,19,12,4,26,8,16,7,27,20,13,2,41,52,31,37,47,55,30,40,51,45,33,48,44,49,39,56,34,53,46,42,50,36,29,32]]
E_selection_table = [x-1 for x in [32,1,2,3,4,5,4,5,6,7,8,9,8,9,10,11,12,13,12,13,14,15,16,17,16,17,18,19,20,21,20,21,22,23,24,25,24,25,26,27,28,29,28,29,30,31,32,1]]
P_table = [x-1 for x in [16,7,0,21,29,12,28,17,1,15,23,26,5,18,31,10,2,8,24,14,32,27,3,9,19,13,30,6,22,11,4,25]]
final_perm_table = [x-1 for x in [40,8,48,16,56,24,64,32,39,7,47,15,55,23,63,31,38,6,46,14,54,22,62,30,37,5,45,13,53,21,61,29,36,4,44,12,52,20,60,28,35,3,43,11,51,19,59,27,34,2,42,10,50,18,58,26,33,1,41,9,49,17,57,25]]
#s-boxes
s_boxes = []
s_boxes.append([[14,4,13,1,2,15,11,8,3,10,6,12,5,9,0,7],[0,15,7,4,14,2,13,1,10,6,12,11,9,5,3,8],[4,1,14,8,13,6,2,11,15,12,9,7,3,10,5,0],[15,12,8,2,4,9,1,7,5,11,3,14,10,0,6,13]])
s_boxes.append([[15,1,8,14,6,11,3,4,9,7,2,13,12,0,5,10],[3,13,4,7,15,2,8,14,12,0,1,10,6,9,11,5],[0,14,7,11,10,4,13,1,5,8,12,6,9,3,2,15],[13,8,10,1,3,15,4,2,11,6,7,12,0,5,14,9]])
s_boxes.append([[10,0,9,14,6,3,15,5,1,13,12,7,11,4,2,8],[13,7,0,9,3,4,6,10,2,8,5,14,12,11,15,1],[13,6,4,9,8,15,3,0,11,1,2,12,5,10,14,7],[1,10,13,0,6,9,8,7,4,15,14,3,11,5,2,12]])
s_boxes.append([[7,13,14,3,0,6,9,10,1,2,8,5,11,12,4,15],[13,8,11,5,6,15,0,3,4,7,2,12,1,10,14,9],[10,6,9,0,12,11,7,13,15,1,3,14,5,2,8,4],[3,15,0,6,10,1,13,8,9,4,5,11,12,7,2,14]])
s_boxes.append([[2,12,4,1,7,10,11,6,8,5,3,15,13,0,14,9],[14,11,2,12,4,7,13,1,5,0,15,10,3,9,8,6],[4,2,1,11,10,13,7,8,15,9,12,5,6,3,0,14],[11,8,12,7,1,14,2,13,6,15,0,9,10,4,5,3]])
s_boxes.append([[12,1,10,15,9,2,6,8,0,13,3,4,14,7,5,11],[10,15,4,2,7,12,9,5,6,1,13,14,0,11,3,8],[9,14,15,5,2,8,12,3,7,0,4,10,1,13,11,6],[4,3,2,12,9,5,15,10,11,14,1,7,6,0,8,13]])
s_boxes.append([[4,11,2,14,15,0,8,13,3,12,9,7,5,10,6,1],[13,0,11,7,4,9,1,10,14,3,5,12,2,15,8,6],[1,4,11,13,12,3,7,14,10,15,6,8,0,5,9,2],[6,11,13,8,1,4,10,7,9,5,0,15,14,2,3,12]])
s_boxes.append([[13,2,8,4,6,15,11,1,10,9,3,14,5,0,12,7],[1,15,13,8,10,3,7,4,12,5,6,11,0,14,9,2],[7,11,4,1,9,12,14,2,0,6,10,13,15,3,5,8],[2,1,14,7,4,10,8,13,15,12,9,0,3,5,6,11]])


#Returns encrypted message, requires message and key length of 8
def encrypt(message, key):
    #transform message to bits
    msgbits = strToBitList(message)
    keybits = strToBitList(key)
    #Generate subkeys
    key56 = [None] * 56
    for i in range(0,56):
        key56[i] = keybits[PC1_table[i]]
    c_key = [None] * 17
    c_key[0] = key56[:28]
    d_key = [None] * 17
    d_key[0] = key56[28:]
    for i in range(1,17):
        c_key[i] = circular_left_shift(c_key[i-1], key_shifts_per_round[i-1])
        d_key[i] = circular_left_shift(d_key[i-1], key_shifts_per_round[i-1])
    k_key = [None] * 16 #Indexed 0-15
    for i in range(0,16):
        k_key[i] = [None] * 48
        concatenated_key = c_key[i+1]+d_key[i+1]
        for j in range(0,48):
            k_key[i][j] =  concatenated_key[PC2_table[i]]

    #initial permutation
    init_perm = [None] * 64
    for i in range(0,64):
        init_perm[i] = msgbits[init_perm_table[i]]
    l_msg = [None] * 17
    r_msg = [None] * 17
    l_msg[0] = init_perm[:32]
    r_msg[0] = init_perm[32:]

    #16 encryptions
    for i in range (1,17):
        l_msg[i] = copy.deepcopy(r_msg[i-1])
        r_msg[i] = xor_bitlists(l_msg[i-1], f_function(r_msg[i-1], k_key[i-1]))
       

    #final permutation
    concatenated_data = r_msg[16] + l_msg[16]
    permed_data = [None] * 64
    for i in range(0,64):
        permed_data[i] = concatenated_data[final_perm_table[i]]
    return bitListToStr(permed_data)

def decrypt(ciphertext, key):
    #transform message to bits
    msgbits = strToBitList(ciphertext)
    keybits = strToBitList(key)
    #Generate subkeys
    key56 = [None] * 56
    for i in range(0,56):
        key56[i] = keybits[PC1_table[i]]
    c_key = [None] * 17
    c_key[0] = key56[:28]
    d_key = [None] * 17
    d_key[0] = key56[28:]
    for i in range(1,17):
        c_key[i] = circular_left_shift(c_key[i-1], key_shifts_per_round[i-1])
        d_key[i] = circular_left_shift(d_key[i-1], key_shifts_per_round[i-1])
    k_key = [None] * 16 #Indexed 0-15
    for i in range(0,16):
        k_key[i] = [None] * 48
        concatenated_key = c_key[i+1]+d_key[i+1]
        for j in range(0,48):
            k_key[i][j] =  concatenated_key[PC2_table[i]]
    #Inverse order of k_keys for decryptions
    k_key.reverse()

    #initial permutation
    init_perm = [None] * 64
    for i in range(0,64):
        init_perm[i] = msgbits[init_perm_table[i]]
    l_msg = [None] * 17
    r_msg = [None] * 17
    l_msg[0] = init_perm[:32]
    r_msg[0] = init_perm[32:]

    #16 encryptions
    for i in range (1,17):
        l_msg[i] = copy.deepcopy(r_msg[i-1])
        r_msg[i] = xor_bitlists(l_msg[i-1], f_function(r_msg[i-1], k_key[i-1]))
       

    #final permutation
    concatenated_data = r_msg[16] + l_msg[16]
    permed_data = [None] * 64
    for i in range(0,64):
        permed_data[i] = concatenated_data[final_perm_table[i]]
    return bitListToStr(permed_data)

def circular_left_shift(bitList, numShifts):
    return bitList[numShifts:] + bitList[:numShifts]

#Given 6 bit list, block, and boxnum, performs the s-box operation
def sbox_output(block, boxNum):
    row = int(str(block[0]) + str(block[5]), 2)
    col = int("".join([str(bit) for bit in block[1:5]]), 2)
    binary = '{0:04b}'.format(s_boxes[boxNum - 1][row][col])
    return list(binary)

def xor_bitlists(bits1, bits2):
    return [(int(bits1[i]) + int(bits2[i])) % 2 for i in range(0,len(bits1))]

#f function takes 32 bit data block and 48 bit key block
def f_function(data, key):
    #use E-bit selection table
    data48 = [None] * 48
    for i in range (0,48):
        data48[i] = data[E_selection_table[i]]
    xored_data = xor_bitlists(data48, key)
    #put data thru sboxes
    sbox_data = []
    for i in range(1,9):
        sbox_data.extend(sbox_output(xored_data[(i-1)*6:6*i], i))
    #Permute data
    permuted_data = [None] * 32
    for i in range(0,32):
        permuted_data[i] = sbox_data[P_table[i]]
    return permuted_data
    

#converts string to list of bits
def strToBitList(string):
    bitlist = []
    for char in string:
        charbits = bin(ord(char))[2:]
        charbits = '00000000'[len(charbits):] + charbits
        bitlist.extend([int(b) for b in charbits])
    return bitlist

def bitListToStr(bitList):
    chars = []
    for bitRange in range(int(len(bitList) / 8)):
        byte = bitList[bitRange*8:(bitRange+1)*8]
        chars.append(chr(int(''.join([str(bit) for bit in byte]), 2)))
    return ''.join(chars)

def main():
    #Test
    key = "highlife"
    print(decrypt(encrypt("12345678",key), key))
    

if __name__ == "__main__":
    main()