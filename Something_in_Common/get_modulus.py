from Crypto.Util.number import *
import random

product = 1
arr = []
while product<(1<<1040):
    x = random.choice([getPrime(256),getPrime(128),getPrime(64)])
    arr.append(x)
    product*=x

for i in range(len(arr)):
    x = random.choice([getPrime(8),getPrime(10),getPrime(12)])
    for j in range(2):
        index = random.randint(0,len(arr)-1)
        arr[index]*=x

print(arr)