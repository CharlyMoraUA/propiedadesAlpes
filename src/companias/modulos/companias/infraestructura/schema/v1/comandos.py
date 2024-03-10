from pulsar.schema import *
from dataclasses import dataclass, field
from companias.seedwork.infraestructura.schema.v1.comandos import (ComandoIntegracion)

class ComandoCrearCompaniaPayload(ComandoIntegracion):
    id_usuario = String()
    # TODO Cree los records 

class ComandoCrearCompania(ComandoIntegracion):
    data = ComandoCrearCompaniaPayload()
    
class ComandoCompaniaPayload(ComandoIntegracion):
    direccion = String()
    nombre = String()
    documento_identidad = String()
    telefono = Integer()
    id = String()

class ComandoCompania(ComandoIntegracion):
    id = String(default=str(uuid.uuid4()))
    time = Long()
    specversion = String()
    type = String()
    ingestion = Long(default=time_millis())
    datacontenttype = String()
    service_name = String()
    data = ComandoCompaniaPayload()