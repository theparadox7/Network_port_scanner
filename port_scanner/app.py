from flask import Flask, render_template, request
import socket

app = Flask(__name__)

def scan_ports(target_ip, start_port, end_port):
    open_ports = []
    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target_ip, port))
        if result == 0:
            open_ports.append(port)
        sock.close()
    return open_ports

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scan', methods=['POST'])
def scan():
    target_ip = request.form['ip']
    start_port = int(request.form['start_port'])
    end_port = int(request.form['end_port'])

    open_ports = scan_ports(target_ip, start_port, end_port)

    return render_template('result.html', target_ip=target_ip, open_ports=open_ports)

if __name__ == '__main__':
    app.run(debug=True)
