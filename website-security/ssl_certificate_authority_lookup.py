import ssl, socket, csv

list = []
hostname = ""
port = 443
    
def getCA(hostname):
    try:
        ctx = ssl.create_default_context()
        s = ctx.wrap_socket(socket.socket(), server_hostname=hostname)
        s.connect((hostname, port))
        cert = s.getpeercert()
        subject = dict(x[0] for x in cert['subject'])
        issued_to = subject['commonName']
        issuer = dict(x[0] for x in cert['issuer'])
        issued_by = issuer['commonName']
        f.write(hostname)
        f.write(",")
        f.write(issued_by)
        f.write("\n")
    except:
        f.write(hostname)
        f.write(",")
        f.write("could not get cert info")
        f.write("\n")

with open('top-1m.csv', 'r') as csvfile:
    read = csv.reader(csvfile, delimiter=' ', quotechar='|')
    #input size, create input list
    for i in range(0,100):
        for row in read:
            list.append(row)
            break
f= open("output","w+")
for i in range(0,len(list)):
    hostname = str(list[i])
    hostname = hostname.replace('[', '')
    hostname = hostname.replace('\'', '')
    hostname = hostname.replace(']', '')
    #print(hostname)
    getCA(hostname)
    
f.close() 
