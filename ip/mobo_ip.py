import os

rootDir = '/home/hadoop/mobodata/t_log_android_client_record'
outputFile = file(os.path.join(rootDir,'t_log_android_client_record_ip.txt'),'w')

#def findIpAndTime(fileName)

list_dirs = os.walk(rootDir)
for root,dirs,files in list_dirs:
    for f in files:
        fileName = os.path.join(root,f)
        print fileName
        inputFile = file(fileName,'r')
        while True:
            line = inputFile.readline()
            if not line : break
            linestr = line.split('\t')
            outputFile.write(linestr[15])
            outputFile.write(linestr[14])
            outputFile.write('\n')

outputFile.close()