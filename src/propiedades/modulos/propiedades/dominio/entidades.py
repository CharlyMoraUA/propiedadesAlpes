"""Entidades del dominio de propiedades

En este archivo usted encontrará las entidades del dominio de propiedades

"""

from __future__ import annotations
from dataclasses import dataclass, field

import propiedades.modulos.propiedades.dominio.objetos_valor as ov
from propiedades.modulos.propiedades.dominio.eventos import PropiedadCreado
from propiedades.seedwork.dominio.entidades import Locacion, AgregacionRaiz, Entidad

@dataclass
class Propiedad(AgregacionRaiz):
    id: uuid.UUID = field(hash=True, default=None)
    estado: ov.EstadoPropiedad = field(default=ov.EstadoPropiedad.PENDIENTE)
    area: ov.Area = field(hash=True, default=None)
    fecha_fin: ov.Fecha_fin = field(hash=True, default=None)
    id_compania: ov.id_compania = field(hash=True, default=None)
    id_inquilino: ov.id_inquilino = field(hash=True, default=None)
    id_propiedad: ov.id_propiedad = field(hash=True, default=None)
    armatriculaea: ov.Matricula = field(hash=True, default=None)

    def crear_propiedad(self, propiedad: Propiedad):
        self.id = propiedad.id
        self.estado = propiedad.estado
        self.area = propiedad.area
        self.fecha_fin = propiedad.fecha_fin
        self.id_compania = propiedad.id_compania
        self.id_inquilino = propiedad.id_inquilino
        self.id_propiedad = propiedad.id_propiedad
        self.area = propiedad.area

        print("propiedad2:")
        print(propiedad)

        self.agregar_evento(PropiedadCreado(id_propiedad=self.id, estado=self.estado.name, matricula=self.matricula))

