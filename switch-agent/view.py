from flask import Flask, render_template, request, url_for, redirect
from datetime import datetime
import json
import os

app = Flask(__name__)


@app.route("/")
def home():
    return "CHEEMS"

@app.route("/qos", methods=["POST", "GET", "DELETE"])
def json_return():
    if request.method == 'POST':
        command = request.get_json()["command"]
        executeValue = os.popen('dir').read()
        #JSON
        result = {
            "content": executeValue
        }
        return result
    elif request.method == 'GET':
        req = request.get_json()
        print(req)
        return "GET"
    elif request.method == 'DELETE':
        req = request.get_json()
        print(req)
        return "DELETE"

if __name__ == "__main__":
    app.run(debug=True)