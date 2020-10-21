#===========================================
# Part 2: On the receiving machine
#===========================================
import ucryptolib

# The output from encrypt_msg.py
aug_data="Instrument1,Sensor3,watertemp,NorthLakeWashingtonWA,3711,2020-3-19 1:20:17,7.6875,b'$\\xd8\\xd8\\xa5\\x93D\\xd1\\xb3\\xd9=\\xa8$x\\xf6n\\xce'"

msg_ind=aug_data.rfind(',')  # find index of the last comma
print(msg_ind)
msg1str=aug_data[msg_ind+1:] # get the encrypted block
print(msg1str)
msg1=eval(msg1str)           # convert back to bytes
orig_data=aug_data[0:msg_ind-1] # get the original data
print(orig_data)

key=b'zlfexqpwozpczacr'
dec = ucryptolib.aes(key, 1) # set up decryption using "key"
data_bytes=dec.decrypt(msg1)
data1=data_bytes.decode().rstrip('\x00')
print('data1 =',data1)
digits=['0','1','2','3','4','5','6','7','8','9']
data1_digits=''.join([data1[i] for i in range(len(data1)) if data1[i] in digits])
new_smpl=int(data1_digits)
print(new_smpl)
