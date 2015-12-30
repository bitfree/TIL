#!/usr/bin/env python

# @File : ck369.py
# @author : bitfree@gmail.com
# @Ver : 0.1
# @Date : 2015.12.29
# @Desc : this script check how many clap 369 number from start to end


import sys
import getopt

L = [0,]
def ck369(a):
	clap = 0
	clap = clap + str(a).count('3') + str(a).count('6') + str(a).count('9')
	return int(clap)


start, end = map(int,sys.stdin.readline().split())
for k in xrange(start,end+1):
	L.append(ck369(k))

print sum(L) 
