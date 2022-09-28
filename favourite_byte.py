hex_string ='73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d'
byte_string = bytes.fromhex(hex_string)

s='' 

for i in range (256):
	s=''.join(chr(int(j) ^ i) for j in byte_string)
	if s[:6]=='crypto':
		print(f"[*] - the secret key is : {i}")
		print(f"[*] - The flag : {s}")
	s=''
