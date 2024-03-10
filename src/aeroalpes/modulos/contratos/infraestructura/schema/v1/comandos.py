from pulsar.schema import *
from dataclasses import dataclass, field
from aeroalpes.seedwork.infraestructura.schema.v1.comandos import (ComandoIntegracion)
from aeroalpes.seedwork.infraestructura.utils import time_millis
import uuid

class ComandoContratoPayload(ComandoIntegracion):
    fecha_inicio = String()
    fecha_fin = String()
    id_compania = Integer()
    id_inquilino = Integer()
    id_propiedad = Integer()
    monto = Float()
    id = String()
    type = String()

class ComandoContrato(ComandoIntegracion):
    id = String(default=str(uuid.uuid4()))
    time = Long()
    specversion = String()
    type = String()
    ingestion = Long(default=time_millis())
    datacontenttype = String()
    service_name = String()
    data = ComandoContratoPayload()