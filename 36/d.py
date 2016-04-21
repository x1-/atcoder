#!/usr/bin/env python
#-*- encoding: utf-8 -*-

import math
import sys
import time

"""
D - 塗り絵
"""

N = int( raw_input() )
xs = [ map( int, raw_input().split() ) for _ in xrange( N - 1 ) ]

start = time.clock()

ss = set([])
for x in xs:
    key   = x[0] if x[0] < x[1] else x[1]
    value = x[1] if x[0] < x[1] else x[0]
    edge  = "{0}:{1}".format( key, value )
    ss.add( edge )

print(ss)
end = time.clock()
#print end - start

sys.exit(0)
