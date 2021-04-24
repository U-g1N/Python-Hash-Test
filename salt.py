import secrets
import scrypt

# password.encode() will convert the password to bytes
password = input()
byte_password = password.encode()
salt = secrets.token_bytes(32)

# scrypt_key = scrypt.hash(byte_password, salt, N=16384, r=8, p=1, b=32)
# N = No. of iterations
# r = Size of Block
# p = paralellism (threads)
# b = bytes
scrypt_key = scrypt.hash(byte_password, salt, 16384, 8, 1, 32)
print('salt: ', salt)
print('key: ', scrypt_key)
