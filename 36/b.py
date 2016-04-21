#!/usr/bin/env python
#-*- encoding: utf-8 -*-

import math
import sys
import time

"""
B - 回転
"""

N = int( raw_input() )
ns = [ raw_input() for _ in xrange( N ) ]

start = time.clock()

rs = [ [ "" for _ in xrange( N ) ] for _ in xrange( N ) ]

for i in xrange( N ):
    for j in xrange( N ):
        rs[i][j] = ns[N-1-j][i]

for s in rs:
    print( "".join( s ) )

end = time.clock()
#print end - start

sys.exit(0)
