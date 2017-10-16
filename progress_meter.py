#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Thomas Isele" 
__copyright__ = "Copyright 2014"
__license__ = "GPL"
__version__ = "0.1"
__date__ = "09/05/2014"

import sys

class ProgressMeter:
    def __init__(self, i=0, end=None):
        self.i = i
        self.endnum = end
        if type(end) == int:
            self.j = self.endnum / 100.0

    def __next(self):
        i = self.i
        if i == 0:
            sys.stdout.write('')
        elif i % 100 == 0 :
            sys.stdout.write("%d\n"%i)
        elif i % 50 == 0:
            sys.stdout.write('L')
        elif i % 10 == 0:
            sys.stdout.write('|')
        elif i % 5 == 0:
            sys.stdout.write(',')
        else:
            sys.stdout.write('.')
        sys.stdout.flush()
        self.i += 1
        
    def next(self):
        if type(self.endnum)==int:
            self.j += 1
            if ((100*self.j)/self.endnum) > self.i:
                self.__next()
        else:
            self.__next()

    def end(self):
        print self.i
