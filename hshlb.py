import hashlib
import secrets

# password.encode() will convert the password to bytes
password = input()
byte_password = password.encode()
salt = secrets.token_bytes(32)

# hashed = hashlib.pbkdf2_hmac('algorithm', b'password', b'salt', number of iterations)
hashed = hashlib.pbkdf2_hmac('sha256', byte_password, salt, 64)
print('sha256: ', hashed)
print('salt: ', salt)