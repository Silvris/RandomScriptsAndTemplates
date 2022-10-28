import base64
import sys
import os

abspath = os.path.abspath(sys.argv[0])

dname = os.path.dirname(abspath)

os.chdir(dname)


def deobfuscateFile(inFile):
    buffer = inFile.read()
    finalFile = inflate(buffer)
    outFile = open(inFile.name+".inflated",'wb')
    print(outFile.name)
    outFile.write(finalFile)


if __name__ == "__main__":

    if len(sys.argv) > 1:
        for i, arg in enumerate(sys.argv):
            if i > 0:
                deobfuscateFile(open(arg,'rb'))
    else:
        filename = input("Enter path to the file:")
        deobfuscateFile(open(filename,'rb'))