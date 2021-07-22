from inc_noesis import *
import math

def registerNoesisTypes():
    handle = noesis.register("Fate/Grand Order Arcade Textures", ".txp")
    noesis.setHandlerTypeCheck(handle, texCheckType)
    noesis.setHandlerLoadRGBA(handle, texLoadTexSet)
    noesis.logPopup()
    return 1


def texCheckType(data):
    bs = NoeBitStream(data)
    fileMagic = bs.readUInt()
    if fileMagic == 0x04505854:
        return 1
    else:
        print("Fatal Error: Unknown file magic: " + str(hex(fileMagic) + " expected 0x03505854!"))
        return 1

def getTextureFormat(format):
    if format == 98:
        return "a8"
    elif format == 99:
        return "r8g8b8"
    elif format == 100:
        return "r8g8b8a8"
    elif format == 101:
        return "r5g5b5"
    elif format == 102:
        return "r5g5b5a1"
    elif format == 103:
        return "r4g4b4a4"
    elif format == 104:
        return noesis.FOURCC_DXT1
    elif format == 105:
        return noesis.FOURCC_DXT1
    elif format == 107:
        return noesis.FOURCC_DXT3
    elif format == 109:
        return noesis.FOURCC_DXT5
    elif format == 112:
        return noesis.FOURCC_ATI1
    elif format == 115:
        return noesis.FOURCC_ATI2
    elif format == 131:
        return noesis.FOURCC_BC6S


def texLoadTexSet(data, texList):
    bs = NoeBitStream(data)
    magic = bs.readUInt()
    mipCount = bs.readUInt()
    mipJunk = bs.readUInt()
    lengths = []
    offsets = []
    for _ in range(mipCount):
        offsets.append(bs.readUInt())

    for i in range(mipCount):
        if i == mipCount-1:
            lengths.append(len(data)-offsets[i])
        else:
            lengths.append(offsets[i+1]-offsets[i])
    
    for i in range(mipCount):
        bs.seek(offsets[i])
        texList.append(texLoadARGB(bs.readBytes(lengths[i])))
    return 1
def texLoadARGB(data):
    bs = NoeBitStream(data)
    magic = bs.readUInt()
    width = max(bs.readUInt(),4)
    height = max(bs.readUInt(),4)
    formatInt = bs.readUInt()
    Format = getTextureFormat(formatInt)
    print(formatInt, Format)
    id = bs.readUInt()
    length = bs.readUInt()
    pix = bs.readBytes(length)
    if formatInt < 104:
        pix = rapi.imageDecodeRaw(pix,width,height,Format)
    else:
        pix = rapi.imageDecodeDXT(pix,width,height,Format)
    return NoeTexture("FGOATex", width, height, pix, noesis.NOESISTEX_RGBA32)