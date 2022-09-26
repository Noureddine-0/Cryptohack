#in this challenge , you should pay attention that the xor operator is self-inverse to get a solid idea about the key .writing a program after this become an easy task
string=bytes.fromhex('0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104')
L=[109,121,88,79,82,107,101,121]
s=''
for i in range(0,len(string),8):
	s=s+''.join(chr(j ^ o) for j,o in list(zip(string[i:i+8],L)))
print(s)
