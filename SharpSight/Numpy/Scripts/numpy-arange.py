#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 12:28:07 2022

@author: craigrupp
"""

# =============================================================================
# Import Package
# =============================================================================
import numpy as np

# =============================================================================
# Create Array 0 : 5
# =============================================================================
np.arange(start=0, stop=6, dtype=float)


# =============================================================================
# Create Array : 1 to 9, then reshape into 3*3
# =============================================================================
one_nine = np.arange(9)
one_nine
print(one_nine.reshape((3,3)))
#print(one_nine.reshape([3,3]))
#print(one_nine.reshape([5,2]))


# =============================================================================
# Create Array : even number 0 to 10
# 
# =============================================================================
print(np.arange(start=0,stop=11,step=2))

# =============================================================================
# Create Array : 1 to 5 - floating points numbers
# 
# =============================================================================
print(np.arange(start=1, stop=6, dtype=float))

# =============================================================================
# Create Array : 10 to 40 in increments of 5
# =============================================================================
print(np.arange(10, 41, 5))
