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

# Display the edges
plt.figure()
plt.imshow(edges)
plt.show()


thres1 = image.min()*0.75
thres2 = image.max()*1.5
edges = cv2.Canny(image, thres1, thres2)

# Display the edges
plt.figure()
plt.imshow(edges)
plt.show()


edges[180:, :] = 0

# Display the edges
plt.figure()
plt.imshow(edges)
plt.show()


import numpy as np
ys, xs = np.where(edges)
ys = np.asarray(-ys, dtype=float)
xs = np.asarray(xs, dtype=float)

# Display the edges
plt.figure()
plt.plot(xs, ys, marker='o', ls='none')
plt.axis('equal')
plt.show()


xs = xs - xs.mean()
ys = ys - ys.min()

# Plot the edges
plt.figure()
plt.plot(xs, ys, marker='o', ls='none')
plt.axhline(0, color='k')
plt.axis('equal')
plt.show()


res = 120 
xs /= res
ys /= res

# Plot the edge
fig, axs = plt.subplots(1, 2, figsize=(10, 4))
plt.sca(axs[0])
plt.plot(xs, ys, marker='o', ls='none')
plt.axhline(0, color='k')
plt.axis('equal')
plt.xlabel('x [mm]')
plt.ylabel('y [mm]')
# Plot a zoom on the edge
plt.sca(axs[1])
plt.plot(xs, ys, marker='o', ls='none')
plt.axhline(0, color='k')
plt.axis('equal')
plt.xlabel('x [mm]')
plt.xlim(-1.15, -0.9)
plt.ylim(-0.05, 0.3)
plt.title("Zoom")
plt.show()


# Ensure increasing x values
new_xs = np.sort(list(set(xs)))
new_ys = []
for x in new_xs:
    new_ys.append(np.mean(ys[xs == x]))
xs = new_xs
ys = np.asarray(new_ys)

# Fitting the drop edge
import scipy.interpolate as spint
edge_f = spint.UnivariateSpline(xs, ys, k=5, s=0.005)

# Display the fit
fig, axs = plt.subplots(1, 2, figsize=(10, 4))
plt.sca(axs[0])
plt.plot(xs, ys, marker='o', ls='none')
plt.plot(xs, edge_f(xs))
plt.axhline(0, color='k')
plt.xlabel('x [mm]')
plt.ylabel('y [mm]')
plt.axis('equal')
# Plot a zoom on the edge
plt.sca(axs[1])
plt.plot(xs, ys, marker='o', ls='none')
plt.plot(xs, edge_f(xs))
plt.axhline(0, color='k')
plt.axis('equal')
plt.xlabel('x [mm]')
plt.xlim(-1.1, -0.7)
plt.ylim(0, 0.5)
plt.title("Zoom")
plt.show()


base_radius = xs.max() - xs.min()
height = ys.max()

# Print
print("Drop base: {} mm".format(base_radius))
print("Drop height: {} mm".format(height))


# Get left and right contact points
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

# Display the fit and the angles
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

