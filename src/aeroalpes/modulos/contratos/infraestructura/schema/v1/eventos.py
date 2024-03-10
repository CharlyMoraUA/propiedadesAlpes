from pulsar.schema import *
from aeroalpes.seedwork.infraestructura.schema.v1.eventos import EventoIntegracion
from aeroalpes.seedwork.infraestructura.utils import time_millis
import uuid

class ContratoCreadoPayload(Record):
    id = String()
    estado = String()
    fecha_creacion = Long()

class EventoContratoCreado(EventoIntegracion):
    id = String(default=str(uuid.uuid4()))
    time = Long()
    ingestion = Long(default=time_millis())
    specversion = String()
    type = String()
    datacontenttype = String()
    service_name = String()
    data = ContratoCreadoPayload()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)