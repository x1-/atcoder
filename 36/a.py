#!/usr/bin/env python
#-*- encoding: utf-8 -*-

import math
import sys
import time

"""
A - お茶
"""

ab = map(int, raw_input().split() )


start = time.clock()

A = ab[0]
B = ab[1]

r = 0
if B < A:
    r = 1
else:
    r = int( math.ceil( float( B ) / A ) )

end = time.clock()
#print end - start
print r
sys.exit(0)
