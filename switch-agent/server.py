from flask import Flask, jsonify, request
from flask_cors import CORS
from subprocess import Popen, PIPE

import json
import os

# configuration
ADDR = '0.0.0.0'
DEBUG = True
SUDO = "'"

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

# sanity check route
@app.route('/qos', methods=['GET', 'POST', 'DELETE'])
def handle_request():
    if request.method == 'POST':
        command = request.get_json()["command"]
        executeValue = os.popen('dir').read()
        #JSON
        result = {
            "content": executeValue
        }
        return result
    elif request.method == 'GET':
        cmd = "ovs-vsctl list qos".split()
        p = Popen(["sudo", "-S"] + cmd, stdin=PIPE, stderr=PIPE, universal_newlines=True)
        result, err = p.communicate(SUDO + "\n")[1]
        to_ret = {
            "content": result
        }
        print(to_ret)
        return json.dumps(to_ret)
    elif request.method == 'DELETE':
        req = request.get_json()
        print(req)
        return "DELETE"

if __name__ == '__main__':
    app.run(host=ADDR, debug=DEBUG)
