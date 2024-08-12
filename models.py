from app import db
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
        return self.nombre


class Celulares(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    modelp = db.Column(db.String(50), nullable=False)
    anio_fabricacion = db.Column(db.Integer)  # Corregido: Column en lugar de Colum
    precio = db.Column(db.Integer)
    marca_id = db.Column(db.Integer, db.ForeignKey('marca.id'), nullable=False)
    equipo_id = db.Column(db.Integer, db.ForeignKey('equipo.id'), nullable=False)
    def __str__(self):
        return self.modelp
    
    marca = db.relationship('Marca', backref=db.backref('celulares', lazy=True))
    equipo = db.relationship('Equipo', backref = db.backref('celulares', lazy=True))

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