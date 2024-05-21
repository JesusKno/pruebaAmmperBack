from fastapi import FastAPI
from routers import lista_bancos, lista_cuentas, lista_transacciones, login_usuario
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

#Routers
app.include_router(lista_bancos.router)
app.include_router(lista_cuentas.router)
app.include_router(lista_transacciones.router)
app.include_router(login_usuario.router)

#permisos cors
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

@app.get("/")
def read():

    return {'Hola Mundo'}