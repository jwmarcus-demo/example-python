# Example-Python - A Flask app for demonstration purposes
# @jwmarcus-demo
# app.py - Entry point for application

from confire import Configuration, environ_setting
from flask import Flask
import os

# Get database credentials
class DbConfig(Configuration):
    CONF_PATHS = ['./db_config.yaml']

# Load settings right away
settings = DbConfig.load()

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello World!"

@app.route('/db_name/')
def print_db_params():
    return settings['database'].get("name")
