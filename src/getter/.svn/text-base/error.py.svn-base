#!/usr/bin/env python
# encoding: utf-8

'''
Created on Jul 2, 2013
@author: mzfa
'''


class DUTError(Exception):
    """define the DUT error
    """
    def __init__(self, **kvargs):
        self.code = kvargs.get("code", 0)
        self.message = kvargs.get("message", "undefined error")

    def __str__(self):
        return repr(self.message)

# Device Error
NO_DEVICE = RuntimeError(True, 0x01, "No Aardvark device found")
PORT_CANNOT_OPEN = RuntimeError(True, 0x02, "Aardvark's port cannot open")

# DUT Error
EE_TIMEOUT = DUTError(code=0x30, message="SMB REG Busy timeout")
DEVICE_RW_ERROR = DUTError(code=0x31, message="Aardvark read write error")
VPD_VERIFY = DUTError(code=0x32, message="VPD verify failed")
SPD_VERIFY = DUTError(code=0x33, message="SPD verify failed")
BYPASS_FAIL = DUTError(code=0x34, message="Bypass test failed")
FCT_FAIL = DUTError(code=0x35, message="FCT test failed")
FW_NOT_MATCH = DUTError(code=0x36, message="FW version is not matched")
HW_NOT_MATCH = DUTError(code=0x37, message="HW version is not matched")
ID_NOT_MATCH = DUTError(code=0x38, message="ID is not matched")



# Config Error
NO_XML_FILE = RuntimeError(True, 0x11, "XML config file doesn't exist")
DUT_NOT_MATCH = RuntimeError(True, 0x12, "Cannot find DUT info in the XML config file")
NULL_VALUE = RuntimeError(True, 0x13, "Null value is found in ebf/bin file, file may be broken")

# User Warning
VPD_DISABLED = UserWarning(True, 0x20, "VPD is disabled")
SPD_DISABLED = UserWarning(True, 0x21, "SPD is disabled")
