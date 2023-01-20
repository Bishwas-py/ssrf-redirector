import json

from flask import Flask, redirect, request

app = Flask(__name__)


@app.route('/')
def index():
    return redirect('/receive')


@app.route('/receive')
def receive():
    print(request.args)
    print("request.referrer: ", request.referrer)
    return 'OK'


@app.route('/grab')
def grabber():
    client_ip = request.referrer
    client_header = request.headers
    client_user_agent = request.user_agent
    client_accept_language = request.accept_languages
    client = {
        'ip': client_ip,
        'header': json.dumps(client_header),
        'user_agent': client_header.get('User-Agent'),
        'accept_language': client_accept_language
    }
    print(client)
    return 'Hello, World!'


if __name__ == '__main__':
    app.run()
