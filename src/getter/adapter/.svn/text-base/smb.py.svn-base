'''
Created on Jul 2, 2013

@author: mzfa
'''
from getter.adapter import aardvark_py as aa
from getter import error


BUS_TIMEOUT = 25  # ms
DEFAULT_REG_VAL = 0xFF


class DeviceAPI(object):
    '''SMBus Device API
    '''

    def __init__(self, **kvargs):
        try:
            type(eval(self.aa_handle))
        except:
            self.aa_port = kvargs.get('port', 0)
            self.aa_bitrate = kvargs.get('bitrate', 0)
            self.aa_slave_addr = kvargs.get('slaveaddr', 0)
            self.aa_handle = kvargs.get('handle', 32)
            self.err = 0
            self.val = 0
        else:
            self.close()
            self.aa_port = kvargs.get('port', 0)
            self.aa_bitrate = kvargs.get('bitrate', 0)
            self.aa_slave_addr = kvargs.get('slaveaddr', 0)
            self.aa_handle = kvargs.get('handle', 32)
            self.err = 0
            self.val = 0

    def open(self):
        '''
        config the aardvark tool params like bitrate, slave address etc,
        '''
        # find port
        (port_num, ports) = aa.aa_find_devices(1)
        if port_num > 0:
            self.aa_port = ports[0]
        else:
            raise error.NO_DEVICE

        # open port
        self.aa_handle = aa.aa_open(self.aa_port)
        if(self.aa_handle <= 0):
            raise error.PORT_CANNOT_OPEN
        # Ensure that the I2C subsystem is enabled
        aa.aa_configure(self.aa_handle,  aa.AA_CONFIG_SPI_I2C)
        aa.aa_i2c_pullup(self.aa_handle, aa.AA_I2C_PULLUP_BOTH)
        aa.aa_target_power(self.aa_handle, aa.AA_TARGET_POWER_NONE)
        # Set the bitrate
        self.aa_bitrate = aa.aa_i2c_bitrate(self.aa_handle, self.aa_bitrate)
        # Set the bus lock timeout
        aa.aa_i2c_bus_timeout(self.aa_handle, BUS_TIMEOUT)
        # Free bus
        aa.aa_i2c_free_bus(self.aa_handle)

    def write(self, reg_addr, wdata):
        '''
        Write data to SMBus register
        reg_addr: register address offset
        wdata: data to be write to SMBus register
        '''
        data_out = aa.array('B', [reg_addr, wdata])
        (ret, num_written) = aa.aa_i2c_write_ext(self.aa_handle,
                                                 self.aa_slave_addr,
                                                 aa.AA_I2C_NO_FLAGS,
                                                 data_out)
        #print "ret = %d, num = %d" % (ret, num_written)
        if(ret != aa.AA_I2C_STATUS_OK):
            aa.aa_i2c_free_bus(self.aa_handle)
            self.err = ret
        if(num_written != 2):
            self.err = aa.AA_I2C_WRITE_ERROR
        return self.err

    def read(self, reg_addr):
        '''
        Read data from SMBus register
        reg_addr: register address offset
        '''
        self.val = DEFAULT_REG_VAL
        data_out = aa.array('B', [reg_addr])
        # write register address
        (ret, num_written) = aa.aa_i2c_write_ext(self.aa_handle,
                                                 self.aa_slave_addr,
                                                 aa.AA_I2C_NO_STOP,
                                                 data_out)
        if(ret != aa.AA_I2C_STATUS_OK):
            aa.aa_i2c_free_bus(self.aa_handle)
            self.err = ret
            return(self.err, self.val)
        if(num_written != 1):
            self.err = aa.AA_I2C_WRITE_ERROR
            return(self.err, self.val)

        # read register data
        (ret, rdata, num_read) = aa.aa_i2c_read_ext(self.aa_handle,
                                                    self.aa_slave_addr,
                                                    aa.AA_I2C_NO_FLAGS, 1)
        if(ret == aa.AA_I2C_STATUS_BUS_LOCKED):
            aa.aa_i2c_free_bus(self.aa_handle)
            self.err = ret
        else:
            # finish read
            if (num_read != 1):
                self.err = aa.AA_I2C_READ_ERROR
            else:
                if (ret != aa.AA_OK):
                    self.err = ret
                else:
                    self.val = rdata[0]
        return(self.err, self.val)

    def sleep(self, ms):
        aa.aa_sleep_ms(ms)

    def close(self):
        '''close device
        '''
        aa.aa_close(self.aa_handle)


if __name__ == "__main__":
    da = DeviceAPI(slaveaddr=16)
    try:
        da.open()
        for i in range(10):
            (ret, rdata) = da.read(1)
            if (ret != 0):
                print ret
            if (rdata == 0x00):     # not busy
                break

        if (i < 20):
            print "OK"
        else:
            print "<E> SMB REG Busy timeout"
    except Exception, e:
        print e
