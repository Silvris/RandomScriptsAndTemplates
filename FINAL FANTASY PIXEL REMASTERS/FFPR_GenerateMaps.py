from PIL import Image
import os
import json
import random

packagePath = input("Enter the path to the package.json of the map:")
packageDir = os.path.dirname(packagePath) + "/"
package = json.load(open(packagePath,'r'))

#first, generate a base map based off of tileset image and tilemap
texturelist = package["texture"] #todo: support multi-image tilemaps and find some way to differentiate them
textures = list()
for texture in texturelist:
    textures.append([texture["name"] + ".png",Image.open(packageDir + texture["name"] +".png")])

for texture in textures:
    texture[1] = texture[1].transpose(Image.FLIP_TOP_BOTTOM)

maps = package["map"]

for Map in maps:
    tilemap = json.load(open(packageDir+Map["tilemap"]+".json",'r'))
    #with the tilemap we can start some interpretation of the map
    outputMaps = list()
    outputMap = None
    layers = tilemap["layers"]
    for layer in layers:
        #print(layer)
        if layer["name"] == "TileGroup":
            #this means it's the actual data layer
            #tiled also supports shader layers, which is used for water/lava
            if "tilesets" in tilemap:
                #go ahead and generate tilemaps
                tilesets = list()
                for tileset in tilemap["tilesets"]:
                    print(tileset["name"])
                    tiles = list()
                    texture = next(x for x in textures if x[0] == tileset["image"])
                    texture = texture[1]
                    theight = tileset["tileheight"]
                    twidth = tileset["tilewidth"]
                    tcolumns = tileset["columns"]
                    for y in range(int(tileset["imageheight"]/theight)):
                        for x in range(tcolumns):
                            tiles.append(texture.crop(((x*twidth),(y*theight),((x+1)*twidth),((y+1)*theight))))
                    #tile animation remap (we only want the first frame)
                    if "tiles" in tileset:
                        for tile in tileset["tiles"]:
                            if "animation" in tile:
                                tiles[tile["id"]] = tiles[tile["animation"][0]["tileid"]]
                    #print(tcolumns, len(tiles))
                    tilesets.append([twidth,theight,tiles])
                lLayers = list()
                for lLayer in layer["layers"]:
                    height = lLayer["height"]
                    width = lLayer["width"]
                    twidth = tilesets[0][0]
                    theight = tilesets[0][1]
                    tileIndexes = lLayer["data"]
                    tiles = list()
                    emptyTile = Image.new("RGBA",(twidth,theight),(0,0,0,0))
                    for i in range(len(tileIndexes)):
                        if(tileIndexes[i] != 0):
                            tiles.insert(i,tilesets[0][2][tileIndexes[i]-1])
                        else:
                            tiles.insert(i,emptyTile)
                    newMap = Image.new("RGBA",(width*twidth,height*theight),(0,0,0,0))

                    for y in range(height):
                        for x in range(width):
                            #this shit runs right to left
                            newMap.paste(tiles[(y*width)+(x)],(((x)*twidth),(y*theight),((x+1)*twidth),((y+1)*theight)))#assume default tileset, since it's not looking like any use more than 1
                    lLayers.append(newMap)
                for i in range(len(lLayers)):
                    if i == 0:
                        outputMap = lLayers[i]
                    else:
                        outputMap.paste(lLayers[i],(0,0),lLayers[i])
                    #lLayer.show()
                    #print(len(lLayer["data"]), tilemap["width"], tilemap["height"])
                outputMaps.append([Map["name"],outputMap])
    
    #now main map is done, generate derivative maps

    if "encount" in Map:
        encount = json.load(open(packageDir+Map["encount"]+".json",'r'))
        twidth = int(outputMap.width / encount["width"])
        theight = int(outputMap.height / encount["height"])
        width = encount["width"]
        height = encount["height"]
        colors = dict()
        for encounterGroup in encount["unique_grid_number"]:
            colors[encounterGroup] = random.choices(range(256), k=3)
            colors[encounterGroup].append(128)
            colors[encounterGroup] = tuple(colors[encounterGroup])
        tiles = list()
        for tile in encount["cells"]:
            tiles.append(Image.new("RGBA",(twidth,theight),colors[tile]))
        encountMap = outputMap.copy()
        for y in range(height):
            for x in range(width):
                encountMap.paste(tiles[(y*width)+(x)],(((x)*twidth),(y*theight),((x+1)*twidth),((y+1)*theight)),tiles[(y*width)+(x)])
        outputMaps.append([Map["name"]+"-encounter",encountMap])
    
    for output in outputMaps:
        os.makedirs(packageDir + "/maps/",exist_ok=True)
        output[1].save(open(packageDir + "/maps/" + output[0] + ".png",'wb'))

    
