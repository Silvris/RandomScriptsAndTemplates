from os import error
import struct
strings = []

def readUniString(file):
    lastByte = file.read(1)
    currentByte = file.read(1)
    string = bytearray()
    while(1):
        if currentByte == b'':
            return
            #this is python's method of EOF
        elif currentByte == b'\x00' and lastByte == b'\x00' and len(string)%2 == 0:
            return string.decode('utf-16-le',errors="ignore")
        elif currentByte == b'\x00' and lastByte == b'\x0A':
            #UTF16 new line, replace with a text one for output
            string.extend(bytes([92,0]))
            currentByte = bytes([110,0])
        elif currentByte == b'\x00' and lastByte == b'\x0D':
            #UTF16 return, replace with a text one for output
            string.extend(bytes([92,0]))
            currentByte = bytes([114,0])
        else:
            string.extend(lastByte)
        lastByte = currentByte
        currentByte = file.read(1)

def deserialize():
    gametext = open(r"D:\New folder (3)\lang_jp\gametext\gametext.bin",'rb')
    outtext = open(r"D:\New folder (3)\lang_jp\gametext\gametextOutNew.csv",'w',encoding="utf-8")

    count = struct.unpack("I",gametext.read(4))[0]
    initialOff = struct.unpack("I",gametext.read(4))[0]
    for i in range(count):
        strings.append(struct.unpack("I",gametext.read(4))[0])
    for i in range(count):
        gametext.seek(strings[i]+initialOff)
        strings[i] = readUniString(gametext)
    for i in range(count):
        outtext.write("{},{}\n".format(i,strings[i]))
    gametext.close()
    outtext.close()

def serialize():
    intext = open(r"D:\New folder (3)\lang_jp\gametext\gametextOutNew.csv",'r',encoding="utf-8")
    gameout = open(r"C:\Users\Owner\AppData\Roaming\Vita3K\Vita3K\ux0\app\PCSG00502\RomImage_PSP2_JP\lang_jp\gametext\gametext.bin",'wb')

    outStrings = bytearray()
    writtenStrings = []
    offsets = []
    outOffs = []
    for line in intext:
        index, strin = line.split(',')
        strin = strin.replace('\n','').replace('\r','')
        strin = strin.replace("\\n","\n")
        strin = strin.replace("\\r","\r")
        if strin in writtenStrings:
            outOffs.append(offsets[writtenStrings.index(strin)])
        else:
            offset = len(outStrings)
            outOffs.append(offset)
            offsets.append(offset)
            writtenStrings.append(strin)
            strin = bytearray(strin.encode('utf-16-le'))
            strin.append(0)
            strin.append(0)#null termination
            outStrings.extend(strin)
    gameout.write(struct.pack("II",len(outOffs),8))
    startingOffset = len(outOffs)*4
    for offset in outOffs:
        gameout.write(struct.pack("I",offset+startingOffset))
    gameout.write(outStrings)
#deserialize()
serialize()