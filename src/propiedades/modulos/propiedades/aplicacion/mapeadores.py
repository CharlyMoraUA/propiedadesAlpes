from propiedades.seedwork.aplicacion.dto import Mapeador as AppMap
from propiedades.seedwork.dominio.repositorios import Mapeador as RepMap
from propiedades.modulos.propiedades.dominio.entidades import Propiedad
from propiedades.modulos.propiedades.dominio.objetos_valor import Area, Matricula, Direccion, Tipo
from datetime import datetime
from .dto import PropiedadDTO
import uuid

from datetime import datetime

class MapeadorPropiedadDTOJson(AppMap):
    
    def externo_a_dto(self, externo: dict) -> PropiedadDTO:
        propiedad_dto = PropiedadDTO(str(uuid.uuid4()), externo.get('matricula'), externo.get('direccion'), externo.get('area'), externo.get('tipo'))

        return propiedad_dto

    def dto_a_externo(self, dto: PropiedadDTO) -> dict:
        return dto.__dict__

class MapeadorPropiedad(RepMap):

    def obtener_tipo(self) -> type:
        return Propiedad.__class__

    def entidad_a_dto(self, entidad: Propiedad) -> PropiedadDTO:
        print("entidad_a_dto_aplicacion")
        print(entidad)
        _id = str(entidad.id)
        matricula = entidad.matricula
        direccion = entidad.direccion
        area = float(entidad.area)
        tipo = entidad.tipo
        
        return PropiedadDTO(_id, matricula, direccion, area, tipo)

    def dto_a_entidad(self, dto: PropiedadDTO) -> Propiedad:
        propiedad = Propiedad()
        print("dto_a_entidad_aplicacion:")
        print(propiedad)
        propiedad.id = dto.id
        propiedad.matricula = dto.matricula
        propiedad.direccion = dto.direccion
        propiedad.area = dto.area
        propiedad.tipo = dto.tipo
        
        return propiedad