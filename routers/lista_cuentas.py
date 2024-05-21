from fastapi import APIRouter

import requests

from requests.auth import HTTPBasicAuth

router = APIRouter()

#Cambiar esto a variables de ambiente
#el link sera un parametro que se reciba, validar como recibirlo en la url de la api y meterlo en el endpoint
url = 'https://sandbox.belvo.com/api/accounts/?page=1&fields=id%2Ccategory%2Ctype%2Camount%2Cdescription%2Cinstitution%2Cname%2Cnumber%2Cbalance%2Ccurrent%2Cavialable'
usu = 'e329e2de-85d5-4f9b-bd25-a2d6d8fe01b5'
contra = 'A8U6eAlVZkUqxs*GpsX2AZt-bqYrmQZXMGarSmbu4#h-YuM28YRUmX0KzhSZgyFh'

@router.get('/cuentas/{link}')
async def lista_cuentas(link):
    
    payload = {'link': link}
    
    response = requests.get(url= url, params=payload ,auth=HTTPBasicAuth(usu, contra))
    response_json = response.json()
    
    return response_json