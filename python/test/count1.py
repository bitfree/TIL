#!/usr/bin/env python

# @File : count1.py
# @author : bitfree@gmail.com
# @Ver : 0.1
# @Date : 2015.12.29
# @Desc : this script count how many number1 is in string


import sys

start, end = map(int,sys.stdin.readline().split())

def count_one(a,b):
	sum = 0
	for c in [str(x) for x in xrange(a, b+1)]:
		sum = sum + c.count('1')
	print sum 

count_one(start,end)
