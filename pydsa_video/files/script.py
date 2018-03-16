#!/bin/env python3
# coding: utf-8

import pyDSA as dsa
import matplotlib.pyplot as plt

# Import an image
ims = dsa.import_from_video('data/video.mp4',
                            dx=1/120, dy=1/120, dt=1/10,
                            unit_x='mm', unit_y='mm', unit_t='s',
                            incr=1)

# Display
ims.display()
plt.show()


ims.set_baseline([0.0, 0.583],
                 [6.492, 0.57])
edges = ims.edge_detection()
edges.fit()
edges.compute_contact_angle()

# Display
fig, axs = plt.subplots(2, 3, figsize=(15, 6.9), sharex=True, sharey=True)
for i, ax in enumerate(axs.flat):
    plt.sca(ax)
    ind = int(i/5*(len(ims) - 1))
    ims[ind]._display()
    edges[ind].display()
    plt.xlabel('')
    plt.ylabel('')
    plt.title('t={:.2f}s'.format(ims.times[ind]))
plt.xlim(0, 6.5)
plt.ylim(0, 4.5)
plt.show()


edges.display_summary(figsize=(10, 8))
plt.show()


thetas, thetas_t = edges.get_contact_angles()
print("=== Left contact angle: ===")
print(thetas[:, 0])
print("\n=== Right contact angle: ===")
print(thetas[:, 1])

radius = edges.get_drop_base()
print("\n=== Drop base: ===")
print(radius)

