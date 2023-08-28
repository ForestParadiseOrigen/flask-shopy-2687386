from flask_wtf import FlaskForm
from wtforms import SubmitField, IntegerField, StringField

class NewProductForm(FlaskForm):
    nombre = StringField("Ingrese el nombre del producto.")
    precio = IntegerField("Ingrese el precio del producto.")
    submit = SubmitField("Guardar")