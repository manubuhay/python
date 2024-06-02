import platform
import subprocess

def is_server_online(ip):
    """
    Checks if the server is online by pinging the specified IP address.
    
    :param ip: The IP address of the server.
    :return: True if the server responds to the ping, False otherwise.
    """
    # Determine the command based on the operating system
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    
    # Build the command
    command = ['ping', param, '1', ip]
    
    try:
        # Execute the command
        output = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        # Check the return code
        if output.returncode == 0:
            return True
        else:
            return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

# Example usage
server_ip = "8.8.8.8"  # Replace with your server's IP address

if is_server_online(server_ip):
    print(f"Server at {server_ip} is online.")
else:
    print(f"Server at {server_ip} is offline.")


# Function Definition: The is_server_online function takes one parameter: the server's IP address.

# Determine Command Based on OS: The script checks the operating system using the platform.system() function. It sets the ping command parameter to -n for Windows and -c for other operating systems (typically Unix-based systems).

# Build the Command: The script builds the ping command with the specified parameter to send a single ping ('1') to the IP address.

# Execute the Command: The script executes the command using subprocess.run, capturing the standard output and standard error.

# Check the Return Code: If the return code of the command is 0, it means the server responded to the ping, so the function returns True. Otherwise, it returns False.

# Error Handling: If an exception occurs during the execution of the command, it prints an error message and returns False.