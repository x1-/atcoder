#-*- encoding: utf-8 -*-

import sys
#import time

"""
B - センター採点
"""
N  = int(raw_input())
cs = list(raw_input())

dic = {}
for x in xrange( 1, 5 ):
    dic[ str(x) ] = 0

#start = time.clock()

for i in cs:
    dic[i] += 1

mx = max( dic.values() )
mn = min( dic.values() )

print mx, mn

#end = time.clock()
#print( end - start )


sys.exit(0)
