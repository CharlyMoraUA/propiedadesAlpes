from pulsar.schema import *
from aeroalpes.seedwork.infraestructura.schema.v1.eventos import EventoIntegracion

class ContratoCreadoPayload(Record):
    id = String()
    estado = String()
    fecha_creacion = Long()

class EventoContratoCreado(EventoIntegracion):
    data = ContratoCreadoPayload()