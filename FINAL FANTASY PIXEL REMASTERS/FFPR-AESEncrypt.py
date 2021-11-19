from py3rijndael import RijndaelCbc, ZeroPadding
from Cryptodome.Protocol import KDF
import zlib
import base64
import sys
import os
from FFPR_GenerateSaveFilenames import GenerateFilenames

abspath = os.path.abspath(sys.argv[0])

dname = os.path.dirname(abspath)

os.chdir(dname)
filenames = GenerateFilenames()
password = b"TKX73OHHK1qMonoICbpVT0hIDGe7SkW0"
salt = b"71Ba2p0ULBGaE6oJ7TjCqwsls1jBKmRL"
keyiv = KDF.PBKDF2(password,salt,64,10)
key = keyiv[:32]
iv = keyiv[32:]
#keylog = open("keyiv.bytes",'wb')
#keylog.write(keyiv)
#print(len(key))
#print(len(iv))
cipher = RijndaelCbc(key,iv,ZeroPadding(32),32)

def deflate(data):
    decompress = zlib.compressobj(
            -1,  # see above
            wbits=-15
    )
    deflated = decompress.compress(data)
    deflated += decompress.flush()
    return deflated

def obfuscateFile(inFile):
    buffer = inFile.read()
    #print(buffer[0])
    defBytes = deflate(bytes(buffer,encoding='utf-8'))
    encBytes = cipher.encrypt(defBytes)
    b64Bytes = base64.b64encode(encBytes)
    print(b64Bytes)
    finalBuffer = bytearray()
    finalBuffer.append(0xef)
    finalBuffer.append(0xbb)
    finalBuffer.append(0xbf)
    finalBuffer.extend(b64Bytes)
    finalBuffer.append(0x0d)
    finalBuffer.append(0x0a)
    outFile = open(inFile.name+".enc",'wb')
    outFile.write(finalBuffer)


if __name__ == "__main__":

    if len(sys.argv) > 1:
        for i, arg in enumerate(sys.argv):
            if i > 0:
                obfuscateFile(open(arg,'r'))
    else:
        filename = input("Enter path to the save file:")
        obfuscateFile(open(filename,'r'))