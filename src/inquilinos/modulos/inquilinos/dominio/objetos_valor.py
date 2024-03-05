"""Objetos valor del dominio de inquilinos

En este archivo usted encontrará los objetos valor del dominio de inquilinos

"""

from __future__ import annotations

from dataclasses import dataclass

@dataclass(frozen=True)
class nombre():
    nombre: str

@dataclass(frozen=True)
class telefono():
    telefono: int