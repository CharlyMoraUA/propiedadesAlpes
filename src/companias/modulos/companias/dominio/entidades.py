"""Entidades del dominio de compañias

En este archivo usted encontrará las entidades del dominio de compañias

"""

from __future__ import annotations
from dataclasses import dataclass, field

import companias.modulos.companias.dominio.objetos_valor as ov
from companias.modulos.companias.dominio.eventos import CompaniaCreada
from companias.modulos.companias.infraestructura.despachadores import Despachador
from companias.seedwork.dominio.entidades import AgregacionRaiz

@dataclass
class Compania(AgregacionRaiz):
    id: uuid.UUID = field(hash=True, default=None)
    estado: ov.EstadoCompania = field(default=ov.EstadoCompania.PENDIENTE)
    documento_identidad: ov.documento_identidad = field(hash=True, default=None)
    nombre: ov.nombre = field(hash=True, default=None)
    direccion: ov.direccion = field(hash=True, default=None)
    telefono: ov.telefono = field(hash=True, default=None)

    def crear_compania(self, compania: Compania):
        self.id = compania.id
        self.estado = compania.estado
        self.documento_identidad = compania.documento_identidad
        self.nombre = compania.nombre
        self.direccion = compania.direccion
        self.telefono = compania.telefono
        
        despachador = Despachador()
        despachador.publicar_evento(CompaniaCreada(id_compania=self.id, estado=self.estado.name, fecha_creacion=self.fecha_creacion), 'eventos-compania')

        self.agregar_evento(CompaniaCreada(id_compania=self.id, estado=self.estado.name, fecha_creacion=self.fecha_creacion))
