from pulsar.schema import *
from propiedades.seedwork.infraestructura.schema.v1.eventos import EventoIntegracion

class PropiedadCreadoPayload(Record):
    id = String()
    matricula = String()

class EventoPropiedadCreado(EventoIntegracion):
    data = PropiedadCreadoPayload()
    