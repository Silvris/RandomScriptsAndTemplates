import json
import sys
import os

abspath = os.path.abspath(sys.argv[0])

dname = os.path.dirname(abspath)

os.chdir(dname)

def prettyPrintJson(fileName):
    jf = open(fileName,'r',encoding='utf-8')
    jdata = json.load(jf)
    jf.close()
    jf = open(fileName,'w',encoding='utf-8')
    json.dump(jdata,jf,indent=4,ensure_ascii=False)
    jf.close()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        for i, arg in enumerate(sys.argv):
            if i > 0:
                prettyPrintJson(arg)
    else:
        filename = input("Enter the name/path to the json:")
        prettyPrintJson(filename)