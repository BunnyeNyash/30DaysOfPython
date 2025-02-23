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
       x1, x2, y1, y2 = 2, 3, 10, 8
       distance = math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2)) # store the euclidean distance
       print(f'Euclidean distance: {distance}')    

euclidean()