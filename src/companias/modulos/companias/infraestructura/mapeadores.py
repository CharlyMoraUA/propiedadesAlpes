""" Mapeadores para la capa de infrastructura del dominio de companias

En este archivo usted encontrará los diferentes mapeadores
encargados de la transformación entre formatos de dominio y DTOs

"""

from companias.seedwork.dominio.repositorios import Mapeador
from companias.modulos.companias.dominio.entidades import Compania
from .dto import Compania as CompaniaDTO
import uuid

class MapeadorCompania(Mapeador):
    _FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'

    def obtener_tipo(self) -> type:
        return Compania.__class__

    def entidad_a_dto(self, entidad: Compania) -> CompaniaDTO:
        print("entidad_a_dto_infra")
        print(entidad)
        compania_dto = CompaniaDTO()
        compania_dto.fecha_creacion = entidad.fecha_creacion
        compania_dto.fecha_actualizacion = entidad.fecha_actualizacion
        compania_dto.id = entidad.id
        compania_dto.documento_identidad = entidad.documento_identidad
        compania_dto.nombre = entidad.nombre
        compania_dto.direccion = entidad.direccion
        compania_dto.telefono = entidad.telefono

        return compania_dto

    def dto_a_entidad(self, dto: CompaniaDTO) -> Compania:
        print("dto_a_entidad_infra")
        print(CompaniaDTO)
        compania = Compania(dto.id, dto.fecha_creacion, dto.fecha_actualizacion)
        compania.documento_identidad = dto.documento_identidad
        compania.nombre = dto.nombre
        compania.direccion = dto.direccion
        compania.telefono = dto.telefono
        
        return compania