'''
Created on Jul 2, 2013
Contains 2 main functions, write_ee_byte() and read_ee_byte()
@author: mzfa
'''
import os
import inspect
from getter import error
from getter.adapter import smb
import xml.etree.ElementTree as ET

path = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
CONFIG = path + '/config/dut.xml'

EEPROM_REG_ADDRL = 2
EEPROM_REG_ADDRH = 3
EEPROM_REG_RWDATA = 4
EESEL = 5
EESEL_VAL = 0       # 0=DIMM, 1=PGEM
LOCK_REG = 0x19
LOCK_VAL = 0
UNLOCK_VAL = 0xA6
LOCK = 1
UNLOCK = 2
WAIT_SLEEP = 10


class VPD(object):
    def __init__(self, PN, RR):
        self.err = 0
        config_tree = ET.parse(CONFIG)
        root = config_tree.getroot()
        for Project in root.findall('Project'):
            name = Project.attrib.get('name')
            revision = Project.attrib.get('revision')
            if (name == PN and revision == RR):
                bit_rate = int(Project.find('vpd_aa_bitrate').text)
                slave_addr = int(Project.find('vpd_aa_slave_address').text)
        self.da = smb.DeviceAPI(slaveaddr=slave_addr, bitrate=bit_rate)
        self.da.open()
#            self.da.write(EESEL, EESEL_VAL)    # select the NVDIMM EEPROM
#        print "vpd opened"

    def __wait_reg_busy(self):
        for i in range(10):
            (ret, rdata) = self.da.read(1)
            if (ret != 0):
                return ret          # err
            if (rdata == 0x00):     # not busy
                return 0
            self.da.sleep(WAIT_SLEEP)
        raise error.EE_TIMEOUT

    def __nvdimm_ee_select(self, addr):
        self.__wait_reg_busy()
        err = self.da.write(EEPROM_REG_ADDRL, addr & 0xFF)
        self.__wait_reg_busy()
        err |= self.da.write(EEPROM_REG_ADDRH, (addr >> 8) & 0xFF)
        self.err = err

    def __nvdimm_ee_write(self, wdata):
        self.__wait_reg_busy()
        err = self.da.write(EEPROM_REG_RWDATA, wdata & 0xFF)
        self.err = err

    def __nvdimm_ee_read(self, addr):
        self.__wait_reg_busy()
        err, val = self.da.read(addr)
        self.err = err
        return val

    def __lock_unlock_rw(self, lock):
        if (lock == LOCK):
            err = self.da.write(LOCK_REG, LOCK_VAL)
        elif (lock == UNLOCK):
            err = self.da.write(LOCK_REG, UNLOCK_VAL)
        self.err = err

    def vpd_write_byte(self, addr, data):
        self.__nvdimm_ee_select(addr)
        self.__nvdimm_ee_write(data)
        if(self.err != 0):
            # print the aardvark device error code
            print self.err
            self.err = 0
            self.vpd_close()
            raise error.DEVICE_RW_ERROR

    def vpd_read_byte(self, addr):
        self.__nvdimm_ee_select(addr)
        val = self.__nvdimm_ee_read(EEPROM_REG_RWDATA)
        if(self.err != 0):
            # print the aardvark device error code
            print self.err
            self.err = 0
            self.vpd_close()
            raise error.DEVICE_RW_ERROR
        return val

    def lock_wr(self):
        self.__lock_unlock_rw(LOCK)
        if(self.err != 0):
            # print the aardvark device error code
            print self.err
            self.err = 0
            self.vpd_close()
            raise error.DEVICE_RW_ERROR

    def unlock_wr(self):
        self.__lock_unlock_rw(UNLOCK)
        if(self.err != 0):
            # print the aardvark device error code
            print self.err
            self.err = 0
            self.vpd_close()
            raise error.DEVICE_RW_ERROR

    def vpd_close(self):
        self.da.close()
#        print "vpd closed"


if __name__ == "__main__":
    vpd = VPD('AGIGA8601-400BCA', '10')
    val = vpd.vpd_read_byte(0x297)
    print val
    vpd.vpd_close()
