from flask_wtf import FlaskForm
from wtforms import SubmitField, IntegerField, StringField
from wtforms.validators import InputRequired, NumberRange
from flask_wtf.file import FileField, FileRequired, FileAllowed

class NewProductForm(FlaskForm):
    nombre = StringField(
        "Ingrese el nombre del producto.",
        validators = [
            InputRequired(
                message='Debe ingresar minimo un nombre.'
            )
        ]
    )
    precio = IntegerField(
        validators = [
            InputRequired(
                message = "Ingrese el precio del producto."
            ),
            NumberRange(
                message = "Precio fuera de rango.",
                min = 10000,
                max = 100000
            )
        ]
    )
    
    imagen = FileField(
        label = "Ingrese una imagen.",
        validators = (
            FileRequired(
                message = "Es necesaria que subas una imagen."
            ),
            FileAllowed(
                ["jpg","png","svg"],
                message = 'Solamente puedes subir archivos tipo "jpg", "png" o "svg"'
            )
        )
    )
    
    submit = SubmitField("Guardar")