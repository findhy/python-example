import os

rootDir = '/home/hadoop/mobodata/t_log_android_client_record';
outputFile = file('output.txt','w');
inputFile = file('data.txt','r');

while True:
    line = inputFile.readline();
    if len(line) == 0:
        break;
    da = line[:line.find(',')]
    ip = line[line.find(',')+1:]
    print da
    print ip
    fpath = 'da='+da
    list_dirs = os.walk(os.path.join(rootDir, fpath));
    for root, dirs, files in list_dirs:
        for f in files:
            print os.path.join(root, f)


inputFile.close();
outputFile.close();