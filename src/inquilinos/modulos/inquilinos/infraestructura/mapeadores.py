""" Mapeadores para la capa de infrastructura del dominio de inquilinos

En este archivo usted encontrará los diferentes mapeadores
encargados de la transformación entre formatos de dominio y DTOs

"""

from inquilinos.seedwork.dominio.repositorios import Mapeador
from inquilinos.modulos.inquilinos.dominio.objetos_valor import nombre, telefono
from inquilinos.modulos.inquilinos.dominio.entidades import Inquilino
from .dto import Inquilino as InquilinoDTO
import uuid

class MapeadorInquilino(Mapeador):

    def obtener_tipo(self) -> type:
        return Inquilino.__class__

    def entidad_a_dto(self, entidad: Inquilino) -> InquilinoDTO:
        print("entidad_a_dto_infra")
        print(entidad)
        inquilino_dto = InquilinoDTO()
        inquilino_dto.nombre = entidad.nombre
        inquilino_dto.telefono = entidad.telefono
        inquilino_dto.id = entidad.id

        return inquilino_dto

    def dto_a_entidad(self, dto: InquilinoDTO) -> Inquilino:
        print("dto_a_entidad_infra")
        print(InquilinoDTO)
        inquilino = Inquilino(dto.id, dto.nombre, dto.telefono)
        inquilino.nombre = dto.nombre
        inquilino.telefono = dto.telefono
        
        return inquilino