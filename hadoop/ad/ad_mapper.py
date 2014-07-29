#!/usr/bin/env python
import sys

for line in sys.stdin:
    line = line.strip()
    if line.find('adActivityCallBack')>0:
        print '%s' % (line)