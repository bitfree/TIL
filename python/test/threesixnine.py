#!/usr/bin/env python

# @author : bitfree@gmail.com
# Ver : 0.2
#
# this script check how many clap 369 number from start to end
# 2015.12.29
# Improvement : speed up check 369 numbers in function

import sys
import getopt



def check369(a,b):
	clap = 0
	for c in [str(x) for x in xrange(a,b+1)]:
		clap = clap + c.count('3') + c.count('6') + c.count('9')
	print clap

check369(int(sys.argv[1]),int(sys.argv[2]))

