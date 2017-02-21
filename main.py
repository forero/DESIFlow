import sys
from matplotlib.dates import strpdate2num
import numpy as np
import  subprocess

try:
    fiberassign_dates = 'epochs_date.txt'
    f = open(fiberassign_dates, 'r')
except IOError as e:
    print('Problem opening file epochs_date.txt')
    exit()
    
dates = {}
fx = f.readlines()
for line in fx:
    line = line.strip()
    if line.startswith('#') or len(line) < 2:
        continue
    line = line.split()
    epoch = int(line[0])
    yearmmdd = [line[1], line[2]]
    dates[epoch] = {}
    dates[epoch]['BEGINS']= line[1]
    dates[epoch]['ENDS']= line[2]

for k in dates.keys():
    print(k)
    make_process = subprocess.Popen("make EPOCH={};".format(k), shell=True, stdout=subprocess.PIPE, stderr=sys.stdout.fileno())
    while True:
        line = make_process.stdout.readline()
        if not line:break
        print(line), #output to console in time
        sys.stdout.flush()



