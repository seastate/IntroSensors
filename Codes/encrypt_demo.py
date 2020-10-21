import ucryptolib
key=b'1234567890123456'
enc = ucryptolib.aes(key, 1) # set up encryption using "key"
data = 'input plaintext'   # first message string
data_bytes = data.encode() # convert string to bytes
# Pad to 16 bytes:
data_bytes16 = data_bytes + b'\x00' * ((16 - (len(data_bytes) % 16)) % 16)
msg1=enc.encrypt(data_bytes16)
print('msg1 = ',msg1)
data = 'input pl'          # shorter second message, should get padded
data_bytes = data.encode() # convert string to bytes
# Pad to 16 bytes:
data_bytes16 = data_bytes + b'\x00' * ((16 - (len(data_bytes) % 16)) % 16)
msg2=enc.encrypt(data_bytes16)
print('msg2 = ',msg2)
