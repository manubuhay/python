#Only use when Python version >= 3.8x
import paramiko
import sys

def send_command(cmd,servers):
    for i in servers:
        client=paramiko.SSHClient()
        client.load_system_host_keys()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) # Bypasses the "The authenticity of host 'x.x.x.x' can't be established."
        client.connect(i["ip"],username=i["user"],password=i["password"]) # You can also use ssh-copy-id(or copy client's id_rsa.pub to server's auth_keys), to omit password as parameter
        ssh_stdin,ssh_stdout,ssh_stderr=client.exec_command(cmd)

def main():
    servers = [
    {
    "ip": "IP1", 
    "user": "root",
    "password": "password"
    },
    {
    "ip": "IP2", 
    "user": "root",
    "password": "password"
    }
              ]
    cmd="reboot"
    send_command(cmd,servers)

main()