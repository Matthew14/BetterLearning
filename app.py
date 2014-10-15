from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
from views import *

def main():
    app.run(debug=False, host="0.0.0.0")

if __name__ == "__main__":
    main()
