key=b'1234567890123456'
dec = ucryptolib.aes(key, 1) # set up decryption using "key"
data_bytes=dec.decrypt(msg1)
data1=data_bytes.decode().rstrip('\x00')
print('data1 =',data1)
data_bytes=dec.decrypt(msg2)
data2=data_bytes.decode().rstrip('\x00')
print('data2 =',data2)
