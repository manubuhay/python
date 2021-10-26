all_servers = list(open('servers.txt'))
for i in range(len(all_servers)):
    print("Server #" + str(i+1) + ": " + all_servers[i].strip('\n'))
