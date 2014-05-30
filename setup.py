#!/usr/bin/env python
# encoding: utf-8

'''
Created on Jul 1, 2013
@author: mzfa
'''
from setuptools import setup
#from setuptools import find_packages

setup(
    name="getter",
    version="2.01",
    package_dir={'': 'src'},
    packages=['getter',
              'getter/adapter',
              'getter/config'],
    package_data={'': ['*.xml', '*.dll', '*.so']},
    author="mzfa",
    description='agiga_crnd_vpd_spd_programmer',
    platforms="any",
    entry_points={
        "console_scripts": [
            'prog = getter.main:programming',
            'fchk = getter.main:finalcheck'
        ]
    }
)
