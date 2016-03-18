#-*- encoding: utf-8 -*-

import sys
#import time

"""
I - ナップサック問題
"""

# number of nodes
nw  = map( int, raw_input().split() )
N = nw[0]
W = nw[1]

nws = [ map( int, raw_input().split()) for _ in xrange( N ) ]

max_value = 0
ws = []
#vs = []
( wl, wr )  = ( 0, 0 )
#( vl, vr )  = ( 0, 0 )

for i in xrange( N ):
    sub_value = 0
    for j in xrange( N ):
        if i == 0:
            wr = 0
        else:
            wr = ws[i-1][j]
        if j == 0:
            wl = 0
        else:
            wl = ws[i][j-1]
        if nws[j] + wr + wl > W:
            break

        ws[i][j] = nws[j][1] + wr + wl

        sub_value += nws[j][0]

    max_value = max( max_value, sub_value )


#end = time.clock()
#print( end - start )


sys.exit(0)
