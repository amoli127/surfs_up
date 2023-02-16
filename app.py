from flask import Flask

#new Flask instance

app = Flask(__name__)

#First route

@app.route('/')
def hello_world():
    return 'Hello world'


