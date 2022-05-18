#Only use when Python version >= 3.8x
import paramiko
import sys

def send_command(cmd,results):
    client=paramiko.SSHClient()
    client.load_system_host_keys()
    client.connect('HOSTNAME',username='U_NAME',password='PASSWD') # You can also use ssh-copy-id(or copy client's id_rsa.pub to server's auth_keys), to omit password as paramter
    ssh_stdin,ssh_stdout,ssh_stderr=client.exec_command(cmd)
    for line in ssh_stdout:
        results.append(line.strip('\n'))

def main():
    # while(cmd:=input("Input Command: "))!="":
    while(cmd:=input("###Input Command: ")):
        results=[] #Do not make this global, so the values will get reset after each input
        send_command(cmd,results) #Result list also needs to be passed to obtain and reset its values in loop iteration
        # for i in results:
        #     print(i.strip())
        print(stripped:=[i.strip() for i in results])

main() #Call function, if you don't, else statement's "return" line(line 22) will be executed by main
