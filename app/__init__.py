from flask import Flask, render_template
from .config import Config
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

#Importacion de Blueprints.
from app.productos import productos

#Importacion de plugins
from flask_bootstrap import Bootstrap

# Inicializando el objeto flask.
app = Flask(__name__)
app.config.from_object(Config)
bootstrap = Bootstrap(app)

# Inicializando el objeto SQLalchemy.
db = SQLAlchemy(app) # Se conecta a la base de datos gracias a "app" que colocamos arriba.
migrate = Migrate(app, db)

# Registrar nodulos/Blueprints.
app.register_blueprint(productos)

#Se cita una dependencia despues de llamar a "db" para que "db" pueda ejecutar.
from .models import Cliente, Venta, Producto, Detalle

@app.route('/prueba')
def prueba():
    return render_template('base.html')