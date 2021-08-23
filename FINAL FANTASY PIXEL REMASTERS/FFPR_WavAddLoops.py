import sys
import os
import struct

class OtherChunk:
    def __main__(self,tag,size,data):
        self.tag = tag
        self.size = size
        self.data = data

class SmplChunk:
    def __main__(self,tag,size,zeros,loops):
        self.tag = tag
        self.size = size
        self.zeros = zeros
        self.loops = loops

class WaveFile:
    def __main__(self,tag,chunks):
        self.tag = tag
        self.chunks = chunks

