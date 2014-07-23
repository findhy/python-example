#!/usr/bin/python
#Filename:t_app_sim.py
f1 = file('test/t_app_sim_in','r');
f2 = file('test/t_app_sim_out','w');
while True:
    line = f1.readline();
    if len(line) == 0:
        break;
    ind = line.rfind(',');
    #print line;
    #print line[:ind];
    f2.write(line[:ind]);
    f2.write('\n');
f1.close();
