# All the imports
import sqlite2
from flask import abort
from flask import flash
from flask import Flask
from flask import g
from flask import render_template
from flask import request
from flask import session
from flask import redirect
from flask import url_for

# configuratoin
DATABASE = '/tmp/flaskr.db'
DEBUG = True
SECRET_KEY = 'some_hard_key'
USERNAME = 'admin'
PASSWORD = 'default'
