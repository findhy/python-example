#!/usr/bin/python

import sys

def reducer():
    lastClickId = '';

    for l in sys.stdin:
        line = l.strip();
        if not line : break
        viewDetail = line[line.find('[{'):]
        fields = line.split(',')
        clickId = fields[0]

        if clickId == lastClickId:
            if fields[1] == '1':
                print ','.join((lastClickId,viewDetail))
        lastClickId = clickId
            

if __name__ == '__main__':
    reducer()

