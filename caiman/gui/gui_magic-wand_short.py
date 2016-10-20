# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 13:59:52 2016

@author: agiovann
"""

import numpy as np
import matplotlib.pyplot as plt
im = plt.imread('/home/agiovann/Downloads/cells.png')
#fig = plt.figure()
#ax = fig.gca()
#ax.add_image(im[:,:,0])
plt.imshow(im)

def onclick(event):
    ix, iy = event.xdata, event.ydata
    
    print 'x = %d, y = %d'%(ix, iy)
    mask = cmw.cell_magic_wand_single_point(im[:,:,0],(iy,ix),5,50,roughness=5)[0]
    bd = plt.contour(mask)    
    bd.collections[0].get_paths()
    print(mask)
    print(bd)
    
cid = fig.canvas.mpl_connect('button_press_event', onclick)