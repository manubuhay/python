import subprocess

def ping_all(servers):
    # The command you want to execute
    cmd = 'ping'
    # send one packet of data to the host
    # this is specified by '-c 1' in the argument list
    outputlist = []
    # Iterate over all the servers in the list and ping each server
    for server in servers:
        # temp = subprocess.Popen([cmd, '-c 1', server], stdout = subprocess.PIPE)\
        # ^Commented, throws out 'needs administrative privileges' error
        temp = subprocess.Popen([cmd, '-n', '3', server], stdout = subprocess.PIPE)
        # get the output as a string
        output = str(temp.communicate())
    # store the output in the list
        outputlist.append(output.split("\\r\\n"))
    return outputlist

if __name__ == '__main__':

    # Get the list of servers from the text file
    servers = list(open('servers.txt'))
    # Iterate over all the servers that we read from the text file
    # and remove all the extra lines. This is just a preprocessing step
    # to make sure there aren't any unnecessary lines.
    for i in range(len(servers)):
        servers[i] = servers[i].strip('\n')
    outputlist = ping_all(servers)

    for list in outputlist:
        print(list)
        print('<===============================================================>')
