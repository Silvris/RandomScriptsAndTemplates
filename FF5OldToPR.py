from PIL import Image
import os
import numpy as np
from pathlib import Path
import shutil

JobToPath = {
    "Knight": "_J07",
    "Thief": "_J02",
    "Monk": "_J03",
    "RedMage": "_J04",
    "WhiteMage": "_J05",
    "BlackMage": "_J06",
    "Ninja": "_J08",
    "Ranger": "_J13",
    "Geomancer":"_J15",
    "Dragoon":"_J16",
    "Bard":"_J18",
    "Summoner":"_J21",
    "Berserker":"_J23",
    "Samurai":"_J24",
    "TimeMage":"_J25",
    "Chemist":"_J26",
    "Dancer":"_J27",
    "BlueMage":"_J28",
    "MysticKnight":"_J29",
    "Beastmaster":"_J30",
    "Mime":"_J31"
}
JobToFilename = {
    "Knight": "fldchr15",
    "Thief": "fldchr17",
    "Monk": "fldchr16",
    "RedMage": "fldchr29",
    "WhiteMage": "fldchr24",
    "BlackMage": "fldchr25",
    "Ninja": "fldchr19",
    "Ranger": "fldchr22",
    "Geomancer":"fldchr32",
    "Dragoon":"fldchr18",
    "Bard":"fldchr33",
    "Summoner":"fldchr27",
    "Berserker":"fldchr21",
    "Samurai":"fldchr20",
    "TimeMage":"fldchr26",
    "Chemist":"fldchr31",
    "Dancer":"fldchr34",
    "BlueMage":"fldchr28",
    "MysticKnight":"fldchr23",
    "Beastmaster":"fldchr30",
    "Mime":"fldchr39"
}

CharacterToPath = {
    "Bartz": "BC_FF5_P001",
    "Lenna": "BC_FF5_P002",
    "Galuf": "BC_FF5_P003",
    "Faris": "BC_FF5_P004",
    "Krile": "BC_FF5_P005"
}

CharacterToFilename = {
    "Bartz": "_0",
    "Lenna": "_1",
    "Galuf": "_2",
    "Faris": "_3",
    "Krile": "_4"
}

def removeWhitespace(pil_image):
    black = Image.new('RGBA', pil_image.size, color=(0,0,0,0))
    pil_image = Image.composite(pil_image, black, pil_image)
    myCroppedImage = pil_image.crop(pil_image.getbbox())
    return myCroppedImage

def clean(pil_image):
    black = Image.new('RGBA', pil_image.size, color=(0,0,0,0))
    pil_image = Image.composite(pil_image, black, pil_image)
    myCroppedImage = pil_image.crop(pil_image.getbbox())
    x,y = myCroppedImage.size
    x = 56-x
    x = x//2
    y = 56 - y
    black.paste(myCroppedImage,(x,y))
    return black

BasePath = "Assets/GameAssets/Serial/Res/Chara/Battle/"
Old = "_O"
Zombie = "_Z"

PoseCoords = {
    "Default_00" : (0,0,56,56),
    "Ready_00" : (56,0,112,56),
    "Dying_00" : (112,0,168,56),
    "Damage_00" : (168,0,224,56),
    "RightAttack_01": (224,0,280,56),
    "RightAttack_00": (280,0,336,56),
    "LeftAttack_01": (336,0,392,56),
    "LeftAttack_00": (392,0,448,56),
    "Win_00" : (448,0,504,56),
    "SkillReady_00" : (0,56,56,112),
    "SkillReady_01" : (56,56,112,112)
}
RECT = "Rect = "
PIVOT = "Pivot = [0.5,0]\n"
PPU = "PixelsPerUnit = 1\n"
BORDER = "Border = [0,0,0,0]\n"
WRAPMODE = "WrapMode = Clamp\n"

OldPath = r"C:\Users\Owner\Pictures\FFV FujiMod\originals/"
OutputPath = r"D:\Program Files\Steam\steamapps\common\FINAL FANTASY V PR\FINAL FANTASY V_Data\StreamingAssets\Magicite\FujiSprites"

DownImages = {
    "Bartz": r"C:\Users\Owner\Pictures\FFV FujiMod\down\bartzDown.png",
    "Lenna": r"C:\Users\Owner\Pictures\FFV FujiMod\down\lennaDown.png",
    "Galuf": r"C:\Users\Owner\Pictures\FFV FujiMod\down\galufDown.png",
    "Faris": r"C:\Users\Owner\Pictures\FFV FujiMod\down\farisDown.png",
    "Krile": r"C:\Users\Owner\Pictures\FFV FujiMod\down\krileDown.png"
}
DownRect = "[0,0,56,56]"
for character in CharacterToPath:
    for job in JobToPath:
        for modifier in {"", Old, Zombie}:
            folderName = CharacterToPath[character]+JobToPath[job]+modifier
            dirPath = os.path.join(OutputPath,folderName,BasePath,folderName)
            if(dirPath != ''):
                os.makedirs(dirPath,exist_ok=True)
                for files in os.listdir(dirPath):
                    path = os.path.join(dirPath, files)
                    try:
                        shutil.rmtree(path)
                    except OSError:
                        os.remove(path)
            #now copy base image and make each sprite
            filename = JobToFilename[job]+CharacterToFilename[character]
            baseImage = Image.open(OldPath + filename + ".png")
            for sprite in PoseCoords:
                sprimg = baseImage.crop(PoseCoords[sprite])
                sprimg = clean(sprimg)
                sprimg.save(dirPath+"/"+sprite+".png")
                sprdata = open(dirPath+"/"+sprite + ".spritedata", 'w')
                sprdata.write(RECT + DownRect + "\n")
                sprdata.write(PIVOT)
                sprdata.write(PPU)
                sprdata.write(BORDER)
                sprdata.write(WRAPMODE)
                sprdata.close()
            #now copy/write the down sprite
            shutil.copy2(DownImages[character], dirPath)
            if os.path.exists(dirPath+ "/" +"Down_00.png"):
                os.remove(dirPath+ "/" +"Down_00.png")
            os.rename(dirPath+ "/" + os.path.basename(DownImages[character]),dirPath+ "/" +"Down_00.png")
            sprdata = open(dirPath+"/Down_00.spritedata", 'w')
            sprdata.write(RECT + DownRect + "\n")
            sprdata.write(PIVOT)
            sprdata.write(PPU)
            sprdata.write(BORDER)
            sprdata.write(WRAPMODE)
            sprdata.close()

#monster sprites here
monstersPath = r"C:\Users\Owner\Pictures\FFV FujiMod\monsters/"
for path in Path(monstersPath).rglob("*.png"):
    im = Image.open(path)
    im = removeWhitespace(im)
    im.save(path)
    #now generate spritedata based on this particular image
    width, height = im.size
    if(width > 384) or (height > 216): 
        print(path)
    sprdata = open(path.with_suffix(".spritedata"),'w')
    sprdata.write(RECT + "[0,0,{},{}]\n".format(width,height))
    sprdata.write(PIVOT)
    sprdata.write(PPU)
    sprdata.write(BORDER)
    sprdata.write(WRAPMODE)
    sprdata.close()