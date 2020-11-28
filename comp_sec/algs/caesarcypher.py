def CaesarRotate(numrotate):
    array = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    rotatedarray=[]
    count = 0
    temp = []
    while count < numrotate:
        temp.append(array[0])
        array.remove(array[0])
        count = count + 1
    for i in range(len(array)-1):
        rotatedarray.append(array[i])
    for i in range(len(temp)-1):
        rotatedarray.append(temp[i])
    return rotatedarray

def CaesarEncrypt(plaintext,numrotate):
    #turn plaintext to lowercase
    plain = plaintext
    plainlist = list(plain)
    for i in range(len(plainlist)):
        plainlist[i] = plaintext[i].lower()

    array = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    #encrypt plaintext
    plain = ''
    for element in plainlist:
        plain += element
    temp = ''
    cipher = ''
    rotatedarray = CaesarRotate(numrotate)
    for element in plain:
        count = 0
        temp = element
        while  temp != rotatedarray[count]:
            count = count + 1
        cipher = cipher + array[count]
    print(cipher)

def CaesarDecrypt(ciphertext, numrotate):
    #Turn ciphertext to lowercase
    cipher = ciphertext
    cipherlist = list(cipher)
    for i in range(len(cipherlist)):
        cipherlist[i] = cipherlist[i].lower()
    cipher = ''
    for element in cipherlist:
        cipher += element
    
    #Decrypt ciphertext
    temp = ''
    plaintext = ''
    rotatedarray = CaesarRotate(numrotate)
    array = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for element in cipher:
        count = 0
        temp = element
        while  temp != array[count]:
            count = count + 1
        plaintext += rotatedarray[count]
    print(plaintext)


