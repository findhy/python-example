#!/usr/bin/python

import os
import sys

def mapper():
    #str = "\"clickId\":\"d603601bce7c43d7a75197a996058a3e\""
    #print str.find('clickId')
    #print str[str.find('clickId')+10:str.find('clickId')+42]
    
    #filepath = os.environ['map_input_file']    
    #filename = os.path.split(filepath)[-1]
    #filename = 'part-00000'
    for l in sys.stdin:
        line = l.strip()
        if not line : break
        #if filename == 'part-00000':
        if line.find('adActivityCallBack')>0:
            clickId = line[-33:-1]
            print ','.join((clickId,'0'))
        elif line.find('imei') > 0 :
            clickId = line[line.find('clickId')+10:line.find('clickId')+42]
            print ','.join((clickId,'1',line[line.find('[{'):]))
                
if __name__ == '__main__':
    mapper()
