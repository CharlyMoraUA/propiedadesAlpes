from pulsar.schema import *
from dataclasses import dataclass, field
from propiedades.seedwork.infraestructura.schema.v1.comandos import (ComandoIntegracion)
from aeroalpes.seedwork.infraestructura.utils import time_millis
import uuid

class ComandoCrearPropiedadPayload(ComandoIntegracion):
    id_usuario = String()
    # TODO Cree los records 

class ComandoCrearPropiedad(ComandoIntegracion):
    data = ComandoCrearPropiedadPayload()
    
    
class ComandoPropiedadPayload(ComandoIntegracion):
    area = Float()
    direccion = String()
    matricula = String()
    tipo = String()
    id = String()

class ComandoPropiedad(ComandoIntegracion):
    id = String(default=str(uuid.uuid4()))
    time = Long()
    specversion = String()
    type = String()
    ingestion = Long(default=time_millis())
    datacontenttype = String()
    service_name = String()
    data = ComandoPropiedadPayload()