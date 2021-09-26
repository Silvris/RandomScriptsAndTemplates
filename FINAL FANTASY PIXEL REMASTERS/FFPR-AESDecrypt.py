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
keylog = open("keyiv.bytes",'wb')
keylog.write(keyiv)
print(len(key))
print(len(iv))
cipher = RijndaelCbc(key,iv,ZeroPadding(32),32)

def inflate(data):
    decompress = zlib.decompressobj(
            -15  # see above
    )
    inflated = decompress.decompress(data)
    inflated += decompress.flush()
    return inflated

def deobfuscateFile(inFile):
    buffer = inFile.read()
    buffer = buffer[3:-2]
    while (len(buffer) % 4) != 0:
        buffer += '='
    #print(buffer[0])
    encBytes = base64.b64decode(buffer,validate=False)
    print(len(encBytes))
    encBytes = bytearray(encBytes)
    while(len(encBytes) % 32) != 0:
        encBytes.append(0)
    decBytes = cipher.decrypt(bytes(encBytes))
    finalFile = inflate(decBytes)
    if os.path.basename(inFile.name).encode('utf-8') in filenames:
        outFile = open(os.path.dirname(inFile.name)+"/"+filenames[os.path.basename(inFile.name).encode('utf-8')],'wb')
    else:
        outFile = open(inFile.name+".dec",'wb')
    print(outFile.name)
    outFile.write(finalFile)


if __name__ == "__main__":

    if len(sys.argv) > 1:
        for i, arg in enumerate(sys.argv):
            if i > 0:
                deobfuscateFile(open(arg,'r'))
    else:
        filename = input("Enter path to the save file:")
        deobfuscateFile(open(filename,'r'))