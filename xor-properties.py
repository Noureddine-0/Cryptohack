from binascii import *
from pwn import xor

# first solution 

def xor(s1,s2):

    return ''.join(format(int(a,16) ^ int(b,16),'x') for a,b in list(zip(s1,s2)))
    
char1='37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e'
char2='c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1'
char3='04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf '
key1='a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313'

key2=xor(char1,key1)
key3=xor(char2,key2)
key4=xor(xor(key1,key2),key3)

flag=xor(char3,key4)

print("the flag is ;",end=' ')
print(f"[*] FLAG:{unhexlify(flag)}")


#seconde solution


L1=bytes.fromhex('a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313')
L2=bytes.fromhex('c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1')
flag=bytes.fromhex('04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf')
print(xor(L1,L2,flag))



# first solution 

def xor(s1,s2):

    return ''.join(format(int(a,16) ^ int(b,16),'x') for a,b in list(zip(s1,s2)))
    
char1='37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e'
char2='c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1'
char3='04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf '
key1='a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313'

key2=xor(char1,key1)
key3=xor(char2,key2)
key4=xor(xor(key1,key2),key3)

flag=xor(char3,key4)

print("the flag is ;",end=' ')
print(f"[*] FLAG:{unhexlify(flag)}")


#seconde solution


L1=bytes.fromhex('a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313')
L2=bytes.fromhex('c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1')
flag=bytes.fromhex('04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf')
print(xor(L1,L2,flag))

