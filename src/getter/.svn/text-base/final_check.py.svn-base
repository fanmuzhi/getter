#!/usr/bin/env python
# encoding: utf-8

'''
Created on Oct 10, 2013
@author: mzfa
'''

import os
import inspect
import xml.etree.ElementTree as ET
from getter.vpd import VPD
from getter import error


path = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
CONFIG = path + '/config/dut.xml'

FINAL_CHECK_ADDR = range(0x2A3, 0x2A7)
FW_VERSION_ADDR = range(0x280, 0x285)
HW_VERSION_ADDR = (0x285, 0x286)
ID_ADDR = range(0x287, 0x28F)

Registers = ["Bypass_Times",
             "Bypass_Result",
             "FCT_Times",
             "FCT_Result"
             ]


def __string_alist(string):
    alist = list(string)
    for i in range(len(alist)):
        alist[i] = ord(alist[i])
    return alist


def __alist_string(alist):
    strlist = []
    for i in range(len(alist)):
        strlist.append(chr(alist[i]))
    string = "".join(strlist)
    return string


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


def final_check(diction):
    conf = read_config(diction["PN"], diction["RR"])
    vpd = VPD(diction['PN'], diction['RR'])
    
    # check ID
    result = []
    for i in ID_ADDR:
        result.append(vpd.vpd_read_byte(i))

    ID_text = __alist_string(result)
    diction.update({"ID_READOUT": ID_text})
    if(ID_text != diction["ID"]):
        vpd.vpd_close()
        raise error.ID_NOT_MATCH
    
    # check FW Version
    expected = conf.find("fw_version").text
    result = []
    for i in FW_VERSION_ADDR:
        result.append(vpd.vpd_read_byte(i))

    result_text = __alist_string(result)
    diction.update({"FW_VER": result_text})
    if(result_text != expected):
        vpd.vpd_close()
        raise error.FW_NOT_MATCH

    # check HW Version
    expected = conf.find("hw_version").text
    result = []
    for i in HW_VERSION_ADDR:
        result.append(vpd.vpd_read_byte(i))

    result_text = __alist_string(result)
    diction.update({"HW_VER": result_text})
    if(result_text != expected):
        vpd.vpd_close()
        raise error.FW_NOT_MATCH

    # check bypass and fct
    result = []
    for i in FINAL_CHECK_ADDR:
        result.append(vpd.vpd_read_byte(i))
    diction.update(zip(Registers, result))
    if(diction["Bypass_Result"] != 0x50):
        vpd.vpd_close()
        raise error.BYPASS_FAIL
    if(diction["FCT_Result"] != 0x50):
        vpd.vpd_close()
        raise error.FCT_FAIL

    vpd.vpd_close()


if __name__ == "__main__":
    diction = {
        'PN': 'AGIGA8601-400BCA',
        'RR': '10',
        'VV': '04',
        'YY': '13',
        'WW': '27',
        'ID': '00000102'
    }
    final_check(diction)
