#!/bin/env python3
# coding: utf-8

import pyDSA as dsa
import matplotlib.pyplot as plt

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

# DisplayF
plt.figure()
im.display()
plt.show()


edge = im.edge_detection()

# Display the edge
plt.figure()
edge.display()
plt.show()


edge.fit(s=0.0005)

# Display the edge
plt.figure()
edge.display()
plt.show()


edge.detect_triple_points()

# Display the edge
plt.figure()
edge.display()
plt.show()


edge.compute_contact_angle()
print('Contact angles: {}'.format(edge.thetas))
print('Triple point angles: {}'.format(edge.thetas_triple))

# Display the edge
fig, axs = plt.subplots(1, 2, figsize=(10, 4))
plt.sca(axs[0])
edge.display()
plt.axis('equal')
plt.ylim(1.5, 3)
# Zoom
plt.sca(axs[1])
edge.display()
plt.axis('equal')
plt.ylim(1.5, 2)
plt.xlim(2, 2.3)
plt.show()


import pyDSA as dsa
import matplotlib.pyplot as plt

im = dsa.import_from_image('data/image.bmp', dx=1/120, dy=1/120, unit_x='mm', unit_y='mm')
im.crop(intervx=[1.5, 5], intervy=[1, 3], inplace=True)
im.set_baseline([2, 1.61], [4.5, 1.61])
edge = im.edge_detection()
edge.fit(s=0.0005)
edge.detect_triple_points()
edge.compute_contact_angle()

# Display the edge
plt.figure(figsize=(20, 8))
edge.display()
im.display()
plt.show()

