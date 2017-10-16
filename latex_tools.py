#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Plot Style for use in LaTex
"""
__author__ = "Nikos E Kouvaris"
__date__ = "26/04/2017"

import matplotlib.pyplot as plt
# from mpl_toolkits.axes_grid import axes_size
# from mpl_toolkits.axes_grid import Divider
from numpy import sqrt
####################################################################################################
#
####################################################################################################
from matplotlib.ticker import NullFormatter

nullfmt = NullFormatter()

def empty_axes(axes):
    axes.xaxis.set_major_formatter(nullfmt) 
    axes.yaxis.set_major_formatter(nullfmt)
    axes.get_xaxis().set_tick_params(bottom=False,top=False,
                                     labelbottom=False,labeltop=False)
    axes.get_yaxis().set_tick_params(left=False,right=False,
                                     labelleft=False,labelright=False)

def half_the_ticks(ax, x=True, y=True, xs=0, ys=0):
    if x:
        xlim = ax.get_xlim()
        ax.set_xticks(ax.get_xticks(),minor=True)
        ax.set_xticks(ax.get_xticks()[xs::2])
        ax.set_xlim(xlim)
    if y:
        ylim=ax.get_ylim()
        ax.set_yticks(ax.get_yticks(),minor=True)
        ax.set_yticks(ax.get_yticks()[ys::2])
        ax.set_ylim(ylim)


## Latex parameters for the figures
#########################################################################
def set_fig_params(fig_width_pt=242.64, style=10):
    fig_width_pt = fig_width_pt  # Get this from LaTeX using \showthe\columnwidth
    inches_per_pt = 1.0 / 72.27               # Convert pt to inch
    golden_mean = (sqrt(5)-1.0) / 2.0         # Aesthetic ratio
    fig_width = fig_width_pt * inches_per_pt  # width in inches
    fig_height = fig_width * golden_mean      # height in inches
    fig_size =  [fig_width, fig_height]

    textsizes = {10: (5 , 7 , 8 , 9  , 10 , 12 , 14 , 17 , 20 , 25),
                 11: (6 , 8 , 9 , 10 , 11 , 12 , 14 , 17 , 20 , 25),
                 12: (6 , 8 , 10, 11 , 12 , 14 , 17 , 20 , 25 , 25),
                 20: (10, 14, 16, 19 , 20 , 24 , 28 , 34 , 40 , 50),
                 24: (12, 16, 20, 22 , 24 , 28 , 34 , 40 , 50 , 50)}

    tiny, scriptsize, footnotesize, small, normal,\
                large, Large, LARGE, huge, Huge = textsizes[12]

    figpars = {'backend':'ps',
               'axes.labelsize':normal,
               'text.fontsize': normal,
               'legend.fontsize':footnotesize,
               'xtick.labelsize':small,
               'ytick.labelsize':small,
               'font.family':'sans-serif',
               'font.sans-serif':['Helvecia'],
               'text.usetex':True,
               'text.latex.preamble':['\usepackage{amssymb}',
                                      '\usepackage{amsmath}'],
                'figure.figsize': fig_size}
    return figpars                                  
