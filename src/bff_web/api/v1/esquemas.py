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

def obtener_contrato(id_contrato: str) -> "Contrato":
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




def obtener_propiedades(root) -> typing.List["Propiedad"]:
    propiedades_json = requests.get(f'http://{PROPIEDADESALPES_HOST}:5004/propiedades/propiedad-query').json()
    propiedades = []

    for propiedad in propiedades_json:
        propiedades.append(
            Propiedad(
                id=propiedad.get('id'),
                area=propiedad.get('area'), 
                direccion=propiedad.get('direccion'), 
                matricula=propiedad.get('matricula'),
                tipo=propiedad.get('tipo')
            )
        )

    return propiedades

def obtener_propiedad(id_propiedad: str) -> "Propiedad":
    propiedades_json = requests.get(f'http://{PROPIEDADESALPES_HOST}:5004/propiedades/propiedad-query/'+id_propiedad).json()
    propiedad = Propiedad(
                id=propiedades_json.get('id'),
                area=propiedades_json.get('area'), 
                direccion=propiedades_json.get('direccion'), 
                matricula=propiedades_json.get('matricula'),
                tipo=propiedades_json.get('tipo')
            )
    return propiedad




def obtener_inquilinos(root) -> typing.List["Inquilino"]:
    inquilinos_json = requests.get(f'http://{PROPIEDADESALPES_HOST}:5003/inquilinos/inquilino-query').json()
    inquilinos = []

    for inquilino in inquilinos_json:
        inquilinos.append(
            Inquilino(
                id=inquilino.get('id'),
                nombre=inquilino.get('nombre'), 
                telefono=inquilino.get('telefono')
            )
        )

    return inquilinos

def obtener_inquilino(id_inquilino: str) -> "Inquilino":
    inquilinos_json = requests.get(f'http://{PROPIEDADESALPES_HOST}:5003/inquilinos/inquilino-query/'+id_inquilino).json()
    inquilino = Inquilino(
                id=inquilinos_json.get('id'),
                nombre=inquilinos_json.get('nombre'), 
                telefono=inquilinos_json.get('telefono')
            )
    return inquilino



def obtener_companias(root) -> typing.List["Compania"]:
    companias_json = requests.get(f'http://{PROPIEDADESALPES_HOST}:5002/companias/compania-query').json()
    companias = []

    for compania in companias_json:
        companias.append(
            Compania(
                id=compania.get('id'),
                direccion=compania.get('direccion'), 
                documento_identidad=compania.get('documento_identidad'), 
                fecha_actualizacion=datetime.strptime(compania.get('fecha_actualizacion'), FORMATO_FECHA), 
                fecha_creacion=datetime.strptime(compania.get('fecha_creacion'), FORMATO_FECHA), 
                nombre=compania.get('nombre'), 
                telefono=compania.get('telefono')
            )
        )

    return companias

def obtener_compania(id_compania: str) -> "Compania":
    companias_json = requests.get(f'http://{PROPIEDADESALPES_HOST}:5002/companias/compania-query/'+id_compania).json()
    compania = Compania(
                id=companias_json.get('id'),
                direccion=companias_json.get('direccion'), 
                documento_identidad=companias_json.get('documento_identidad'), 
                fecha_actualizacion=datetime.strptime(companias_json.get('fecha_actualizacion'), FORMATO_FECHA), 
                fecha_creacion=datetime.strptime(companias_json.get('fecha_creacion'), FORMATO_FECHA), 
                nombre=companias_json.get('nombre'), 
                telefono=companias_json.get('telefono')
            )
    return compania





@strawberry.type
class Compania:
    id: str
    direccion: str
    documento_identidad: str
    fecha_actualizacion: datetime
    fecha_creacion: datetime
    nombre: str
    telefono:float

@strawberry.type
class CompaniaRespuesta:
    mensaje: str
    codigo: int




@strawberry.type
class Inquilino:
    id: str
    nombre: str
    telefono: int

@strawberry.type
class InquilinoRespuesta:
    mensaje: str
    codigo: int
    
    

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
    
    

@strawberry.type
class Propiedad:
    id: str
    area: float
    direccion: str
    matricula: str
    tipo: str

@strawberry.type
class PropiedadRespuesta:
    mensaje: str
    codigo: int





