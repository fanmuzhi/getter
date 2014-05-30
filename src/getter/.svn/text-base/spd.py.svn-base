#!/usr/bin/env python
# encoding: utf-8

'''
Created on Jul 2, 2013
ontains 2 main functions, write_ee_byte() and read_ee_byte()
@author: mzfa
'''
from getter import error
from getter.adapter import smb
import xml.etree.ElementTree as ET
import os
import inspect


path = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
CONFIG = path + '/config/dut.xml'

WR_SLEEP = 20
WAIT_SLEEP = 10
EEPROM_REG_RWDATA = 4
EESEL = 5
EESEL_VAL = 0   # 0=DIMM, 1=PGEM


class SPD(object):
    '''main class for SPD programming
    '''

    def __init__(self, PN, RR):
        self.err = 0
        if not os.path.exists(CONFIG):
            raise error.NO_XML_FILE

        config_tree = ET.parse(CONFIG)
        root = config_tree.getroot()
        for Project in root.findall('Project'):
            name = Project.attrib.get('name')
            revision = Project.attrib.get('revision')
            if (name == PN and revision == RR):
                bit_rate = int(Project.find('spd_aa_bitrate').text)
                slave_addr = int(Project.find('spd_aa_slave_address').text)
        self.da = smb.DeviceAPI(slaveaddr=slave_addr, bitrate=bit_rate)
        self.da.open()

    def __nvdimm_ee_write(self, addr, wdata):
        err = self.da.write(addr, wdata & 0xFF)
        self.err = err

    def __nvdimm_ee_read(self, addr):
        err, val = self.da.read(addr)
        self.err = err
        return val

    def spd_write_byte(self, addr, data):
        self.__nvdimm_ee_write(addr, data)
        self.da.sleep(WR_SLEEP)
        if(self.err != 0):
            print self.err
            self.err = 0
            self.spd_close()
            raise error.DEVICE_RW_ERROR

    def spd_read_byte(self, addr):
        val = self.__nvdimm_ee_read(addr)
        if(self.err != 0):
            print self.err
            self.err = 0
            self.spd_close()
            raise error.DEVICE_RW_ERROR
        return val

    def spd_close(self):
        self.da.close()
#        print "spd closed"


if __name__ == "__main__":
    spd = SPD('AGIGA8601-400BCA', '10')
    spd.spd_read_byte(0)
    spd.spd_close()
