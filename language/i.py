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

vws = [ map( int, raw_input().split()) for _ in xrange( N ) ]

if N < 30:
    val   = 0
    total = 0
    for i in xrange( N ):
        V = vws[i][0]
        W = vws[i][1]
        for j in xrange( N ):
        if total + W
        val   += V
        total += W

        print vws

#end = time.clock()
#print( end - start )


sys.exit(0)
