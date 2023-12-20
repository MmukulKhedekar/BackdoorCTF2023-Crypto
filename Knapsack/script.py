import random
import hashlib
from Crypto.Util.number import bytes_to_long
from Crypto.Cipher import AES

flag = b"flag{N0t_r34dy_f0r_M3rkl3-H3llman}"
secret = b"atTS4"
key = hashlib.sha256(secret).digest()[:16]

cipher = AES.new(key, AES.MODE_ECB)
padded_flag = flag + b'\x00'*(-len(flag)%16)

ciphertext = cipher.encrypt(padded_flag)

f = open('output.txt','w')
f.write(f"Ciphertext: {ciphertext.hex()}\n\n")

while True:
    arr = [ random.randint(1,1000000000000) for i in range(40) ]
    print(*arr,sep=', ')

    k = bytes_to_long(secret)

    s = 0
    for i in range(40):
        if k&(1<<i):
            s+=arr[i]
    print(s)

    dicl = dict()
    dicr = dict()

    for i in range((1<<20)):
        su = 0
        for j in range(20):
            if i&(1<<j):
                su+=arr[j]
        if su not in dicl:
            dicl[su] = list()
        dicl[su].append(i)

    for i in range((1<<20)):
        su = 0
        for j in range(20):
            if i&(1<<j):
                su+=arr[j+20]
        if su not in dicr:
            dicr[su] = list()
        dicr[su].append(i)

    count = 0
    for i in dicl:
        if s-i in dicr:
            count += 1
            print(i,s-i)
            print(dicl[i],dicr[s-i])

    if count==1:
        f.write(f'numbers: {str(arr)[1:-1]}\nsum: {s}\n')
        f.close()
        break