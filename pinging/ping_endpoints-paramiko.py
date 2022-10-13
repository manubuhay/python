#Only use when Python version >= 3.8x
import paramiko

def send_command(cmd,results):
    client=paramiko.SSHClient()
    client.load_system_host_keys()
    client.connect('IP',username='USER',password='PASSWD') # You can also use ssh-copy-id(or copy client's id_rsa.pub to server's auth_keys), to omit password as parameter
    ssh_stdin,ssh_stdout,ssh_stderr=client.exec_command(cmd)
    results=[results.append(line.strip('\n')) for line in ssh_stdout]

def main()->None:
    while True:
        mapping = {1: "IP1",2: "IP2",3: "www.google.com",4: "8.8.8.8"}
        print("####################################################")
        print("# 1 - Ping Firewall                                #")
        print("# 2 - Ping Cloudkey                                #")
        print("# 3 - Ping Internet                                #")
        print("# 4 - Ping Internet(No DNS)                        #")
        print("####################################################")
        opt=int(input("Which Option: "))
        if opt < 5:
            print("Pinging, please wait....")
            results=[]
            options=mapping.get(opt,None)
            cmd = "ping -c 4 %s"%(options)
            send_command(cmd,results)
            for x in results:
                print(x.strip())
        else:
            print("Invalid Option")
        print("\n")

main()