"""Entidades del dominio de contratos

En este archivo usted encontrará las entidades del dominio de contratos

"""

from __future__ import annotations
from dataclasses import dataclass, field

import aeroalpes.modulos.contratos.dominio.objetos_valor as ov
from aeroalpes.modulos.contratos.dominio.eventos import ContratoCreado
from aeroalpes.seedwork.dominio.entidades import Locacion, AgregacionRaiz, Entidad

@dataclass
class Contrato(AgregacionRaiz):
    id: uuid.UUID = field(hash=True, default=None)
    estado: ov.EstadoContrato = field(default=ov.EstadoContrato.PENDIENTE)
    fecha_inicio: ov.Fecha_inicio = field(hash=True, default=None)
    fecha_fin: ov.Fecha_fin = field(hash=True, default=None)
    id_compania: ov.id_compania = field(hash=True, default=None)
    id_inquilino: ov.id_inquilino = field(hash=True, default=None)
    id_propiedad: ov.id_propiedad = field(hash=True, default=None)
    monto: ov.Monto = field(hash=True, default=None)

    def crear_contrato(self, contrato: Contrato):
        self.id = contrato.id
        self.estado = contrato.estado
        self.fecha_inicio = contrato.fecha_inicio
        self.fecha_fin = contrato.fecha_fin
        self.id_compania = contrato.id_compania
        self.id_inquilino = contrato.id_inquilino
        self.id_propiedad = contrato.id_propiedad
        self.monto = contrato.monto

        print("contrato2:")
        print(contrato)

        self.agregar_evento(ContratoCreado(id_contrato=self.id, estado=self.estado.name, fecha_creacion=self.fecha_creacion))

    """ def firmar_contrato(self):
        self.estado = ov.EstadoContrato.FIRMADO
        self.agregar_evento(ContratoFirmado(self.id, self.fecha_actualizacion))

    def procesar_contrato(self):
        self.estado = ov.EstadoContrato.PROCESADO
        self.agregar_evento(ContratoProcesado(self.id, self.fecha_actualizacion)) """
