# Example-Python - A Flask app for demonstration purposes
# @jwmarcus-demo
# app.py - Entry point for application

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello World!"
