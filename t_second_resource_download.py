#!/usr/bin/python
#Filename:t_second_resource_download.py
import os

rootDir = '/home/hadoop/mobodata/t_second_resource_download';
#rootDir = 'E:\cy-bigdata-project\mobodata\data';
outputFile = file('/home/hadoop/mobodata/output/t_second_resource_download.txt','w');

list_dirs = os.walk(rootDir)
for root, dirs, files in list_dirs:
    for f in files:
	fname = os.path.join(root, f)
	print fname
        inputFile = file(fname,'r');
        while True:
            line = inputFile.readline();
            if len(line) == 0:
                break;
            #\001 hive default split Symbol
            index1 = line.find('\001');
            index2 = line.find('\001',index1+1);
            index3 = line.rfind('\001');
            index4 = line.rfind('\001',0,index3);
            uuid = line[index1+1:index2];
            resourceId = line[index4+1:index3]

            #begin wirte into output file
            if resourceId and uuid:
                outputFile.write(uuid)
                outputFile.write(',')
                outputFile.write(resourceId)
                outputFile.write('\n');
        #print os.path.join(root, f)

inputFile.close();
outputFile.close();
