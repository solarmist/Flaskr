from flask import Flask

app = Flask(__name__)
app.config.from_pyfile('setup.py', silent=False)

def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

if __name__ == '__main__':
    app.run()
