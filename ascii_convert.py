import base64

#print(ord("A"))
#print(chr(65))
#print(hex(65))


#decimal_values = [65,66,67]
#byte_stream = bytes(decimal_values)
#print(byte_stream)


#plainText = "A"
#password = "B"
#ascii_decimal = ord(plainText) ^ ord(password)
#ascii_human = chr(ascii_decimal)
#ascii_hex = hex(ascii_decimal)
#base64_encoded = base64.b64encode(ascii_human.encode('utf-8')).decode('utf-8')
#print(ascii_hex)

#ascii_decrypt = int(ascii_hex, 16) ^ ord(password)
#print(ascii_decrypt)
#print(chr(ascii_decrypt))

#Only One Character At A Time
#ascii_integer = ord("AAA")
#print(ascii_integer)

MyPlainText = "ABCDE"
XOR_KEY = "PASSW"
Encrypted_Values = []
for Position, PlainTextCharacter in enumerate(MyPlainText):
    print(Position, PlainTextCharacter)
    print(Position, XOR_KEY[Position])
    print("XORing the two above values together and saving the result to a list!")
    encrypted_byte = ord(PlainTextCharacter) ^ ord(XOR_KEY[Position])

    Encrypted_Values.append(encrypted_byte)
print("The encrypted Decimal Values when XORing each of these letters together is:")
print(Encrypted_Values)

print("Here are the Hex values")
for i in Encrypted_Values:
    print(hex(i)+" ", end='')
print()
print("Here are the Hex Values with a space between them instead of 0x")
for i in Encrypted_Values:
    print(format(i, 'x')+" ", end='')