"""Entidades del dominio de propiedades

En este archivo usted encontrará las entidades del dominio de propiedades

"""

from __future__ import annotations
from dataclasses import dataclass, field

import propiedades.modulos.propiedades.dominio.objetos_valor as ov
from propiedades.modulos.propiedades.dominio.eventos import PropiedadCreado
from propiedades.seedwork.dominio.entidades import Locacion, AgregacionRaiz, Entidad
from propiedades.modulos.propiedades.infraestructura.despachadores import Despachador

@dataclass
class Propiedad(AgregacionRaiz):
    id: uuid.UUID = field(hash=True, default=None)
    matricula: ov.Matricula = field(hash=True, default=None)
    direccion: ov.Direccion = field(hash=True, default=None)
    area: ov.Area = field(hash=True, default=None)
    tipo: ov.Tipo = field(hash=True, default=None)

    def crear_propiedad(self, propiedad: Propiedad):
        self.id = propiedad.id
        self.matricula = propiedad.matricula
        self.direccion = propiedad.direccion
        self.area = propiedad.area
        self.tipo = propiedad.tipo

        
        # despachador = Despachador()
        # despachador.publicar_evento(PropiedadCreado(id_propiedad=self.id, matricula=self.matricula), 'eventos-propiedad')
            #ATENCION
        self.agregar_evento(PropiedadCreado(id_propiedad=self.id, matricula=self.matricula))

