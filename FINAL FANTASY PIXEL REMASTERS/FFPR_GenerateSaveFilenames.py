import base64
from hashlib import sha256
import sys
import os
def GenerateFilename(filename):
    print(filename)
    hashval = sha256(filename.encode('utf-8'))
    #print(hashval.digest())
    encname = base64.b64encode(hashval.digest())
    print(encname)
    return encname

def GenerateFilenames(lockTo30 = False):
    filenames = list()
    for i in range(99):
        #unknown if it actually goes to 99, easier to just prepare in case
        #slot22 is quick save
        filenames.append("slot{}.sav".format(i))
    filenames.append("system_slot.sav")#autosave
    filenames.append("PictureBook.sav")#backgrounds? bestiary?
    gennedFilenames = dict()
    for filename in filenames:
        #print(filename)
        hashval = sha256(filename.encode('utf-8'))
        #print(hashval.digest())
        encname = base64.b64encode(hashval.digest())
        #print(encname)
        gennedFilenames[encname] = filename

    return gennedFilenames

if __name__ == "__main__":

    if len(sys.argv) > 1:
        for i, arg in enumerate(sys.argv):
            if i > 0:
                GenerateFilename(arg)
    else:
        os.chdir(os.path.dirname(sys.argv[0]))
        outfile = open("FFPR-SaveFileNames.txt",'w')
        filenames = GenerateFilenames(True)
        for file in list(filenames.keys()):
            outfile.write("{}:\t{}\n".format(filenames[file],file.decode('utf-8')))
        outfile.close()