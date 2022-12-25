import os
import sys
import zlib
import struct

def readUInt(file):
    return struct.unpack("I",file.read(4))[0]

def readNullTermString(file):
    string = bytearray()
    byte = file.read(1)
    while(byte[0] != 0x00):
        string.extend(byte)
        byte = file.read(1)
    return string.decode('utf-8')

def align(file, modulo):
    current = file.tell()
    over = current % modulo
    if(over != 0):
        remaining = modulo - over
        file.seek(current+remaining)

def readFile(f):
    basePath = f.name.split('.')[0] + "/"
    os.makedirs(basePath,exist_ok=True)
    f.seek(0,os.SEEK_END)
    fileSize = f.tell() + 1
    f.seek(0,0)
    assert f.read(8) == b"TLSK3100"
    fileNum = readUInt(f) #number of files present within the container
    f.read(4) #remaining file
    offsetOff = readUInt(f)
    #have all the info we really need
    sizes = list()
    offsets = list()
    names = list()
    f.seek(offsetOff + 64) #64 is header length
    for i in range(fileNum):
        offsets.append(readUInt(f))
        f.read(16) #16 null bytes between
    for i in range(fileNum):
        names.append(readNullTermString(f))
    for i in range(fileNum):
        if i == fileNum - 1:
            sizes.append(fileSize - offsets[i])
        else:
            sizes.append(offsets[i+1] - offsets[i])
    for i in range(fileNum):
        #time for the magic
        f.seek(offsets[i])
        output = f.read(sizes[i])
        nFile = open(basePath+"{}.tlsktex".format(names[i]),'wb')
        nFile.write(output)
        nFile.close()

if __name__ == "__main__":
    for i, arg in enumerate(sys.argv):
        if i > 0:
            readFile(open(arg,'rb'))