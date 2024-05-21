from fastapi import APIRouter

import requests

from requests.auth import HTTPBasicAuth

router = APIRouter()
INGRESO = 'INFLOW'
EGRESO = 'OUTFLOW'
#Cambiar esto a variables de ambiente
#el link sera un parametro que se reciba, validar como recibirlo en la url de la api y meterlo en el endpoint
url = 'https://sandbox.belvo.com/api/transactions/?page=1&fields=number%2Caccount%2Cid%2Ccategory%2Ctype%2Camount%2Cdescription%2Cinstitution%2Cname'
usu = 'e329e2de-85d5-4f9b-bd25-a2d6d8fe01b5'
contra = 'A8U6eAlVZkUqxs*GpsX2AZt-bqYrmQZXMGarSmbu4#h-YuM28YRUmX0KzhSZgyFh'

@router.get('/transacciones/{link}/{idAccount}')
async def lista_transacciones(link, idAccount):
    
    payload = {'link': link, 'account': idAccount}
    
    response = requests.get(url=url, params=payload ,auth=HTTPBasicAuth(usu,contra))
    response_json = response.json()

    monto_balance = balance(response_json['results'])
    
    return {"data": response_json, 'balance': monto_balance}


def balance(data):
    lista_ingresos = []
    lista_egresos = []
    total_ingresos = 0
    total_egresos = 0
    for i in data:
        indice = data.index(i)
        tipo_transaccioon = data[indice]['type']
        monto_transaccion = data[indice]['amount']
        if tipo_transaccioon == EGRESO:
            lista_egresos.append(monto_transaccion)
        else:
            lista_ingresos.append(monto_transaccion)

    total_ingresos = sum(lista_ingresos)
    total_egresos = sum(lista_egresos)
    total_balance = total_ingresos - total_egresos
    
    return total_balance