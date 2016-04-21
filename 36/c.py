#!/usr/bin/env python
#-*- encoding: utf-8 -*-

import math
import sys
import time

"""
C - 座圧
"""

N = int( raw_input() )
xs = [ int( raw_input() ) for _ in xrange( N ) ]

start = time.clock()

s = set( xs )
ls = list( s )
ls.sort()
d = {}
for (i, x) in enumerate( ls ):
    d[x] = i

for x in xs:
    print d[x]

end = time.clock()
#print end - start

sys.exit(0)
