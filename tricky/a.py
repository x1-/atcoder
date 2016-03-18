#-*- encoding: utf-8 -*-

import math
import sys
#import time

"""
A - 整数割り算
"""

N  = int( raw_input() )

ab = [ map( float, raw_input().split()) for _ in xrange( N ) ]

res = []
for x in ab:
    a = x[0]
    b = x[1]
    c = a / b
    if c > 0:
        res.append( int( c ) )
    else:
        d = math.modf( c )
        res.append( int(d[1]) )


#end = time.clock()
#print( end - start )

for x in res:
    print x

sys.exit(0)
