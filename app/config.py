# Establecemos la direccion de nuestra base de datos.
class Config:
    # Ruta de nuesta base de datos
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost/flask-shopy-2687386'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'admin'