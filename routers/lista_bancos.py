import os
from fastapi import APIRouter
from dotenv import load_dotenv


import requests
from requests.auth import HTTPBasicAuth
load_dotenv()
router = APIRouter()
URL_BANCO = os.getenv('URL')
#Cambiar esto a variables de ambiente
#url = 'https://sandbox.belvo.com/api/institutions/'
urlLinks = 'https://sandbox.belvo.com/api/links/?page=1&fields=id,institution,external_id'
usu = 'e329e2de-85d5-4f9b-bd25-a2d6d8fe01b5'
contra = 'A8U6eAlVZkUqxs*GpsX2AZt-bqYrmQZXMGarSmbu4#h-YuM28YRUmX0KzhSZgyFh'


@router.get('/bancos')
async def lista_bancos():
    lista_links = links()
    #esta lista tratar de mandar nombre de banco en los parametros para que me regrese los bancos que necesito
    # response_json= []
    # for i in lista_links:
    #     payload = {"page":1, "name": i}
    #     response = requests.get(url = url, params=payload ,auth=HTTPBasicAuth(usu, contra))
    #     response_json.append(response.json()['results'][0])
    return lista_links

@router.get('/banco/{id}')
async def banco(id):
    
    
    return {'Hola', id}


def links():
    name_banks = []
    response = requests.get(url= urlLinks, auth=HTTPBasicAuth(usu, contra), verify=False)
    response_json = response.json()
    #revisar como enviar el link para que se vea reflejado en el api de bancos
    for i in response_json["results"]:
        print(i)
        name_banks.append(i) 
    return name_banks