import typing
import strawberry
import uuid
import requests
import os

from datetime import datetime


PROPIEDADESALPES_HOST = os.getenv("AEROALPES_ADDRESS", default="localhost")
FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'

def obtener_contratos(root) -> typing.List["Contrato"]:
    contratos_json = requests.get(f'http://{PROPIEDADESALPES_HOST}:5001/contratos/contrato-query').json()
    contratos = []

    for contrato in contratos_json:
        contratos.append(
            Contrato(
                fecha_creacion=datetime.strptime(contrato.get('fecha_creacion'), FORMATO_FECHA), 
                fecha_actualizacion=datetime.strptime(contrato.get('fecha_actualizacion'), FORMATO_FECHA), 
                id=contrato.get('id'),
                fecha_inicio=datetime.strptime(contrato.get('fecha_inicio'), FORMATO_FECHA),
                fecha_fin=datetime.strptime(contrato.get('fecha_fin'), FORMATO_FECHA),
                id_compania=contrato.get('id_compania'),
                id_inquilino=contrato.get('id_inquilino'),
                id_propiedad=contrato.get('id_propiedad'),
                monto=contrato.get('monto')
            )
        )

    return contratos

def obtener_contrato(root, id_contrato: str) -> "Contrato":
    print(id_contrato)
    contratos_json = requests.get(f'http://{PROPIEDADESALPES_HOST}:5001/contratos/contrato-query/'+id_contrato).json()
    contrato = Contrato(
        fecha_creacion=datetime.strptime(contratos_json.get('fecha_creacion'), FORMATO_FECHA), 
        fecha_actualizacion=datetime.strptime(contratos_json.get('fecha_actualizacion'), FORMATO_FECHA), 
        id=contratos_json.get('id'),
        fecha_inicio=datetime.strptime(contratos_json.get('fecha_inicio'), FORMATO_FECHA),
        fecha_fin=datetime.strptime(contratos_json.get('fecha_fin'), FORMATO_FECHA),
        id_compania=contratos_json.get('id_compania'),
        id_inquilino=contratos_json.get('id_inquilino'),
        id_propiedad=contratos_json.get('id_propiedad'),
        monto=contratos_json.get('monto')
                )
    return contrato


@strawberry.type
class Contrato:
    id: str
    fecha_inicio: datetime
    fecha_fin: datetime
    id_compania: int
    id_inquilino: int
    id_propiedad: int
    monto: float
    fecha_creacion: datetime
    fecha_actualizacion: datetime

@strawberry.type
class ContratoRespuesta:
    mensaje: str
    codigo: int






