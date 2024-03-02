"""Objetos valor del dominio de contratos

En este archivo usted encontrará los objetos valor del dominio de contratos

"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from enum import Enum

@dataclass(frozen=True)
class Fecha_inicio():
    fecha_inicio: datetime

@dataclass(frozen=True)
class Fecha_fin():
    fecha_fin: datetime

@dataclass(frozen=True)
class id_compania():
    id_compania: integer

@dataclass(frozen=True)
class id_inquilino():
    id_inquilino: integer

@dataclass(frozen=True)
class id_propiedad():
    id_propiedad: integer

@dataclass(frozen=True)
class Monto():
    monto: float

class EstadoContrato(str, Enum):
    PENDIENTE = "Pendiente"
    #FIRMADO = "Firmado"
    #PROCESADO = "Procesado"