'''
Created on Jul 2, 2013
@author: mzfa
'''
from getter.spd import SPD
from getter import buff


def prog_spd(diction):
    try:
        spd_buff = buff.load_spd(diction)
    except UserWarning, w:
        print w
        return
    else:
        print "\nSPD: ",
        spd = SPD(diction['PN'], diction['RR'])
#        print "spd programming start, please wait: ",
        for i in range(len(spd_buff)):
            if (i % 16 == 0):
                print "*",
            spd.spd_write_byte(i, spd_buff[i])
#                print hex(i), spd_buff[i]
        spd.spd_close()
#        print "\nspd programmed"


if __name__ == "__main__":
    diction = {
        'SN': 'AGIGA8601-400BCA00000102-10',
        'PN': 'AGIGA8601-400BCA',
        'RR': '10',
        'VV': '04',
        'YY': '13',
        'WW': '27',
        'ID': '00000102'
    }
    prog_spd(diction)
#    err, spd_buff = buff.load_spd(diction)
#    spd = SPD(diction['PN'], diction['RR'])
#    spd.spd_write_byte(4, 0)
