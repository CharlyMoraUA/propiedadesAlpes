from pulsar.schema import *
from dataclasses import dataclass, field
from procesador.seedwork.infraestructura.schema.v1.comandos import (ComandoIntegracion)

class ComandoCrearProcesadorPayload(ComandoIntegracion):
    id_usuario = String()
    # TODO Cree los records 

class ComandoCrearProcesador(ComandoIntegracion):
    data = ComandoCrearProcesadorPayload()