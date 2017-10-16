#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author      : Nikos E Kouvaris
# Email       : nkouba@gmail.com
# Date        : 07/04/2017


from __future__ import division, absolute_import

# check for Python verion
import sys
if sys.version_info[:2] < (2, 6):
    raise ImportError("Python version 2.6 or later"\
                    "is required for multiNetX (%d.%d detected)." % 
                    sys.version_info[:2])
del sys

__author__ = "Nikos E. Kouvaris <nkouba@gmail.com>"
__copyright__ = "Copyright (C) 2017 by Nikos E. Kouvaris <nkouba@gmail.com>"
__license__ = "GNU GPL"
__version__ = "0.1."



try:
    from numpy import pi, floor
except ImportError:
    raise ImportError("numpy is required")


def fmod_pi (angle_rad):
    '''Return the modulo of an angle in rad within the regime (-pi,pi)
    Parameters:
    -----------
    angle_rad: float
    
    Returns:
    --------
    A float in the regime (-pi,pi)
    '''
    return angle_rad - 2.0 * pi * floor((angle_rad+pi)/(2.0*pi))