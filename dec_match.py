encrypted_hex = ["0xc", "0x3b", "0x13", "0x2d", "0x23", "0x2a", "0x2f", "0x16", "0x26", "0x39", "0x36"] 

KEY = "ABC"

encrypted_values = [int(h, 16) for h in encrypted_hex]
print(encrypted_values)

decrypted_text = []
for position, encrypted_byte in enumerate(encrypted_values):
    letter_in_key = KEY[position % len(KEY)]
    decrypted_byte = encrypted_byte ^ ord(letter_in_key)
    decrypted_text.append(chr(decrypted_byte))

original_text = ''.join(decrypted_text)
print(original_text)
