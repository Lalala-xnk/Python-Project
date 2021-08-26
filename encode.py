# -*- coding: utf-8 -*-

import base64
from Crypto.Cipher import AES

password = None
try:
    password = open(".pwd", "r").read()
except IOError:
    pass

pwd = "G!thuB"

def add_to_16(value):
    while len(value) % 16 != 0:
        value += '\0'
    return str.encode(value)

def encode(text, key=pwd):
    aes = AES.new(add_to_16(key), AES.MODE_ECB)
    encrypt_aes = aes.encrypt(add_to_16(text))
    encrypted_text = str(base64.encodebytes(encrypt_aes), encoding='utf-8')
    return encrypted_text

def decode(text, key=pwd):
    aes = AES.new(add_to_16(key), AES.MODE_ECB)
    base64_decrypted = base64.decodebytes(text.encode(encoding='utf-8'))
    decrypted_text = str(aes.decrypt(base64_decrypted), encoding='utf-8').replace('\0', '')
    return decrypted_text
