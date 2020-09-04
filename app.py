from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello Worlddd!'


if __name__ == '__main__':
    app.run(port=5000)
