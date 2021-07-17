from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)


app.config['SECRET_KEY'] = 'b77360658cc17407b2sdfgdfbdfbfd3469b'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'


db = SQLAlchemy(app)

from boot_flask import routes