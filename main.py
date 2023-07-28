# Importaciones o dependencias
from flask import Flask
from config import Config
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

# Inicializando el objeto flask.
app = Flask(__name__)
app.config.from_object(Config)

# Inicializando el objeto SQLalchemy.
db = SQLAlchemy(app) # Se conecta a la base de datos gracias a "app" que colocamos arriba.
migrate = Migrate(app, db)

# Modelos/Entidades del proyecto.
class Cliente(db.Model):
    __tablename__= "clientes"
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(100), unique = True)
    password = db.Column(db.String(200))
    email = db.Column(db.String(100), unique = True)
    
