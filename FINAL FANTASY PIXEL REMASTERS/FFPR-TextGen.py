import sys
import os
import struct

abspath = os.path.abspath(sys.argv[0])

dname = os.path.dirname(abspath)

os.chdir(dname)

def writeInt(file,val):
    file.write(struct.pack("i",val))

def writeCSharpString(file,stringIn):
    writeInt(file,len(stringIn))
    file.write(stringIn.encode(encoding='utf-8'))
    while(file.tell()%4) != 0:
        file.write(bytes([0]))

#script generates a TextAsset data structure based on the given file
#TextAsset only has two major structures
#Name and Buffer
#Editing buffer requires editing the size of the buffer at the start, which is what this will do programmatically
#

def createUnityTextAsset(inFile):
    outFile = open(inFile.name+".textasset",'wb') #write binary is to allow this to also work on .mab/.sab audio present within the files
    dropExtension = input("Drop Extension from asset name? (y/n)")
    name = os.path.basename(inFile.name)
    if dropExtension == 'y' or dropExtension == 'Y':
        name = name.split(".")[0]
    writeCSharpString(outFile,name)
    buffer = inFile.read()
    writeInt(outFile,len(buffer))
    outFile.write(buffer)
    inFile.close()
    outFile.close()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        for i, arg in enumerate(sys.argv):
            if i > 0:
                createUnityTextAsset(open(arg,'rb'))
    else:
        filename = input("Enter the name of the file you want to convert to a TextAsset:")
        createUnityTextAsset(open(filename,'rb'))
