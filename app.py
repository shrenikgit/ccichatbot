from flask import Flask
from chatbot import chat
from flask import request
app = Flask(__name__)

@app.route('/hello/', methods=['GET'])
def welcome():
    return "Hello World!"

@app.route('/query/', methods=['POST'])
def query():
    question = request.json['question']
    response = chat(question)
    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9876)