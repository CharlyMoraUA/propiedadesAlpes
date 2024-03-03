""" Mapeadores para la capa de infrastructura del dominio de inquilinos

En este archivo usted encontrará los diferentes mapeadores
encargados de la transformación entre formatos de dominio y DTOs

"""

from inquilinos.seedwork.dominio.repositorios import Mapeador
from inquilinos.modulos.inquilinos.dominio.objetos_valor import Fecha_inicio, Fecha_fin, Monto
from inquilinos.modulos.inquilinos.dominio.entidades import Inquilino
from .dto import Inquilino as InquilinoDTO
import uuid

class MapeadorInquilino(Mapeador):
    _FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'

    def obtener_tipo(self) -> type:
        return Inquilino.__class__

    def entidad_a_dto(self, entidad: Inquilino) -> InquilinoDTO:
        print("entidad_a_dto_infra")
        print(entidad)
        inquilino_dto = InquilinoDTO()
        inquilino_dto.fecha_creacion = entidad.fecha_creacion
        inquilino_dto.fecha_actualizacion = entidad.fecha_actualizacion
        inquilino_dto.id = entidad.id
        inquilino_dto.fecha_inicio = entidad.fecha_inicio 
        inquilino_dto.fecha_fin = entidad.fecha_fin
        inquilino_dto.id_propiedad = entidad.id_propiedad
        inquilino_dto.id_inquilino = entidad.id_inquilino
        inquilino_dto.id_compania = entidad.id_compania
        inquilino_dto.monto = float(entidad.monto)

        return inquilino_dto

    def dto_a_entidad(self, dto: InquilinoDTO) -> Inquilino:
        print("dto_a_entidad_infra")
        print(InquilinoDTO)
        inquilino = Inquilino(dto.id, dto.fecha_creacion, dto.fecha_actualizacion)
        inquilino.fecha_inicio = dto.fecha_inicio
        inquilino.fecha_fin = dto.fecha_fin
        inquilino.id_propiedad = dto.id_propiedad
        inquilino.id_inquilino = dto.id_inquilino
        inquilino.id_compania = dto.id_compania
        inquilino.monto = dto.monto
        
        return inquilino