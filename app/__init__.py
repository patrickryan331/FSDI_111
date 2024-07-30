#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Sample Hello world Flask App"""

from flask import Flask                    # from the flask module import the Flask class instance

app  = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>Hello World</h1>"


# test