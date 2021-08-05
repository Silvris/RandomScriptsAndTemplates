import json
import base64
import os
import sys
abspath = os.path.abspath(sys.argv[0])

dname = os.path.dirname(abspath)

os.chdir(dname)
catalog = json.load(open("catalog.json",'r'))
for key in catalog.keys():
    os.makedirs("catalog/",exist_ok=True)
    data = catalog[key]
    if key in ["m_KeyDataString","m_BucketDataString","m_EntryDataString","m_ExtraDataString"]:
        out = open("catalog/"+key+".json",'wb')
        data = base64.b64decode(data.replace("\"","").replace("\n","").replace("\r",""))
        out.write(data)
    else:
        out = open("catalog/"+key+".json",'w')
        data = json.dump(data,out)