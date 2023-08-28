from flask import render_template
from app.productos import productos
from .forms import NewProductForm

@productos.route('/create')
def crear():
    form = NewProductForm()
    return render_template('new.html', form = form)

# @productos.route('/update')
# def actualizar():
#     return 'Aqui vamos a registrar productos...'

# @productos.route('/consult')
# def consultar():
#     return 'Aqui vamos a registrar productos...'

# @productos.route('/delete')
# def eliminar():
#     return 'Aqui vamos a registrar productos...'