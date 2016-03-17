#-*- encoding: utf-8 -*-

import sys
#import time

"""
http://language-test-201603.contest.atcoder.jp/tasks/practice_1
A - はじめてのあっとこーだー
"""
a      = int(raw_input())
(b, c) = map(int, raw_input().split())
s      = raw_input()

#start = time.clock()

print str( a + b + c ) + " " + s

#end = time.clock()
#print( end - start )

sys.exit(0)
