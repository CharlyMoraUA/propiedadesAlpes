from pulsar.schema import *
from companias.seedwork.infraestructura.schema.v1.eventos import EventoIntegracion

class CompaniaCreadaPayload(Record):
    id = String()
    estado = String()
    fecha_creacion = Long()

class EventoCompaniaCreada(EventoIntegracion):
    data = CompaniaCreadaPayload()