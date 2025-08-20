import socket, subprocess, platform

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
def ping_once(ip):
    sys = platform.system().lower()
    if sys == "windows":
        cmd = ["ping", "-n", "1", "-w", "500", ip]  # 1 echo, 500ms
    else:
        cmd = ["ping", "-c", "1", "-W", "1", ip]    # 1 echo, 1s
    return subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).returncode == 0

def neighbors(ip):
    # assume /24 -> same first 3 octets, try .1 to .10 (skip own IP)
    a,b,c,_ = ip.split(".")
    for last in range(1, 11):
        yield f"{a}.{b}.{c}.{last}"

def main():
    me = get_local_ip()
    if not me:
        print("Could not get local IP"); return
    print("My IP:", me)
    print("Pinging a few neighbors (.1 to .10):")
    alive = []
    for host in neighbors(me):
        if host == me: 
            continue
        ok = ping_once(host)
        print(f"  {host:15} -> {'UP' if ok else 'down'}")
        if ok: alive.append(host)
    print("\nSummary: found", len(alive), "alive hosts among first 10 addresses.")

if __name__ == "__main__":
    main()


