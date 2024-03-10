""" Mapeadores para la capa de infrastructura del dominio de propiedades

En este archivo usted encontrará los diferentes mapeadores
encargados de la transformación entre formatos de dominio y DTOs

"""

from propiedades.seedwork.dominio.repositorios import Mapeador
from propiedades.modulos.propiedades.dominio.objetos_valor import Matricula, Direccion, Area, Tipo
from propiedades.modulos.propiedades.dominio.entidades import Propiedad
from .dto import Propiedad as PropiedadDTO
import uuid

class MapeadorPropiedad(Mapeador):
    _FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'

    def obtener_tipo(self) -> type:
        return Propiedad.__class__

    def entidad_a_dto(self, entidad: Propiedad) -> PropiedadDTO:
        print("entidad_a_dto_infra")
        print(entidad)
        propiedad_dto = PropiedadDTO()
        propiedad_dto.id = entidad.id
        propiedad_dto.matricula = entidad.matricula
        propiedad_dto.direccion = entidad.direccion
        propiedad_dto.area = entidad.area 
        propiedad_dto.tipo = entidad.tipo

        return propiedad_dto

    def dto_a_entidad(self, dto: PropiedadDTO) -> Propiedad:
        print("dto_a_entidad_infra")
        print(PropiedadDTO)
        propiedad = Propiedad(dto.id, dto.matricula, dto.direccion) #ATENCION
        propiedad.id =dto.id
        propiedad.matricula =dto.matricula
        propiedad.direccion =dto.direccion
        propiedad.area =dto.area
        propiedad.tipo =dto.tipo
        
        return propiedad