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


edges[180:, :] = 0
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
plt.axhline(0, color='k')
plt.axis('equal')
plt.show()


res = 120 
xs /= res
ys /= res
# Plot the edges
plt.figure()
plt.plot(xs, ys, marker='o', ls='none')
plt.axhline(0, color='k')
plt.axis('equal')
plt.xlabel('x [mm]')
plt.ylabel('y [mm]')
plt.show()


# Ensure increasing x values
new_xs = np.sort(list(set(xs)))
new_ys = []
for x in new_xs:
    new_ys.append(np.mean(ys[xs == x]))
xs = new_xs
ys = new_ys
# Find a fit
import scipy.interpolate as spint
edge_f = spint.UnivariateSpline(xs, ys, k=5, s=0.001)
# Display the fit
plt.figure()
plt.plot(xs, ys, marker='o', ls='none')
plt.plot(xs, edge_f(xs))
plt.axhline(0, color='k')
plt.xlabel('x [mm]')
plt.ylabel('y [mm]')
plt.axis('equal')
plt.show()


base_radius = np.max(xs) - np.min(xs)
height = np.max(ys)
# Print
print("Base radius: {} mm".format(base_radius))
print("Drop height: {} mm".format(height))

