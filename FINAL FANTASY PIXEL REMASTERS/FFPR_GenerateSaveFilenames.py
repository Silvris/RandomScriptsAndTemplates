import base64
from hashlib import sha256
def GenerateFilenames():
    filenames = list()
    for i in range(99):
        #unknown if it actually goes to 99, easier to just prepare in case
        filenames.append("slot{}.sav".format(i))
    filenames.append("system_slot.sav")#quicksave
    filenames.append("PictureBook.sav")#backgrounds?
    gennedFilenames = dict()
    for filename in filenames:
        print(filename)
        hashval = sha256(filename.encode('utf-8'))
        print(hashval.digest())
        encname = base64.b64encode(hashval.digest())
        print(encname)
        gennedFilenames[encname] = filename

    return gennedFilenames