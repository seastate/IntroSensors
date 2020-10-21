#===========================================
# Part 1: On the sending machine
#===========================================
import ucryptolib
# The original data message:
orig_data='Instrument1,Sensor3,watertemp,NorthLakeWashingtonWA,3711,2020-3-19 1:20:17,7.6875'
smpl=3711

# Encrypting the sample number
key=b'zlfexqpwozpczacr'
enc = ucryptolib.aes(key, 1)   # set up encryption using "key"
salt='kiypsxsult'
data = salt+str(smpl)  # convert smpl to a string, and add the "salt"
data_bytes = data.encode() # convert string to bytes
# Pad to 16 bytes:
data_bytes16 = data_bytes + b'\x00' * ((16 - (len(data_bytes) % 16)) % 16)
msg1=enc.encrypt(data_bytes16) # encrypt the block of bytes
print('msg1 = ',msg1)
# Append the encrypted block to the message
aug_data=str(orig_data+','+msg1) 
print(aug_data)

