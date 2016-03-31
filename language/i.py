#-*- encoding: utf-8 -*-

import sys
import time

"""
I - ナップサック問題
"""

# number of nodes
nw  = map( int, raw_input().split() )
N = nw[0]
W = nw[1]

nws = [ map( int, raw_input().split()) for _ in xrange( N ) ]

start = time.clock()

print ( N, W )
if N <=30 and W > 1000:
#elif N > 30 and W <=1000:
    print "N <= 30 and W > 1000"

    # memo
    memo = []

    def rec( i, j ):
        res = dict()
        if len( memo ) < i+1:
            memo.append( res )
        else:
            res = memo[i]

        if i == N:
            res[j] = 0
        elif j in memo[i]:
            res[j] = memo[i][j]
        elif j < nws[i][1]:
            res[j] = rec( i+1, j )
        else:
            res[j] = max( rec( i+1, j ),
                       rec( i+1, j-nws[i][1] ) + nws[i][0] )
        memo[i] = res
        return res[j]

    print ( rec( 0, W ) )

else:
    print "N > 30 or W <= 1000"

    # memo
    memo = [ [ 0 for _ in xrange( W+1 ) ] for _ in xrange( N+1 ) ]

    for i in xrange( N-1, -1, -1 ):
        for j in xrange( W+1 ):
            if j < nws[i][1]:
                memo[i][j] = memo[i+1][j]
            else:
                memo[i][j] = max( memo[i+1][j], memo[i+1][j - nws[i][1]] + nws[i][0] )

    print ( memo[0][W] )


end = time.clock()
print( end - start )


sys.exit(0)
