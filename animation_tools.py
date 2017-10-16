# !/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Nikos Kouvaris"
__email__ = "nikos.kouvaris@ub.edu"
__copyright__ = "Copyright 2013-2014"
__license__ = "GPL"
__version__ = "0.1"
__date__ = "07/01/2014"
__update__ = "18/06/2017"

import matplotlib.pyplot as plt
import numpy as np
#
#
#
pause = False
def onClick(event):
    global pause
    pause ^= True
#
#
#
def show_animation(data, ymin=None, ymax=None, 
                pos_separate_lines=None,
                title='', axis_labels=False, 
                fig_number=1):
    '''Animation (with plot) of the values of a numpy
    array with shape (time,size)
    '''
    import matplotlib.animation as animation

    fig = plt.figure(fig_number)
    fig.clf()
    fig.canvas.mpl_connect('button_press_event', onClick)
    ax = fig.add_subplot(111)
    ttl = ax.set_title('')
    line, = ax.plot([],[],
                    marker='o',ms=5,mfc='black',mec='black',lw=0,
                    linestyle=':',color='gray')

    def init():
        if not pause:
            ttl.set_text('')
            line.set_data([], [])
            return line, ttl

    def update_line(i):
        if not pause:
            x = np.arange(data.shape[0])
            y = data[:,i]
            ttl.set_text('{}, t={}'.format(title,i))
            line.set_data(x,y)
            return line, ttl

    ax.set_xlim(0,data.shape[0])
    ax.set_ylim(ymin,ymax)
    ax2 = ax.twinx()
    if axis_labels:
        ax.set_ylabel(r'module 1: $\theta_i$')
        ax2.set_ylabel(r'module 2: $\theta_i$')
    ax2.set_ylim(ymin,ymax)
    

    # define the number of separation lines
    # if pos_separate_lines is None:
    #     pos_separate_lines = [(data.shape[0]/(1.0*pos_separate_lines))*i
    #                 for i in range(0,pos_separate_lines)]
    if pos_separate_lines is not None:
        for vertical_line in pos_separate_lines:
            ax.axvline(vertical_line, linewidth=2, color = 'red', alpha=0.7)

    anim = animation.FuncAnimation(fig,
                                   update_line,
                                   init_func=init,
                                   frames=data.shape[1],
                                   interval=100,
                                   repeat=False,
                                   blit=False)
    return anim
###############################################################################



# if __name__ == '__main__':
    # import numpy as np
    # import matplotlib.pylab as plt
    #
    # num_nodes = 1000
    # data = np.loadtxt('/Users/nkoub/Downloads/data.txt')
    # data2 = data[:,2]
    #
    # space_time_x = np.reshape(data2,(len(data2)/num_nodes,num_nodes))
    # nodes_id = np.arange(space_time_x.shape[1])
    #
    # fig = plt.figure()
    # ax = fig.add_subplot(111)
    #
    # def plot_data(t=0):
    #     ax.scatter(nodes_id,space_time_x[t],
    #                c=space_time_x[t],s=20,
    #                cmap=plt.cm.YlOrBr)
    #
    # plt.ion()
    # txtitle = fig.suptitle('time: {}'.format(0))
    #
    # def plot(snap):
    #     ax.cla()
    #     ax.set_ylim(-1,2)
    #     ax.set_xlim(0,num_nodes)
    #     plot_data(t=snap)
    #     txtitle.set_text('time: {:.1f}'.format(snap))
    #     # use the line below to save png files
    #     plt.savefig('video/snapshot_{:05d}'.format(t),
    #                 dpi=300,bbox_inches='tight')
    #     # OR
    #     # use the line below to see the animation in python
    #     # plt.draw()
    #
    # # use the line below to see the animation in python
    # # plt.show()
    # #
    # for t in np.arange(space_time_x.shape[0]):
    #     plot(t)
    #
    # print 'ok'