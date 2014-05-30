'''
Created on Jul 22, 2013

@author: mzfa
'''
#!/usr/bin/env python
# encoding: utf-8

import struct
from getter import error

test_ebf = './config/101-40035-01-Rev02-AGIGA8601-400BCA-Coronado 4GB for Diamond VPD.ebf'
test_bin = './config/101-40020-01-Rev01-Coronado-SPD-Inphi_Register-Micron_SDRAM-4GB.bin'


def load_ebf(path, size=1024):
    bf = BinaryFile(path, size)
    return bf.read_byte()


def load_bin(path, size=256):
    bf = BinaryFile(path, size)
    return bf.read_byte()


class BinaryFile(object):
    def __init__(self, fpath, size):
        self.path = fpath
        self.size = size

    def read_byte(self):
        datas = []
        f = open(self.path, 'rb')
        for i in range(self.size):
            rdata = 0
            rchar = f.read(1)
            if (rchar == ""):
                raise error.NULL_VALUE
            else:
                rdata = struct.unpack("B", rchar)[0]
                datas.append(rdata)
        f.close()
        return datas


if __name__ == "__main__":
    ret, datas = load_ebf(test_ebf)
    if(ret == error.NULL_VALUE):
        print "ebf has null value"
    print datas
    print "lenth = : " + str(len(datas))

    ret, datas = load_bin(test_bin)
    if(ret == error.NULL_VALUE):
        print "bin has null value"
    print datas
    print "lenth = : " + str(len(datas))
