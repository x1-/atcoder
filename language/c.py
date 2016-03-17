#-*- encoding: utf-8 -*-

import sys
#import time

"""
C - 高橋くんと木の直径
"""

# number of nodes
N  = int(raw_input())

mx = 0

# ask
for i in xrange( 1, N + 1 ):
    for j in xrange( i + 1, N + 1 ):
        print "? {0} {1}".format( i, j )
        sys.stdout.flush()
        ans = int( raw_input() )
        mx = max( mx, ans )
        if mx >= 1000000:
            break

    if mx >= 1000000:
        break


print "! {0}".format( mx )
sys.stdout.flush()

#end = time.clock()
#print( end - start )


sys.exit(0)
