import struct

def readSingle(file):
    return struct.unpack("f",file.read(4))[0]

def readInt(file):
    return struct.unpack("i",file.read(4))[0]

def readUInt(file):
    return struct.unpack("I",file.read(4))[0]

def readInt64(file):
    return struct.unpack("q",file.read(8))[0]

def writeSingle(file,val):
    file.write(struct.pack("f",val))

def writeInt(file,val):
    file.write(struct.pack("i",val))

def writeUInt(file,val):
    file.write(struct.pack("I",val))

def writeInt64(file,val):
    file.write(struct.pack("q",val))

def readCSharpString(file):
    stringLen = readInt(file)
    stringData = file.read(stringLen)
    while(file.tell()%4) != 0:
        file.read(1)
    return stringData.decode('utf-8')

def writeCSharpString(file,stringIn):
    writeInt(file,len(stringIn))
    file.write(stringIn.encode(encoding='utf-8'))
    while(file.tell()%4) != 0:
        file.write(bytes([0]))

class PPtr:
    def __init__(self,fileID,pathID):
        self.m_FileID = fileID
        self.m_PathID = pathID
    
    def Export(self,file):
        writeInt(file,self.m_FileID)
        writeInt64(file,self.m_PathID)

class Font:
    def __init__(self,values,buffer):
        self.m_Name = values[0]
        self.m_LineSpacing = values[1]
        self.m_DefaultMaterial = values[2]
        self.m_FontSize = values[3]
        self.m_Texture = values[4]
        self.m_AsciiStartOffset = values[5]
        self.m_Tracking = values[6]
        self.m_CharacterSpacing = values[7]
        self.m_CharacterPadding = values[8]
        self.m_ConvertCase = values[9]
        self.m_CharacterRects = values[10]
        self.m_KerningValues = values[11]
        self.m_PixelScale = values[12]
        self.m_FontData = buffer
        self.m_Ascent = values[13]
        self.m_Descent = values[14]
        self.m_DefaultStyle = values[15]
        self.m_FontNames = values[16]
        self.m_FallbackFonts = values[17]
        self.m_FontRenderingMode = values[18]
        self.m_UseLegacyBoundsCalculation = values[19]
        self.m_ShouldRoundAdvanceValue = values[20]
    
    def Export(self,file):
        writeCSharpString(file,self.m_Name)
        writeSingle(file,self.m_LineSpacing)
        self.m_DefaultMaterial.Export(file)
        writeSingle(file,self.m_FontSize)
        self.m_Texture.Export(file)
        writeInt(file,self.m_AsciiStartOffset)
        writeSingle(file,self.m_Tracking)
        writeInt(file,self.m_CharacterSpacing)
        writeInt(file,self.m_CharacterPadding)
        writeInt(file,self.m_ConvertCase)
        writeInt(file,len(self.m_CharacterRects))
        #TODO - write export for whatever character rects are
        writeInt(file,len(self.m_KerningValues))
        #TODO - write export for kerning values
        writeSingle(file,self.m_PixelScale)
        writeUInt(file,len(self.m_FontData))
        file.write(self.m_FontData)
        writeSingle(file,self.m_Ascent)
        writeSingle(file,self.m_Descent)
        writeUInt(file,self.m_DefaultStyle)
        writeInt(file,len(self.m_FontNames))
        for name in self.m_FontNames:
            writeCSharpString(file,name)
        writeInt(file,len(self.m_FallbackFonts))
        for font in self.m_FallbackFonts:
            font.Export(file)
        writeInt(file,self.m_FontRenderingMode)
        file.write(self.m_UseLegacyBoundsCalculation)
        file.write(self.m_ShouldRoundAdvanceValue)

def readUnityFont(inFile):
    values = list()
    values.append(readCSharpString(inFile))
    values.append(readSingle(inFile))
    values.append(PPtr(readInt(inFile),readInt64(inFile)))
    values.append(readSingle(inFile))
    values.append(PPtr(readInt(inFile),readInt64(inFile)))
    values.append(readInt(inFile))
    values.append(readSingle(inFile))
    values.append(readInt(inFile))
    values.append(readInt(inFile))
    values.append(readInt(inFile))
    characterRectsLen = readInt(inFile)
    if characterRectsLen > 0:
        print("Unable to open file. Reason: CharacterRects present")
    values.append([])
    #read CharacterRects
    kerningValuesLen = readInt(inFile)
    if kerningValuesLen > 0:
        print("Unable to open file. Reason: KerningValues present")
    values.append([])
    #read KerningValues
    values.append(readSingle(inFile))
    bufferLen = readInt(inFile)
    buffer = inFile.read(bufferLen)
    values.append(readSingle(inFile))
    values.append(readSingle(inFile))
    values.append(readUInt(inFile))
    fontNameCount = readInt(inFile)
    fontNames = list()
    for _ in range(fontNameCount):
        fontNames.append(readCSharpString(inFile))
    values.append(fontNames)
    fallbackCount = readInt(inFile)
    fallbacks = list()
    for _ in range(fallbackCount):
        fallbacks.append(PPtr(readInt(inFile),readInt64(inFile)))
    values.append(fallbacks)
    values.append(readInt(inFile))
    values.append(inFile.read(1))
    values.append(inFile.read(1))
    return Font(values,buffer)

originalFilePath = input("Enter Unity Font file path:")
newFontPath = input("Enter new font file path:")
outputPath = input("Enter output path:")

oFont = readUnityFont(open(originalFilePath,'rb'))
replace = open(newFontPath,'rb')
nBuffer = replace.read()
nFont = open(outputPath,'wb')
oFont.m_FontData = nBuffer
oFont.Export(nFont)
