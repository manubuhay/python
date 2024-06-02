import socket

def is_server_online(ip, port=80, timeout=5):
    """
    Checks if the server is online by trying to connect to the specified IP address and port.
    
    :param ip: The IP address of the server.
    :param port: The port number to connect to. Default is 80 (HTTP).
    :param timeout: Timeout in seconds for the connection attempt. Default is 5 seconds.
    :return: True if the server is online, False otherwise.
    """
    try:
        # Create a socket object
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Set the timeout for the connection attempt
        sock.settimeout(timeout)
        # Try to connect to the server
        sock.connect((ip, port))
        # If the connection is successful, return True
        return True
    except (socket.timeout, socket.error):
        # If there is a timeout or any socket error, return False
        return False
    finally:
        # Always close the socket
        sock.close()

# Example usage
# server_ip = "192.168.1.1"  # Replace with your server's IP address
server_ip=input("Input IP Address: ")
server_port = 80  # Replace with your server's port if it's not 80
timeout=5 #Added/appended, not part of initial code

if is_server_online(server_ip, server_port, timeout):
    print(f"Server at {server_ip}:{server_port} is online.")
else:
    print(f"Server at {server_ip}:{server_port} is offline.")


# Function Definition: The is_server_online function takes three parameters: the server's IP address, the port number (default is 80, which is commonly used for HTTP), and a timeout duration (default is 5 seconds).

# Socket Creation: The script creates a socket object for IPv4 (AF_INET) and TCP (SOCK_STREAM).

# Set Timeout: The socket's timeout is set to the specified value to avoid hanging indefinitely.

# Connection Attempt: The script tries to connect to the server using the specified IP and port.

# Error Handling: If there is a timeout or any socket error (e.g., the server is offline), the function catches the exception and returns False.

# Close Socket: The script ensures the socket is always closed after the connection attempt, whether successful or not.