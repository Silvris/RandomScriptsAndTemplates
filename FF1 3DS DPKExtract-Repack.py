import os
import sys
import struct

class DPKEntry():
    def __init__(self,name,namesum,offset,comp,decomp):
        self.name = name
        self.namesum = namesum
        self.offset = offset
        self.compSize = comp
        self.decompSize = decomp

class DPKFile():
    def __init__(self,entries):
        self.entries = entries
