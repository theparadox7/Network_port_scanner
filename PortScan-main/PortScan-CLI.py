import socket
import sys
import ipaddress

def scan_host(ip_addr, start_port, end_port):
    print('[*] Starting TCP port scan on host %s' % ip_addr)
    # Begin TCP scan on host
    tcp_scan(ip_addr, start_port, end_port)
    print('[+] TCP scan on host %s complete' % ip_addr)

def scan_range(network, start_port, end_port):
    print('[*] Starting TCP port scan on network %s.0' % network)
    for host in range(1, 255):
        ip = network + '.' + str(host)
        tcp_scan(ip, start_port, end_port)
    print('[+] TCP scan on network %s.0 complete' % network)

def tcp_scan(ip_addr, start_port, end_port):
    for port in range(start_port, end_port + 1):
        try:
            tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            if not tcp.connect_ex((ip_addr, port)):
                print('[+] %s:%d/TCP Open' % (ip_addr, port))
                tcp.close()
        except Exception:
            pass

if __name__ == '__main__':
    socket.setdefaulttimeout(0.01)
    # Check if enough command-line arguments are provided
    if len(sys.argv) != 4:
        sys.exit("Usage: python script.py <IP address> <start port> <end port>")
    ip = sys.argv[1]
    # Validate the IP address
    try:
        ipaddress.ip_address(ip)
    except ValueError:
        sys.exit("Argument 1 is not a valid IP address.")
    # Validate the start port number
    try:
        start_port = int(sys.argv[2])
    except ValueError:
        sys.exit("Argument 2 is not a valid port number.")
    # Validate the end port number
    try:
        end_port = int(sys.argv[3])
    except ValueError:
        sys.exit("Argument 3 is not a valid port number.")
    # Perform the TCP port scan
    scan_host(ip, start_port, end_port)
