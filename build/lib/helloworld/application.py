#!flask/bin/python
import json
from flask import Flask, Response
from helloworld.flaskrun import flaskrun
from Post import app

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8000)
