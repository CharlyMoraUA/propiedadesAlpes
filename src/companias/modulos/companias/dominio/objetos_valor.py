"""Objetos valor del dominio de companias

En este archivo usted encontrará los objetos valor del dominio de companias

"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum

@dataclass(frozen=True)
class documento_identidad():
    documento_identidad: str

@dataclass(frozen=True)
class nombre():
    nombre: str

@dataclass(frozen=True)
class direccion():
    direccion: str

@dataclass(frozen=True)
class telefono():
    telefono: str

class EstadoCompania(str, Enum):
    PENDIENTE = "Pendiente"