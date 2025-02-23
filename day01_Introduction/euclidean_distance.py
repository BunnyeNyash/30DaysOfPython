# Find an Euclidean Distance between (2, 3) and (10, 8)
"""
1. Find the difference in the x-coordinates: (x2 - x1)
2. Find the difference in the y-coordinates: (y2 - y1)
3. Square both differences: (x2 - x1) ** 2 and (y2 -y1) ** 2
4. Add them together
5. Take the square root of the sum
"""

import math

def euclidean():
       x1, x2 = 2, 3
       y1, y2 = 10, 8
       print(x1, x2, y1, y2)
       diff1 = x2 - x1
       diff2 = y2 - y1
       square1 = diff1 ** 2
       square2 = diff2 ** 2
       addition = square1 + square2
       distance = math.sqrt(addition) # store the euclidean distance
       print(f'Euclidean distance: {distance}')
       

euclidean()