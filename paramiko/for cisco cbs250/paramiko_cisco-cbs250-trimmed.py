# Enable "SSH User Authentication by Password" in Cisco Switch GUI in Security >> SSH Server >> SSH User Authentication
import paramiko
import time

def connect_to_cbs250(hostname, username, password, command):
    ssh = paramiko.SSHClient()
    # Automatically add the server's host key (this is insecure, not recommended for production)
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(hostname, username=username, password=password, allow_agent=False, look_for_keys=False)
        # Create a shell channel for interaction
        channel = ssh.invoke_shell()
        # Wait for the prompt after connecting
        time.sleep(1)
        # Receive and decode the initial output
        output = channel.recv(65535).decode('utf-8')
        print(output)

        # Send the command to be executed in Privileged Exec mode
        channel.send(command + "\n")
        time.sleep(1)
        
        # Sends the yes(Y/y) command when the CLI asks "This command will reset the whole system and disconnect your current session. 
        # Do you want to continue ? (Y/N)[N]" comment these 2 lines if you are NOT rebooting or copying running config to startup config
        channel.send("y\n")
        time.sleep(1)
            
        enable_output = channel.recv(65535).decode('utf-8')
        print(enable_output)
        ssh.close()
    except Exception as e:
        print(f"Error: {e}")
        print("Login failed!")

if __name__ == "__main__":
    # command = "show vlan"
    command = "reload"
    connect_to_cbs250("hostname", "username", "password", command)
