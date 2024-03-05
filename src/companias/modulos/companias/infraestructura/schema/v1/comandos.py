from pulsar.schema import *
from dataclasses import dataclass, field
from companias.seedwork.infraestructura.schema.v1.comandos import (ComandoIntegracion)

class ComandoCrearCompaniaPayload(ComandoIntegracion):
    id_usuario = String()
    # TODO Cree los records 

class ComandoCrearCompania(ComandoIntegracion):
    data = ComandoCrearCompaniaPayload()