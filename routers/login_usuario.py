from fastapi import APIRouter
from db.cliente import db_cliente



router = APIRouter()


@router.get('/login/{usuario}/{password}')
async def login_usuario(usuario, password):
    #la contraseña esta hasheada con md5 es 12345
    print(usuario)
    print(password)
    response = {}
    usuario = db_cliente.local.users.find_one({"usuario": usuario})
    if usuario:
        if usuario['password'] == password:
            response = {"usuario" : usuario['nombre']}
        else:
            response = {'Error': 'Contraseña no valida'}
    else:
        response = {'Error': 'Usuario no valido'}
        
    print(response)
    return response

@router.post('/loginRegister/{nombre}/{usuario}/{password}')
async def login_usuario(nombre, usuario, password):
    #la contraseña esta hasheada con md5 es 12345
    userRegister = db_cliente.local.users.find_one({"usuario": usuario})
    if userRegister:
        return {'Error': 'El usuario ya existe'}
    else:
        usuarioBD = {"nombre": nombre, 'usuario': usuario, 'password': password}
        usuarioDict = dict(usuarioBD)
        db_cliente.local.users.insert_one(usuarioDict)
    
        return {"usuario" : nombre}