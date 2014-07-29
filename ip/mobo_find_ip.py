import os
import sys

rootDir = '/home/hadoop/mobodata/t_log_android_client_record'
sourceIpFile = file(os.path.join(rootDir,'t_log_android_client_record_ip.txt'),'r')
targetIpFile = file(os.path.join(rootDir,'data.txt'),'r')
outputIpFile = file(os.path.join(rootDir,'output.txt'),'w')

def findIpAndDate(dateStr,ip):
    while True:
        lineIp = sourceIpFile.readline();
        if not lineIp : break
        if lineIp.find(dateStr)>0 and lineIp.find(ip)>0 :
            outputIpFile.write('1')
            outputIpFile.write(',')
            outputIpFile.write(dateStr)
            outputIpFile.write(',')
            outputIpFile.write(ip)
            outputIpFile.write('\n')
            return


while True:
    line = targetIpFile.readline()
    line = line.strip()
    if not line : break
    dateStr = line[:line.find(',')]
    ipStr = line[line.find(',')+1:]
    ip = ipStr.replace('\n','');
    print dateStr
    print ip
    findIpAndDate(dateStr,ip)