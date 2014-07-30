#!/usr/bin/python
import sys

for l in sys.stdin:
    try:
        line = l.strip()
        if len(line) > 0:
            if line.find('adActivityCallBack')>0:
                print line
                #print line[-33:-1]
    except Exception,ex:
        pass
        
    