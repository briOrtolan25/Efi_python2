from app import db
from flask_marshmallow import Marshmallow
# No necesitas importar SQLAlchemy aquí si ya lo estás importando desde app

class Marca(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)

    def __str__(self) -> str:
        return self.nombre


class Equipo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)

    def __str__(self) -> str:
        return f"Tipo {self.nombre}"
    

class Vehiculo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    modelo = db.Column(db.String(50), nullable=False)
    anio_fabricacion = db.Column(db.Integer)
    precio = db.Column(db.Integer)

    # Pertenecer a
    marca_id = db.Column(db.Integer, db.ForeignKey('marca.id'), nullable=False)
    tipo_id = db.Column(db.Integer, db.ForeignKey('tipo.id'), nullable=False)

    # Relacion directa con el otro objeto
    marca = db.relationship('Marca', backref=db.backref('vehiculos', lazy=True))
    tipo = db.relationship('Tipo', backref=db.backref('vehiculos', lazy=True))


class Celulares(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    modelo = db.Column(db.String(50), nullable=False)
    anio_fabricacion = db.Column(db.Integer)
    precio = db.Column(db.Integer)

    # Pertenecer a
    marca_id = db.Column(db.Integer, db.ForeignKey('marca.id'), nullable=False)
    tipo_id = db.Column(db.Integer, db.ForeignKey('tipo.id'), nullable=False)

    # Relacion directa con el otro objeto
    marca = db.relationship('Marca', backref=db.backref('celulares', lazy=True))
    tipo = db.relationship('Tipo', backref=db.backref('celulares', lazy=True))
class Tipo(db.Model):
    __tablename__ = 'tipo'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80))

class Fabricantes(db.Model):
     id = db.Column(db.Integer, primary_key=True)
     nombre = db.Column(db.String(100), nullable=False)
     pais_origen = db.Column(db.String(100), nullable=False)

     def __repr__(self):
        return f'<Fabricante {self.nombre}>'

class Caracteristica(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<Caracteristicas_list.html {self.tipo}>'
class Stock(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cantidad_disponible = db.Column(db.Integer, nullable=False)
    ubicacion = db.Column(db.String(100), nullable=True)

    def __repr__(self):
        return f'<Stock_list.html {self.cantidad_disponible}>'

class Proveedor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    contacto = db.Column(db.String(100), nullable=True)

    def __repr__(self):
        return f'<Proveedores_list.html {self.nombre}>'

class Accesorios(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String(100), nullable=False)
    compatible_con = db.Column(db.String(200), nullable=True)

    def __repr__(self):
        return f'<Accesorio_list.html {self.tipo}>'
    
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(300), nullable=False)
    is_admin = db.Column(db.Boolean)


    def to_dict(self):
        return dict(
            username=self.username,
            password=self.password_hash
        )
        