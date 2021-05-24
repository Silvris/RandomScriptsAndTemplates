from inc_noesis import *

def registerNoesisTypes():
    handle = noesis.register("Final Fantasy XIV Textures", ".atex")
    noesis.setHandlerTypeCheck(handle, texCheckType)
    noesis.setHandlerLoadRGBA(handle, texLoadARGB)
    noesis.logPopup()
    return 1

#note: I cannot confirm most formats to be read correctly (in particular, any float formats are almost definitely read incorrectly)
#this was mainly to batch all of the textures present in the 0800000 dat, which holds vfx (for weapons I believe?)

def texCheckType(data):
    return 1 #no notable magic number

def getDataType(dataType):
    if dataType == 4401:
        dataReturn = "a8"
    if dataType == 5184:
        dataReturn = "a4r4g4b4"
    if dataType == 5185:
        dataReturn = "a1r5g5b5"
    if dataType == 5200:
        dataReturn = "a8r8g8b8"
    if dataType == 5201:
        dataReturn = "x8r8g8b8"
    if dataType == 8528:
        dataReturn = "r32f"
    if dataType == 8784:
        dataReturn = "g16r16f"
    if dataType == 8800:
        dataReturn = "g32r32f"
    if dataType == 9312:
        dataReturn = "a16b16g16r16f"
    if dataType == 9328:
        dataReturn = "a32b32g32r32f"
    if dataType == 13344:
        dataReturn = noesis.NOESISTEX_DXT1
    if dataType == 13360:
        dataReturn = noesis.NOESISTEX_DXT3
    if dataType == 13361:
        dataReturn = noesis.NOESISTEX_DXT5
    return dataReturn

def texLoadARGB(data, texList):
    bs = NoeBitStream(data)
    bs.seek(4)
    dataType = bs.readUInt()
    print(dataType)
    width = bs.readUShort()
    print(width)
    height = bs.readUShort()
    print(height)
    DUMMY = bs.readUShort()
    mipCount = bs.readUShort()
    DUMMY = bs.readUInt()
    DUMMY = bs.readUInt()
    DUMMY = bs.readUInt()
    offset = bs.readUInt()
    mip2Offset = bs.readUInt()
    dataString = getDataType(dataType)
    print(dataString)
    length = mip2Offset-offset
    bs.seek(offset)
    if dataString in (noesis.NOESISTEX_DXT1,noesis.NOESISTEX_DXT3,noesis.NOESISTEX_DXT5):
        pix = rapi.imageDecodeDXT(bs.readBytes(length), width, height, dataString)
    else:
        pix = rapi.imageDecodeRaw(bs.readBytes(length), width, height, dataString)
    texList.append(NoeTexture("FFTex", width, height, pix, noesis.NOESISTEX_RGBA32))
    return 1