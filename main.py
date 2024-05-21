from fastapi import FastAPI
from routers import lista_bancos, lista_cuentas, lista_transacciones


app = FastAPI()

#Routers
app.include_router(lista_bancos.router)
app.include_router(lista_cuentas.router)
app.include_router(lista_transacciones.router)


@app.get("/")
def read():

    return {'Hola Mundo'}