'''
Created on Jul 2, 2013

@author: mzfa
'''
import re


class ScanLabel(object):
    pattern = re.compile(r'(?P<SN>(?P<PN>AGIGA\d{4}-\d{3}\w{3})(?P<VV>\d{2})(?P<YY>[1-2][0-9])(?P<WW>[0-4][0-9]|5[0-3])(?P<ID>\d{8})-(?P<RR>\d{2}))')
    
    def __init__(self):
        self.dut = {}
    
    def scan(self):
        '''scan serial number from user input
        '''
        sn = raw_input("Scan Product Label: ")
        r = self.pattern.search(sn)
        if r:
            result = r.groupdict()
            self.dut = result
            return True
        else:
            return False


if __name__ == "__main__":
    sl = ScanLabel()
    result = sl.scan()
    print result
