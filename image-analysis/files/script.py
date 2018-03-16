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

# Display
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
edge_f = spint.UnivariateSpline(xs, ys, k=5, s=0.005)

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


left_x = np.min(xs)
right_x = np.max(xs)
dx = (right_x - left_x)/100

# Left angle
import scipy.misc as spmisc
deriv = spmisc.derivative(edge_f, left_x, dx=dx)
theta_left =  np.arctan(deriv)

# Right angle
deriv = spmisc.derivative(edge_f, right_x, dx=dx)
theta_right = np.pi + np.arctan(deriv)

# Print
print(theta_left/np.pi*180)
print(theta_right/np.pi*180)

# Display the fit
plt.figure()
plt.plot(xs, ys, marker='o', ls='none')
plt.plot(xs, edge_f(xs))
plt.axhline(0, color='k')
angle_len = .6
plt.plot([left_x, left_x + angle_len*np.cos(theta_left)],
         [edge_f(left_x), edge_f(left_x) + angle_len*np.sin(theta_left)])
plt.plot([right_x, right_x + angle_len*np.cos(theta_right)],
         [edge_f(right_x), edge_f(right_x) + angle_len*np.sin(theta_right)])
plt.xlabel('x [mm]')
plt.ylabel('y [mm]')
plt.axis('equal')
plt.show()

