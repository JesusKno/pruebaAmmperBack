from fastapi import APIRouter



router = APIRouter()


@router.get('/login/{usuario}/{password}')
async def login_usuario(usuario, password):
    #la contraseña esta hasheada con md5 es 12345
    print(usuario)
    print(password)
    usuarioParams = usuario
    usuarioBD = {"nombre": 'Jesus', 'usuario': 'jcano1460@gmail.com', 'password': '827ccb0eea8a706c4c34a16891f84e7b'}
    return {"usuario" : "Jesus"}


@router.get('/loginRegister/{nombre}/{usuario}/{password}')
async def login_usuario(nombre, usuario, password):
    #la contraseña esta hasheada con md5 es 12345
    print(usuario)
    print(password)
    usuarioParams = usuario
    usuarioBD = {"nombre": 'Jesus', 'usuario': 'jcano1460@gmail.com', 'password': '827ccb0eea8a706c4c34a16891f84e7b'}
    return {"usuario" : nombre}