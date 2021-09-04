# AES 256 encryption/decryption using pycrypto library
from base64 import b64encode, b64decode
import hashlib
import os
from Cryptodome import Random
from Cryptodome.Cipher import AES

# AES encryption uses a 16 byte block size. Padding with characters at the end
def block_padding(block):
    BLOCK_SIZE = 16
    return block + ((BLOCK_SIZE - len(block) % BLOCK_SIZE) * chr(BLOCK_SIZE - len(block) % BLOCK_SIZE)).encode("utf-8")

# Unpadding the extra characters at the end after decrpytion
def block_unpadding(block):
    return block.rstrip()

key = "F!ntecH"

def encode(raw_text, password=key):
    # Encode the raw_text if the input is string format (i.e., not byte format)
    if(isinstance(raw_text, str)):
        raw_text = raw_text.encode("utf-8")
    private_key = hashlib.sha256(password.encode("utf-8")).digest() # Generate a secure private key
    raw_text = block_padding(raw_text)
    iv = Random.new().read(AES.block_size) # A random initialization vector (salt) for a cipher
    cipher = AES.new(private_key, AES.MODE_CBC, iv) # Cipher Blocker Chaining (advanced form of block cipher encryption)
    return b64encode(iv + cipher.encrypt(raw_text)) # encode bytes-type data into base64 a convenient string representation

def decode(cipher_text, password=key):
    private_key = hashlib.sha256(password.encode("utf-8")).digest()
    cipher_text = b64decode(cipher_text)
    iv = cipher_text[:16]
    cipher = AES.new(private_key, AES.MODE_CBC, iv)
    decrypted_text = block_unpadding(cipher.decrypt(cipher_text[16:]))
    return bytes.decode(decrypted_text)

password = None
try:
    password = open(".pwd", "r").read()
except IOError:
    pass

# Uncomment the following lines to test it standalone
# Case 1 - If input is in bytes already
# encrypted = encode("This is a secret message".encode("utf-8"), key)
# print(encrypted)
# Case 2 - If input is in string
# encrypted = encode("This is a secret message", key)
# print(encrypted)
# decrypted = decode(encrypted, key)
# print(decrypted)