#Only use when Python version >= 3.8x
import paramiko

def send_command(cmd,results):
    client=paramiko.SSHClient()
    client.load_system_host_keys()
    client.connect('IP',username='USER',password='PASSWD') # You can also use ssh-copy-id(or copy client's id_rsa.pub to server's auth_keys), to omit password as paramter
    ssh_stdin,ssh_stdout,ssh_stderr=client.exec_command(cmd)
    results=[results.append(line.strip('\n')) for line in ssh_stdout]

def main()->None:
    opt=0
    try:
        print("1 - Ping Firewall")
        print("2 - Ping Cloudkey")
        print("3 - Ping Internet")
        print("4 - Ping No DNS Lookup")
        opt=int(input("Which Option:"))
    except:
        print("Invalid option!")
        return
    if(opt==1):
        ip="IP1"
    elif(opt==2):
        ip="IP2"
    elif(opt==3):
        ip="www.google.com"
    elif(opt==4):
        ip="8.8.8.8"
    else:
        print("Number out of range!")
    results=[]
    cmd="ping -c 4 "+ip
    send_command(cmd,results)
    for x in results:
        print(x.strip())

main()