import json
import base64
import os

def checkLowerJson(jobj):
    for key in jobj:
        #print(key)
        #check for lower layers of json
        if isinstance(jobj[key],str):
            if len(jobj[key]) > 1:
                #print(key)
                #print(jobj[key][0])
                if jobj[key][0] == '{':
                    #we have a lower level of json
                    newJson = json.loads(jobj[key])
                    jobj[key] = checkLowerJson(newJson)
        elif isinstance(jobj[key],list):
            #check each item under the same settings
            for i in range(len(jobj[key])):
                if isinstance(jobj[key][i],str):
                    if len(jobj[key][i]) > 1:
                        #print(key)
                        #print(jobj[key][0])
                        if jobj[key][i][0] == '{':
                            #we have a lower level of json
                            newJson = json.loads(jobj[key][i])
                            jobj[key][i] = checkLowerJson(newJson)
    return jobj

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
            removeKeys.append(key)
            #this one goes rather deep
            userData = json.loads(saveFile[key])
            userData = checkLowerJson(userData)
            userOut = open(outputPath+"userData.json",'w')
            json.dump(userData,userOut,indent=4)
                
        elif(key in ['configData','dataStorage','mapData']):
            #these are all one layer json, aside from mapData
            data = json.loads(saveFile[key])
            if(key == 'mapData'):
                data = checkLowerJson(data)
            outFile = open(outputPath+key+".json",'w')
            json.dump(data,outFile,indent=4)
            outFile.close()
            removeKeys.append(key)
    for key in removeKeys:
        saveFile.pop(key)
    mainOut = open(outputPath+"saveData.json",'w')
    json.dump(saveFile,mainOut,indent=4)
cleanSaveFile(input("Input the path to your decrypted save: "))