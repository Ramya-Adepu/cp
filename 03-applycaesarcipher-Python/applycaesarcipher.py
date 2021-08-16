# A Caesar Cipher is a simple cipher that works by shifting each letter in 
# the given message by a certain number. For example, if we shift the message 
# "We Attack At Dawn" by 1 letter, it becomes "Xf Buubdl Bu Ebxo"
# Write the function applyCaesarCipher(message, shift) which shifts the given 
# message by shift letters. You are guaranteed that message is a string, and 
# that shift is an integer between -25 and 25. Capital letters should stay capital 
# and lowercase letters should stay lowercase, and non-letter characters should not be changed. 
# Note that "Z" wraps around to "A". So, for example:
# assert(applyCaesarCipher("We Attack At Dawn", 1) == "Xf Buubdl Bu Ebxo")
# assert(applyCaesarCipher("zodiac", -2) == "xmbgya")


def fun_applycaesarcipher(msg, shift):
	s=""
	# print(ord("A"), ord("Z"), ord("a"), ord("z"))
	# A-65, Z-90, a-97, z-122
	for i in  msg:
		r=ord(i)
		if((r>=65 and r<=90) or (r>=97  and r<=122)):
			if(r+shift<65):
				b=65-(r+shift+1)
				s+=chr(90-b)
			elif(r<=90 and r+shift>90):
				b=r+shift-90-1
				s+=chr(65+b)
			elif(r>=97 and r+shift<97):
				b=97-(r+shift+1)
				s+=chr(122-b)
			elif(r+shift>122):
				b=r+shift-122-1
				s+=chr(97+b)
			else:
				s+=chr(r+shift)
		else:
			s+=i	
	return s
print(fun_applycaesarcipher("abcdxyz", 3))
#     ("We Attack At Dawn", 1, "Xf Buubdl Bu Ebxo"), ("zodiac", -2, "xmbgya"),
# ("ABCDXYZ", -3,"XYZAUVW"),("ABCDXYZ", 3,"DEFGABC"), ("abcdxyz", -3,"xyzauvw"),
# ("abcdxyz", 3,"defgabc")
# ])


