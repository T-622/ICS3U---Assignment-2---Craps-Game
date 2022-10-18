from cryptography.fernet import Fernet
import os

def generateKey():
  key = Fernet.generate_key()
  # Write Encryption Key To "MyKey.key" File
  with open('MyKey.key', 'wb') as mykey:
   mykey.write(key)

def readKey():
  with open('MyKey.key', 'rb') as mykey:
    key = mykey.read()
  return key
