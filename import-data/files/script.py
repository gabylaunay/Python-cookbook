#!/bin/env python3
# coding: utf-8

import numpy as np
data = np.genfromtxt('data/data.csv')
print(data)


new_data = data*4.3
np.savetxt('data/new_data.csv', new_data)


import pandas as pd
data = pd.read_csv('data/data_mixed.csv')
print(data)


with open('data/data_complex.txt', 'r') as f:
    data = f.readlines()
for line in data:
    print(line)


from scipy import misc
image = misc.imread('data/image.bmp')


import matplotlib.pyplot as plt
plt.figure()
plt.imshow(image)
plt.show()


print("Pixel values:\n{}".format(image))
print("Value of the pixel at (10,10): {}".format(image[10, 10]))

