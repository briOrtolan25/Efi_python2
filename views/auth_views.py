from datetime import timedelta

from flask import Blueprint, request, jsonify, make_response
from flask_jwt_extended import (
    create_access_token,
    get_jwt,
    jwt_required,
)
from werkzeug.security import (
    check_password_hash,
    generate_password_hash
)

from app import db
from models import User, Celulares
from schemas import UserSchema, UserMinimalSchema, CelularesSchema


auth_bp = Blueprint('auth', __name__)
celulares_bp = Blueprint('api_celulares', __name__)

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.authorization
    username = data.username
    password =data.password

    usuario = User.query.filter_by(username=username).first()

    if usuario and check_password_hash(
        pwhash=usuario.password_hash, password=password
    ):
        access_token = create_access_token(
        identity=username,
        expires_delta=timedelta(minutes=10),
        additional_claims=dict(
            administrador=usuario.is_admin
        ))
        return jsonify({'Token': f'Bearer {access_token}'})
   
   
    return jsonify(Mensaje = "El usuario y la contraseña son incorrectos")

@auth_bp.route('/users', methods=['GET', 'POST'])
@jwt_required()
def users():
    additional_data = get_jwt()
    administrador = additional_data.get('administrador')

    if request.method == 'POST':
        if administrador is True:
            data = request.get_json()
            username = data.get('usuario')
            password = data.get('contrasenia')

            try:
                nuevo_usuario = User(
                    username=username,
                    password_hash=generate_password_hash(password),
                    is_admin=False,
                )
                db.session.add(nuevo_usuario)
                db.session.commit()
                return jsonify(
                    {
                    "Mensaje":"Usuario creado correctamente",
                    "Usuario": nuevo_usuario.to_dict()
                    }
                )
            except:
                return jsonify(
                    {
                    "Mensaje":"Fallo la creacion del nuevo usuario",
                    }
                )
        else:
            return jsonify(Mensaje= "Solo el admin puede crear nuevos usuarios")
    
    usuarios = User.query.all()
    if administrador is True:
        return UserSchema().dump(obj=usuarios, many=True)
    else:
        return UserMinimalSchema().dump(obj=usuarios, many=True)
    


#CREAR CELULAR
@celulares_bp.route('/celulares_list', methods= ['GET','POST'])
def celulares():
    if request.method == 'POST':
        data = request.get_json()


        nuevo_celular = Celulares(
            modelo=data.get('modelo'),
            anio_fabricacion=data.get('anio_de_fabricacion'),
            precio=data.get('precio'),
            marca_id=data.get('marca_id'),
            tipo_id=data.get('tipo_id' )
        )
        db.session.add(nuevo_celular)
        db.session.commit()
        return CelularesSchema().dump(nuevo_celular)
    
    celulares = celulares.query.all()
    return CelularesSchema().dump(celulares, many=True)