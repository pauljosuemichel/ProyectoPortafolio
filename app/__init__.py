from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = 'f5b4c3e7a1f38f841a1fbba779f3acd70e32a3a79c31f8c3'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://ube4fcqrzl0mmiau:SqvA7bBLmB0wHewnFrN5@b0xhxyxbeaxlnhzyfa2m-mysql.services.clever-cloud.com/b0xhxyxbeaxlnhzyfa2m'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

from app import routes
