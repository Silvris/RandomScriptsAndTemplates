import json
import base64
import os

def cleanSaveFile(savePath):
    saveFile = json.load(open(savePath,'r'))
    print(saveFile.keys())
    outputPath = savePath.replace(".sav","/").replace(".dec","/")
    os.makedirs(outputPath,exist_ok=True)
    removeKeys = []
    for key in saveFile:
        if(key == 'pictureData'):
            saveImage = base64.b64decode(saveFile[key])
            ImageOut = open(outputPath+"pictureData.png",'wb')
            ImageOut.write(saveImage)
            ImageOut.close()
            removeKeys.append(key)
        elif(key == 'userData'):
            userDataOut = outputPath + "userData/"
            os.makedirs(userDataOut,exist_ok=True)
            removeKeys.append(key)
            #this one goes rather deep
            userData = json.loads(saveFile[key])
            for key2 in userData:
                outFile = open(userDataOut+key2+".json",'w')
                outFile.write(str(userData[key2]))
        elif(key in ['configData','dataStorage','mapData']):
            #these are all one layer json
            data = json.loads(saveFile[key])
            if(key == 'mapData'):
                #two more smaller json in here, but handle it easier
                data['playerEntity'] = json.loads(data['playerEntity'])
                data['gpsData'] = json.loads(data['gpsData'])
            outFile = open(outputPath+key+".json",'w')
            json.dump(data,outFile,indent=4)
            outFile.close()
            removeKeys.append(key)
    for key in removeKeys:
        saveFile.pop(key)
    mainOut = open(outputPath+"saveData.json",'w')
    jsonOut = json.dump(saveFile,mainOut,indent=4)
cleanSaveFile(input("Input the path to your decrypted save: "))