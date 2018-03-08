#!/bin/env python3
# coding: utf-8

import imageio
image = imageio.imread('data/image.bmp')


import matplotlib.pyplot as plt
plt.figure()
plt.imshow(image)
plt.colorbar()
plt.show()


image = image[200:400, 200:550]
plt.figure()
plt.imshow(image)
plt.show()
              


import cv2
thres1 = image.min()
thres2 = image.max()
edges = cv2.Canny(image, thres1, thres2)
# Display the obtained edges
plt.figure()
plt.imshow(edges)
plt.show()


thres1 = image.min()*0.75
thres2 = image.max()*1.5
edges = cv2.Canny(image, thres1, thres2)
# Display the obtained edges
plt.figure()
plt.imshow(edges)
plt.show()


edges[180:] = 0
# Display the obtained edges
plt.figure()
plt.imshow(edges)
plt.show()


import numpy as np
ys, xs = np.where(edges)
ys = np.asarray(-ys, dtype=float)
xs = np.asarray(xs, dtype=float)
# Plot the edges
plt.figure()
plt.plot(xs, ys, marker='o', ls='none')
plt.axis('equal')
plt.show()


xs -= xs.mean()
ys -= ys.min()
# Plot the edges
plt.figure()
plt.plot(xs, ys, marker='o', ls='none')
plt.axis('equal')
plt.show()

