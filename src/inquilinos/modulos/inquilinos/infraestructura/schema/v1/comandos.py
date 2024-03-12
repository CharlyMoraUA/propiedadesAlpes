from pulsar.schema import *
from dataclasses import dataclass, field
from inquilinos.seedwork.infraestructura.schema.v1.comandos import (ComandoIntegracion)
from inquilinos.seedwork.infraestructura.utils import time_millis
import uuid

class ComandoCrearInquilinoPayload(ComandoIntegracion):
    id_usuario = String()
    # TODO Cree los records 

class ComandoCrearInquilino(ComandoIntegracion):
    data = ComandoCrearInquilinoPayload() 
    
    
class ComandoInquilinoPayload(ComandoIntegracion):
    nombre = String()
    telefono = Integer()
    id = String()

class ComandoInquilino(ComandoIntegracion):
    id = String(default=str(uuid.uuid4()))
    time = Long()
    specversion = String()
    type = String()
    ingestion = Long(default=time_millis())
    datacontenttype = String()
    service_name = String()
    data = ComandoInquilinoPayload()