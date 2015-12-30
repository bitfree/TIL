#!/usr/bin/env python

# @author : bitfree@gmail.com
# @Ver : 0.1
#
# this script check how many clap 369 number from start to end


import sys
import getopt

L = [0,]
def ck369(a):
	clap = 0
	clap = clap + str(a).count('3') + str(a).count('6') + str(a).count('9')
	return int(clap)

for k in xrange(int(sys.argv[1]),int(sys.argv[2])+1):
	L.append(ck369(k))

print sum(L) 
