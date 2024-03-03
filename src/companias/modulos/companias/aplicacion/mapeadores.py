from companias.seedwork.aplicacion.dto import Mapeador as AppMap
from companias.seedwork.dominio.repositorios import Mapeador as RepMap
from companias.modulos.companias.dominio.entidades import Compania
from datetime import datetime
from .dto import CompaniaDTO
import uuid

from datetime import datetime

class MapeadorCompaniaDTOJson(AppMap):
    
    def externo_a_dto(self, externo: dict) -> CompaniaDTO:
        fecha_creacion = datetime.strptime("2025-02-25T05:12:58Z", '%Y-%m-%dT%H:%M:%SZ')
        fecha_actualizacion = datetime.strptime("2025-02-25T05:12:58Z", '%Y-%m-%dT%H:%M:%SZ')
        compania_dto = CompaniaDTO(str(uuid.uuid4()),fecha_creacion,fecha_actualizacion,externo.get('documento_identidad'),externo.get('nombre'),externo.get('direccion'),externo.get('telefono'))

        return compania_dto

    def dto_a_externo(self, dto: CompaniaDTO) -> dict:
        return dto.__dict__

class MapeadorCompania(RepMap):
    _FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'

    def obtener_tipo(self) -> type:
        return Compania.__class__

    def entidad_a_dto(self, entidad: Compania) -> CompaniaDTO:
        print("entidad_a_dto_aplicacion")
        print(entidad)
        _id = str(entidad.id)
        fecha_creacion = entidad.fecha_creacion.strftime(self._FORMATO_FECHA)
        fecha_actualizacion = entidad.fecha_actualizacion.strftime(self._FORMATO_FECHA)
        documento_identidad = entidad.documento_identidad
        nombre = entidad.nombre
        direccion = entidad.direccion
        telefono = entidad.telefono
        
        return CompaniaDTO(_id, fecha_creacion, fecha_actualizacion, documento_identidad, nombre, direccion, telefono)

    def dto_a_entidad(self, dto: CompaniaDTO) -> Compania:
        compania = Compania()
        print("dto_a_entidad_aplicacion:")
        print(compania)
        compania.id = dto.id
        compania.documento_identidad = dto.documento_identidad
        compania.nombre = dto.nombre
        compania.direccion = dto.direccion
        compania.telefono = dto.telefono
        
        return compania