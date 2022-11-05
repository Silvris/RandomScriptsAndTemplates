import os
import sys
import struct
import PIL
from PIL import Image

def ReadUInt(file):
    return struct.unpack("I",file.read(4))[0]

def ReadUShort(inFile):
    return struct.unpack("H",inFile.read(2))[0]

abspath = os.path.abspath(sys.argv[0])

dname = os.path.dirname(abspath)

os.chdir(dname)

universalHeight = 0 #if this stays zero, then there's problems
nullTerminator = 0 #likewise
class Character:
    def __init__(self,x,y,width,height,isNullTerm):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.isNull = isNullTerm
    
    def GetImageChr(self):
        return self.image

    def SetImageChr(self,image):
        self.image = image

    def GetWidth(self):
        return self.width

def ParseFIF(inFile):
    global universalHeight, nullTerminator
    #first read the header
    universalHeight = ReadUShort(inFile)
    characterCount = ReadUShort(inFile)
    nullTerminator = ReadUShort(inFile)
    #no clue what these are, but they're *probably* important for something
    for _ in range(137):
        ReadUShort(inFile)
    #now read characters
    characters = list()
    for i in range(characterCount):
        characters.append(Character(ReadUShort(inFile),ReadUShort(inFile),ReadUShort(inFile),universalHeight,i==nullTerminator))
    return characters

def CropCharacter(image,chara):
    return image.crop((chara.x,chara.y,chara.x+chara.width,chara.y+chara.height))

def ParseMSG(inFile):
    ReadUInt(inFile)
    assert inFile.read(4) == b"TEXT"
    inFile.read(1) #version
    messageCount = inFile.read(1)
    inFile.read(2)
    inFile.read(4) #file length
    offsets = list()
    strings = list()
    for _ in range(int.from_bytes(messageCount,"little")):
        offsets.append(ReadUInt(inFile))
    for offset in offsets:
        inFile.seek(offset)
        sb = int.from_bytes(inFile.read(1),"little")
        string = list()
        while(sb != nullTerminator):
            string.append(sb)
            sb = int.from_bytes(inFile.read(1),"little")
        strings.append(string)
    return strings
    
def CreateStringImages(characters, strings):
    print()
    outputDirectory = input("Give the directory you would like to output into:")
    log = open(outputDirectory+"/output.log",'w')
    currentStrIndex = 0
    for string in strings:
        currentStrIndex +=1
        log.write("String {}:\n".format(currentStrIndex))
        characterIndex = 0
        width = 0
        characterImages = list()
        for index in string:
            if index >= len(characters):
                log.write("Character at index {} ran out of range: {}\n".format(characterIndex,index))
            else:
                width += characters[index].GetWidth()
                characterImages.append(characters[index].GetImageChr())
                characterIndex += 1
        outImage = Image.new("RGBA",(width+1,universalHeight),(0,0,0,0))
        runningWidth = 0
        for image in characterImages:
            #print(runningWidth,outImage.width,image.width,outImage.height,image.height)
            outImage.paste(image,(runningWidth,0,runningWidth+image.width,outImage.height))
            runningWidth += image.width
        outImage.save(outputDirectory+"/string{}.png".format(currentStrIndex))
        log.write("\n")

FIF = open(input("Give the path to the .FIF file to use:"),'rb')
MSG = open(input("Give the path to the .MSG file to use:"),'rb')
IMG = Image.open(input("Give the path to the converted .CTPK file (conversion can be done in Noesis):")).convert("RGBA")

#parse FIF first
characters = ParseFIF(FIF)

#now generate images for each character
for character in characters:
    character.SetImageChr(CropCharacter(IMG,character))

#now we can parse the MSG and create character lists to represent our strings
strings = ParseMSG(MSG)

#now interpret the strings and create files
CreateStringImages(characters,strings)