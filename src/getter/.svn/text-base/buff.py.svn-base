'''
Created on Jul 2, 2013
Read config/dut.xml to load path, size of vpd and spd.
From rawfile.py load raw *.ebf file and *.bin file.
Rewrite the config list to buffer(ex:YY,WW,VV,ID...) and
return the buffer content.
@author: mzfa
'''
import os
import inspect
from getter import rawfile
import xml.etree.ElementTree as ET
from getter import error


path = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
CONFIG = path + '/config/dut.xml'

def load_vpd(diction):
    buff = BufferConstruct()
    conf = read_config(diction['PN'], diction['RR'])
    vpd_en = conf.find('vpd_enable').text
    if(int(vpd_en) != 1):
        raise error.VPD_DISABLED
    else:
        vpd_buff = buff.vpd_buffer(diction, conf)
    return vpd_buff


def load_spd(diction):
    buff = BufferConstruct()
    conf = read_config(diction['PN'], diction['RR'])
    spd_en = conf.find('spd_enable').text
    if(int(spd_en) != 1):
        raise error.SPD_DISABLED
    else:
        spd_buff = buff.spd_buffer(diction, conf)
    return spd_buff


def read_config(pn, rr):
    val = None
    if not os.path.exists(CONFIG):
        raise error.NO_XML_FILE

    config_tree = ET.parse(CONFIG)
    root = config_tree.getroot()
    for Project in root.findall('Project'):
        name = Project.attrib.get('name')
        revision = Project.attrib.get('revision')
        if (name == pn and rr == revision):
            val = Project
    if val is None:
        raise error.DUT_NOT_MATCH

    return val


class BufferConstruct(object):
    '''
    '''

    def __accii_list(self, string):
        strlist = list(string)
        for i in range(len(strlist)):
            strlist[i] = ord(strlist[i])
        return strlist

    def __bcd_code(self, string):
        bcd = ((int(string[-2]) & 0xff) << 4) | (int(string[-1]) & 0xff)
        return bcd

    def vpd_buffer(self, diction, conf):
        '''
        vpd buffer rewrite content position
        ID:     0x287--0x28E 8Bytes(647--654 in buff list)
        MFDATE: 0X291--0X294 4Bytes(657--660 in buff list),
                the content in MFDATE IS YYWW
        ENDUSR: 0X295--0X296 2Bytes(661--662 in buff list),
                the content in ENDUSR is VV
        '''
        vpd_file = str(conf.find('vpd_file').text)
        vpd_size = int(conf.find('vpd_size').text)
        buffebf = rawfile.load_ebf(vpd_file, vpd_size)

        # rewrite buffer content here
        # put buffer into self.vpd_buff
        idlist = self.__accii_list(diction['ID'])
        yywwlist = self.__accii_list(str(diction['YY']) + str(diction['WW']))
        vvlist = self.__accii_list(diction['VV'])
        buffebf[647:647 + len(idlist)] = idlist
        buffebf[657:657 + len(yywwlist)] = yywwlist
        buffebf[661:661 + len(vvlist)] = vvlist
        return buffebf

    def spd_buffer(self, diction, conf):
        '''
        spd buffer rewrite content position
            VV:     0x077 1Bytes(119 in buff list), VV 04 == 0x04
            YY:     0x078 1Bytes(120 in buff list), year 12 == 0x12
            WW:     0x079 1Bytes(121 in buff list), week 51 == 0x51
            ID:     0x07A--0x07D 4Bytes(122--125 in buff list),
                      ex:  ID'12345678' => 0x7A:0x78;
                                           0x7B:0x56;
                                           0x7C:0x34;
                                           0x7D:0x12
        '''
        spd_file = str(conf.find('spd_file').text)
        spd_size = int(conf.find('spd_size').text)
        buffbin = rawfile.load_bin(spd_file, spd_size)
        # rewrite buffer content here
        # put buffer into self.spd_buff
        buffbin[119] = self.__bcd_code(diction['VV'])
        buffbin[120] = self.__bcd_code(diction['YY'])
        buffbin[121] = self.__bcd_code(diction['WW'])
        buffbin[122] = self.__bcd_code(diction['ID'][6:8])
        buffbin[123] = self.__bcd_code(diction['ID'][4:6])
        buffbin[124] = self.__bcd_code(diction['ID'][2:4])
        buffbin[125] = self.__bcd_code(diction['ID'][0:2])
        return buffbin


if __name__ == "__main__":
    diction = {
        'PN': 'AGIGA8601-400BCA',
        'RR': '10',
        'VV': '04',
        'YY': '13',
        'WW': '28',
        'ID': '12345678'
    }
    result = load_vpd(diction)
    if(result is None):
        print result
    else:
        print "Error: value is none"
