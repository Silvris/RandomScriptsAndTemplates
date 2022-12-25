from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import pad
import zlib
import sys
import os
import json

xorTbl1 = [146, 171, 137, 62, 115, 248, 151, 216, 185, 39, 222, 236, 82, 100, 168, 247, 231, 220, 26, 76, 54, 5, 139, 101, 9, 13, 81, 106, 213, 61, 65, 228, 122, 25, 244, 184, 126, 188, 214, 191, 16, 169, 67, 6, 217, 42, 120, 39, 210, 212, 222, 105, 100, 5, 158, 213, 30, 21, 246, 207, 80, 238, 15, 122, 29, 182, 245, 31, 11, 18, 14, 72, 218, 102, 144, 156, 14, 104, 6, 86, 61, 238, 34, 32, 101, 126, 163, 148, 233, 166, 35, 112, 64, 102, 228, 136, 127, 251, 5, 137, 112, 11, 9, 4, 196, 240, 103, 136, 253, 239, 242, 201, 134, 221, 90, 33, 28, 89, 26, 6, 209, 198, 7, 32, 171, 23, 17, 32, 178, 63, 86, 101, 117, 177, 176, 138, 233, 6, 229, 128, 220, 70, 164, 171, 169, 79, 28, 245, 73, 55, 75, 172, 16, 45, 179, 64, 116, 19, 208, 201, 212, 112, 180, 74, 175, 12, 112, 129, 224, 250, 252, 108, 68, 141, 235, 0, 71, 87, 147, 86, 202, 83, 133, 233, 119, 104, 53, 53, 135, 143, 1, 251, 99, 239, 112, 7, 133, 175, 144, 148, 124, 131, 191, 218, 244, 34, 130, 219, 145, 82, 58, 207, 220, 166, 119, 154, 164, 141, 247, 27, 145, 15, 182, 84, 125, 212, 83, 198, 180, 137, 33, 167, 131, 46, 244, 164, 197, 33, 131, 129, 20, 150, 5, 143, 112, 185, 121, 141, 202, 189, 60, 62, 116, 85, 141, 65, 196]
xorTbl2 = [15, 32, 19, 53, 25, 5, 112, 117, 174, 4, 186, 145, 244, 73, 64, 222, 185, 41, 147, 145, 192, 17, 213, 241, 171, 15, 200, 199, 197, 150, 188, 245, 177, 33, 102, 116, 190, 58, 30, 60, 210, 202, 199, 52, 98, 251, 164, 129, 54, 218, 210, 133, 126, 87, 139, 253, 75, 34, 138, 9, 60, 168, 176, 23, 72, 197, 224, 210, 227, 204, 31, 126, 11, 87, 191, 245, 74, 161, 142, 176, 107, 71, 145, 235, 196, 55, 118, 89, 149, 104, 41, 155, 176, 20, 0, 41, 26, 175, 235, 157, 26, 209, 157, 105, 186, 83, 121, 39, 152, 150, 179, 169, 147, 218, 158, 244, 23, 196, 83, 17, 78, 134, 61, 123, 162, 132, 206, 247, 86, 149, 218, 154, 181, 241, 149, 154, 169, 40, 49, 112, 189, 79, 193, 255, 181, 128, 8, 213, 118, 11, 18, 86, 92, 218, 78, 147, 148, 34, 198, 54, 132, 130, 208, 2, 187, 24, 243, 162, 69, 4, 75, 239, 147, 226, 83, 255, 197, 61, 198, 34, 124, 248, 129, 74, 131, 132, 62, 218, 163, 1, 5, 135, 97, 251, 236, 58, 126, 190, 67, 156, 140, 102, 144, 114, 192, 35, 194, 121, 135, 79, 206, 86, 92, 163, 185, 140, 1, 133, 126, 54, 218, 24, 254, 68, 254, 196, 141, 152, 246, 25, 128, 6, 249, 41, 150, 22, 104, 15, 138, 96, 194, 196, 83, 84, 50, 175, 42, 189, 65, 96, 57, 248, 63, 13, 193, 115, 103, 76, 115, 252, 149, 42, 131, 109, 206, 199, 92, 50, 13, 163, 35, 242, 251, 30, 116, 22, 197, 170, 17, 79, 153, 208, 87, 150, 223, 136, 198, 236, 104, 34, 174, 27, 155, 141, 202, 151, 65, 230, 134, 107, 82, 247, 175, 157, 60, 71, 252, 33, 153, 170, 174, 188, 59, 36, 98, 197, 210, 236, 141, 69, 0, 112, 201, 235, 245, 8, 86, 109, 83, 220, 213, 222, 36, 166, 252, 161, 32, 185, 90, 152, 139, 165, 83, 190, 115, 242, 224, 118, 43, 5, 197, 84, 88, 64, 106, 226, 45, 196, 168, 51, 240, 142, 205, 188, 213, 207, 152, 148, 40, 193, 165, 24, 146, 245, 185, 91, 28, 11, 119, 2, 39, 223, 66, 78, 23, 128, 134, 228, 59, 26, 115, 91, 17, 38, 167, 253, 215, 150, 232, 164, 90, 75, 78, 105, 96, 172, 194, 98, 134, 15, 197, 34, 77, 165, 12, 16, 75, 127, 165, 85, 72, 180, 89, 13, 77, 73, 7, 107, 77, 188, 131, 133, 35, 211, 168, 220, 145, 216, 237, 107, 189, 35, 93, 44, 84, 81, 13, 108, 26, 151, 177, 88, 241, 147, 91, 166, 242, 64, 28, 22, 164, 87, 21, 202, 140, 63, 255, 122, 252, 47, 127, 114, 145, 58, 151, 37, 86, 45, 185, 251, 59, 154, 80, 182, 11, 42, 148, 143, 120, 2, 234, 80, 188, 215, 198, 101, 14, 146, 159, 20, 82, 147, 111, 234, 23, 62, 198, 183, 252, 53, 79]
BasePath = ""
#0xBE39A63C this is passed as key2 to xor
#StreamingAssets\AssetBundle\rt6si7fva7\vq97ei8iuk\h2egg19b83 - this is the only hardcoded file, it's very likely a file table
def xor(encLen, key, bytearr):
    k1 = key >> 5
    k2 = key >> 19
    q, mod1 = divmod(k1,257)
    q, mod2 = divmod(k2,511)
    v1 = mod1
    v2 = mod2
    if len(bytearr) <= encLen:
        encLen = len(bytearr)
    for i in range(encLen):
        bytearr[i] = bytearr[i] ^ xorTbl1[v1]
        v1 += 1
        if v1 > 256:
            #print("v1 = 257:{}".format(i))
            v1 = 0
        bytearr[i] = bytearr[i] ^ xorTbl2[v2]
        v2 -= 1
        if v2 < 0:
            v2 = 510


    return bytearr

def inflate(data):
    return zlib.decompress(data,-15)

def decAes(bytearr):
    key = bytearr[:15]
    iv = bytearr[16:31]
    cipher = AES.new(key,AES.MODE_CBC,iv=iv)
    data = bytearr[32:]
    cipher.block_size = 1024
    ct_bytes = cipher.decrypt(pad(data, 1024))
    return ct_bytes

def decode(enctype,key2,bytearr):
    if enctype == 1:
        data = xor(0x1000,key2,bytearr)
    elif enctype == 2:
        data = decAes(bytearr)
    else:
        data = bytearr
    return data
    


def _Read(pacName,offset,size):
    inFile = open(os.path.join(BasePath,pacName),'rb')
    inFile.seek(offset)
    data = inFile.read(size)
    inFile.close()
    return data

def Read(info):
    name = info["name"]
    pacName = info["pacName"]
    offset = info["offset"]
    size = info["size"]
    bytearr = bytearray(_Read(pacName,offset,size))
    enctype = info["type"]
    orgCrc = info["orgCrc"]
    data = decode(enctype,orgCrc,bytearr)
    outputPath = os.path.join(BasePath.replace("\\","/").replace("AssetBundle/rt6si7fva7",""),name)
    print(outputPath)
    os.makedirs(os.path.dirname(outputPath),exist_ok=True)
    outFile = open(outputPath,'wb')
    outFile.write(data)
    outFile.close()




def readFileTable(inFile):
    data = inFile.read()
    data = inflate(data)
    data = bytearray(data)
    data = xor(len(data),0xBE39A63C,data)
    outFile = open(inFile.name + ".json", 'wb')
    outFile.write(bytes(data))
    outFile.close()

    #now open and interpret
    table = json.load(open(outFile.name,'r',encoding='utf-16-le'))
    fat = table["fat"]
    for file in fat:
        Read(file)






if __name__ == "__main__":
        BasePath = input("Enter path to the StreamingAssets/AssetBundle/rt6si7fva7 folder:")
        readFileTable(open(os.path.join(BasePath,"vq97ei8iuk/h2egg19b83"),'rb'))