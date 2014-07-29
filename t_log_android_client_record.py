import os

rootDir = '/home/hadoop/mobodata/t_log_android_client_record';
outputFile = file('output.txt','w');
inputFile = file('data.txt','r');

def findIp(fpath,da,ip):
    list_dirs = os.walk(fpath);
    for root, dirs, files in list_dirs:
        for f in files:
            print os.path.join(root, f)
            inFile = file(os.path.join(root, f),'r');
            while True:
                line2 = inFile.readline();
                if len(line2) == 0 :
                        break;
                if line2.find(ip)>0:
                        #moboStr = line2.split('\t');
			#outputFile.write(moboStr[1]+','+moboStr[2]+','+moboStr[3]+','+moboStr[5]+','+moboStr[6]+','+moboStr[7]+','+moboStr[8]+','+moboStr[9]+','+moboStr[10]+','+moboStr[11]+','+moboStr[12]+','+moboStr[13]+','+moboStr[14]+','+moboStr[15]+','+moboStr[16]+','+moboStr[17]+',');
			#outputFile.write(ip+','+moboStr[2]+','+moboStr[10]+','+moboStr[14]+','+moboStr[15]+','+moboStr[16]+','+moboStr[23]);
			outputFile.write(line2);
			outputFile.write('\n');
			#outputFile.write(da);
                        #outputFile.write(',');
                        #outputFile.write(ip);
			#moboStr = line2.split('\t');
			#outputFile.write(moboStr[2]);
                        return


i = 1

while True:
    print i;
    i = i + 1 ;
    line = inputFile.readline();
    if len(line) == 0:
        break;
    da = line[:line.find(',')]
    ip = line[line.find(',')+1:len(line)]
    ip = ip.replace('^M','');
    fpath = os.path.join(rootDir, 'dt='+da)
    #print fpath
    findIp(fpath,da,ip);


inputFile.close();
outputFile.close();
