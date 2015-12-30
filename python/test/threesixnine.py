#!/usr/bin/env python

# @File : threesixnine.py
# @author : bitfree@gmail.com
# @Ver : 0.2
# @Date : 2015.12.29
# @Desc : this script check how many clap 369 number from start to end
#
# Improvement : speed up 2time  check 369 numbers in function when 1000,000

import sys
import getopt


def check369(a,b):
	clap = 0
	for c in [str(x) for x in xrange(a,b+1)]:
		clap = clap + c.count('3') + c.count('6') + c.count('9')
	print clap

start, end = map(int,sys.stdin.readline().split())

check369(start,end)
