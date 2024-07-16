import paramiko
import sys

results=[]

def send_command():
    client=paramiko.SSHClient()
    client.load_system_host_keys()
    client.connect('HOSTNAME',username='U_NAME',password='PASSWD') # You can also use ssh-copy-id(or copy client's id_rsa.pub to server's auth_keys), to omit password as paramter
    cmd="netstat -tulpn"
    ssh_stdin,ssh_stdout,ssh_stderr=client.exec_command(cmd)
    for line in ssh_stdout:
        results.append(line.strip('\n')) #Removes new line outputted in ssh_stdout

send_command()
for i in results:
    print(i.strip())

sys.exit()
#Note: -Target server's ssh fingerprint(public key, saved in known_host on client machine) must be saved in client where this script is to be executed
#      -You can try logging in once to save the fingerprint(marked as trusted device) into your client machine
