#!/usr/bin/env python
# encoding: utf-8

'''
Created on Jul 2, 2013

@author: mzfa
'''
import os

LOG_PATH = 'D:\\Agiga_VPD_SPD_TestLog\\'
LOG_TYPE = 'xml'


class Log():
    def __init__(self, **kvargs):
        self.logpath = kvargs.get("log_path", LOG_PATH)
        self.logtype = kvargs.get("log_type", LOG_TYPE)
        self.__check_path(self.logpath)

    def __check_path(self, path):
        if not os.path.exists(path):
            os.makedirs(path)

    def __file_name(self, name):
        filepath = self.logpath + name + '.' + self.logtype
        i = 1
        while os.path.exists(filepath):
            filepath = (self.logpath + name
                        + '(' + str(i) + ')'
                        + '.' + self.logtype)
            i += 1
        return filepath

    def save(self, filename, filecontent):
        '''save string to file
        '''
        file_full_name = self.__file_name(filename)
        with open(file_full_name, 'w') as f:
            f.write(filecontent)


if __name__ == "__main__":
    log = Log()
    log.save("test", "this is a test")
