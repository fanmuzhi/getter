'''
Created on Jul 2, 2013

@author: mzfa
'''
from getter.vpd import VPD
from getter import buff
from getter import error


def verify_vpd(diction):
    try:
        vpd_buff = buff.load_vpd(diction)
    except UserWarning, w:
        print w
        return
    else:
        vpd = VPD(diction['PN'], diction['RR'])
#        print "verifying vpd: ",
        for i in range(512) + range(645, 675):
            if (i % 32 == 0):
                print "#",
            data = vpd.vpd_read_byte(i)
#                print hex(i), data, vpd_buff[i]
            if (data != vpd_buff[i]):
                vpd.vpd_close()
                raise error.VPD_VERIFY
        vpd.vpd_close()
#        print "\nprogram verified"


if __name__ == "__main__":
    diction = {
        'PN': 'AGIGA8601-400BCA',
        'RR': '10',
        'VV': '04',
        'YY': '12',
        'WW': '51',
        'SN': '12345678'
    }
    verify_vpd(diction)
