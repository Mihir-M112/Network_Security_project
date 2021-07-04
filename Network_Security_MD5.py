#----------------ShapeAI Network Security project ------------------

import hashlib

print(hashlib.algorithms_available)
print('--------------------------------------------------------')

result = hashlib.md5(b"Hello MD5").hexdigest()

result = hashlib.md5("Hello MD5".encode("utf-8")).hexdigest()
print("Hello MD5 : ",result)
print('--------------------------------------------------------')


M = hashlib.md5(b"Hello MD5")
 
print(M.name)
print(M.digest_size) # 16 bytes (128 bits)
print(M.digest())    # bytes
print(M.hexdigest()) # bytes in hex representation
print('--------------------------------------------------------')
print('--------------------------------------------------------')




blake = "Hello Blake-2b".encode()
print("BLAKE2b:", hashlib.blake2b(blake).hexdigest())
print('--------------------------------------------------------')
print('--------------------------------------------------------')


sha = "SHA-256".encode()
print("SHA-256:", hashlib.sha256(sha).hexdigest())


