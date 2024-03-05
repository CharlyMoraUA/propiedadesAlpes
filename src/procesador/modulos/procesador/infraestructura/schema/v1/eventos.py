from pulsar.schema import *
from procesador.seedwork.infraestructura.schema.v1.eventos import EventoIntegracion

class ProcesadorCreadoPayload(Record):
    id = String()

class EventoProcesadorCreado(EventoIntegracion):
    data = ProcesadorCreadoPayload()