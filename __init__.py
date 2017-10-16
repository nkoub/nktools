#! /usr/bin/env python
# -*- coding: utf-8 -*-

###########################################################################
#    
#    
#
#    Copyright (C) 2013-2017 by Nikos E. Kouvaris <nkouba@gmail.com>
#    
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
###########################################################################    
    
"""
"""

from __future__ import division, absolute_import

# check for Python verion
import sys
if sys.version_info[:2] < (2, 6):
    raise ImportError("Python version 2.6 or later is required (%d.%d detected)." % sys.version_info[:2])
del sys

__author__ = "Nikos E. Kouvaris"
__copyright__ = "Copyright (C) 2013-2017 \
				by Nikos E. Kouvaris <nkouba@gmail.com>"
__license__ = "GNU GPL"

#
#import all modules of the packages
#
from nktools.progress_meter import *
from nktools.fmod_pi import fmod_pi
from nktools.animation_tools import *
from nktools.latex_tools import *
# from nktools.data_tools import *
# from nktools.scatter_animation import *
# from nktools.colormaps import *