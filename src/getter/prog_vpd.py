'''
Created on Jul 2, 2013

@author: mzfa
'''
from getter.vpd import VPD
from getter import buff


def prog_vpd(diction):
    try:
        vpd_buff = buff.load_vpd(diction)
    except UserWarning, w:
        print w
        return
    else:
        print "\nVPD: ",
#        print "vpd programming start, please wait: ",
        vpd = VPD(diction['PN'], diction['RR'])
        vpd.unlock_wr()
        for i in range(len(vpd_buff)):
            if (i % 64 == 0):
                print "*",
            vpd.vpd_write_byte(i, vpd_buff[i])
        vpd.lock_wr()
        vpd.vpd_close()
#        print "\nvpd programmed"


if __name__ == "__main__":
    diction = {
        'PN': 'AGIGA8601-400BCA',
        'RR': '10',
        'VV': '04',
        'YY': '12',
        'WW': '51',
        'SN': '12345678'
    }
    prog_vpd(diction)
