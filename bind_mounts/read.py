with open("server.txt" ,"r") as f:
    servers = [line.strip() for line in f]

print ("Server list")
for servver in servers:
    print (servver)