#!/bin/env python3
# coding: utf-8

import pyDSA as dsa
import matplotlib.pyplot as plt

# Import an image
im = dsa.import_from_image('data/image.bmp', dx=1/120, dy=1/120, unit_x='mm', unit_y='mm')

# Display
plt.figure()
im.display()
plt.show()


im.crop(intervx=[1.5, 5], intervy=[1, 3], inplace=True)

# Display
plt.figure()
im.display()
plt.show()


im.set_baseline([2, 1.61], [4.5, 1.61])

# Display
plt.figure()
im.display()
plt.show()


edge = im.edge_detection()

# Display the edge
plt.figure()
edge.display()
plt.show()


edge.fit()

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

# Display the edge
plt.figure()
edge.display()
plt.show()


import pyDSA as dsa
import matplotlib.pyplot as plt

im = dsa.import_from_image('data/image.bmp', dx=1/120, dy=1/120, unit_x='mm', unit_y='mm')
im.crop(intervx=[1.5, 5], intervy=[1, 3], inplace=True)
im.set_baseline([2, 1.61], [4.5, 1.61])
edge = im.edge_detection()
edge.fit()
edge.detect_triple_points()
edge.compute_contact_angle()

# Display the edge
plt.figure(figsize=(20, 8))
edge.display()
im.display()
plt.show()


