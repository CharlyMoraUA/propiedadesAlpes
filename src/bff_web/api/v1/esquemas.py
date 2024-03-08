import typing
import strawberry
import uuid
import requests
import os

from datetime import datetime


PROPIEDADESALPES_HOST = os.getenv("AEROALPES_ADDRESS", default="localhost")
FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'

def obtener_contrato(root) -> "Contrato":
    contrato_json = requests.get(f'http://{PROPIEDADESALPES_HOST}:5001/contratos/contrato-query').json()

    Contrato(
        fecha_creacion=datetime.strptime(contrato_json.get('fecha_creacion'), FORMATO_FECHA), 
        fecha_actualizacion=datetime.strptime(contrato_json.get('fecha_actualizacion'), FORMATO_FECHA), 
        id=contrato_json.get('id'), 
        id_usuario=contrato_json.get('id_usuario', '')
    )

    return Contrato

@strawberry.type
class Contrato:
    id: str
    fecha_inicio: str
    fecha_fin: str
    id_compania: int
    id_inquilino: int
    id_propiedad: int
    monto: int
    fecha_creacion: datetime
    fecha_actualizacion: datetime

@strawberry.type
class ContratoRespuesta:
    mensaje: str
    codigo: int






