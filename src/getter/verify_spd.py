'''
Created on Jul 2, 2013
@author: mzfa
'''
from getter.spd import SPD
from getter import buff
from getter import error


def verify_spd(diction):
    try:
        spd_buff = buff.load_spd(diction)
    except UserWarning, w:
        print w
        return
    else:
        spd = SPD(diction['PN'], diction['RR'])
#        print "verifying spd: ",
        for i in range(len(spd_buff)):
            if (i % 16 == 0):
                print "#",
            data = spd.spd_read_byte(i)
            if (data != spd_buff[i]):
                spd.spd_close()
                raise error.SPD_VERIFY
        spd.spd_close()
#        print "\nspd verified"


if __name__ == "__main__":
    diction = {
        'PN': 'AGIGA8601-400BCA',
        'RR':  '10',
        'VV': '04',
        'YY': '12',
        'WW': '51',
        'SN': '12345678'
    }
    verify_spd(diction)
