"""Entidades del dominio de inquilinos

En este archivo usted encontrará las entidades del dominio de inquilinos

"""

from __future__ import annotations
from dataclasses import dataclass, field

import inquilinos.modulos.inquilinos.dominio.objetos_valor as ov
from inquilinos.modulos.inquilinos.dominio.eventos import InquilinoCreado
from inquilinos.seedwork.dominio.entidades import Locacion, AgregacionRaiz, Entidad

@dataclass
class Inquilino(AgregacionRaiz):
    id: uuid.UUID = field(hash=True, default=None)
    nombre: ov.nombre = field(default=ov.nombre)
    telefono: ov.telefono = field(default=ov.telefono)
    

    def crear_inquilino(self, inquilino: Inquilino):
        self.id = inquilino.id
        self.nombre = inquilino.nombre
        self.telefono = inquilino.telefono

        print("inquilino2:")
        print(inquilino)

        self.agregar_evento(InquilinoCreado(id_inquilino=self.id, nombre=self.nombre, telefono=self.telefono))

    """ def firmar_inquilino(self):
        self.estado = ov.EstadoInquilino.FIRMADO
        self.agregar_evento(InquilinoFirmado(self.id, self.fecha_actualizacion))

    def procesar_inquilino(self):
        self.estado = ov.EstadoInquilino.PROCESADO
        self.agregar_evento(InquilinoProcesado(self.id, self.fecha_actualizacion)) """
