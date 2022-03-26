# Message digest (Rivest back in 1991)
# 128 bits long sequence (hash or the message digest)
# This approach is not collision free !!!
# So it's no longer secure
from hashlib import md5

s = 'This is a message!'
result = md5(s.encode())
# 32 hexadecimal characters
# Nibles (we can store a hexadecimal character on 4 bits which is 0.5 byte)
print(result.hexdigest())