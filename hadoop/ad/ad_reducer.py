#!/usr/bin/python
import sys

for line in sys.stdin:
    line = line.strip()
    print '%s' % (line)
    #if line.find('adActivityCallBack')>0:
        #print '%s' % (line)