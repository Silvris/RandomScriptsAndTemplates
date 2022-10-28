import os
import sys
import zlib
import struct

def readUInt(file):
    return struct.unpack("I",file.read(4))[0]

def align(file, modulo):
    current = file.tell()
    over = current % modulo
    if(over != 0):
        remaining = modulo - over
        file.seek(current+remaining)

def readFile(f):
    basePath = f.name.split('.')[0] + "/"
    os.makedirs(basePath,exist_ok=True)
    fileNum = readUInt(f) #number of files present within the container
    sizes = list()
    for _ in range(fileNum):
        sizes.append([readUInt(f), readUInt(f)])
    for i in range(fileNum):
        output = bytearray()
        #time for the magic
        f.seek(sizes[i][0])
        output.extend(f.read(sizes[i][1]))
        nFile = open(basePath+"{}.bin".format(i),'wb')
        nFile.write(output)
        nFile.close()

if __name__ == "__main__":
    for i, arg in enumerate(sys.argv):
        if i > 0:
            readFile(open(arg,'rb'))