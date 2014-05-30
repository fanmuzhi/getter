#!/usr/bin/env python
# encoding: utf-8

'''
Created on Jul 19, 2013

@author: mzfa
'''
import platform

WHITE = 15
YELLOW = 14
GREEN = 10
RED = 12

if(platform.system() == "Windows"):
    from ctypes import *
    windll.Kernel32.GetStdHandle.restype = c_ulong
    h = windll.Kernel32.GetStdHandle(c_ulong(0xfffffff5))


def print_color(text, color):
    if(platform.system() == "Windows"):
        windll.Kernel32.SetConsoleTextAttribute(h, color)
        print text
        windll.Kernel32.SetConsoleTextAttribute(h, WHITE)
    else:
        print text


def p_yellow(text):
    print_color(text, YELLOW)


def p_green(text):
    print_color(text, GREEN)


def p_red(text):
    print_color(text, RED)
    
if __name__ ==  "__main__":
    p_green("asdfas")
    p_red("sdf")
    p_yellow("asdfasd")
