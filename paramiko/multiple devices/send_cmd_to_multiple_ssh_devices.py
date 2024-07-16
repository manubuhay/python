#Only use when Python version >= 3.8x
import paramiko
import sys

def send_command(cmd,servers):
    client=paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    for i in servers:
        print()
        # results=[] # No need for this list, we will traverse and print values found in ssh_stdout
        print("Information for %s"%(i["name"]))
        client.connect(i["ip"],username=i["user"],password=i["password"])
        ssh_stdin,ssh_stdout,ssh_stderr=client.exec_command(cmd)

        # This line needs a catcher outside the function/method "send_command"
        # But printing of values needs to be done inside this for loop for each ssh device connected
        # Otherwise it will create a 2D list 
        # results=[results.append(line.strip('\n')) for line in ssh_stdout]

        # 1st option to print
        # for line in ssh_stdout:
        #     # results.append(line.strip('\n'))
        #     print(line.strip())

        # 2nd option to print, most optimal, using just one line and list comprehension
        print([line.strip() for line in ssh_stdout])

def main():
    servers = [
    {
     "name": "AP18",
     "ip": "x.x.x.x", 
     "user": "admin",
     "password": "password"
    },
    {
     "name": "SW4",
     "ip": "x.x.x.x", 
     "user": "admin",
     "password": "password"
    },
    {
     "name": "Cloud Key",
     "ip": "x.x.x.x", 
     "user": "root",
     "password": "password"
    }
            ]

    # cmd="poweroff"
    cmd="ifconfig | grep '10.5'"
    # cmd="""date +"%d %b %Y %T %Z" -s "$(wget -qSO- --max-redirect=0 http://google.com 2>&1 | grep '^  Date:' | cut -d' ' -f 5-)"""""
    send_command(cmd,servers)

main()
