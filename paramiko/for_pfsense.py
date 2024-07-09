import paramiko
import time

def connect_to_pfsense(hostname, username, password, command):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(hostname, username=username, password=password, allow_agent=False, look_for_keys=False)
        channel = ssh.invoke_shell()
        time.sleep(1)

        # Receive and decode the initial output
        output = channel.recv(65535).decode('utf-8')
        print(output)

        # Press 6 to Halt system and concatenate '\n'
        channel.send("6\n")
        time.sleep(1)

        # Sends the yes(Y/y) command when the CLI asks if you want to continue to shutdown the system
        channel.send(command + "\n")
        time.sleep(1)

        enable_output = channel.recv(65535).decode('utf-8')
        print(enable_output)
        
        # Wait for 30 seconds for command to finish before closing the SSH session
        time.sleep(30)
    except Exception as e:
        print(f"Error: {e}")
        print("Login failed!")
    ssh.close()
if __name__ == "__main__":
    command = "y"
    # User needs to have access to Halt option if you want to shutdown the system
    connect_to_pfsense('hostname', 'username', 'password', command)