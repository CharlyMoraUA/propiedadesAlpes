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
    estado: ov.EstadoInquilino = field(default=ov.EstadoInquilino.PENDIENTE)
    fecha_inicio: ov.Fecha_inicio = field(hash=True, default=None)
    fecha_fin: ov.Fecha_fin = field(hash=True, default=None)
    id_compania: ov.id_compania = field(hash=True, default=None)
    id_inquilino: ov.id_inquilino = field(hash=True, default=None)
    id_propiedad: ov.id_propiedad = field(hash=True, default=None)
    monto: ov.Monto = field(hash=True, default=None)

    def crear_inquilino(self, inquilino: Inquilino):
        self.id = inquilino.id
        self.estado = inquilino.estado
        self.fecha_inicio = inquilino.fecha_inicio
        self.fecha_fin = inquilino.fecha_fin
        self.id_compania = inquilino.id_compania
        self.id_inquilino = inquilino.id_inquilino
        self.id_propiedad = inquilino.id_propiedad
        self.monto = inquilino.monto

        print("inquilino2:")
        print(inquilino)

        self.agregar_evento(InquilinoCreado(id_inquilino=self.id, estado=self.estado.name, fecha_creacion=self.fecha_creacion))

    """ def firmar_inquilino(self):
        self.estado = ov.EstadoInquilino.FIRMADO
        self.agregar_evento(InquilinoFirmado(self.id, self.fecha_actualizacion))

    def procesar_inquilino(self):
        self.estado = ov.EstadoInquilino.PROCESADO
        self.agregar_evento(InquilinoProcesado(self.id, self.fecha_actualizacion)) """
