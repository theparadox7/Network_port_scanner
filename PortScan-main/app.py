from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/scan', methods=['POST'])
def scan():
    ip = request.form['ip']
    start_port = int(request.form['startPort'])
    end_port = int(request.form['endPort'])

    output = subprocess.check_output(['python', 'PortScan.py', ip, str(start_port), str(end_port)])
    return output.decode('utf-8')


if __name__ == '__main__':
    app.run(debug=True)
