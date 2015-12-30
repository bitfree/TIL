#!/usr/bin/env python

import sys
import getopt


def check369(a,b):
	clap = 0
	for c in [str(x) for x in xrange(a,b+1)]:
		clap = clap + c.count('3') + c.count('6') + c.count('9')
	print clap


check369(int(sys.argv[1]),int(sys.argv[2]))

