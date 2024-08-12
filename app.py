from flask import Flask, render_template, redirect, request, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Instancia de Flask
app = Flask(__name__)

# Configuración de SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/celulares1'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Importa los modelos después de la inicialización de SQLAlchemy para evitar importaciones circulares
from models import Marca, Equipo, Celulares, Fabricantes, Caracteristica, Stock, Proveedor, Accesorios

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/celulares", methods=['POST', 'GET'])
def celulares():
    celulares = Celulares.query.all()
    marcas = Marca.query.all()
    equipos = Equipo.query.all()
    fabricantes = Fabricantes.query.all()
    caracteristicas = Caracteristica.query.all()
    stock = Stock.query.all()
    proveedores = Proveedor.query.all()
    accesorios = Accesorios.query.all()

    if request.method == 'POST':
        modelo = request.form['modelo']
        year_fabricacion = request.form['yearFabricacion']
        precio = request.form['precio']
        marca = request.form['marca']
        equipo = request.form['equipo']
        fabricante = request.form['fabricante']
        caracteristica_d = request.form['caracteristica']
        stock_c = request.form['stock']
        proveedor = request.form['proveedor']
        accesorio = request.form['accesorio']

        celular_nuevo = Celulares(
            modelo=modelo,
            anio_fabricacion=year_fabricacion,
            precio=precio,
            marca_id=marca,
            equipo_id=equipo,
            fabricante_id=fabricante,
            caracteristica_id=caracteristica_d,
            stock_id=stock_c,
            proveedor_id=proveedor,
            accesorio_id=accesorio
        )
        db.session.add(celular_nuevo)
        db.session.commit()
        return redirect(url_for('celulares'))

    return render_template(
        'celulares.html',
        celulares=celulares,
        marcas=marcas,
        equipos=equipos,
        fabricantes=fabricantes,
        caracteristicas=caracteristicas,
        stock=stock,
        proveedores=proveedores,
        accesorios=accesorios
    )

# Agrega aquí las rutas para marca, modelo, tipo, fabricante, proveedor
# (similar a la función `celulares`)

# Configuración del entorno de desarrollo
if __name__ == "__main__":
    app.run(debug=True)
