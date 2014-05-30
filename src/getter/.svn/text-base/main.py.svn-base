#!/usr/bin/env python
# encoding: utf-8

'''
Created on Jul 2, 2013

@author: mzfa
'''
from getter.scan_sn import ScanLabel
from getter import prog_vpd
from getter import prog_spd
from getter import verify_vpd
from getter import verify_spd
#from getter import error
from getter import simplexml
from getter.save_log import Log
from getter.pcolor import p_yellow, p_green, p_red
from datetime import datetime
from getter.error import DUTError
from getter import final_check
import traceback
import sys


def print_pass():
    print "\n",
    p_green("|---------------------------|")
    p_green("|--------  P A S S  --------|")
    p_green("|---------------------------|")
    print "\n"


def print_fail():
    print "\n",
    p_red("|---------------------------|")
    p_red("|--------  F A I L  --------|")
    p_red("|---------------------------|")
    print "\n"


def programming():
    print("""
          Programming Software for Agiga VPD and SPD.
          Version 2.0.
          Warning: Please check the config file at ./config/dut.xml
          for right configuration.
          The xml test result will be grenerated at D:\Agiga_VPD_SPD_TestLog\
          """)
    while True:
        sl = ScanLabel()
        while(not sl.scan()):
            p_red("Invalid Serial Number")
        dut = sl.dut
        dut.update({"Test_Time":
                    datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
        dut.update({"Test_Station": "Programming"})
        dut.update({"Error_Code": 0})
        dut.update({"Error_Message": "No Error"})
        while (raw_input("Press s to Start:") not in ['s', 'S']):
            pass
        try:
            log = Log(log_path = "D:\\Agiga_VPD_SPD_TestLog\\")
            prog_vpd.prog_vpd(dut)
            verify_vpd.verify_vpd(dut)
            prog_spd.prog_spd(dut)
            verify_spd.verify_spd(dut)
            print_pass()
            log.save(dut["SN"], simplexml.dumps(dut))
        except DUTError, e:
            print_fail()
            p_red("ErrorCode: " + str(e))
            dut.update({"Error_Code": e.code})
            dut.update({"Error_Message": e.message})
            log.save(dut["SN"], simplexml.dumps(dut))
        except Exception:
            p_yellow("Unexpected Error Occured On: ")
            exc_type, exc_value, exc_traceback = sys.exc_info()
            p_yellow(traceback.format_exception(exc_type,
                                                exc_value,
                                                exc_traceback))


def finalcheck():
    print("""
          Final Check Station for Agiga VPD and SPD.
          Version 2.0.
          The xml test result will be grenerated at D:\AGIGA\Agiga_Final_Check_Log\
          """)
    while True:
        sl = ScanLabel()
        while(not sl.scan()):
            p_red("Invalid Serial Number")
        dut = sl.dut
        dut.update({"Test_Time":
                    datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
        dut.update({"Test_Station": "FinalCheck"})
        dut.update({"Error_Code": 0})
        dut.update({"Error_Message": "No Error"})
        while (raw_input("Press s to Start:") not in ['s', 'S']):
            pass
        try:
            log = Log(log_path = "D:\\AGIGA\\Agiga_Final_Check_Log\\")
            final_check.final_check(dut)

            print_pass()
            log.save(dut["SN"], simplexml.dumps(dut))
        except DUTError, e:
            print_fail()
            p_red("ErrorCode: " + str(e))
            dut.update({"Error_Code": e.code})
            dut.update({"Error_Message": e.message})
            log.save(dut["SN"], simplexml.dumps(dut))
        except Exception:
            p_yellow("Unexpected Error Occured On: ")
            exc_type, exc_value, exc_traceback = sys.exc_info()
            p_yellow(traceback.format_exception(exc_type,
                                                exc_value,
                                                exc_traceback))


if __name__ == "__main__":
#     finalcheck()
    programming()
#    pass
