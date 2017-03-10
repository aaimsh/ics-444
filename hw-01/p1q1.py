import hashlib
file = open('PythonCrypto.txt', 'r')
txt = file.read()
file.close()
print('text before hashing:\n' + txt)
m = hashlib.sha512(txt).hexdigest()
print('text after hashing: \n' + m)
