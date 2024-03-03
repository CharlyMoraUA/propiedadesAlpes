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
        inquilino = Inquilino(dto.id, dto.nombre, dto.telefono)
        inquilino.fecha_inicio = dto.nombre
        inquilino.fecha_fin = dto.telefono
        
        return inquilino