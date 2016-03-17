#-*- encoding: utf-8 -*-

import math
import sys
#import time

"""
A - 整数割り算
"""

N  = int( raw_input() )

ab = [ map( int, raw_input().split()) for _ in xrange( N ) ]

res = []
for x in ab:
    a = x[0]
    b = x[1]
    c = a / b
    res.append( c )
    # if c < 0:
    #     if c > -1:
    #         res.append( "0" )
    #     else:
    #         d = str( c )
    #         pos = d.index(".")
    #         res.append( d[0:pos] )
    # else:
    #     res.append( int( c ) )


#end = time.clock()
#print( end - start )

for x in res:
    print x

sys.exit(0)
