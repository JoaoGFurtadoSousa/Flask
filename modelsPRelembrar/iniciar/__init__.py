from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///databaseTeste.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db=SQLAlchemy(app)
migrate=Migrate(app,db)

from iniciar.routes import ola
from iniciar.model import Pessoas