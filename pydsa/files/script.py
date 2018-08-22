#!/bin/env python3
# coding: utf-8

import pyDSA as dsa
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = 15, 9

# Import an image
im = dsa.import_from_image('data/image.bmp', dx=1/120, dy=1/120, unit_x='mm', unit_y='mm')

# Display it
plt.figure()
im.display()
plt.show()


im.crop(intervx=[1.5, 5], intervy=[1, 3], inplace=True)

# Display
plt.figure()
im.display()
plt.show()


im.set_baseline(pt1=[2, 1.61], pt2=[4.5, 1.61])

# Display
plt.figure()
im.display()
plt.show()


edge = im.edge_detection()

# Display the edge
plt.figure()
im.display()
edge.display()
plt.show()


edge_cont = im.edge_detection_contour(level=.25)

# Display the edge
plt.figure()
im.display()
edge_cont.display()
plt.show()


cfit = edge.fit_circle()

# Display the edge
plt.figure()
im.display()
cfit.display()
plt.show()


elfit = edge.fit_ellipse()

# Display the edge
plt.figure()
im.display()
elfit.display()
plt.show()


pfit = edge.fit_polyline(deg=5)

# Display the edge
plt.figure()
im.display()
pfit.display()
plt.show()


sfit = edge.fit_spline()

# Display the edge
plt.figure()
im.display()
sfit.display()
plt.show()


csfit = edge_cont.fit_circles(triple_pts=[[2.1, 1.7], [4.2, 1.7]])

# Display the edge
plt.figure()
im.display()
csfit.display()
plt.show()


elfit.compute_contact_angle()
print('Contact angles: {}'.format(elfit.thetas))

# Display the edge
fig, axs = plt.subplots(1, 2, figsize=(13, 4))
plt.sca(axs[0])
im.display()
elfit.display()
plt.ylim(1.5, 3)
# Zoom
plt.sca(axs[1])
im.display()
elfit.display()
plt.ylim(1.5, 2)
plt.xlim(1.8, 2.4)
plt.show()

