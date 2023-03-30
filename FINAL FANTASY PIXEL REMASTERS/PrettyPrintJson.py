import json
import sys
import os
from pathlib import Path

abspath = os.path.abspath(sys.argv[0])

dname = os.path.dirname(abspath)

os.chdir(dname)

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

def prettyPrintJson(fileName):
    if(os.path.isdir(fileName)):
        for path in Path(fileName).rglob("*.json"):
            jf = open(path,'r',encoding='utf-8')
            jdata = json.load(jf)
            jf.close()
            #jdata = checkLowerJson(jdata)
            jf = open(path,'w',encoding='utf-8')
            json.dump(jdata,jf,indent=4,ensure_ascii=False)
            jf.close()
    else:
        jf = open(fileName,'r',encoding='utf-8')
        jdata = json.load(jf)
        jf.close()
        #jdata = checkLowerJson(jdata)
        jf = open(fileName,'w',encoding='utf-8')
        json.dump(jdata,jf,ensure_ascii=False)
        jf.close()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        for i, arg in enumerate(sys.argv):
            if i > 0:
                prettyPrintJson(arg)
    else:
        filename = input("Enter the name/path to the json:")
        prettyPrintJson(filename)