from pulsar.schema import *
from inquilinos.seedwork.infraestructura.schema.v1.eventos import EventoIntegracion

class InquilinoCreadoPayload(Record):
    id = String()

class EventoInquilinoCreado(EventoIntegracion):
    data = InquilinoCreadoPayload()