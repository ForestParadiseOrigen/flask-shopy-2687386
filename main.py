# Importaciones o dependencias
from flask import Flask
from flask import render_template
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from config import Config
from datetime import datetime
from wtforms import StringField, PasswordField, SubmitField

# Inicializando el objeto flask.
app = Flask(__name__)
app.config.from_object(Config)

# Inicializando el objeto SQLalchemy.
db = SQLAlchemy(app) # Se conecta a la base de datos gracias a "app" que colocamos arriba.
migrate = Migrate(app, db)

#Formulario de registro de cliente
class RegistroClienteForm(FlaskForm):
    username = StringField("Nombre de Usuario")
    email = StringField("Correo Electronico")
    password = PasswordField("Contraseña")
    submit = SubmitField("Registrar")

# Modelos/Entidades del proyecto.
class Cliente(db.Model):
    __tablename__= "clientes"
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(100), unique = True)
    password = db.Column(db.String(200))
    email = db.Column(db.String(100), unique = True)
    

class Producto(db.Model):
    __tablename__="productos"
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(120), unique = True)
    precio = db.Column(db.Numeric(precision = 10, scale = 2))
    imagen = db.Column(db.String(120), unique = True)

class Venta(db.Model):
    __tablename__="ventas"
    id = db.Column(db.Integer, primary_key = True)
    fecha = db.Column(db.DateTime, default = datetime.utcnow)
    cliente_id = db.Column(db.Integer, db.ForeignKey('clientes.id'))

class Detalle(db.Model):
    __tablename__="detalles"
    id = db.Column(db.Integer, primary_key = True)
    producto_id = db.Column(db.Integer, db.ForeignKey('productos.id'))
    venta_id = db.Column(db.Integer, db.ForeignKey('ventas.id'))
    cantidad = db.Column(db.Integer)

@app.route('/clientes/create', methods = ['GET', 'POST'])
def crear_cliente():
    #Intanciando el formulario
    form = RegistroClienteForm()
    if form.validate_on_submit():
        #Crear el nuevo cliente.
        c = Cliente(
            username = form.username.data, 
            email = form.email.data,
            password = form.password.data
            )
        db.session.add(c)
        db.session.commit()
        
        return "Registro de registrado"
    return render_template('registro.html', form = form)

@app.route('/clientes', methods = ['GET'])
def listar():
    #Consultar todos los clientes
    clientes = Cliente.query.all()
    return render_template('listar.html', clientes = clientes)