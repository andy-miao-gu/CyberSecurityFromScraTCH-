import socket as socket
def get_local_ip():
    try:
        # Create a UDP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # Connect to an address (doesn't have to be reachable)
        sock.connect(("8.8.8.8", 80))
        ip = sock.getsockname()[0]
        sock.close()
        return ip
    except Exception as e:
        print(f"Error retrieving local IP address: {e}")
        return None

if __name__ == "__main__":
    local_ip = get_local_ip()
    if local_ip:
        print("Local IP of Andyiscoolhe:")
        print(f"Local IP address: {local_ip}")
    else:
        print("Could not retrieve local IP address.")