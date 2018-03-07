#!/bin/env python 3


import matplotlib.pyplot as plt
import numpy as np
import pdb
import pandas as pd

# table
a = np.random.rand(13, 4)*50
np.savetxt("data.csv", a)

# mixed table
a = [['yellow', 125, np.random.rand(3)],
     ['blue', 24, np.random.rand(3)],
     ['red', 93, np.random.rand(3)],
     ['grey', 23, np.random.rand(3)]]
with open("data_mixed.csv", "w") as f:
    for ai in a:
        f.write(", ".join([str(aii) for aii in ai]))
        f.write('\n')

# More complex data_mixed
txt = ("From wikipedia: ",
       "Python is an interpreted high-level programming language for",
       "general-purpose programming. Created by Guido van Rossum and",
       "first released in 1991, Python has a design philosophy that",
       "emphasizes code readability, and a syntax that allows programmers",
       "to express concepts in fewer lines of code,[25][26]",
       "notably using significant whitespace. It provides constructs that",
       "enable clear programming on both small and large scales.[27]")
with open("data_complex.txt", "w") as f:
    for txti in txt:
        f.write(txti)
        f.write('\n')
