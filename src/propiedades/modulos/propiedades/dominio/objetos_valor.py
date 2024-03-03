"""Objetos valor del dominio de propiedades

En este archivo usted encontrará los objetos valor del dominio de propiedades

"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from enum import Enum

@dataclass(frozen=True)
class Matricula():
    matricula: str

@dataclass(frozen=True)
class Direccion():
    direccion: str

@dataclass(frozen=True)
class Area():
    area: int

class Tipo(str, Enum):
    tipo: str