from py3rijndael import RijndaelCbc, ZeroPadding
from Cryptodome.Cipher import AES
import os
import sys
from binascii import hexlify, unhexlify

abspath = os.path.abspath(sys.argv[0])

dname = os.path.dirname(abspath)

os.chdir(dname)

key = unhexlify("aec60f320d10219be940a19cb6cc1c60")
iv = unhexlify("97ca910f529581b43b847a27b5064fa5")
cipher = AES.new(key,AES.MODE_CBC,iv)

def decryptFile(inputFile):
    output = open("gamenew.rom",'wb')
    encData = inputFile.read()
    decData = cipher.decrypt(encData)
    output.write(decData)
    output.close()

def encryptFile(inputFile):
    output = open("gamenew.rom",'wb')
    decData = inputFile.read()
    encData = cipher.encrypt(decData)
    output.write(encData)
    output.close()

if __name__ == "__main__":

    filename = input("Enter path to the SNES rom:")
    encrypt = input("Encrypt file? (y/n):")
    if encrypt == "y":
        encryptFile(open(filename,'rb'))
    else:
        decryptFile(open(filename,'rb'))