import os, csv, time, subprocess

list = []
hostname = ""
port = 443
    
def ping(hostname):
    while True:
        try:
            res = subprocess.call(['ping', '-c', '1', '-w', '2',  hostname])
            print('\n')
            if res is not None:
                break
        except:
            print('\n')    
    
        
with open('top-1m.csv', 'r') as csvfile:
    read = csv.reader(csvfile, delimiter=' ', quotechar='|')
    #input size, create input list
    for i in range(0,100):
        for row in read:
            list.append(row)
            break
for i in range(0,len(list)):
    hostname = str(list[i])
    hostname = hostname.replace('[', '')
    hostname = hostname.replace('\'', '')
    hostname = hostname.replace(']', '')

    ping(hostname)

