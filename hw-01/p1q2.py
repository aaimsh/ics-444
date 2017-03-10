import hashlib
from Crypto import PublicKey
from Crypto.PublicKey import RSA

#Read the txt file and generate md5 signture
file = open('PythonCrypto.txt', 'rw')
text = file.read()
file.close()
m = hashlib.md5(text).hexdigest()

#encrypt the signture using RSA PublicKey
key = RSA.generate(2048) #RSA key using 2048 bits
publicKey = key.publickey()
publicKey.exportKey(format='DIR', passphrase=None, pkcs=1)
mEncrypted = publicKey.encrypt(m, 32) #encrypt with 32 byte
print(mEncrypted)
encoded_file = open('PythonCrypto_encoded.txt', 'w')
encoded_file.write(str(mEncrypted))
encoded_file.close
