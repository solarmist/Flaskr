from __future__ import with_statement
from contectlib import closing
# from flask import abort
# from flask import flash
from flask import Flask
# from flask import g
# from flask import render_template
# from flask import request
# from flask import session
# from flask import redirect
# from flask import url_for
import sqlite3

app = Flask(__name__)
app.config.from_pyfile('setup.py', silent=False)


def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('schema.sql') as f:
            db.cursor().executescript(f.read())
        db.commit()


def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

if __name__ == '__main__':
    app.run()
